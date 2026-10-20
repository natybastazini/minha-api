from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha API", version="1.0.0")

# Modelo de dados de um item
class Item(BaseModel):
    name: str
    price: float

# Rota principal
@app.get("/")
async def root():
    return {"status": "ok", "message": "API rodando!"}

# Rota usada no health check do deploy
@app.get("/health")
async def health():
    return {"status": "healthy"}

# Rota para criar um item
@app.post("/items")
async def create_item(item: Item):
    return {"created": item}