from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import router as index_router
from src.routes.search import router as search_router
from src.routes.players import router as player_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[""],
)

app.include_router(index_router, tags=["Index"])
app.include_router(player_router, prefix="/players", tags=["Players"])
app.include_router(search_router, prefix="/search", tags=["Search"])
