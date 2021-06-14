def get_onload_scripts(scripts: list):
    onload_scripts = """
<script>
    window.addEventListener('load', (event) => {"""
    for script in scripts:
        onload_scripts = f"""{onload_scripts}
    {script}
"""
    onload_scripts = f"""{onload_scripts}
    }});
</script>
"""
    return onload_scripts

def get_onclick_script():
    return"""
<script>
function OnClickUpdate(targetPath, divIdToUpdate, runAfter = null){{
    var request = new XMLHttpRequest();

    request.open("GET", targetPath);

    request.onreadystatechange = function(){{
        if (request.readyState === 4){{
            if (request.state === 200){{
                console.log("received the response - " + request);
            }} 
            else {{
                if (divIdToUpdate === 'body'){{
                    $(divIdToUpdate)[0].innerHTML = request.response;
                }}else{{
                    console.log("time to modify: "+ divIdToUpdate);
                    $('#'+divIdToUpdate)[0].innerHTML = request.response
                    if (runAfter !== null) {{
                        runAfter()
                    }}
                }}
            }}
        }} else {{
                console.log("waiting for the response to come");
        }}
    }}
    request.send();
}}
</script>
"""

def get_onclick_form_submit_script(transform=False):
    """
    returns the following script
    if transform == True
        OnClickSendFormAndTransform(targetFormId, submitMethod, submitPath, transformId)
    else:
        OnClickSendForm(targetFormId, submitMethod, submitPath, transformId)
    
    targetFormId: 
        Target form which will be submitted by method
    submitMethod: 
        HTTP VERB used to send form i.e 'post', 'put', 'delete'
    submitPath: 
        Where to send the submitted form '/form_endpoint'
    transformId: 
        requires: transform to be True
        Id of the html element which will be edited with the response of the submitted form



    
    """
    and_transform = 'AndTransform' if transform else ''

    form_top = f"""
<script>
function OnClickSendForm{and_transform}(targetFormId, submitMethod, submitPath, transformId, runAfter = null){{
    var formGroup = $('#'+targetFormId)
    console.log('Input Id to check for inputs is: '+ targetFormId)
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

    request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8')

    request.open(submitMethod, submitPath);

    request.onreadystatechange = function(){{
        if (request.readyState === 4){{
            if (request.state === 200){{
                console.log("received the response - " + request);
            }} 
            else {{
                if (transformId === 'body'){{
                    $(transformId)[0].innerHTML = request.response;
                }}else{{
"""
    if transform:
        form_top = f"""{form_top}
                    console.log('time to modify: ' + transformId);
                    $('#'+ transformId)[0].innerHTML = request.response
                    if (runAfter !== null) {{
                        runAfter()
                    }}
"""
    else:
        form_top = f"""{form_top}
                    console.log("request resp: "+request);
                    prompt("Response: ", request.response);
"""
    form_top = f"""{form_top}
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
"""
    return form_top


def get_chart(
    name: str = 'DefaultChartName',
    label: str = 'default label',
    data: dict = {'March': 20, 'April': 30, 'May': 25, 'June': 35}
):
    labels = ", ".join([f"'{k}'" for k in list(data.keys())])
    data = ', '.join([str(v) for v in list(data.values())])
    print(f"get_chart name: {name}")
    return f"""
<canvas id="{name}" width="400" height="400"></canvas>
<script>

function loadChart{name}(){{
    var ctx = document.getElementById('{name}').getContext('2d');
    var myChart = new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: [{labels}],
            datasets: [{{
                label: '{label}',
                data: [{data}],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }}]
        }},
        options: {{
            scales: {{
                y: {{
                    beginAtZero: true
                }}
            }}
        }}
    }});
}}

</script>
"""

def get_google_signout_script():
    return """
<script>
    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            console.log('User signed out.');
            window.location.href = '/logout';
        });
    }

    function onLoad() {
        gapi.load('auth2', function() {
        gapi.auth2.init();
        });
    }

</script>
"""