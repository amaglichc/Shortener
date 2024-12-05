from fastapi import HTTPException, status


UserNotFoundException = HTTPException(
    detail="User not found", status_code=status.HTTP_404_NOT_FOUND
)
InvalidCredentialsException = HTTPException(
    detail="Invalid email or password", status_code=status.HTTP_403_FORBIDDEN
)
