from datetime import timedelta

from src.celery_app import celery_app
from database import SessionLocal
from services.traffic_service import get_traffic_data
from services.feature_service import create_features
from services.model_service import predict


@celery_app.task
def predict_speed(timestamp):
    db = SessionLocal()

    try:
        start_time = timestamp - timedelta(minutes=30)
        end_time = timestamp

        df = get_traffic_data(db, start_time, end_time)
        features_df = create_features(df)
        prediction = predict(features_df)
        prediction = float(prediction[-1])
        return prediction

    finally:
        db.close()