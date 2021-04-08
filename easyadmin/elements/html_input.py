def get_text_input(
    name: str = 'input text name',
    input_type: str = 'text', # 'text', 'password', 'email',
    size: int = 6
):
    return f"""
<div class="col-sm-{size}">
    <input type="text" class="form-control name="{name}" form-control-user" id="exampleFirstName"
        placeholder="{name}">
</div>
"""

def get_checkbox_item(
    label: str
):
    return f"""
<div class="col-sm-4 col-md-2">
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" value="" id="{label}">
        <label class="form-check-label" for="{label}">
        {label}
        </label>
    </div>
</div>
"""

def get_checkbox(
    choices: set
):
    choices = set(choices)
    choices = ''.join(
        [get_checkbox_item(choice) for choice in choices]
    )
    return f"""
<div class="row">
    {choices}
</div>
"""