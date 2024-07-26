from fastapi.exceptions import HTTPException


def badRequest(detail: str = None) -> HTTPException:
    return HTTPException(status_code=400, detail=detail)


def unauthorized(detail: str = None) -> HTTPException:
    return HTTPException(status_code=401, detail=detail)


def permissionDenied(detail: str = None) -> HTTPException:
    return HTTPException(status_code=403, detail=detail)


def notFound(detail: str = None) -> HTTPException:
    return HTTPException(status_code=404, detail=detail)


def conflict(detail: str = None) -> HTTPException:
    return HTTPException(status_code=409, detail=detail)


def internalServerError(detail: str = None) -> HTTPException:
    return HTTPException(status_code=500, detail=detail)
