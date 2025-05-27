# Proyecto inicial Retail Fashion
# preprocesamiento.py

import os
import pandas as pd

# Cargar datos y procesar CSV de Kaggle
df = pd.read_csv(
    "C:/Users/kiera/OneDrive/Documents/Data Scientist Bootcamp/Retail Fashion env/fashion_retail_sales.csv")

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/fashion_retail_clean.csv", index=False)

# Revisar estructura
print(df.info())

# 2. Estandarizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Verificar estructura
print("\n Dimensiones:", df.shape)
print("\n Primeras filas:\n", df.head())

# 4. Revisar duplicados
print("\n Duplicados:", df.duplicated().sum())
df = df.drop_duplicates()

# 5. Revisar valores nulos
print("\n Valores nulos:\n", df.isnull().sum())

# 6. Convertir columnas
df['purchase_amount_(usd)'] = pd.to_numeric(
    df['purchase_amount_(usd)'], errors='coerce')
df['review_rating'] = pd.to_numeric(df['review_rating'], errors='coerce')
df['date_purchase'] = pd.to_datetime(
    df['date_purchase'], format="%d-%m-%Y", errors='coerce')

# 7. Rellenar nulos con la media
df['purchase_amount_(usd)'].fillna(
    df['purchase_amount_(usd)'].mean(), inplace=True)
df['review_rating'].fillna(df['review_rating'].mean(), inplace=True)

print("\n Valores nulos después del procesamiento:\n", df.isnull().sum())

