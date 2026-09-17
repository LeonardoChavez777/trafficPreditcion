from sqlalchemy import Column, DateTime, Float, Integer  # Tipos de columnas
from database import Base  # Clase Base de SQLAlchemy


class TrafficData(Base):
    __tablename__ = "traffic_data"  # Nombre de la tabla

    id = Column(Integer, primary_key=True)  # Identificador único
    timestamp = Column(DateTime, nullable=False, index=True)  # Fecha de la medición

    sensor_773869 = Column(Float, nullable=False)  # Sensor objetivo
    sensor_773906 = Column(Float, nullable=False)  # Sensor vecino
    sensor_718204 = Column(Float, nullable=False)  # Sensor vecino
    sensor_773927 = Column(Float, nullable=False)  # Sensor vecino
    sensor_773953 = Column(Float, nullable=False)  # Sensor vecino
    sensor_773916 = Column(Float, nullable=False)  # Sensor vecino
    sensor_717572 = Column(Float, nullable=False)  # Sensor vecino
    sensor_718090 = Column(Float, nullable=False)  # Sensor vecino
    sensor_718496 = Column(Float, nullable=False)  # Sensor vecino
    sensor_773904 = Column(Float, nullable=False)  # Sensor vecino
    sensor_761003 = Column(Float, nullable=False)  # Sensor vecino
    sensor_774204 = Column(Float, nullable=False)  # Sensor vecino