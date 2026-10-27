"""Print each narration line beside the balloons/captions of its panel, with an echo score
(share of the narration's content words that also appear in the panel's lettering)."""
import json, re, sys, yaml
ch = sys.argv[1]
S = yaml.safe_load(open(f'/home/claude/msgf-bible/scripts_v2/{ch}.yaml'))
R = json.load(open(f'/home/claude/msgf-bible/recaps_v2/{ch}.json'))
P = {p['id']: p for p in S['panels']}
STOP = set('a an the and or but of to in on at for with is are was were be been it its it\'s he she they them his her their him i you we me my your our this that these those as by from into up out so if then than not no just one more all any'.split())
def words(t): return [w for w in re.findall(r"[a-z']+", t.lower()) if w not in STOP]
thr = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
for e in R:
    p = P[e['panel']]
    let = [f"{l.get('who','')}:{l.get('type','')}: {l['text']}" for l in (p.get('lines') or []) if l.get('text')]
    let += [f"ui: {u.get('text') or u.get('title') or ''}" for u in (p.get('ui') or []) if isinstance(u, dict)]
    lw = set(words(' '.join(let)))
    nw = words(e['text'])
    score = sum(1 for w in nw if w in lw) / max(1, len(nw))
    if score >= thr:
        print(f"{e['panel']} [{score:.2f}] N: {e['text']}")
        for l in let: print('      ', l)
