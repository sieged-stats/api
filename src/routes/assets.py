import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

import src.utils.exceptions as exceptions

router = APIRouter()


@router.get("/operators/{operator_name}/icon")
def get_operator_icon(operator_name: str):
    # Ubisoft gave us different extension for operators
    paths = [
        (f"/app/public/operators/icons/{operator_name}.png", "png"),
        (f"/app/public/operators/icons/{operator_name}.avif", "avif"),
    ]

    for path, extension in paths:
        if os.path.exists(path):
            return FileResponse(path, media_type=f"image/{extension}")

    raise exceptions.notFound()
