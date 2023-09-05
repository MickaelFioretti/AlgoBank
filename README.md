# AlgoBank

P7 - Résolvez des problèmes en utilisant des algorithmes en Python

## Installation

### Prérequis

-   Docker
-   Docker-compose

### Installation avec Docker

1. Cloner le projet

```bash
git clone https://github.com/MickaelFioretti/AlgoBank.git
```

2. Build les image docker

```bash
docker-compose build
```

3. Lancer les containers

```bash
docker-compose up -d
```

4. Accéder au container

```bash
docker compose exec -it algo_bank bash
```

### Installation sans docker

1. Cloner le projet

```bash
git clone https://github.com/MickaelFioretti/AlgoBank.git
```

2.  Create a virtual environment and activate it:

```bash
pipenv --python 3.11
```

```bash
pipenv shell
```

3.  Install the dependencies:

```bash
pip install -r requirements.txt
```

## Execution

### Brute force

1. Aller dans le docier

```bash
cd app/bruteforce
```

2. Executer le script

```bash
python3 bruteforce "nom du fichier"
```

3. Fichier disponible

action

### Optimiser

1. Aller dans le docier

```bash
cd app/algorithme
```

2. Executer le script

```bash
python3 algorithme.py "nom du fichier"
```

3. Fichier disponible

action  
dataset1_Python+P7  
dataset2_Python+P7  
