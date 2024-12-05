from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from Schemas.URLSchemas import ShortenedURLSchema, UrlToShortSchema
from DB.Repos.URLRepository import create_url, get_url

router = APIRouter(tags=["Links"])


@router.post("/short")
async def short_url(url: UrlToShortSchema) -> ShortenedURLSchema:
    shortened: ShortenedURLSchema = await create_url(url.url)
    return shortened


@router.get("/{shorted_url}")
async def redirect(shorted_url: str) -> RedirectResponse:
    schema: ShortenedURLSchema = await get_url(shorted_url)
    return RedirectResponse(f"{schema.url}", status_code=308)
