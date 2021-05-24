from . import card

def get_text_input(
    name: str = 'input text name',
    input_type: str = 'text', # 'text', 'password', 'email',
    value: str = None,
    size: int = 6,
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
    checked=False, 
    unique_id: str = ''
):
    unique_label = f'{unique_id}{label}'
    checked= ' checked="true"' if checked else ''
    return f"""
<div class="col-sm-12 col-md-8 col-lg-6">
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" name="{checkbox_name}" value="{label}" id="{unique_label}"{checked}>
        <label class="form-check-label" for="{unique_label}">
        {label}
        </label>
    </div>
</div>
"""

def get_checkbox(
    name: str,
    choices: set,
    size: int = 4,
    unique_id = '',
):
    choices = set(choices)
    choices = ''.join(
        [get_checkbox_item(name, label=choice[0], checked=choice[1], unique_id=unique_id) for choice in choices]
    )
    check_box =  f"""
<div class="row">
    {choices}
</div>
"""
    return card.get_card(
        name,
        body=check_box,
        size=size
    )