# Détection d'Anomalies et Analyse des Journaux de Requête

## 📝 Description du Projet
Ce projet vise à analyser des journaux de requête (logs) afin de détecter des anomalies, classifier les erreurs, et regrouper les événements similaires à l'aide de techniques de Machine Learning et d'analyse de données. Les logs, générés par des systèmes, contiennent des informations précieuses pour la surveillance, le diagnostic et l'optimisation des performances.

## Objectifs Principaux
Détection d'Anomalies : Identifier des comportements inhabituels dans les logs, tels que des pics de requêtes anormaux ou des erreurs inattendues.

Classification des Erreurs : Distinguer les logs normaux des logs d'erreur à l'aide de modèles de classification supervisée.

Clustering des Événements : Regrouper les logs similaires pour découvrir des motifs récurrents et mieux comprendre les tendances.

Visualisation des Résultats : Fournir des graphiques et des rapports clairs pour faciliter l'interprétation des résultats.
## Dataset

| Date                             | Hostname  | Process         | IdProcess | Message                                           |
|----------------------------------|-----------|-----------------|-----------|---------------------------------------------------|
| 2024-12-11T17:14:51.738480+01:00 | hilbert02 | gnome-shell     | 2026.0    | meta_window_set_stack_position_no_sync: assert... |
| 2024-12-11T17:20:14.050043+01:00 | hilbert02 | gnome-text-edit | 6677.0    | Trying to snapshot GtkGizmo 0x559f9a9e7800 wit... |
## 🏛️ Architecture
Les principales étapes de l'analyse sont les suivantes :

1. **Préparation des Données** : Chargement et nettoyage des données issues des journaux de requêtes.
2. **Analyse Exploratoire** : Analyse des occurrences des processus, des erreurs et de leur répartition temporelle.
3. **Détection des Anomalies** :
   - Identification des pics de logs inhabituels
   - Utilisation de l'algorithme Isolation Forest
4. **Classification** : Modélisation supervisée pour distinguer les erreurs des logs normaux (Random Forest).
5. **Clustering** : Regroupement des logs similaires avec K-Means.
6. **Visualisation & Génération de Rapports** : Statistiques et graphiques.
+-------------------+       +-------------------+       +-------------------+
|  Données Brutes   | ----> |  Préparation des  | ----> |  Analyse          |
|                   |       |  Données          |       |  Exploratoire     |
+-------------------+       +-------------------+       +-------------------+
                                                                 |
                                                                 v
+-------------------+       +-------------------+       +-------------------+
|  Détection des    | <---- |  Classification   | <---- |  Clustering       |
|  Anomalies        |       |                   |       |                   |
+-------------------+       +-------------------+       +-------------------+
                                                                 |
                                                                 v
+-------------------+
|  Visualisation &  |
|  Rapports         |
+-------------------+
## ⚙️ Prérequis
Assurez-vous d'avoir les éléments suivants :
- Python 3.7 ou supérieur
- Librairies Python :
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - jupyter 

# 📈 Résultats et Visualisation
## 1-Détection d'Anomalies
Après applicationde la méthode **Isolation Forest**, il a été obtenu **1848 anomalies** et le graphique d'evaluation des nombres logs montre une évolution des logs par heure avec une détection d'anomalies marquées par des points rouges, principalement corrélées à des pics massifs d'activité. Ces pics, particulièrement concentrés autour de la mi-décembre 2024, dépassent les **20 000** logs par heure, ce qui constitue une déviation majeure par rapport aux volumes standards. Une hausse moins prononcée est également visible début janvier 2025. La concentration des anomalies sur ces périodes suggère des incidents critiques tels que des pannes système, des surcharges liées à une maintenance, voire des attaques potentielles (type Denial of Service).
![image](https://github.com/user-attachments/assets/4a64bc8f-15a7-40b8-ab5b-85e3ae8369b6)

## 2-Classification des Erreurs
Le modèle de classification obtenue affiche une accuracy de 99,99 %, ce qui signifie qu'il classe correctement presque toutes les instances du jeu de données. Le rapport de classification montre une précision et un rappel de 1,00 pour la classe majoritaire (0), indiquant une performance parfaite. Pour la classe minoritaire (1), la précision est également de 1,00, mais le rappel est légèrement inférieur à 0,99, ce qui signifie que 1 % des anomalies n'ont pas été détectées. Les moyennes macro et pondérée des métriques (précision, rappel, F1-Score) sont toutes de 1,00, confirmant une performance équilibrée et excellente. Cependant, il est important de vérifier si le modèle généralise bien sur de nouvelles données et de s'assurer que le déséquilibre entre les classes n'affecte pas sa robustesse.
![image](https://github.com/user-attachments/assets/f9fa9662-78d8-42e5-ad0c-6f3dfef6cc93)

## 3-Clustering des Événements
On observe une bonne séparation entre les groupes, ce qui indique une différenciation nette des logs selon les processus et les hôtes associés. Les clusters semblent répartis selon des plages spécifiques de processus, suggérant des comportements homogènes pour certains processus ou groupes de machines.
Le cluster 1 (vert) présente une dispersion plus large sur les hôtes, tandis que les clusters 0 (bleu) et 2 (orange) sont concentrés autour de certaines plages de processus.
![image](https://github.com/user-attachments/assets/eb557155-03ae-4760-a7f7-82041a89a9e3)
## Visualisation 
![image](https://github.com/user-attachments/assets/26a5f2aa-f918-466b-9adc-264a40bce4df)
![image](https://github.com/user-attachments/assets/bc19211f-90bf-4a34-bf97-b42fae999e1b)

# Technologies Utilisées
**Python** : Langage principal pour le traitement des données et l'implémentation des modèles.

**Pandas et NumPy** : Pour la manipulation et l'analyse des données.

**Scikit-learn** : Pour les algorithmes de Machine Learning (classification, clustering, détection d'anomalies).

**Matplotlib et Seaborn** : Pour la visualisation des données.

**Jupyter Notebook** : Pour l'exploration interactive des données et la documentation des analyses.

