from .admin import get_admin_page

def get_table_body(
    name: str,
    table_headers_html: str,
    table_rows_html: str,
    above: str = '',
    below: str = '',
):
    return f"""
<!-- Page Heading -->
{above}

<!-- DataTales Example -->
<div class="card shadow mb-4">
    <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">{name}</h6>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                <thead>
                    <tr>
                        {table_headers_html}
                    </tr>
                </thead>
                <tfoot>
                    <tr>
                        {table_headers_html}
                    </tr>
                </tfoot>
                <tbody>
                    {table_rows_html}
                </tbody>
            </table>
        </div>
    </div>
</div>

{below}
"""


def get_table_page(
    name: str, 
    data: list,
    sidebar: str, 
    current_user: str,
    modals: str = "",
    above: str = "",
    below: str = "",
    root_path: str = '/',
    google: str = '',
):
    navbar = sidebar
    table_headers = [th for th in data[0]]
    table_headers_html = ''.join(
        [f'<th>{th}</th>\n' for th in table_headers]
    )
    table_rows = [list(tr.values()) for tr in data]
    table_rows_html = []
    for tr in table_rows:
        row = [f"<td>{td}</td>\n" for td in tr]
        row_html = ''.join(row)
        table_rows_html.append(f"""
<tr>\n
    {row_html}
</tr>
""")
    table_rows_html = ''.join(table_rows_html)
    admin_page = get_admin_page(
        name=name,
        sidebar=sidebar,
        body=get_table_body(
            name,
            table_headers_html,
            table_rows_html,
            above=above,
            below=below
        ),
        current_user=current_user,
        modals=modals,
        root_path=root_path,
        google=google
    )
    return admin_page