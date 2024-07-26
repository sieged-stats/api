from src.app import app
import src.models as models
from src.database import engine
from src.utils.service import auth

models.Base.metadata.create_all(bind=engine)
