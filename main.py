from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse
import json
from models import SearchResult
from vector_store import find_in_vector_store, docs_to_json

FIND_LIMIT = 5
STREAM_FIND_LIMIT = 10

app = FastAPI(
    title="Statista Case Study",
    description="Case study demo app",
)


@app.get("/find",response_model=list[SearchResult])
async def find(query: str):
    top_items = docs_to_json(find_in_vector_store(query, k=FIND_LIMIT))
    return JSONResponse(content=top_items)


@app.get("/stream/find", response_model=list[SearchResult])
async def stream_find(request: Request, query: str):
    top_items = docs_to_json(find_in_vector_store(query, k=STREAM_FIND_LIMIT))

    async def event_generator():
        yield "[\n"
        first = True
        for item in top_items:
            if first:
                first = False
            else:
                yield ",\n"

            if await request.is_disconnected():
                break
            yield json.dumps(item)

        yield "\n]"

    return StreamingResponse(event_generator(), media_type="application/x-json")
