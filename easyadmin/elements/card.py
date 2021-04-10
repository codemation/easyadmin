def get_card(
    name: str,
    body: str,
    size: int
):
    return f"""
<div class="col-{size}">
    <div class="card shadow mb-4">
        <div class="card-header py-3">
            <h6 class="m-0 font-weight-bold text-primary">{name}</h6>
        </div>
        <div class="card-body">
            {body}
        </div>
    </div>
</div>
"""