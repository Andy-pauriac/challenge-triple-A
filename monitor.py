from flask import Flask, render_template
import psutil, socket, time, platform

# Configuration de l'application
app = Flask(__name__)

# Route pour afficher les différentes pages
@app.route("/")
def index():

    # SECTION SYSTEME
    host_name = socket.gethostname()
    os = platform.system()
    os_release = platform.release()
    uptime = psutil.boot_time()
    uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(uptime))
    user_number = psutil.users()
    user_number = len(user_number)

    # SECTION CPU
    cpu_cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()

    # SECTION MEMOIRE
    ram = psutil.virtual_memory()
    ram_available = f"{ram.available /  (1024 ** 3):.2f}"
    ram_total = f"{ram.total /  (1024 ** 3):.2f}"
    ram_used = f"{ram.used /  (1024 ** 3):.2f}"
    ram_percent = ram.percent

    # SECTION RESEAU
    ip = psutil.net_connections(kind='inet') 

    for i in ip:
        ipv4 = i.laddr
        ipv6 = i.raddr
        status = i.status

    # SECTION PROCESSUS
    

    # SECTION FICHIER

    return render_template("template.html", cpu_cores = cpu_cores, 
                           cpu_percent = cpu_percent,
                           cpu_freq = cpu_freq,
                           host_name = host_name,
                           ipv4 = ipv4,
                           ipv6 = ipv6,
                           status = status,
                           uptime = uptime,
                           os = os,
                           os_release = os_release,
                           user_number = user_number,
                           ram_available = ram_available,
                           ram_used = ram_used,
                           ram_total = ram_total,
                           ram_percent = ram_percent,)


