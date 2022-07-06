import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
countries = [
    {"id": 1, "surname": "Lucho", "firstname": "Dominguez", "name_C": "Mexico","name_L":"Español","name_A":"Aeropuerto Internacional de Toluca"},
    {"id": 2, "surname": "Jean", "firstname": "Paul Gaultier", "name_C": "Francia","name_L":"Frances","name_A":"Aeropuerto Internacional de la Ciudad de México"}
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1
@app.get("/country")
def get_countries():
    return jsonify(countries)
@app.post("/country")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


def _find_next_id_Em():
    return max(employee["id"] for employee in countries) + 1
@app.get("/apiv1/employee/add")
def get_employee():
    return jsonify(countries)
@app.post("/apiv1/employee/add")
def add_employee():
    if request.is_json:
        employee = request.get_json()
        employee["id"] = _find_next_id()
        countries.append(employee)
        return employee, 201
    return {"error": "Request must be JSON"}, 415

def _find_next_id_Ai():
    return max(airport["id"] for airport in countries) + 1
@app.get("/airport")
def get_airport():
    return jsonify(countries)
@app.post("/airport")
def add_airport():
    if request.is_json:
        airport = request.get_json()
        airport["id"] = _find_next_id()
        countries.append(airport)
        return airport, 201
    return {"error": "Request must be JSON"}, 415

def _find_next_id_Lan():
    return max(language["id"] for language in countries) + 1
@app.get("/language")
def get_language():
    return jsonify(countries)
@app.post("/language")
def add_language():
    if request.is_json:
        language = request.get_json()
        language["id"] = _find_next_id()
        countries.append(language)
        return language, 201
    return {"error": "Request must be JSON"}, 415
