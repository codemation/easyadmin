def get_split_button(
    name: str = "DEFAULT_BUTTON_NAME",
    href: str = "#",
    color: str = 'primary',
    icon: str = 'plus',
    modal: str = None
):
    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""

    return f"""
<a href="{href}" class="btn btn-{color} btn-icon-split"{modal}>
    <span class="icon text-white-50">
        <i class="fas fa-{icon}"></i>
    </span>
    <span class="text">{name}</span>
</a>
"""
def get_button(
    name: str = "DEFAULT_BUTTON_NAME",
    href: str = "#",
    color: str = 'primary',
    modal: str = None
):
    if modal:
        modal = f' data-toggle="modal" data-target="#{modal}"'
    else:
        modal = ""
    return f"""
<a class="btn btn-{color}" href="{href}"{modal}>{name}</a>
"""