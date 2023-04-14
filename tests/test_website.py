from main import app
import responses
from website.models import User


def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 302


def test_registration(client, app):
    response = client.post("/register", data={"email": "accord@gmail.com", "password": "accord1234"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "accord@gmail.com"



def test_invalid_login(client):
    client.post("/login", data={"email": "accord@gmail.com", "password": "accord1234"})

    response = client.get("/User")

    assert response.status_code == 404