from black.cache import dataclass

from src.forms.form_create.form_create import Form
from src.storage.forms_storage.forms_storage import FormStorage


@dataclass
class CheckForm:

    @classmethod
    def find_form_db(cls, form: Form, storage: FormStorage) -> bool:

        if form.form_fields in storage.forms:
            return True

        return False
