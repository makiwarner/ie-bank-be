from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is updated (PUT)
    THEN check the response is valid and the account is updated
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200
    account_id = response.json['id']  

    #now update client's name:
    response = testing_client.put(f'/accounts/{account_id}', json={'name': 'John Updated'})
    assert response.status_code == 200
    assert response.json['name'] == 'John Updated'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is requested (DELETE)
    THEN check the response is valid and the account is deleted
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200
    account_id = response.json['id']  
    #delete the account
    response = testing_client.delete(f'/accounts/{account_id}')
    assert response.status_code == 200

    #Try to retrieve the deleted account (it should return 'None') 
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 404  # Not found

