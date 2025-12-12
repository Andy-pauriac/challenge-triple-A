from flask import Flask, render_template
import psutil, time, platform, os

logo = os.path.join('static', 'logo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = logo

@app.route("/", methods=["GET"])
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')

    # SECTION SYSTEME
    host_name = psutil.users()[0].name
    os_name = platform.system()
    os_release = platform.release()
    uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time()))
    user_number = len(psutil.users())

    # SECTION CPU
    cpu_cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq() 

    # SECTION MEMOIRE
    ram = psutil.virtual_memory()
    ram_available = f"{ram.available / (1024 ** 3):.2f}"
    ram_total = round(ram.total / (1024 ** 3),2)
    ram_used = f"{ram.used / (1024 ** 3):.2f}"
    ram_percent = ram.percent

    # SECTION RESEAU
    ip = psutil.net_connections(kind='inet')
    ipv4 = ipv6 = status = None
    for i in ip:
        ipv4 = i.laddr
        ipv6 = i.raddr
        status = i.status

    # SECTION PROCESSUS 
        # CPU
    num_core = psutil.cpu_count()
    procs_cpu = []

    for p in psutil.process_iter(['pid', 'name']):
        if p.pid in (0, 4):
            continue
            
        try:
            cpu_percent = p.cpu_percent()
            proc_name = p.name()
            
            
            procs_cpu.append((round(cpu_percent / num_core , 2), p.pid, proc_name))
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    procslist_cpu = sorted(procs_cpu, reverse=True)[:3]

        # RAM
    procs_ram = []

    for p in psutil.process_iter(['pid', 'name']):
        if p.pid in (0, 4):
            continue
            
        try:
            memory_percent = p.memory_percent()
            proc_name = p.name()
            
            
            procs_cpu.append((round(memory_percent), p.pid, proc_name))
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    procslist_ram = sorted(procs_ram, reverse=True)[:3]
    
    # SECTION FICHIERS
    if os_name == "Windows":
        root_directory = fr"C:\Users\{host_name}\Downloads"
    else:
        root_directory = r"/home/ubuntu/Bureau/challenge/challenge-triple-A"

    extensions = [".txt", ".py", ".pdf", ".jpg"]
    counts = {ext: 0 for ext in extensions}

    for current_dir, subdirs, files in os.walk(root_directory):
        for filename in files:
            lower_name = filename.lower()
            for ext in extensions:
                if lower_name.endswith(ext):
                    counts[ext] += 1

    total_files = sum(counts.values())

    return render_template(
        "template.html",
        cpu_cores=cpu_cores,
        cpu_percent=cpu_percent,
        cpu_freq=cpu_freq,
        host_name=host_name,
        ipv4=ipv4,
        ipv6=ipv6,
        status=status,
        uptime=uptime,
        os=os_name,
        os_release=os_release,
        user_number=user_number,
        ram_available=ram_available,
        ram_used=ram_used,
        ram_total=ram_total,
        ram_percent=ram_percent,
        root_directory=root_directory,
        total_files=total_files,
        counts=counts,
        procslist_cpu=procslist_cpu,
        procslist_ram=procslist_ram,
        logo=logo,
    )

if __name__ == "__main__":
    app.run(debug=True)
