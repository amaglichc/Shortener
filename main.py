from fastapi import FastAPI
from routers.LinkRouter import router as LinkRouter
from routers.UserRouter import router as UserRouter

app = FastAPI(title="Shortener")

app.include_router(LinkRouter)
app.include_router(UserRouter)
