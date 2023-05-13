from main import app

from website.models import User


def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 302


def test_invalid_login(client):
    client.post("/login", data={"email": "accord@gmail.com", "password": "accord1234"})

    response = client.get("/User")

    assert response.status_code == 404


