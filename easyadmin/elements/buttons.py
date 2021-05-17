def get_split_button(
    name: str = "DEFAULT_BUTTON_NAME",
    href: str = None,
    color: str = 'primary',
    icon: str = 'plus',
    size: str = None,
    modal: str = None,
    onclick: str = None
):
    size = f' btn-{size}' if size else ''
    href = f' href="{href}"' if href else ''
    button_id = ''.join(name.split(' '))
    if onclick:
        html_onclick = f' onclick="{onclick}"'
    else:
        html_onclick = ''

    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""

    button = f"""
<a id="{button_id}" {href} class="btn btn-{color} btn-icon-split{size}"{modal}{html_onclick}>
    <span class="icon text-white-50">
        <i class="fas fa-{icon}"></i>
    </span>
    <span class="text">{name}</span>
</a>
"""
    if onclick and modal:
        button = f"""{button}
<script>
$(document).on("click", "#{button_id}", function() {{
    {onclick}()
}});
</script>
"""
    return button
def get_button(
    name: str = "DEFAULT_BUTTON_NAME",
    href: str = None,
    color: str = 'primary',
    size: str = None,
    modal: str = None,
    onclick: str = None
):
    button_id = ''.join(name.split(' '))
    href = f' href="{href}"' if href else ''
    size = f' btn-{size}' if size else ''
    if onclick:
        html_onclick = f' onclick="{onclick}"'
    else:
        html_onclick = ''
    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""
    button = f"""
<a id="{button_id}" class="btn btn-{color}{size}"{href}{modal}{html_onclick}>{name}</a>
"""
    if onclick and modal:
        button = f"""{button}
<script>
$(document).on("click", "#{button_id}", function() {{
    {onclick}()
}});
</script>
"""
    return button