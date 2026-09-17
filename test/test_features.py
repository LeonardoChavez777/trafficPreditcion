import pandas as pd
from services.feature_service import create_features

df = pd.read_csv("data/METR-LA.csv")

df = df.rename(columns={"Unnamed: 0": "timestamp"})
df["timestamp"] = pd.to_datetime(df["timestamp"])


features_df = create_features(df)

features_df = features_df.dropna()  # Elimina filas sin suficientes datos

from services.model_service import predict
prediction = predict(features_df.head(5))
print("\nPredicciones")
print(prediction)