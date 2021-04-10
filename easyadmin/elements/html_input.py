def get_text_input(
    name: str = 'input text name',
    input_type: str = 'text', # 'text', 'password', 'email',
    value: str = None,
    size: int = 6
):
    value = f' value="{value}"' if value else ''
    return f"""
<div class="col-sm-{size}">
    <input type="{input_type}"{value} class="form-control" name="{name}" form-control-user" id="exampleFirstName"
        placeholder="{name}">
</div>

"""

def get_checkbox_item(
    checkbox_name: str,
    label: str,
    checked=False
):
    checked= ' checked="true"' if checked else ''
    return f"""
<div class="col-sm-4 col-md-4">
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" name="{checkbox_name}" value="{label}" id="{label}"{checked}>
        <label class="form-check-label" for="{label}">
        {label}
        </label>
    </div>
</div>
<div col-2></div>
"""

def get_checkbox(
    name: str,
    choices: set
):
    choices = set(choices)
    choices = ''.join(
        [get_checkbox_item(name, label=choice[0], checked=choice[1]) for choice in choices]
    )
    return f"""

<div class="row">
    <div class="col-12 text-center">
        <h4>{name}</h4>
    </div>
    {choices}
</div>
"""