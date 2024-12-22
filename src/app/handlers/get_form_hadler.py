from fastapi import APIRouter

from src.forms.form_create.form_create import Form
from src.forms.form_search.form_search_model import SearchFormModel
from src.validator.validate_form import Validator

get_form_router = APIRouter(prefix="/get_form", tags=["Get Form"])


@get_form_router.post("")
def get_form(form: dict[str, str]):

    valid_form = Validator.validate_data(form=form)

    if valid_form:
        searched_form = SearchFormModel()
        searched_form.create_form_keys(form=valid_form)

    return valid_form
