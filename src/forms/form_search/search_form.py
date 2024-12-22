from collections import Counter
from dataclasses import dataclass, asdict


@dataclass
class SearchForm:

    @classmethod
    def search_form(cls, form_fields: list[str], all_fields: dict[str, list[str]]):
        forms_names: list[str] = []
        for item in form_fields:
            if item in all_fields:
                forms_names.extend(all_fields[item])

        if not forms_names:
            return False
        res = Counter(forms_names)

        for key, value in res.items():
            if value == max(res.values()):
                print(key)
                return key


SearchForm.search_form(
    form_fields=["123#email", "213#phone", "1232123#date"],
    all_fields={
        "123#email": ["Test form name", "Another form names", "Second form names"],
        "213#phone": ["Test form name", "Second form names"],
        "1232123#date": ["Second form names"],
    },
)
