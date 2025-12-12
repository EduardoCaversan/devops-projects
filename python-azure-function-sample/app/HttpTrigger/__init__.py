import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    message = f"Olá, {name}!" if name else "Olá! Esta é uma Azure Function em Python. 🎉"
    body = {"message": message}
    return func.HttpResponse(json.dumps(body), status_code=200, mimetype="application/json")
