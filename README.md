to run jupyter:

jupyter notebook

(Use Control-C to stop this server)
----
pip install -r requirements.txt

pip install notebook

python -m notebook

---
memory profile:

@memory_profiler.profile

python -m memory_profiler main.py

---

from line_profiler_pycharm import profile

@profile

python -m line_profiler main.py.lprof > results.txt
