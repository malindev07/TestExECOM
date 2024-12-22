from dataclasses import dataclass, field

from src.forms.form_create.form_create import FormTypes


@dataclass
class FormStorage:
    forms: dict[str, dict[str, str]] = field(default_factory=dict)

    def save_form(self, data: dict[str, dict[str, str]]):

        for key in data:
            if key in self.forms:
                return False

            self.forms[key] = data[key]
            return True


# a = FormStorage()
# a.save_form()
