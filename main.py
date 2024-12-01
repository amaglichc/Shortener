from fastapi import FastAPI
from Schemas.URLShemas import ShortenedURLSchema
from DB.Repos.URLRepository import create_url

app = FastAPI(title="Shortener")


@app.post("/short/{url}")
async def short_url(url: str) -> ShortenedURLSchema:
    shortened: ShortenedURLSchema = await create_url(url)
    return shortened
