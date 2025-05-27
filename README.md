# MiniProjet6-TransportUrbain

## Description

Projet universitaire pour modéliser un réseau de transport urbain avec Neo4j, NetworkX, et Gephi.

## Structure du projet

- `data/stations.csv` : Dataset des stations (nœuds).
- `data/connections.csv` : Dataset des connexions (relations).
- `project.ipynb` : Notebook Jupyter contenant les scripts d'importation Neo4j et de modélisation NetworkX.

## Instructions pour utiliser le projet

1. Clonez ce dépôt : `git clone https://github.com/Aboubakr-Tahir/TransportUrbain_TheorieDeGraphe.git`
2. Installez Neo4j Desktop sur votre machine (https://neo4j.com/download).
3. Créez une base de données Neo4j nommée "transporturbain".
4. Installez les bibliothèques Python requises : `pip install neo4j networkx matplotlib numpy pandas python-louvain seaborn jupyter`.
5. Mettez à jour le mot de passe dans `project.ipynb` avec votre mot de passe Neo4j.
6. Lancez Jupyter Notebook : `jupyter notebook`
7. Ouvrez `project.ipynb` et exécutez les cellules dans l'ordre.
