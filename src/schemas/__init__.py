from typing import Optional, Any
from pydantic import BaseModel


class PlayerSearchResult(BaseModel):
    class Config:
        from_attributes = True

    uid: str
    name: str
    icon: str


class PlayerPersona(BaseModel):
    class Config:
        from_attributes = True

    enabled: bool
    nickname: Optional[str] = None
    tag: Optional[str] = None


class PlayerRankedProfile(BaseModel):
    class Config:
        from_attributes = True

    rank: str
    rank_id: int
    rank_points: int
    prev_rank_points: int
    next_rank_points: int
    rank_percentage: float
    rank_icon: str


class PlayerOverview(BaseModel):
    class Config:
        from_attributes = True

    id: str
    profile_pic_url: str
    name: str
    level: int
    level_percentage: float
    xp: int
    total_xp: int
    xp_to_level_up: int
    total_time_played: int
    persona: PlayerPersona
    ranked_profile: PlayerRankedProfile
