from typing import Any, Dict, List, Iterable
from fastapi import FastAPI
from hmac_token.generate import generate_digest


app = FastAPI()


@app.post("/")
async def process(request: Dict[Any, Any]):
    LABEL_SIGNATURE = "signature"
    request[LABEL_SIGNATURE] = generate_digest(request)
    return request
