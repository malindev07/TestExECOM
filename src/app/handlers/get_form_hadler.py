from fastapi import APIRouter

from src.validator.validate_form import Validator

get_form_router = APIRouter(prefix="/get_form", tags=["Get Form"])


@get_form_router.post("")
def get_form(form: dict[str, str]):

    res = Validator.validate_data(form=form)

    return res
