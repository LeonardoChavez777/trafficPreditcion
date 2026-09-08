from pathlib import Path  # Permite trabajar con rutas de forma segura
import joblib  # Permite cargar los archivos .pkl


BASE_DIR = Path(__file__).resolve().parent.parent  # Obtiene la carpeta raíz del proyecto

MODEL_PATH = BASE_DIR / "models" / "traffic_model.pkl"  # Ruta del modelo

FEATURES_PATH = BASE_DIR / "models" / "features.pkl"  # Ruta de las features


model = joblib.load(MODEL_PATH)  # Carga el modelo guardado

features = joblib.load(FEATURES_PATH)  # Carga la lista de features


def predict(data):
    """
    Recibe las features necesarias y devuelve una predicción.
    """

    return model.predict(data)  # Ejecuta la predicción con el modelo