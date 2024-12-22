from dataclasses import dataclass, field
from enum import StrEnum


@dataclass
class FormTypes(StrEnum):
    EMAIL = "email"
    PHONE = "phone"
    DATE = "date"
    TEXT = "text"


@dataclass
class Form:
    form_name: str
    form_fields: dict[str, str] = field(default_factory=dict)

    def create_form(self, **fields) -> dict[str, dict[str, str]] | bool:

        try:
            if fields == {}:
                return False

            for key, value in fields.items():
                match value:
                    case FormTypes.EMAIL:
                        self.form_fields[key] = FormTypes.EMAIL.value
                    case FormTypes.PHONE:
                        self.form_fields[key] = FormTypes.PHONE.value
                    case FormTypes.DATE:
                        self.form_fields[key] = FormTypes.DATE.value
                    case FormTypes.TEXT:
                        self.form_fields[key] = FormTypes.TEXT.value
            # print({self.form_name: self.form_fields})
            return {self.form_name: self.form_fields}

        except ValueError:
            return False
