import requests

res = requests.post('http://localhost:5000/api/v1/persons', json={"nombre":"Elena", "correo":"Elenanoquierepastel@mail.com", "kmcaminados":"4"})
if res.ok:
    print res.json()