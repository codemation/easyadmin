from easyadmin.elements import scripts
from . import html_input
from . import buttons, modal
from . import scripts

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
        html_input.get_text_input('username', value='test') + html_input.get_text_input('pasword', input_type='password'),
        html_input.get_text_input('email', size=12),
        html_input.get_text_input('address'),
        html_input.get_checkbox('choices', [(f'choice{i}', False) for i in range(20)], unique_id='c1')+
        html_input.get_checkbox('options', [(f'options{i}', True) for i in range(20)], unique_id='o1')
    ],
    submit_name: str = 'Default Submit Name',
    action: str = "/DEFAULT_ACTION",
    method: str = "POST",
    transform_id = None,
    run_after: str = None,
):
    title_id = ''.join(title.split(' '))
    rows = ''.join([get_form_row(row) for row in rows])
    transform_id = f"'{transform_id}'" if transform_id else 'null'
    run_after = f'{run_after}' if run_after else 'null'
    and_transform = '' if not transform_id else 'AndTransform'
    submit_button = buttons.get_button(
        submit_name, 
        size='block', 
        onclick=f"OnClickSendForm{and_transform}('{title_id}', '{method}', '{action}', {transform_id}, {run_after})"
        #targetFormId, submitMethod, submitPath, transformId)
    )
    submit_script = scripts.get_onclick_form_submit_script(transform=True)
    form_top = f"""
<div class="card o-hidden border-0 shadow-lg my-5">
    <div class="card-body p-0">
        <!-- Nested Row within Card Body -->
        <div class="row">
            <div class="col-lg-12">
                <div class="p-5">
                    <div class="text-center">
                        <h1 class="h4 text-gray-900 mb-4">{title}</h1>
                    </div>
                    
                    <form id="{title_id}" action="{action}" method="{method}">
                        {rows}
                        
                        <div class="col-12">
                            {submit_button}
                        </div>
                        {submit_script}
                        <hr>
                    </form>
                
                </div>
            </div>
        </div>
    </div>
</div>
"""
    return form_top

def get_login_form():
    return """
<form class="user" action="{login_action}" method="{login_method}">
    <div class="form-group">
        <input type="{identity_type}" name="username" class="form-control form-control-user"
            id="exampleInputEmail" aria-describedby="emailHelp"
            placeholder="{placeholder}">
    </div>
    <div class="form-group">
        <input type="password" name="password" class="form-control form-control-user"
            id="exampleInputPassword" placeholder="Password" value="None">
    </div>
    <button class="btn btn-primary btn-user btn-block" type="submit">
        Login
    </button
</form>
"""