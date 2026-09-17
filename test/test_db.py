from database import engine  # Importa el motor de SQLAlchemy

try:
    with engine.connect() as connection:  # Intenta abrir conexión
        print("Conexión exitosa a PostgreSQL")
except Exception as e:
    print("Error de conexión:", e)