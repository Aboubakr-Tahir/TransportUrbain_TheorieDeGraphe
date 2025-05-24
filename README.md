# MiniProjet6-TransportUrbain

## Description

Projet universitaire pour modéliser un réseau de transport urbain avec Neo4j, NetworkX, et Gephi.

## Structure du projet

- `stations.csv` : Dataset des stations (nœuds).
- `connections.csv` : Dataset des connexions (relations).
- `import_transport_data.py` : Script Python pour importer les données dans Neo4j.

## Instructions pour utiliser le projet

1. Clonez ce dépôt : `git clone https://github.com/votreusername/MiniProjet6-TransportUrbain.git`
2. Installez Neo4j Desktop sur votre machine (https://neo4j.com/download).
3. Créez une base de données Neo4j nommée "transporturbain".
4. Installez la bibliothèque Python `neo4j` : `pip install neo4j`.
5. Mettez à jour le mot de passe dans `import_transport_data.py` avec votre mot de passe Neo4j.
6. Exécutez le script : `python import_transport_data.py`.
