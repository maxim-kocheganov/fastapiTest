from fastapi import FastAPI
from pydantic import BaseModel
from time import monotonic
import asyncio

app = FastAPI()

class TestResponse(BaseModel):
    elapsed: float

async def work() -> None:
    #print("start")
    await asyncio.sleep(3)
    #print("end")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic() 
    lock = asyncio.Lock()
    async with lock:
        await work()  
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)