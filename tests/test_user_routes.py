import requests

test_user = {
    'username': 'testUser',
    'password': 'aI3kdl0s',
    'id': '',
    'access_token': '',
    'token_type': 'bearer'
}

# get user


def test_get_user():
    # Arrange
    url = 'http://localhost:8000/get_user/1'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert 1 is body['id']


def test_get_user_raises_not_found():
    # Arrange
    url = 'http://localhost:8000/get_user/99999999999'

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert 'User Not Found' in body['detail']


def test_create_user():
    url = 'http://localhost:8000/create_user'

    response = requests.get(url)
    body = response.json()

    assert response.status_code == 400
    assert 'User Not Found' in body['detail']
