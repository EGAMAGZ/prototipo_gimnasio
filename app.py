from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

app = FastAPI()


@app.get("/", response_class=JSONResponse)
def root(request: Request) -> Response:
    return {"message": "Hello world"}
