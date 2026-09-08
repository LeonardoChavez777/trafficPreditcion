import pandas as pd  # Permite trabajar con los datos históricos
from pathlib import Path  # Permite construir rutas de archivos
import joblib  # Permite cargar el archivo .pkl

BASE_DIR = Path(__file__).resolve().parent.parent  # Obtiene la raíz del proyecto

FEATURES_PATH = BASE_DIR / "models" / "features.pkl"  # Ruta de features.pkl

features = joblib.load(FEATURES_PATH)  # Carga las 22 features en el orden correcto


def create_features(df):
    df["lag_1"] = df["773869"].shift(1)  # Velocidad de hace 5 minutos
    df["lag_2"] = df["773869"].shift(2)  # Velocidad de hace 10 minutos
    df["lag_3"] = df["773869"].shift(3)  # Velocidad de hace 15 minutos
    df["lag_4"] = df["773869"].shift(4)  # Velocidad de hace 20 minutos
    df["lag_5"] = df["773869"].shift(5)  # Velocidad de hace 25 minutos
    df["lag_6"] = df["773869"].shift(6)  # Velocidad de hace 30 minutos

    df["hour"] = df["timestamp"].dt.hour  # Extrae la hora del timestamp
    df["day_of_week"] = df["timestamp"].dt.dayofweek  # 0=lunes, 6=domingo

    neighbors = [
        "773906", "718204", "773927", "773953", "773916",
        "717572", "718090", "718496", "773904", "761003", "774204"
    ]# Los valores de estos sensores se mantienen como features del modelo

    df["rolling_mean_2"] = df["773869"].rolling(2).mean()  # Promedio de las últimas 2 mediciones
    df["rolling_std_2"] = df["773869"].rolling(2).std()  # Desviación estándar de las últimas 2 mediciones

    df["delta_1"] = df["773869"] - df["lag_1"]  # Cambio de velocidad respecto a hace 5 minutos

    return df[features]