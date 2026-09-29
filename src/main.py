from fastapi import FastAPI
from src.schemas.prediction import PredictionRequest
from src.tasks.prediction import predict_speed
from src.celery_app import celery_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(request: PredictionRequest):
    task = predict_speed.delay(request.timestamp)

    return {
        "task_id": task.id,
        "status": "PENDING"
    }


@app.get("/predict/{task_id}")
def get_prediction(task_id: str):
    task = celery_app.AsyncResult(task_id)

    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result
    }