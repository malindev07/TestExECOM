from contextlib import asynccontextmanager


import uvicorn
from fastapi import FastAPI

from src.app.handlers.create_form_handler import create_form_router
from src.app.handlers.get_form_hadler import get_form_router

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

app.include_router(create_form_router)
app.include_router(get_form_router)


if __name__ == "__main__":
    uvicorn.run(app)
