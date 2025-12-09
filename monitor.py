from flask import Flask, render_template, request, url_for
import psutil, socket, time, platform, os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # SECTION SYSTEME
    host_name = socket.gethostname()
    os_name = platform.system()
    os_release = platform.release()
    uptime = psutil.boot_time()
    uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(uptime))
    user_number = len(psutil.users())

    # SECTION CPU
    cpu_cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()

    # SECTION MEMOIRE
    ram = psutil.virtual_memory()
    ram_available = f"{ram.available / (1024 ** 3):.2f}"
    ram_total = f"{ram.total / (1024 ** 3):.2f}"
    ram_used = f"{ram.used / (1024 ** 3):.2f}"
    ram_percent = ram.percent

    # SECTION RESEAU
    ip = psutil.net_connections(kind='inet')
    for i in ip:
        ipv4 = i.laddr
        ipv6 = i.raddr
        status = i.status

     # SECTION ANALYSE DES FICHIERS (TOUT LE DISQUE C:)
    root_directory = r"C:\\"  
    extensions = [".txt", ".py", ".pdf", ".jpg"]
    counts = {ext: 0 for ext in extensions}

    for current_dir, subdirs, files in os.walk(root_directory):
        for filename in files:
            for ext in extensions:
                if filename.lower().endswith(ext):
                    counts[ext] += 1

    total_files = sum(counts.values())

    lines = [f"Dossier analysé : {root_directory} (tous les sous-dossiers)"]
    for ext in extensions:
        count = counts[ext]
        
        percentage = (count / total_files) * 100 if total_files > 0 else  0
        
    lines.append(f"{ext} : {count} fichiers, soit {percentage:.1f}%")
    
    files_stats = "\n".join(lines)


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
        files_stats=files_stats,  
    )
    