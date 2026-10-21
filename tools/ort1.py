#!/usr/bin/env python3
"""Run a script (recap_video.py) unchanged, but give ONNX Runtime a single non-spinning thread.

The container is shared by several concurrent renders; ORT's default pool of busy-waiting threads burns most of its
CPU share while waiting on a descheduled sibling thread. Same model, voice and speed: only thread settings change.
usage: ort1.py SCRIPT.py [script args...]
"""
import os
import runpy
import sys
from pathlib import Path

import cv2
import onnxruntime as ort

cv2.setNumThreads(1)
_orig_init = ort.InferenceSession.__init__


def _init(self, path_or_bytes, sess_options=None, *a, **kw):
    if sess_options is None:
        so = ort.SessionOptions()
        so.intra_op_num_threads = int(os.environ.get("ORT_THREADS", "1"))
        so.inter_op_num_threads = 1
        so.add_session_config_entry("session.intra_op.allow_spinning", "0")
        so.add_session_config_entry("session.inter_op.allow_spinning", "0")
        sess_options = so
    _orig_init(self, path_or_bytes, sess_options, *a, **kw)


ort.InferenceSession.__init__ = _init

script = Path(sys.argv[1]).resolve()
sys.argv = [str(script)] + sys.argv[2:]
sys.path.insert(0, str(script.parent))
runpy.run_path(str(script), run_name="__main__")
