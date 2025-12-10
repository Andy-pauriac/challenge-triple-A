import psutil

procs = [(p.memory_percent(), p.pid, p.name())
         for p in psutil.process_iter(['pid','name'])]

for ram,pid,name in sorted(procs, reverse=True)[:3]:
    print(f"{name} (PID {pid}) — {ram:.2f}% RAM")