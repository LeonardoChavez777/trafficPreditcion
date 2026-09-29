import pandas as pd
from sqlalchemy.orm import Session
from sqlmodels.traffic import TrafficData


def get_traffic_data(db: Session, start_time, end_time):
    records = (
        db.query(TrafficData)
        .filter(
            TrafficData.timestamp >= start_time,
            TrafficData.timestamp <= end_time
        )
        .order_by(TrafficData.timestamp)
        .all()
    )

    df = pd.DataFrame([
        {
            column.name: getattr(record, column.name)
            for column in TrafficData.__table__.columns
        }
        for record in records
    ])

    # Quitamos el prefijo sensor_ de las columnas
    df = df.rename(columns={
        column: column.replace("sensor_", "")
        for column in df.columns
        if column.startswith("sensor_")
    })

    return df