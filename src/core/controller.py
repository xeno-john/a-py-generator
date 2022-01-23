from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from view import Resource
import json
import sys
import logging

sys.path.insert(0, '.')
from src.sql_generator import generate_creation_script
from src.sqlalchemy_code_generator import generate_db_connection
from src.sqlalchemy_code_generator import generate_models

app = FastAPI()
logging.basicConfig(filename="fastapi_generator.log", level=logging.INFO, format="%(asctime)s %(message)s")


@app.post("/api/generate")
def generate(resources: List[Resource]):
    logging.info("Generate request was received.")
    resource_list = [x.dict() for x in resources]
    try:
        generate_creation_script.generate_db_create_code(json.dumps(resource_list))
        generate_db_connection.generate_connection()
        generate_models.generate_sqlalchemy_classes(json.dumps(resource_list))
        logging.info("Successfully generated the SQL and Python code.")
        return JSONResponse(status_code=200, content={})
    except Exception as e:
        logging.error("An exception occured")


if __name__ == "__main__":
    uvicorn.run("controller:app", host='0.0.0.0', port=8002, reload=True, debug=True)
