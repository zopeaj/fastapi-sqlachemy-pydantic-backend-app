from fastapi import FastAPI
from app.api.endpoints.routes import api_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
