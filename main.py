from fastapi import FastAPI
from routers.LinkRouter import router as LinkRouter
from routers.UserRouter import router as UserRouter
from routers.AuthRouter import router as AuthRouter

app = FastAPI(title="Shortener")

app.include_router(LinkRouter)
app.include_router(UserRouter)
app.include_router(AuthRouter)
