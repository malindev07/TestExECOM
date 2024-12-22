from dataclasses import dataclass, field

from src.forms.form_create.form_create import Form


@dataclass
class FieldsStorage:
    fields: dict[str, list[str]] = field(default_factory=dict)

    def check_fields(self, form: dict[str, dict[str, str]]) -> None:

        for form_name in form:
            for key, value in form[form_name].items():
                field_key_value = key + "#" + value

                if field_key_value not in self.fields:
                    self.fields[field_key_value] = [form_name]
                else:
                    self.fields[field_key_value].append(form_name)


# test_field_storage = FieldsStorage()
#
# test_form = Form(form_name="Test From Name")
# new_form = test_form.create_form(
#     user_email="email",
#     user_phone="phone",
#     user_date_reg="date",
#     user_text="text",
# )
# test_form = {
#     "FORM_NAME": {
#         "user_email": "email",
#         "user_phone": "phone",
#         "user_date_reg": "date",
#         "user_text": "text",
#     }
# }
#
# print(test_field_storage.fields)
# test_field_storage.check_fields(form=new_form)
# print(test_field_storage.fields)
# test_form2 = {
#     "SECOND_FORM_NAME": {
#         "user_email": "email",
#         "user_phone": "phone",
#     }
# }
# print("First add")
# print(test_field_storage.fields)
#
# test_field_storage.check_fields(form=test_form2)
#
# print("SECOND add")
# print(test_field_storage.fields)
#
#
# test_form3 = {
#     "THIRD_FORM_NAME": {"user_email": "email", "user_phone": "phone", "user_age": "age"}
# }
#
# test_field_storage.check_fields(form=test_form3)
#
# print("THIRD add")
# print(test_field_storage.fields)
