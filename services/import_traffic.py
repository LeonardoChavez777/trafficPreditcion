import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from sqlmodels.traffic import TrafficData


SENSORS = [
    "773869",
    "773906",
    "718204",
    "773927",
    "773953",
    "773916",
    "717572",
    "718090",
    "718496",
    "773904",
    "761003",
    "774204",
]


def import_traffic_data():
    df = pd.read_csv("data/METR-LA.csv")

    # La primera columna del CSV contiene los timestamps
    df = df.rename(columns={"Unnamed: 0": "timestamp"})

    # Convertimos el timestamp a datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Nos quedamos únicamente con timestamp + nuestros sensores
    columns = ["timestamp"] + SENSORS
    df = df[columns]

    # Renombramos los sensores para coincidir con el modelo SQLAlchemy
    df = df.rename(
        columns={sensor: f"sensor_{sensor}" for sensor in SENSORS}
    )

    db: Session = SessionLocal()

    try:
        for _, row in df.iterrows():
            traffic = TrafficData(
                timestamp=row["timestamp"],
                **{
                    column: row[column]
                    for column in df.columns
                    if column != "timestamp"
                },
            )

            db.add(traffic)

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    import_traffic_data()