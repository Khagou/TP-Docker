# TP-Docker
TP-docker deploiement d'une application python avec une base de donnee mariadb sur 2 containers

# TP-Docker
Application python avec une base de donnée MariaDB sur des containers docker

Les images nécessaires ce trouvent dans le repo git et sur le hub docker sur les liens ci dessous:

Python: https://hub.docker.com/repository/docker/khagu/tp-docker-python/general

MariaDB: https://hub.docker.com/repository/docker/khagu/tp-docker-mariadb/general

Installation:

Si vous avez téléchargé les images sur le hub docker commencez par réaliser les commandes suivantes afin des les rename:
- docker tag khagu/tp-docker-python:1.0.0 python-app:latest
- docker tag khagu/tp-docker-mariadb:1.0.0 mariadb-app:latest
- docker rmi khagu/tp-docker-python:1.0.0 khagu/tp-docker-mariadb:1.0.0

Puis placez vous maintenant dans le répertoire contenant le docker compose et exécutez la commande:
- docker compose u -d


Si vous utilisez les dockerfile du repo github:

Placez vous dans le dossier mariadb puis lancez la commande qui suit pour créer l'image maraidb:
- docker build -t mariadb-app .

Placez vous ensuite dans le dossier app-python pous lancez la commande qui suit pour créer l'image de l'application:
- docker build -t python-app .

Puis placez vous maintenant dans le répertoire contenant le docker compose et exécutez la commande:
- docker compose u -d

Pour lancer l'app:
- docker exec -it tp-docker-python-app-1 python3 main.py
