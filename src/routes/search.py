from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import siegeapi

import src.models as models
import src.schemas as schemas
import src.utils.exceptions as exceptions

from src.database import get_db
from src.utils.service import auth

router = APIRouter()


@router.get("/")
async def search(username: str, db: Session = Depends(get_db)):
    players = (
        db.query(models.Players)
        .filter(models.Players.name.ilike(f"%{username}%"))
        .limit(5)
        .all()
    )
    player_list = [
        schemas.PlayerSearchResult.model_validate(player) for player in players
    ]

    try:
        if not any(player.name == username for player in player_list):
            player = await auth.get_player(name=username)
            player_list = [
                schemas.PlayerSearchResult(
                    uid=player.uid, name=player.name, icon=player.profile_pic_url_146
                )
            ] + player_list
    except siegeapi.exceptions.InvalidRequest:
        pass

    if not player_list:
        raise exceptions.notFound()

    return player_list
