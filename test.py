import psutil
#nombre de coeur dasn la console 
print("Number of cores in system", psutil.cpu_count())
print("\nNumber of physical cores in system",)
# stat principale du CPU dans la console
print("CPU Statistics", psutil.cpu_stats()) 
#cette fonction fournit des statistiques d'utilisation du disque sous forme de tuple pour un chemin donné. 
# L'espace total, l'espace utilisé et l'espace libre sont exprimés en octets, ainsi que le pourcentage d'utilisation.

print(psutil.disk_usage('/'))




