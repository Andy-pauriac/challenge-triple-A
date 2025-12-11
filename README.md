# challenge-triple-A
# Dashboard Monitoring – Challenge Triple A

Ce projet est une application Flask affichant un tableau de bord de monitoring système ainsi qu’une analyse de fichiers dans un dossier donné.

## 1. Fonctionnalités

### Monitoring système

La page principale du tableau de bord affiche :

- Informations système :
  - Nom de la machine (hostname)
  - Système d’exploitation et version
  - Uptime de la machine
  - Nombre d’utilisateurs connectés
- CPU :
  - Nombre de cœurs
  - Pourcentage d’utilisation
  - Fréquence actuelle / min / max
- Mémoire :
  - RAM totale
  - RAM utilisée
  - RAM disponible
  - Pourcentage d’utilisation
- Réseau :
  - Adresse IPv4
  - Adresse IPv6
  - Statut de la connexion

Ces informations sont récupérées avec le module `psutil`, ainsi que `socket`, `time` et `platform`.

### Analyse des fichiers

L’application analyse un dossier (par défaut `C:\Users\doria\Desktop` ou `C:\Users`) ainsi que tous ses sous-dossiers, et :

- Compte le nombre de fichiers pour 4 extensions précises :
  - `.txt`
  - `.py`
  - `.pdf`
  - `.jpg`
- Calcule le nombre total de fichiers correspondant à ces extensions
- Calcule, pour chaque extension, le pourcentage par rapport au total

Les résultats sont affichés dans la section **Section Fichier** du tableau de bord sous forme de tableau HTML :

- Colonne **Extension**
- Colonne **Nombre**
- Colonne **Pourcentage**

Le calcul est fait en Python avec `os.walk` pour parcourir récursivement les dossiers, puis transmis au template HTML. Le pourcentage peut être calculé soit côté Python, soit directement dans le template (par exemple avec `{{ (count / total_files * 100) | round(1) }}`).

## 2. Structure du projet

Exemple de structure :


- `monitor.py` contient :
  - La création de l’application Flask
  - La route `/` (fonction `index`) qui :
    - Récupère les infos système / CPU / RAM / réseau
    - Parcourt le dossier cible avec `os.walk`
    - Compte les fichiers par extension
    - Calcule le total
    - Passe toutes les variables au template via `render_template`

- `template.html` :
  - Affiche les sections Système, Réseau, CPU, RAM
  - Contient la **Section Fichier** avec :
    - Le dossier analysé
    - Le total de fichiers analysés
    - Le tableau HTML des extensions avec nombre + pourcentage
  - Le texte du tableau peut être forcé en blanc (par exemple `style="color: white;"`) pour rester lisible sur fond sombre.

## 3. Prérequis

- Python 3.x installé
- Modules Python :
  - `flask`
  - `psutil`

## 4. Lancement de l’application

1. Se placer dans le dossier du projet :


2. Lancer l’application :


3. Ouvrir un navigateur et aller sur :

http://127.0.0.1:5000/


À chaque rafraîchissement de la page, l’application :

- Met à jour les informations système et réseau
- Relance l’analyse des fichiers dans le dossier choisi et met à jour le tableau des extensions.

## 5. Personnalisation

- Pour changer le dossier analysé, modifier dans `monitor.py` la variable :

root_directory = r"C:\Users\doria\Desktop" sur windows 
ou 
root_directory = r"/home/ubuntu/Bureau/challenge/challenge-triple-A" sur Ubuntu

en la remplaçant par le chemin souhaité (par exemple `r"C:\Users"` ou un autre dossier).

extensions = [".txt", ".py", ".pdf", ".jpg"]

- Pour ajouter ou retirer des extensions suivies, modifier la liste :



