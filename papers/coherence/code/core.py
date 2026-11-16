"""core.py -- core library for the paper
"Coherence, Not Error Rate, Limits the Self-Correction of Learned Computation".

Pure numpy.  Run the self-tests with

    python3 code/core.py --selftest

CONVENTIONS
-----------
* G = Z_{p_1} x ... x Z_{p_n} (usually Z_p^n).  A function on G is a "table": an integer array of
  shape (p_1, ..., p_n).  The FLAT INDEX of a group element is its C-order (row-major) index, i.e.
  flat = np.ravel_multi_index(coords, shape); |G| = table.size.
* H = Z_q.  f is the task (a homomorphism G -> H, or the bilinear map a*b for the "mul" task),
  M the model's argmax prediction table, E = (M - f) mod q the ERROR TABLE.
* A "channel" is an array T of shape (X, q) whose row x is a probability vector over the OFFSET
  FROM THE TRUTH h = vote - f(x).  Column 0 is therefore always "the vote is correct".  The
  functions *_counts return the same thing as exact integers (rows sum to the number of
  randomisations); *_channel = counts / row sum.  Rows are ordered by the flat index of x.
* Plurality of k votes: a tie for first place is counted as a FAILURE everywhere.

PUBLIC API
----------
Group helpers
  group_shape(p, n)                      -> (p,)*n
  coords(shape)                          -> (|G|, n) int array, coords of every flat index
  flat_index(xc, shape)                  -> flat indices of coordinate rows (reduced mod shape)
  add_table(shape)                       -> (|G|, |G|) int32, ADD[x, r] = flat index of x + r (cached)
  translate(table, x)                    -> table S with S[r] = table[x + r]; x = flat index or coords

Tasks
  true_table(task, p, n=2, w=None)       -> f as a table; task in {"add", "lin", "mul"}
  make_error_table(M, f, q)              -> (M - f) mod q as int64

Twirled channel of the BLR vote V_r(x) = M(x+r) - M(r)   [D_x(r) = E(x+r) - E(r)]
  twirled_counts(E, q, method="fft")     -> (|G|, q) int64, N[x,h] = #{r : E(x+r)-E(r) = h mod q}
  twirled_channel(E, q, method="fft")    -> (|G|, q) float64 = twirled_counts / |G|   (exact)
  twirled_counts_brute(E, q)             -> same, plain Python loops (reference, small cases only)
      method="fft":  character lift phi_j = exp(2 pi i j E / q); N[x,.] is the inverse DFT over j of
                     the autocorrelation of phi_j; rounded to integers (asserted to be within 1e-6).
      method="enum": direct vectorised enumeration over all (x, r) with integer arithmetic.

Bilinear (4-query) vote for multiplication on G = Z_p1 x Z_p2
  bilinear_counts(E, q)                  -> (p1*p2, q) int64, D = e(x+r,y+s)-e(r,y+s)-e(x+r,s)+e(r,s)
  bilinear_channel(E, q)                 -> counts / (p1*p2)                      (exact enumeration)
  bilinear_counts_brute(E, q)            -> reference implementation

Invariance twirl (test-time augmentation over the level set) for f(a,b) = a+b
  invariance_counts_add(E, q)            -> (p*p, q) int64, N[(a,b),h] = #{r : E(a+r, b-r) = h}
  invariance_channel_add(E, q)           -> counts / p

Label-free BLR linearity test
  blr_pass_rate(M, q, method="fft")      -> exact Pr_{x,y}[M(x)+M(y) = M(x+y)]  ("enum" = reference)
  lam_hat_from_pass(pi, q)               -> ((pi - 1/q)/(1 - 1/q))^(1/3)   (real cube root)
  eps_hat_from_pass(pi, q)               -> (1 - lam_hat)(1 - 1/q)

Depolarizing law (claim C3) and exponents
  lam(eps, q)                            -> 1 - eps/(1 - 1/q)
  eps_from_lam(lam_, q)                  -> (1 - lam_)(1 - 1/q)
  pc_law(eps, q, c)                      -> 1/q + (1 - 1/q) lam^c       Pr[sum of c errors = 0]
  pw_law(eps, q, c)                      -> (1 - lam^c)/q               Pr[sum = h], each h != 0
  depolarizing_channel(eps, q, c)        -> length-q vector (pc, pw, ..., pw)
  hellinger_rate(t0, th)                 -> -ln(1 - (sqrt t0 - sqrt th)^2), 0 where th >= t0
  rate_law(eps, q, c)                    -> hellinger_rate(pc_law, pw_law)
  channel_rate(T)                        -> per-input exponent I_x (strongest wrong value h*)
  channel_stats(T)                       -> dict of per-input arrays: t0, tw (max wrong), hstar,
                                            margin = t0 - tw, strict_mode (bool), rate
  votes_needed(rate, delta, q)           -> smallest k with (q-1) exp(-k rate) <= delta
  lam_c_heuristic(G, q)                  -> finite-size estimate of the critical lambda (C3)

Plurality failure of Multinomial(k, T_x)   (claim C1)
  chernoff_union_bound(T, k)             -> per-input upper bound on delta_k(x); k scalar or array
  plurality_fail_exact(T, k)             -> per-input exact delta_k(x) (cost O(X q k^3); k <= 150)
  plurality_fail_mc(T, k, n_samples, rng, chunk=...) -> per-input Monte Carlo estimate
  plurality_fail_enum(t, k)              -> exact by enumerating all q^k vote strings (tiny cases)

Actual voting on a table (to check enumeration against real self-correction)
  plurality(votes, q)                    -> (winner, tied) per row of an (m, k) vote array
  sc_votes(table, xs, k, rng, q=None)    -> (m, k) votes M(x+r) - M(r) mod q, r uniform on G
  sc_predict(table, xs, k, rng, q=None)  -> (pred, tied): plurality of k real votes per input
  sc_fail(table, f, xs, k, rng, q=None)  -> bool per input: pred != f(x) or tied
  bilinear_votes(table, xs, k, rng, q=None)        -> votes of the 4-query multiplication corrector
  invariance_votes_add(table, xs, k, rng)          -> votes M(a+r, b-r)

Model zoo (written by code/make_zoo.py)
  load_index(full=False)                 -> list of model records (or the whole index dict)
  get_record(model_id)                   -> one record
  load_table(model_id)                   -> prediction table M, int64, shape (p,)*n
  load_train_mask(model_id)              -> bool table, True where the input was in the training set
  error_table(model_id)                  -> (M - f) mod q, int64, shape (p,)*n
  model_true_table(model_id)             -> f for that model
  load_logits(model_id)                  -> (|G|, q) float16 logits from cache/ (add/memo only)
  load_run(file)                         -> dict of the arrays of one run file (all snapshots)
"""
import functools
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ZOO_DIR = os.path.join(ROOT, "zoo")
CACHE_DIR = os.path.join(ROOT, "cache")
RESULTS_DIR = os.path.join(ROOT, "results")
FIG_DIR = os.path.join(ROOT, "figures")
LIN_W = (3, 5, 2, 6)          # secret weights of the "lin" task on Z_7^4


# --------------------------------------------------------------------------------------------
# group helpers
# --------------------------------------------------------------------------------------------
def group_shape(p, n):
    """Shape of a table on G = Z_p^n."""
    return (int(p),) * int(n)


@functools.lru_cache(maxsize=16)
def _coords_cached(shape):
    c = np.stack(np.unravel_index(np.arange(int(np.prod(shape))), shape), axis=1).astype(np.int64)
    c.setflags(write=False)
    return c


def coords(shape):
    """(|G|, n) array: row i holds the coordinates of the group element with flat index i."""
    return _coords_cached(tuple(int(s) for s in shape))


def flat_index(xc, shape):
    """Flat indices of coordinate rows xc (..., n); coordinates are reduced modulo the shape."""
    xc = np.asarray(xc, dtype=np.int64) % np.asarray(shape, dtype=np.int64)
    return np.ravel_multi_index(tuple(np.moveaxis(xc, -1, 0)), shape)


@functools.lru_cache(maxsize=8)
def _add_table_cached(shape):
    c = coords(shape)
    out = flat_index(c[:, None, :] + c[None, :, :], shape).astype(np.int32)
    out.setflags(write=False)
    return out


def add_table(shape):
    """ADD[x, r] = flat index of x + r, shape (|G|, |G|), int32 (cached; 31 MB for |G| = 2809)."""
    return _add_table_cached(tuple(int(s) for s in shape))


def translate(table, x):
    """Return S with S[r] = table[x + r].  x is a flat index or a coordinate tuple."""
    table = np.asarray(table)
    xc = coords(table.shape)[int(x)] if np.ndim(x) == 0 else np.asarray(x)
    return np.roll(table, tuple(-int(v) for v in xc), axis=tuple(range(table.ndim)))


# --------------------------------------------------------------------------------------------
# tasks
# --------------------------------------------------------------------------------------------
def true_table(task, p, n=2, w=None):
    """Ground-truth table f of a task.
    "add": f(a,b) = a+b mod p (n=2);  "mul": f(a,b) = a*b mod p (n=2);
    "lin": f(x) = <w,x> mod p on Z_p^n, default w = LIN_W = (3,5,2,6) (p=7, n=4)."""
    p = int(p)
    if task == "add":
        a = np.arange(p)
        return (a[:, None] + a[None, :]) % p
    if task == "mul":
        a = np.arange(p)
        return (a[:, None] * a[None, :]) % p
    if task == "lin":
        w = np.asarray(LIN_W if w is None else w, dtype=np.int64)
        n = len(w)
        shape = group_shape(p, n)
        return ((coords(shape) @ w) % p).reshape(shape)
    raise ValueError(f"unknown task {task!r}")


def make_error_table(M, f, q):
    """E = (M - f) mod q as int64 (safe for uint8 inputs)."""
    return (np.asarray(M, dtype=np.int64) - np.asarray(f, dtype=np.int64)) % int(q)


# --------------------------------------------------------------------------------------------
# twirled channel of the BLR vote
# --------------------------------------------------------------------------------------------
def twirled_counts_brute(E, q):
    """Reference: N[x, h] = #{r in G : E(x+r) - E(r) = h mod q}, plain loops."""
    E = np.asarray(E, dtype=np.int64)
    shape = E.shape
    C = coords(shape)
    N = len(C)
    out = np.zeros((N, q), dtype=np.int64)
    for ix in range(N):
        for ir in range(N):
            s = tuple((C[ix] + C[ir]) % shape)
            out[ix, (E[s] - E[tuple(C[ir])]) % q] += 1
    return out


def _twirled_counts_enum(E, q, chunk=256):
    E = np.asarray(E, dtype=np.int64)
    Ef = E.ravel() % q
    N = Ef.size
    ADD = add_table(E.shape)
    out = np.empty((N, q), dtype=np.int64)
    for lo in range(0, N, chunk):
        hi = min(N, lo + chunk)
        v = (Ef[ADD[lo:hi]] - Ef[None, :]) % q
        v += q * np.arange(hi - lo)[:, None]
        out[lo:hi] = np.bincount(v.ravel(), minlength=(hi - lo) * q).reshape(hi - lo, q)
    return out


def _twirled_counts_fft(E, q):
    E = np.asarray(E, dtype=np.int64) % q
    N = E.size
    axes = tuple(range(1, E.ndim + 1))
    j = np.arange(q).reshape((q,) + (1,) * E.ndim)
    phi = np.exp(2j * np.pi * ((j * E[None]) % q) / q)            # (q, *shape)
    F = np.fft.fftn(phi, axes=axes)
    A = np.fft.ifftn(F.real ** 2 + F.imag ** 2, axes=axes)        # A_j(x) = sum_r phi_j(x+r) conj(phi_j(r))
    C = np.fft.fft(A, axis=0) / q                                 # inverse DFT over j -> counts[h, x]
    C = C.reshape(q, N).T
    R = np.rint(C.real)
    dev = max(float(np.abs(C.real - R).max()), float(np.abs(C.imag).max()))
    if dev > 1e-6:
        raise FloatingPointError(f"twirled_counts(fft): not integral to 1e-6 (dev={dev:.2e}); use method='enum'")
    R = R.astype(np.int64)
    assert (R.sum(1) == N).all() and (R >= 0).all()
    return R


def twirled_counts(E, q, method="fft"):
    """Exact integer counts N[x, h] = #{r : E(x+r) - E(r) = h mod q}; shape (|G|, q); rows sum to |G|.
    E: error table of shape (p_1,...,p_n) with values in Z_q.  method in {"fft", "enum", "brute"}."""
    q = int(q)
    if method == "fft":
        return _twirled_counts_fft(E, q)
    if method == "enum":
        return _twirled_counts_enum(E, q)
    if method == "brute":
        return twirled_counts_brute(E, q)
    raise ValueError(method)


def twirled_channel(E, q, method="fft"):
    """T[x, h] = Pr_r[E(x+r) - E(r) = h mod q], exact (integer counts / |G|); shape (|G|, q)."""
    return twirled_counts(E, q, method) / float(np.asarray(E).size)


# --------------------------------------------------------------------------------------------
# bilinear 4-query vote (multiplication)
# --------------------------------------------------------------------------------------------
def bilinear_counts_brute(E, q):
    E = np.asarray(E, dtype=np.int64)
    p1, p2 = E.shape
    out = np.zeros((p1 * p2, q), dtype=np.int64)
    for x in range(p1):
        for y in range(p2):
            for r in range(p1):
                for s in range(p2):
                    d = E[(x + r) % p1, (y + s) % p2] - E[r, (y + s) % p2] - E[(x + r) % p1, s] + E[r, s]
                    out[x * p2 + y, d % q] += 1
    return out


def bilinear_counts(E, q):
    """Exact counts of D = e(x+r,y+s) - e(r,y+s) - e(x+r,s) + e(r,s) mod q over all (r,s), for every
    (x,y) in G = Z_p1 x Z_p2.  Shape (p1*p2, q), rows ordered by flat index x*p2 + y, rows sum to p1*p2.
    This D is the error of the vote M(x+r,y+s) - M(r,y+s) - M(x+r,s) + M(r,s) for a bilinear f."""
    E = np.asarray(E, dtype=np.int64) % q
    q = int(q)
    p1, p2 = E.shape
    ys = (np.arange(p2)[:, None] + np.arange(p2)[None, :]) % p2          # [y, s] -> y + s
    off = q * np.arange(p2)[None, :, None]
    out = np.empty((p1, p2, q), dtype=np.int64)
    for x in range(p1):
        A = (np.roll(E, -x, axis=0) - E) % q                              # A[r, s] = e(x+r, s) - e(r, s)
        D = (A[:, ys] - A[:, None, :]) % q                                # [r, y, s]
        out[x] = np.bincount((D + off).ravel(), minlength=p2 * q).reshape(p2, q)
    return out.reshape(p1 * p2, q)


def bilinear_channel(E, q):
    """Exact channel of the 4-query multiplication vote; shape (p1*p2, q); column 0 = vote correct."""
    return bilinear_counts(E, q) / float(np.asarray(E).size)


# --------------------------------------------------------------------------------------------
# invariance twirl for f(a,b) = a + b
# --------------------------------------------------------------------------------------------
def invariance_counts_add(E, q):
    """N[(a,b), h] = #{r in Z_p : E(a+r, b-r) = h}: the error histogram on the level set a+b = const.
    Shape (p*p, q), rows sum to p.  (The vote M(a+r, b-r) has offset E(a+r, b-r) from the truth.)"""
    E = np.asarray(E, dtype=np.int64) % q
    p = E.shape[0]
    assert E.shape == (p, p)
    a = np.arange(p)
    level = (a[:, None] + a[None, :]) % p
    hist = np.bincount((level * q + E).ravel(), minlength=p * q).reshape(p, q)
    return hist[level.ravel()]


def invariance_channel_add(E, q):
    return invariance_counts_add(E, q) / float(np.asarray(E).shape[0])


# --------------------------------------------------------------------------------------------
# label-free BLR test
# --------------------------------------------------------------------------------------------
def blr_pass_rate(M, q, method="fft"):
    """Exact Pr_{x,y uniform on G}[M(x) + M(y) = M(x+y) mod q].  No labels needed.
    "fft": pi = (1/q) sum_j sum_alpha |phihat_j(alpha)|^2 phihat_j(alpha), phi_j = exp(2 pi i j M/q).
    "enum": direct enumeration of all |G|^2 pairs (reference)."""
    M = np.asarray(M, dtype=np.int64) % q
    N = M.size
    if method == "enum":
        Mf = M.ravel()
        ADD = add_table(M.shape)
        cnt = 0
        for lo in range(0, N, 256):
            hi = min(N, lo + 256)
            cnt += int((((Mf[lo:hi, None] + Mf[None, :]) % q) == Mf[ADD[lo:hi]]).sum())
        return cnt / float(N * N)
    axes = tuple(range(1, M.ndim + 1))
    j = np.arange(q).reshape((q,) + (1,) * M.ndim)
    phi = np.exp(2j * np.pi * ((j * M[None]) % q) / q)
    F = np.fft.fftn(phi, axes=axes) / N
    val = float(((F.real ** 2 + F.imag ** 2) * F).sum().real) / q
    cnt = round(val * N * N)
    if abs(val * N * N - cnt) > 1e-4:
        raise FloatingPointError("blr_pass_rate(fft): count not integral; use method='enum'")
    return cnt / float(N * N)


def lam_hat_from_pass(pi, q):
    """Label-free estimate of the normalised advantage: ((pi - 1/q)/(1 - 1/q))^(1/3)."""
    return np.cbrt((np.asarray(pi, dtype=float) - 1.0 / q) / (1.0 - 1.0 / q))


def eps_hat_from_pass(pi, q):
    """Label-free estimate of the error rate under the depolarizing law (C6)."""
    return (1.0 - lam_hat_from_pass(pi, q)) * (1.0 - 1.0 / q)


# --------------------------------------------------------------------------------------------
# depolarizing law and exponents
# --------------------------------------------------------------------------------------------
def lam(eps, q):
    """Normalised advantage lambda = 1 - eps/(1 - 1/q)."""
    return 1.0 - np.asarray(eps, dtype=float) / (1.0 - 1.0 / q)


def eps_from_lam(lam_, q):
    return (1.0 - np.asarray(lam_, dtype=float)) * (1.0 - 1.0 / q)


def pc_law(eps, q, c):
    """Pr[signed sum of c i.i.d. depolarizing errors = 0] = 1/q + (1 - 1/q) lambda^c."""
    return 1.0 / q + (1.0 - 1.0 / q) * lam(eps, q) ** c


def pw_law(eps, q, c):
    """Pr[signed sum of c i.i.d. depolarizing errors = h] for each fixed h != 0: (1 - lambda^c)/q."""
    return (1.0 - lam(eps, q) ** c) / q


def depolarizing_channel(eps, q, c):
    t = np.full(int(q), float(pw_law(eps, q, c)))
    t[0] = float(pc_law(eps, q, c))
    return t


def hellinger_rate(t0, th):
    """Per-vote error exponent -ln(1 - (sqrt t0 - sqrt th)^2); 0 where th >= t0 (no decay)."""
    t0 = np.asarray(t0, dtype=float)
    th = np.asarray(th, dtype=float)
    with np.errstate(divide="ignore"):
        r = -np.log(1.0 - (np.sqrt(t0) - np.sqrt(th)) ** 2)
    return np.where(t0 > th, r, 0.0)


def rate_law(eps, q, c):
    """Exponent of the depolarizing channel with c error terms."""
    return hellinger_rate(pc_law(eps, q, c), pw_law(eps, q, c))


def channel_stats(T):
    """Per-input summary of a channel T (X, q) (column 0 = truth).  Returns a dict of arrays:
    t0, tw (largest wrong mass), hstar (its offset), margin = t0 - tw, strict_mode (t0 > tw), rate."""
    T = np.asarray(T, dtype=float)
    t0 = T[:, 0]
    hstar = 1 + T[:, 1:].argmax(1)
    tw = T[np.arange(len(T)), hstar]
    return dict(t0=t0, tw=tw, hstar=hstar, margin=t0 - tw, strict_mode=t0 > tw, rate=hellinger_rate(t0, tw))


def channel_rate(T):
    """I_x = -ln(1 - (sqrt T_x(0) - sqrt T_x(h*))^2), h* the strongest wrong value; 0 if not strict mode."""
    return channel_stats(T)["rate"]


def votes_needed(rate, delta, q):
    """Smallest k with (q-1) exp(-k rate) <= delta (union bound with the worst exponent); inf if rate = 0."""
    rate = np.asarray(rate, dtype=float)
    with np.errstate(divide="ignore"):
        k = np.ceil(np.log((q - 1) / delta) / rate)
    return np.where(rate > 0, np.maximum(k, 1.0), np.inf)


def lam_c_heuristic(G, q):
    """Heuristic critical advantage from lambda_c^2 (q-1)/q = 2 sqrt(ln(|G| q)/(|G| q))  (claim C3)."""
    return math.sqrt(2.0 * math.sqrt(math.log(G * q) / (G * q)) * q / (q - 1.0))


# --------------------------------------------------------------------------------------------
# plurality failure of Multinomial(k, T_x)
# --------------------------------------------------------------------------------------------
def chernoff_union_bound(T, k):
    """Upper bound on delta_k(x) = Pr[plurality of k votes ~ T_x is not uniquely the truth]:
        sum_{h != 0} (1 - (sqrt T_x(0) - sqrt T_x(h))^2)^k,
    with the term set to 1 whenever T_x(h) >= T_x(0) (the Chernoff argument needs T_x(0) > T_x(h)),
    and the total clipped at 1.  T: (X, q) or (q,).  k scalar -> (X,); k array (K,) -> (K, X)."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    t0 = T[:, :1]
    th = T[:, 1:]
    base = np.where(th < t0, 1.0 - (np.sqrt(t0) - np.sqrt(th)) ** 2, 1.0)        # (X, q-1)
    ks = np.atleast_1d(np.asarray(k, dtype=float))
    out = np.stack([np.minimum(1.0, (base ** kk).sum(1)) for kk in ks])
    return out[0] if np.ndim(k) == 0 else out


def plurality_fail_enum(t, k):
    """Exact failure probability for ONE probability vector t by enumerating all q^k vote strings."""
    import itertools
    t = np.asarray(t, dtype=float)
    q = len(t)
    ok = 0.0
    for votes in itertools.product(range(q), repeat=k):
        cnt = np.bincount(votes, minlength=q)
        if cnt[0] > cnt[1:].max():
            ok += float(np.prod(t[list(votes)]))
    return 1.0 - ok


def plurality_fail_exact(T, k):
    """Exact delta_k(x) = 1 - Pr[N_0 > max_{h != 0} N_h], N ~ Multinomial(k, T_x), for every row of T.
    Uses Pr[N_0 = m, all others < m] = (k!/m!) T_0^m [z^(k-m)] prod_{h != 0} sum_{j < m} (T_h z)^j / j!.
    Cost O(X q k^3) (about 1 s for X = 2809, q = 53, k = 33).  Sums of non-negative terms only, so the
    success probability is accurate to ~1e-13 relative; the returned failure 1 - success therefore has
    ABSOLUTE accuracy ~1e-12: below that, quote chernoff_union_bound instead."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    k = int(k)
    if not 1 <= k <= 150:
        raise ValueError("plurality_fail_exact supports 1 <= k <= 150")
    X, q = T.shape
    t0 = T[:, 0]
    wrong = [T[:, h] for h in range(1, q) if T[:, h].any()]
    success = np.zeros(X)
    lg = [math.lgamma(i + 1.0) for i in range(k + 1)]
    for m in range(1, k + 1):
        d = k - m                                   # votes left for wrong values
        if d > (m - 1) * len(wrong):
            continue                                # cannot place d votes with every count < m
        poly = np.zeros((X, d + 1))
        poly[:, 0] = 1.0
        jmax = min(m - 1, d)
        for th in wrong:
            if jmax == 0:
                break
            new = poly.copy()
            c = np.ones(X)
            for j in range(1, jmax + 1):
                c = c * th / j                      # th^j / j!
                new[:, j:] += poly[:, :d + 1 - j] * c[:, None]
            poly = new
        with np.errstate(divide="ignore"):
            logc = lg[k] - lg[m] + m * np.log(t0)
        success += np.where(t0 > 0, np.exp(logc), 0.0) * poly[:, d]
    return np.clip(1.0 - success, 0.0, 1.0)


def plurality_fail_mc(T, k, n_samples, rng, chunk=4_000_000):
    """Monte Carlo estimate of delta_k(x) for every row of T: n_samples draws of Multinomial(k, T_x)
    per input, failure = truth is not the strict plurality.  Returns (X,) float64 failure fractions
    (standard error sqrt(d(1-d)/n_samples)).  Vectorised over inputs."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    X, q = T.shape
    keep = np.concatenate([[True], T[:, 1:].any(0)])        # drop wrong values that never occur
    P = T[:, keep]
    P = P / P.sum(1, keepdims=True)
    per = max(1, int(chunk // max(1, X * P.shape[1])))
    fails = np.zeros(X, dtype=np.int64)
    done = 0
    while done < n_samples:
        s = min(per, n_samples - done)
        cnt = rng.multinomial(int(k), P, size=(s, X))
        if P.shape[1] == 1:
            pass                                            # no wrong value ever: never fails
        else:
            fails += (cnt[..., 0] <= cnt[..., 1:].max(-1)).sum(0)
        done += s
    return fails / float(n_samples)


# --------------------------------------------------------------------------------------------
# actual voting on a table
# --------------------------------------------------------------------------------------------
def plurality(votes, q):
    """Row-wise plurality of an (m, k) integer vote array with values in Z_q.
    Returns (winner, tied): winner = smallest value among the most frequent; tied = True when the
    maximum count is attained by two or more values (to be counted as a failure)."""
    votes = np.asarray(votes, dtype=np.int64)
    m = votes.shape[0]
    cnt = np.bincount((votes + q * np.arange(m)[:, None]).ravel(), minlength=m * q).reshape(m, q)
    top = cnt.max(1)
    return cnt.argmax(1), (cnt == top[:, None]).sum(1) > 1


def sc_votes(table, xs, k, rng, q=None):
    """Real BLR votes V_r(x) = M(x+r) - M(r) mod q with r i.i.d. uniform on G.
    table: M of shape (p_1..p_n); xs: flat indices (m,); returns (m, k) int64.  q defaults to p_1."""
    table = np.asarray(table)
    q = int(table.shape[0] if q is None else q)
    Mf = table.ravel().astype(np.int64)
    C = coords(table.shape)
    xs = np.asarray(xs, dtype=np.int64)
    r = rng.integers(0, Mf.size, size=(len(xs), int(k)))
    xr = flat_index(C[xs][:, None, :] + C[r], table.shape)
    return (Mf[xr] - Mf[r]) % q


def sc_predict(table, xs, k, rng, q=None):
    """Self-corrected prediction SC_k(x): plurality of k real votes.  Returns (pred, tied)."""
    table = np.asarray(table)
    q = int(table.shape[0] if q is None else q)
    return plurality(sc_votes(table, xs, k, rng, q), q)


def sc_fail(table, f, xs, k, rng, q=None):
    """Bool per input: the self-corrector fails (wrong plurality or a tie for first place)."""
    pred, tied = sc_predict(table, xs, k, rng, q)
    return (pred != np.asarray(f).ravel()[np.asarray(xs)]) | tied


def bilinear_votes(table, xs, k, rng, q=None):
    """Real 4-query votes M(x+r,y+s) - M(r,y+s) - M(x+r,s) + M(r,s) mod q on a 2-D table; (m, k)."""
    table = np.asarray(table)
    p1, p2 = table.shape
    q = int(p1 if q is None else q)
    M = table.astype(np.int64)
    xs = np.asarray(xs, dtype=np.int64)
    x = (xs // p2)[:, None]
    y = (xs % p2)[:, None]
    r = rng.integers(0, p1, size=(len(xs), int(k)))
    s = rng.integers(0, p2, size=(len(xs), int(k)))
    return (M[(x + r) % p1, (y + s) % p2] - M[r, (y + s) % p2] - M[(x + r) % p1, s] + M[r, s]) % q


def invariance_votes_add(table, xs, k, rng):
    """Votes of the invariance twirl for f(a,b) = a+b: M(a+r, b-r), r uniform on Z_p; (m, k)."""
    table = np.asarray(table)
    p = table.shape[0]
    M = table.astype(np.int64)
    xs = np.asarray(xs, dtype=np.int64)
    a = (xs // p)[:, None]
    b = (xs % p)[:, None]
    r = rng.integers(0, p, size=(len(xs), int(k)))
    return M[(a + r) % p, (b - r) % p]


# --------------------------------------------------------------------------------------------
# model zoo
# --------------------------------------------------------------------------------------------
@functools.lru_cache(maxsize=1)
def _index():
    with open(os.path.join(ZOO_DIR, "index.json")) as fh:
        return json.load(fh)


@functools.lru_cache(maxsize=1)
def _by_id():
    return {m["id"]: m for m in _index()["models"]}


def load_index(full=False):
    """List of model records (dicts) from zoo/index.json; full=True returns the whole index dict
    (keys: schema, config, runs, models, ...)."""
    return _index() if full else _index()["models"]


def get_record(model_id):
    return _by_id()[model_id]


@functools.lru_cache(maxsize=256)
def load_run(file):
    """All arrays of one run file (path relative to the paper directory, e.g. 'zoo/xxx.npz'):
    tables (S, p, ..., p) uint8, steps (S,), train_mask (p, ..., p) bool."""
    with np.load(os.path.join(ROOT, file)) as z:
        return {k: z[k] for k in z.files}


def load_table(model_id):
    """Prediction table M of a zoo model: int64 array of shape (p,)*n."""
    rec = get_record(model_id)
    return load_run(rec["file"])["tables"][rec["snap"]].astype(np.int64)


def load_train_mask(model_id):
    """Bool table: True where the input belonged to the model's training set."""
    return load_run(get_record(model_id)["file"])["train_mask"].astype(bool)


def model_true_table(model_id):
    rec = get_record(model_id)
    return true_table(rec["task"], rec["p"], rec["n"])


def error_table(model_id):
    """E = (M - f) mod q of a zoo model: int64 array of shape (p,)*n."""
    rec = get_record(model_id)
    return make_error_table(load_table(model_id), model_true_table(model_id), rec["q"])


def load_logits(model_id):
    """(|G|, q) float16 logits of an add/memo model (rows in flat-index order), from cache/."""
    rec = get_record(model_id)
    if not rec.get("logits_file"):
        raise KeyError(f"{model_id} has no saved logits")
    with np.load(os.path.join(ROOT, rec["logits_file"])) as z:
        return z["logits"]


# --------------------------------------------------------------------------------------------
# self-tests
# --------------------------------------------------------------------------------------------
def _selftest(verbose=True):
    import time
    t_start = time.time()
    rng = np.random.default_rng(12345)
    log = []

    def ok(name, detail=""):
        log.append(name)
        if verbose:
            print(f"  ok  {name}  {detail}")

    # 1. twirled channel: fft == enum == brute on random small cases (including q != p, mixed shapes)
    cases = [((5,), 5), ((7,), 3), ((6,), 4), ((3, 3), 3), ((4, 4), 4), ((5, 5), 5), ((4, 6), 2),
             ((3, 3, 3), 3), ((2, 3, 4), 5), ((7, 7), 7), ((3, 3, 3, 3), 3)]
    n_checked = 0
    for shape, q in cases:
        for dens in (0.05, 0.3, 1.0):
            E = rng.integers(0, q, size=shape) * (rng.random(shape) < dens)
            b = twirled_counts_brute(E, q)
            assert np.array_equal(twirled_counts(E, q, "fft"), b), (shape, q, "fft")
            assert np.array_equal(twirled_counts(E, q, "enum"), b), (shape, q, "enum")
            assert (b.sum(1) == E.size).all() and b[0, 0] == E.size
            n_checked += 1
    ok("twirled_counts: fft == enum == brute", f"{n_checked} random cases")
    for shape, q in (((53, 53), 53), ((47, 47), 47), ((7, 7, 7, 7), 7), ((31, 31), 31)):
        E = rng.integers(0, q, size=shape) * (rng.random(shape) < 0.4)
        assert np.array_equal(twirled_counts(E, q, "fft"), twirled_counts(E, q, "enum")), shape
    ok("twirled_counts: fft == enum at zoo sizes", "(53,53) (47,47) (31,31) (7,7,7,7)")

    # 2. bilinear channel
    for shape, q in (((5, 5), 5), ((4, 6), 3), ((7, 7), 7), ((3, 5), 2)):
        E = rng.integers(0, q, size=shape) * (rng.random(shape) < 0.5)
        b = bilinear_counts_brute(E, q)
        assert np.array_equal(bilinear_counts(E, q), b), shape
        assert (b.sum(1) == E.size).all()
    # the vote really returns xy + D for M = xy + e
    p = 11
    f = true_table("mul", p)
    E = rng.integers(0, p, size=(p, p)) * (rng.random((p, p)) < 0.3)
    M = (f + E) % p
    xs = np.arange(p * p)
    v = bilinear_votes(M, xs, 4000, rng, p)
    emp = np.stack([np.bincount((v[i] - f.ravel()[i]) % p, minlength=p) for i in xs]) / 4000.0
    Tb = bilinear_channel(E, p)
    assert np.abs(emp - Tb).max() < 6 * 0.5 / math.sqrt(4000), np.abs(emp - Tb).max()
    ok("bilinear_counts == brute; real 4-query votes match the channel", f"max dev {np.abs(emp - Tb).max():.4f}")

    # 3. depolarizing law algebra, and agreement with exact channels of i.i.d. error fields
    for q in (2, 3, 7, 53):
        for c in (1, 2, 3, 4):
            for eps in (0.0, 0.1, 0.5, 1 - 1 / q, 1.0):
                assert abs(pc_law(eps, q, c) + (q - 1) * pw_law(eps, q, c) - 1) < 1e-12
        assert abs(pc_law(0.2, q, 1) - 0.8) < 1e-12 and abs(float(eps_from_lam(lam(0.37, q), q)) - 0.37) < 1e-12
    p = q = 53
    devs = []
    for eps in (0.1, 0.5, 0.9):
        E = rng.integers(1, q, size=(p, p)) * (rng.random((p, p)) < eps)
        T = twirled_channel(E, q)[1:]                       # x != 0
        e_emp = (E != 0).mean()
        devs.append(abs(T[:, 0].mean() - pc_law(e_emp, q, 2)))
        assert devs[-1] < 0.01, devs
        assert abs(T[:, 1:].mean() - pw_law(e_emp, q, 2)) < 0.001
        Tb = bilinear_channel(E, q)
        nz = (np.arange(p * p) // p != 0) & (np.arange(p * p) % p != 0)
        assert abs(Tb[nz, 0].mean() - pc_law(e_emp, q, 4)) < 0.01
        pi = blr_pass_rate(E, q)                            # f = 0 is a homomorphism, M = E
        assert abs(pi - pc_law(e_emp, q, 3)) < 0.01
    ok("depolarizing law: algebra + i.i.d. fields (c = 2, 3, 4)", f"max |T0 - law| at c=2: {max(devs):.4f}")

    # 4. worst-case facts: T_x(0) >= 1 - 2 eps ; 1 - pi <= 3 eps
    for _ in range(40):
        shape, q = cases[rng.integers(len(cases))]
        E = rng.integers(0, q, size=shape) * (rng.random(shape) < rng.random())
        eps = (E != 0).mean()
        assert (twirled_channel(E, q)[:, 0] >= 1 - 2 * eps - 1e-12).all()
        assert 1 - blr_pass_rate(E, q) <= 3 * eps + 1e-12
        assert abs(blr_pass_rate(E, q) - blr_pass_rate(E, q, "enum")) < 1e-12
    ok("T_x(0) >= 1 - 2 eps;  1 - pi <= 3 eps;  blr fft == enum", "40 random tables")

    # 5. plurality failure: exact == enumeration == closed forms; Chernoff bound >= exact; MC agrees
    for q, k in ((2, 1), (2, 4), (3, 5), (4, 6), (5, 4), (3, 7)):
        Tr = rng.dirichlet(np.ones(q), size=4)
        ex = plurality_fail_exact(Tr, k)
        en = np.array([plurality_fail_enum(t, k) for t in Tr])
        assert np.abs(ex - en).max() < 1e-12, (q, k, ex, en)
    Tr = rng.dirichlet(np.ones(9) * 0.5, size=300)
    Tr[:20, 3] = 0.0
    Tr /= Tr.sum(1, keepdims=True)
    t0 = Tr[:, 0]
    assert np.abs(plurality_fail_exact(Tr, 1) - (1 - t0)).max() < 1e-12
    assert np.abs(plurality_fail_exact(Tr, 2) - (1 - t0 ** 2)).max() < 1e-12
    assert np.abs(plurality_fail_exact(Tr, 3) - (1 - 3 * t0 ** 2 * (1 - t0) - t0 ** 3)).max() < 1e-12
    worst = 0.0
    for k in (1, 2, 3, 5, 9, 17, 33, 65, 129):
        ex = plurality_fail_exact(Tr, k)
        bd = chernoff_union_bound(Tr, k)
        assert (bd >= ex - 1e-12).all(), (k, (ex - bd).max())
        if k in (5, 33):
            mc = plurality_fail_mc(Tr, k, 4000, rng)
            z = np.abs(mc - ex) / np.sqrt(np.maximum(ex * (1 - ex), 1e-4) / 4000)
            assert z.max() < 6, (k, z.max())
            worst = max(worst, float(z.max()))
    assert chernoff_union_bound(Tr, np.array([3, 9])).shape == (2, 300)
    ok("plurality_fail_exact == enumeration / closed forms; Chernoff >= exact; MC consistent",
       f"max MC z-score {worst:.2f} over 600 (input, k) pairs")

    # 6. real self-correction votes vs the exact channel
    for task, p, n in (("add", 13, 2), ("lin", 7, 4)):
        f = true_table(task, p, n)
        q = p
        E = rng.integers(0, q, size=f.shape) * (rng.random(f.shape) < 0.35)
        M = (f + E) % q
        xs = np.arange(f.size)
        pred, tied = sc_predict(f, xs, 5, rng, q)
        assert (pred == f.ravel()).all() and not tied.any()            # a perfect model is never changed
        T = twirled_channel(make_error_table(M, f, q), q)
        for k in (1, 5, 15):
            ex = plurality_fail_exact(T, k)
            reps = 300
            emp = np.mean([sc_fail(M, f, xs, k, rng, q) for _ in range(reps)], axis=0)
            z = (emp.mean() - ex.mean()) / math.sqrt(max(ex.mean() * (1 - ex.mean()), 1e-6) / (reps * f.size))
            assert abs(z) < 5, (task, k, emp.mean(), ex.mean())
    ok("real votes M(x+r) - M(r): failure rate matches exact Multinomial(k, T_x) plurality", "add p=13, lin Z_7^4")

    # 7. invariance twirl channel vs real votes; group helpers
    p = 11
    f = true_table("add", p)
    E = rng.integers(0, p, size=(p, p)) * (rng.random((p, p)) < 0.3)
    M = (f + E) % p
    Ti = invariance_channel_add(E, p)
    v = invariance_votes_add(M, np.arange(p * p), 3000, rng)
    emp = np.stack([np.bincount((v[i] - f.ravel()[i]) % p, minlength=p) for i in range(p * p)]) / 3000.0
    assert np.abs(emp - Ti).max() < 6 * 0.5 / math.sqrt(3000)
    shape = (3, 4, 5)
    tab = rng.integers(0, 9, size=shape)
    C = coords(shape)
    for x in (0, 7, 59):
        S = translate(tab, x)
        for r in (0, 13, 44):
            assert S[tuple(C[r])] == tab[tuple((C[x] + C[r]) % shape)]
            assert add_table(shape)[x, r] == flat_index(C[x] + C[r], shape)
    assert np.array_equal(true_table("lin", 7).ravel()[:8], (np.arange(8) % 7 * 6 + (np.arange(8) // 7) * 2) % 7)
    ok("invariance channel == real orbit votes; translate / add_table / flat_index consistent")

    # 8. zoo round trip (only if the zoo has been built)
    if os.path.exists(os.path.join(ZOO_DIR, "index.json")):
        recs = load_index()
        pick = [recs[i] for i in rng.choice(len(recs), size=min(40, len(recs)), replace=False)]
        for rec in pick:
            Mz = load_table(rec["id"])
            Ez = error_table(rec["id"])
            assert Mz.shape == group_shape(rec["p"], rec["n"]) and Mz.max() < rec["q"]
            assert abs((Ez != 0).mean() - rec["eps"]) < 1e-12, rec["id"]
            mask = load_train_mask(rec["id"])
            assert abs((Ez[mask] == 0).mean() - rec["train_acc"]) < 1e-12, rec["id"]
            if rec.get("logits_file") and os.path.exists(os.path.join(ROOT, rec["logits_file"])):
                assert np.array_equal(load_logits(rec["id"]).astype(np.float32).argmax(1), Mz.ravel()), rec["id"]
        ok("zoo: tables reproduce the eps / train_acc stored in index.json", f"{len(pick)} of {len(recs)} models sampled")
    else:
        print("  --  zoo not built yet: zoo round-trip test skipped")
    if verbose:
        print(f"core.py self-test passed: {len(log)} groups of checks in {time.time() - t_start:.1f} s")
    return True


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    else:
        print(__doc__)
