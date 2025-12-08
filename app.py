from flask import Flask, render_template, request, url_for
import psutil, socket

# Configuration de l'application
app = Flask(__name__)

# Route pour afficher les différentes pages
@app.route("/", methods=["GET"])
def index():

    host_name = socket.gethostname()
    cpu_cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()

    return render_template("template.html", cpu_cores = cpu_cores, 
                           cpu_percent = cpu_percent,
                           cpu_freq = cpu_freq,
                           host_name = host_name)


