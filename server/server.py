from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/activity")
async def receive(request: Request):
    data = await request.json()

    with open("/app/data/activity.jsonl", "a") as file:
        file.write(json.dumps(data) + "\n")

    return {"status": "received"}
