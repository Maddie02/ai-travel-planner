from fastapi.testclient import TestClient

from app.core.config import get_settings


def test_health_returns_ok(client: TestClient) -> None:
    settings = get_settings()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }


def test_unknown_route_returns_error_envelope(client: TestClient) -> None:
    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert response.json() == {"code": "http_error", "message": "Not Found"}


def test_openapi_docs_available(client: TestClient) -> None:
    assert client.get("/docs").status_code == 200
    assert client.get("/openapi.json").status_code == 200
