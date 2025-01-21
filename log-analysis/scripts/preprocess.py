import pandas as pd


# Charger et inspecter les données
def load_and_inspect_data(filepath):
    # Charger les données depuis un fichier CSV
    df = pd.read_csv(filepath)

    # Afficher les 5 premières lignes pour vérifier le chargement
    print("Aperçu des données :\n", df.head())

    # Vérifier les valeurs manquantes
    print("Valeurs manquantes par colonne :\n", df.isnull().sum())

    return df


# Nettoyage des données
def clean_data(df):
    # Remplacer les NaN dans 'IdProcess' par une valeur indicative, par exemple 'Unknown'
    df['IdProcess'] = df['IdProcess'].fillna('Unknown')

    # Conversion des dates en format datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Vérifier le type des dates
    print("Type de la colonne 'Date' :", df['Date'].dtypes)

    return df


# Ajout d'une colonne 'ErrorType' basée sur les mots-clés dans 'Message'
def categorize_messages(df):
    def categorize_message(message):
        message = str(message)  # S'assurer que le message est une chaîne de caractères
        if "Error" in message:
            return "Error"
        elif "Warning" in message:
            return "Warning"
        else:
            return "Info"

    df['ErrorType'] = df['Message'].apply(categorize_message)

    # Vérifier la distribution des catégories
    print("Distribution des types d'erreur :\n", df['ErrorType'].value_counts())

    return df
