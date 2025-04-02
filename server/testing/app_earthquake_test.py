
from os import environ
import re
import json

from app import app


class TestApp:
    '''Flask application in flask_app.py'''

    def test_earthquake_found_route(self):
        '''has a resource available at "/earthquakes/<id>".'''
        response = app.test_client().get('/earthquakes/1')
        assert response.status_code == 200

    def test_earthquake_not_found_route(self):
        '''has a resource available at "/earthquakes/<id>".'''
        response = app.test_client().get('/earthquakes/999')
        assert response.status_code == 404

    def test_earthquakes_found_response(self):
        '''displays json in earthquake route with keys for id, magnitude, location, year'''

        response = app.test_client().get('/earthquakes/2')
        # get the response body
        response_body = response.data.decode()
        # convert to JSON
        response_json = json.loads(response_body)
        # confirm JSON data
        assert response_json["id"] == 2
        assert response_json["magnitude"] == 9.2
        assert response_json["location"] == "Alaska"
        assert response_json["year"] == 1964

        # confirm status
        assert response.status_code == 200

    def test_earthquakes_not_found_response(self):
        '''displays appropriate message if id not found'''

        response = app.test_client().get('/earthquakes/9999')
        # get the response body
        response_body = response.data.decode()
        # convert to JSON
        response_json = json.loads(response_body)
        # confirm JSON data
        assert response_json["message"] == "Earthquake 9999 not found."

        # confirm status
        assert response.status_code == 404
