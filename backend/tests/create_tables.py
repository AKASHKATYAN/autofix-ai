from app.database import Base
from app.database import engine

# Import models
from app.database.models import Repository

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")