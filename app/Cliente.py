import requests

res = requests.post('http://localhost:5000/api/v1/persons', json={"nombre":"Elyssa", "correo":"Ely@ssa", "kmcaminados":"4"})
if res.ok:
    print res.json()