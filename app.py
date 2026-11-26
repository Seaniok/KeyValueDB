from fastapi import FastAPI, HTTPException

from main import KeyValueDB

app = FastAPI()
db = KeyValueDB("database.json")

@app.post("/items")
async def set_item(key: str, value: str):
    db[key] = value
    return {"status": "saved", "key": key}

@app.get("/items/{key}")
async def get_item(key: str):
    try:
        return {"key": key, "value": db[key]}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"No key named {key}")
