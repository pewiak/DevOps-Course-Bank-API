"""Integration tests for app.py"""
import pytest
import json

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation_post(client):
    # Use the client to make requests e.g.:
    # client.post(...)
    # client.get(...)
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    post_response = client.post('/accounts/Test1')
    assert post_response.status_code == 200
    assert json.loads(post_response.data)['name'] == 'Test1'

def test_account_creation_post_and_get(client):
    post_response = client.post('/accounts/Test1')
    assert post_response.status_code == 200
    assert json.loads(post_response.data)['name'] == 'Test1'
    get_response = client.get('/accounts/Test1')
    assert get_response.status_code == 200