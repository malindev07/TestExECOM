from fastapi import APIRouter, Request

from src.forms.form_create.form_create import Form

form_router = APIRouter(prefix="/create_form", tags=["Create Forms"])


@form_router.post("/create_form")
def create_form(req: Request, form_name: str, form: dict[str, str]):
    new_form = Form(form_name=form_name).create_form(**form)

    if new_form:
        if req.state.form_storage.save_form(new_form):
            req.state.fields_storage.check_fields(new_form)
        return req.state.fields_storage.fields

    return False
