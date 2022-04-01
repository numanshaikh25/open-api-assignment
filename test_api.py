from re import T
import pytest
import json
from app_config import app
from model import db, Entry

@pytest.fixture
def client():
    
    app.config["TESTING"] = True
    app.testing = True
    client = app.test_client()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield client



def test_get_all_entries_successfully(client):
    response = client.get('/entry/list')
    print(response.json)
    assert response.status_code == 200

def test_get_all_entries_with_wrong_method(client):
    response = client.post('/entry/list')
    print(response.json)
    assert response.status_code == 405

def test_create_entry_successfully(client):
    response = client.post('/entry/create',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 200

def test_create_entry_with_wrong_method(client):
    response = client.get('/entry/create',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 405

def test_update_entry_successfully(client):
    response = client.put('/entry/update/3',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 200

def test_update_entry_with_wrong_method(client):
    response = client.post('/entry/update/5',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 405

def test_delete_entry_successfully(client):
    response = client.delete('/entry/delete/6',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 200

def test_delete_entry_with_wrong_method(client):
    response = client.post('/entry/delete/5',json={'age': 25, 'checked': True, 'description': 'Graphic Designer', 'name': 'John Doe', 'type': 'Employee'})
    print(response)
    assert response.status_code == 405
