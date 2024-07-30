from typing import Coroutine, Any

import siegeapi
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import src.models as models
import src.schemas as schemas
import src.utils.exceptions as exceptions

from src.database import get_db
from src.utils.service import auth

router = APIRouter()


async def get_player_or_not_found(
    username: str,
) -> Coroutine[Any, Any, siegeapi.Player]:
    try:
        return await auth.get_player(name=username)
    except siegeapi.exceptions.InvalidRequest:
        raise exceptions.notFound()


def build_rank_icon(rank: str) -> str:
    return f"https://imgsvc.trackercdn.com/url/max-width(168),quality(66)/https%3A%2F%2Ftrackercdn.com%2Fcdn%2Fr6.tracker.network%2Franks%2Fs28%2Fsmall%2F{rank.lower().replace(' ', '-')}.png/image.png"


@router.get("/{username}")
async def get_player_overview(username: str, db: Session = Depends(get_db)):
    player = await get_player_or_not_found(username)

    _player = db.query(models.Players).filter(models.Players.uid == player.uid).first()
    if _player is None:
        db.add(
            models.Players(
                uid=player.uid, name=player.name, icon=player.profile_pic_url_146
            )
        )
    else:
        if _player.name != player.name:
            _player.name = player.name
    db.commit()

    await player.load_persona()
    await player.load_playtime()
    await player.load_progress()
    await player.load_ranked_v2()

    player.ranked_profile.__setattr__(
        "rank_icon", build_rank_icon(player.ranked_profile.rank)
    )

    actual_progression = (
        player.ranked_profile.rank_points - player.ranked_profile.prev_rank_points
    )
    needed_progression = (
        player.ranked_profile.next_rank_points - player.ranked_profile.prev_rank_points
    )

    player.ranked_profile.__setattr__(
        "rank_percentage", ((actual_progression / needed_progression) * 100)
    )

    try:
        total_level_xp = player.xp_to_level_up + player.xp
        player.__setattr__("level_percentage", (player.xp / total_level_xp) * 100)
    except ZeroDivisionError:
        player.__setattr__("level_percentage", 0.0)

    return schemas.PlayerOverview.model_validate(player)


@router.get("/{username}/operators")
async def get_player_operators(
    username: str, sorted_by: str = None, db: Session = Depends(get_db)
):
    player = await get_player_or_not_found(username)

    await player.load_operators()
    operators = player.operators.all.attacker + player.operators.all.defender

    if sorted_by is not None:
        if len(operators) > 0 and sorted_by in operators[0].__dict__:
            operators = sorted(
                operators, key=lambda x: x.__getattribute__(sorted_by), reverse=True
            )

    return operators


@router.get("/{username}/weapons")
async def get_player_weaponss(
    username: str, sorted_by: str = None, db: Session = Depends(get_db)
):
    player = await get_player_or_not_found(username)

    await player.load_weapons()
    weapons = (
        player.weapons.all.attacker.primary
        + player.weapons.all.attacker.secondary
        + player.weapons.all.defender.primary
        + player.weapons.all.defender.secondary
    )

    if sorted_by is not None:
        if len(weapons) > 0 and sorted_by in weapons[0].__dict__:
            weapons = sorted(
                weapons, key=lambda x: x.__getattribute__(sorted_by), reverse=True
            )

    return weapons
