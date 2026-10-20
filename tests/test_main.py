from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Testa a rota principal
def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"

# Testa a rota de health check
def test_health():
    res = client.get("/health")
    assert res.status_code == 200