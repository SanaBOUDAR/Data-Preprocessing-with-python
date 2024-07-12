import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Étape 1: Lire le fichier Excel
df = pd.read_excel('Data.xls')

# Select the columns to encode
colonnes_categorielles = ['CATEGORIE','t24_Profession','CODE','s107_TypeCredit','t18_Genre','t23_EtatCivil','I_CLASS']  # Replace with your columns names

#Encoding the categorical data wtih Ordinal Encoder
encoder = OrdinalEncoder()
df_encoded = df.copy()
df_encoded[colonnes_categorielles] = encoder.fit_transform(df[colonnes_categorielles])

# Check the encoding
print(df_encoded)

# Save the encoded dataset
df_encoded.to_excel('DataEncoded.xls', index=False, engine='openpyxl')
