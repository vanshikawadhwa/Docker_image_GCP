from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import socket

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def read_root(request: Request):
    return {
        "message": "hello world",
        "worker_pid": os.getpid(),          # unique per worker process
        "host": socket.gethostname()        # container hostname
    }
