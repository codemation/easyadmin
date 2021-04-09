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

    if onclick:
        onclick = f' onclick="{onclick}"'
    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""

    return f"""
<a{href} class="btn btn-{color} btn-icon-split{size}"{modal}>
    <span class="icon text-white-50">
        <i class="fas fa-{icon}"></i>
    </span>
    <span class="text">{name}</span>
</a>
"""
def get_button(
    name: str = "DEFAULT_BUTTON_NAME",
    href: str = None,
    color: str = 'primary',
    size: str = None,
    modal: str = None,
    onclick: str = None
):
    href = f' href="{href}"' if href else ''
    size = f' btn-{size}' if size else ''
    if onclick:
        onclick = f' onclick="{onclick}"'
    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""
    return f"""
<a class="btn btn-{color}{size}"{href}{modal}{onclick}>{name}</a>
"""