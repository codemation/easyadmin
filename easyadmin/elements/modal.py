def get_modal(
    name: str,
    alert: str = "DEFAULT ALERT STRING",
    body: str = "Extra details pertaining to Modal, or html",
    footer: str = "DEFAULT MODAL FOOTER HTML / TEXT",
    size: str = None,
):
    size = f'-{size}' if size else ''
    return f"""
<!-- {name} Modal-->
<div class="modal fade" id="{name}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal{size}" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{alert}</h5>
                <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
                {body}
            </div>
            <div class="modal-footer">
                {footer}
            </div>
        </div>
    </div>
</div>
"""