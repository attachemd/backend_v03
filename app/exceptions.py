from fastapi import HTTPException, status


def token_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_user_exception(scope: str = "general"):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials - {scope}",
        headers={"WWW-Authenticate": "Bearer"},
    )
