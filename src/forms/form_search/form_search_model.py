from dataclasses import dataclass, field


@dataclass
class SearchFormModel:
    form_keys: list[str] = field(default_factory=list)

    def create_form_keys(self, form: dict[str, str]):

        for key, value in form.items():
            self.form_keys.append(key + "#" + value)
