from . import html_input
from . import buttons

def get_form_row(
    form_items: str
):

    return f"""
<div class="form-group row">
    {form_items}
</div>
"""


def get_form(
    title: str = 'Form Title',
    rows: list = [
        html_input.get_text_input('username') + html_input.get_text_input('pasword'),
        html_input.get_text_input('email', size=12),
        html_input.get_text_input('address'),
        html_input.get_checkbox([f'choice{i}' for i in range(20)])
    ],
    submit_name: str = 'Default Submit Name',
    action: str = "/DEFAULT_ACTION",
    method: str = "POST"
):
    rows = ''.join([get_form_row(row) for row in rows])
    submit_button = buttons.get_button(submit_name, href=action, size='block')
    return f"""

<div class="card o-hidden border-0 shadow-lg my-5">
    <div class="card-body p-0">
        <!-- Nested Row within Card Body -->
        <div class="row">
            <div class="col-lg-12">
                <div class="p-5">
                    <div class="text-center">
                        <h1 class="h4 text-gray-900 mb-4">{title}</h1>
                    </div>
                    <form action="{action}" method="{method}">
                        {rows}
                        <div class="col-12">
                            {submit_button}
                        </div>
                        <hr>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
"""