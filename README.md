# Dummy-server

Small Flask application to test POST requests.

## Runn app

`export FLASK_APP=main`

## Test app

`curl -X POST -H "Content-Type: application/JSON" --data '["test"]' http://0.0.0.0:5000/predict`