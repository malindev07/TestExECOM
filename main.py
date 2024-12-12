from contextlib import asynccontextmanager
from dataclasses import fields

import uvicorn
from fastapi import FastAPI

from src.app.handlers.form_handler import form_router

from src.storage.fields_storage.fields_storage import FieldsStorage
from src.storage.forms_storage.forms_storage import FormStorage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # con = DataBaseConnection(host = "localhost", port = 27017, db_name = "forms_db")
    # # con = DataBaseConnection(host="mongo", port=27017, db_name="forms_db")
    #
    # DB = con.get_db()

    fields_storage = FieldsStorage()
    form_storage = FormStorage()

    yield {"fields_storage": fields_storage, "form_storage": form_storage}


app = FastAPI(lifespan=lifespan)

app.include_router(form_router)


if __name__ == "__main__":
    uvicorn.run(app)
