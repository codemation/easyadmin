from . import html_input
from . import buttons, modal

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
        html_input.get_checkbox('choices', [(f'choice{i}', False) for i in range(20)]),
        html_input.get_checkbox('options', [(f'options{i}', True) for i in range(20)])
    ],
    submit_name: str = 'Default Submit Name',
    action: str = "/DEFAULT_ACTION",
    method: str = "POST"
):
    title_id = ''.join(title.split(' '))
    rows = ''.join([get_form_row(row) for row in rows])
    submit_button = buttons.get_button(
        submit_name, 
        size='block', 
        onclick=f"SendForm{title_id}('{title_id}', '{submit_name}', null)"
    )
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
                    <form id="{title_id}" action="{action}" method="{method}">
                        {rows}
                        <div class="col-12">
                            {submit_button}
                        </div>
                        <hr>
                    </form>
                    <script>
                    function SendForm{title_id}(InputId, buttonName, divIdToUpdate){{
                        var formGroup = $('#'+InputId)
                        console.log('Input Id to check for inputs is: '+ InputId)
                        //var fData = new FormData(formGroup[0].id)
                        var fData = new FormData(formGroup[0])
                        var formJson = {{}}
                        var fInput = formGroup.find(':input')
                        var session;
                        for (var i = 0; i < fInput.length; i++) {{
                            if (!(fInput[i].type === "submit")){{
                                if (fInput[i].type === "checkbox"){{
                                    if (!(fInput[i].name in formJson)){{
                                        formJson[fInput[i].name] = []
                                    }}
                                    
                                    //fData.append(fInput[i].value, fInput[i].checked)
                                    if (fInput[i].checked){{
                                        formJson[fInput[i].name].push(fInput[i].value)
                                    }}
                                    
                                }}else{{
                                    formJson[fInput[i].name] = fInput[i].value
                                    fData.append(fInput[i].name, fInput[i].value);
                                    console.log('name: ' + fInput[i].value + ' val: '+ fInput[i].name);
                                }}

                            }}
                        }}
                        var request = new XMLHttpRequest();

                        request.open("{method}", "{action}");

                        request.onreadystatechange = function(){{
                            if (request.readyState === 4){{
                                if (request.state === 200){{
                                    console.log("received the response - " + request);
                                }} 
                                else {{
                                    if (divIdToUpdate === 'body'){{
                                        $(divIdToUpdate)[0].innerHTML = request.response;
                                    }}else{{
                                        console.log("request resp: "+request);
                                        prompt("{title}", request.response);
                                    }}
                                }}
                            }} else {{
                                    console.log("waiting for the response to come");
                            }}
                        }}
                        var object = {{}};
                        fData.forEach(function(value, key){{
                            object[key] = value;
                        }});
                        var json = JSON.stringify(formJson);

                        request.send(json);
                    }}
                    </script>
                </div>
            </div>
        </div>
    </div>
</div>
"""