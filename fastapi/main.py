from fastapi import FastAPI, Query, Path, Header, Cookie

from src.api import api_router

app = FastAPI()
app.include_router(
    router=api_router,
    prefix="/api",
)


@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., ge=1),
    q: str = Query(None, max_length=50),
    user_agent: str = Header(None),
    session_id: str = Cookie(None),
):
    return {
        "item_id": item_id,
        "q": q,
        "user_agent": user_agent,
        "session_id": session_id,
    }
