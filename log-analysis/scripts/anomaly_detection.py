import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest


# Identifier les moments avec un nombre de logs supérieur à une certaine valeur
def detect_anomalies_in_logs(logs_per_hour):
    # Détecter les anomalies basées sur une règle statistique
    anomalies = logs_per_hour[logs_per_hour > logs_per_hour.mean() + 2 * logs_per_hour.std()]

    print("Anomalies détectées :\n", anomalies)
    print("Nombre d'anomalies détectées :", len(anomalies))

    return anomalies


# Nettoyage et préparation des données pour l'Isolation Forest
def preprocess_dataframe(df):
    # Convertir 'IdProcess' en numérique, remplacer les valeurs non convertibles par -1
    df['IdProcess'] = pd.to_numeric(df['IdProcess'], errors='coerce').fillna(-1).astype(int)

    # Sélectionner les caractéristiques numériques
    numerical_data = df[['IdProcess']].dropna()
    return numerical_data


# Détection des anomalies avec Isolation Forest
def detect_anomalies_with_isolation_forest(numerical_data):
    # Initialiser et entraîner le modèle Isolation Forest
    model = IsolationForest(contamination=0.01, random_state=42)
    numerical_data['Anomaly'] = model.fit_predict(numerical_data[['IdProcess']])

    # Extraire les anomalies détectées
    anomalies = numerical_data[numerical_data['Anomaly'] == -1]
    print("Anomalies détectées avec Isolation Forest :\n", anomalies)

    return anomalies


# Visualisation des logs et des anomalies
def plot_logs_with_anomalies(logs_per_hour, anomalies_if):
    plt.figure(figsize=(10, 6))
    plt.plot(logs_per_hour.index, logs_per_hour.values, label='Logs per Hour')

    # Obtenir les indices horaires des anomalies
    anomaly_indices = anomalies_if.index.floor('H')  # Arrondir les timestamps à l'heure

    # Sélectionner uniquement les anomalies présentes dans logs_per_hour
    common_indices = anomaly_indices.intersection(logs_per_hour.index)
    anomaly_values = logs_per_hour.loc[common_indices]

    # Tracer les anomalies
    plt.scatter(common_indices, anomaly_values, color='red', label='Anomalies (Isolation Forest)')

    plt.title('Logs per Hour with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Number of Logs')
    plt.legend()
    plt.show()
