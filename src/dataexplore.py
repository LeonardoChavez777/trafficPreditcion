import pandas as pd

DATA_PATH = "data/METR-LA.csv"
#este data set contiene informacion de la velocidad de los vehiculos capturada por los sensores.

df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("DIMENSIONES")
print("=" * 50)
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")

print("\n" + "=" * 50)
print("PRIMERAS FILAS")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("COLUMNAS")
print("=" * 50)
print(df.columns.tolist())

print("\n" + "=" * 50)
print("TIPOS DE DATOS")
print("=" * 50)
print(df.dtypes)

print("\n" + "=" * 50)
print("INFORMACIÓN")
print("=" * 50)
df.info()

print("\n" + "=" * 50)
print("VALORES NULOS")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("ESTADÍSTICAS")
print("=" * 50)
print(df.describe())