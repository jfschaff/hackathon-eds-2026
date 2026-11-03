# Atelier 2 – évaluer la qualité des données d'un EDS

## Objectif

Développer des **indicateurs de qualité des données** chargées dans un entrepôt de données de santé (EDS) au format OMOP, puis les mesurer sur la base fournie.

On s'intéresse aux données elles-mêmes, pas à la façon dont elles ont été produites : l'analyse de l'ETL est l'objet de l'atelier 1.

Deux thématiques possibles : **biologie** (`measurement`) et **parcours patient** (`person`, `visit_occurrence`, `condition_occurrence`, `procedure_occurrence`…).

## Environnement fourni

- **Une VM**, avec une base PostgreSQL **OMOP CDM v5.4 déjà chargée** : environ 385 000 patients, leurs séjours, diagnostics, actes et résultats de biologie (données synthétiques du hackathon 2025), ainsi que le vocabulaire OMOP complet.
- **Un environnement Python prêt à l'emploi** avec Marimo, SQLAlchemy, polars et Altair pour la visualisation.

Connexion à la base : hôte `localhost`, port `5433`, base `postgres`, schéma `omop`. Les identifiants vous sont communiqués sur place.

## Mode de travail recommandé : Marimo

Travaillez dans un notebook [Marimo](https://docs.marimo.io) : il permet d'enchaîner des cellules SQL et Python et d'afficher tableaux et graphiques. Pour démarrer, voir le Quickstart en fin de document.

Conseils :

- Les tables sont volumineuses (`measurement` : 15,8 millions de lignes). Faites les calculs en SQL (`count`, `avg`, `GROUP BY`) et ne rapatriez que les résultats agrégés.
- La base est en lecture seule : vous ne pouvez que lire (`SELECT`).

## Restitution

Le dernier jour, en plénière :
- une synthèse des défis auxquels vous avez été confrontés, apprentissages ;
- les indicateurs développés, les « scores » obtenus, etc.
- ce que vous envisagez d'implémenter en priorité dans vos EDS (ou qui est déjà en place).

## Quickstart

Python est déjà installé sur votre machine, mais vous devez créer votre environnement virtuel et installer les dépendances.

```bash
git clone https://github.com/jfschaff/hackathon-eds-2026.git
cd hackathon-eds-2026/atelier2/
python -m venv env
source env/bin/activate
uv pip install -r requirements.txt
uvx marimo edit --sandbox marimo-quickstart-atelier2-nb.py
```
