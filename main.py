from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Schemas.URLShemas import ShortenedURLSchema,UrlToShortSchema
from DB.Repos.URLRepository import create_url, get_url

app = FastAPI(title="Shortener")


@app.post("/short")
async def short_url(url: UrlToShortSchema) -> ShortenedURLSchema:
    shortened: ShortenedURLSchema = await create_url(url.url)
    return shortened

@app.get("/get/{shorted_url}",status_code=308)
async def redirect(shorted_url: str) -> RedirectResponse:
    url: ShortenedURLSchema = await get_url(shorted_url)
    return RedirectResponse(f"{url.url}")
    
