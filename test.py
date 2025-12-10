import psutil, time

cores = psutil.cpu_count()
for p in psutil.process_iter(): p.cpu_percent()
time.sleep(0.1)

procs = [(p.cpu_percent()/cores, p.pid, p.name())
         for p in psutil.process_iter() if p.pid not in (0,4)]

for cpu,pid,name in sorted(procs, reverse=True)[:3]:
    print(f"{name} (PID {pid}) — {cpu:.2f}% CPU")