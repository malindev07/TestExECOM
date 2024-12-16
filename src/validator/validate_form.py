import re


from dataclasses import dataclass
from enum import Enum

from src.forms.form_create.form_create import FormTypes


@dataclass
class Patterns(Enum):
    PHONE = re.compile(r"[+]7 \d{3} \d{3} \d{2} \d{2}")
    EMAIL = re.compile(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]+$")
    DATE1 = re.compile(r"^\d{2}.(0[0-9]|1[0-2]).\d{4}")
    DATE2 = re.compile(r"^\d{4}-(0[0-9]|1[0-2])-\d{2}")


@dataclass
class Validator:

    @staticmethod
    def validate_data(form: dict[str, str]) -> dict[str, str] | None:
        valid_form: dict[str, str] = {}

        for k, v in form.items():

            if Patterns.EMAIL.value.fullmatch(v):
                valid_form[k] = FormTypes.EMAIL.value
            elif Patterns.PHONE.value.fullmatch(v):
                valid_form[k] = FormTypes.PHONE.value
            elif Patterns.DATE1.value.fullmatch(v) or Patterns.DATE2.value.fullmatch(v):
                valid_form[k] = FormTypes.DATE.value
        if valid_form:
            return valid_form

        return None
