from .admin import get_admin_page

def get_table_body(
    name: str,
    table_headers_html: str,
    table_rows_html: str,
    above: str = '',
    below: str = ''
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
        modals=modals
    )
    return admin_page

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>{name}</title>

    <!-- Custom fonts for this template -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/css/sb-admin-2.min.css" rel="stylesheet" type="text/css">

    <!-- Custom styles for this page -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/vendor/datatables/dataTables.bootstrap4.min.css" rel="stylesheet" type="text/css">

</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        {navbar}
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">

                    <!-- Sidebar Toggle (Topbar) -->
                    <form class="form-inline">
                        <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
                            <i class="fa fa-bars"></i>
                        </button>
                    </form>

                    <!-- Topbar Navbar -->
                    <ul class="navbar-nav ml-auto">

                        <div class="topbar-divider d-none d-sm-block"></div>

                        <!-- Nav Item - User Information -->
                        <li class="nav-item dropdown no-arrow">
                            <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button"
                                data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <span class="mr-2 d-none d-lg-inline text-gray-600 small">{current_user}</span>
                                <img class="img-profile rounded-circle"
                                    src="https://codemation.github.io/easyadmin/easyadmin/img/undraw_profile.svg">
                            </a>
                            <!-- Dropdown - User Information -->
                            <div class="dropdown-menu dropdown-menu-right shadow animated--grow-in"
                                aria-labelledby="userDropdown">
                                <a class="dropdown-item" href="#">
                                    <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Profile
                                </a>
                                <a class="dropdown-item" href="#">
                                    <i class="fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Settings
                                </a>
                                <a class="dropdown-item" href="#">
                                    <i class="fas fa-list fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Activity Log
                                </a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Logout
                                </a>
                            </div>
                        </li>

                    </ul>

                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

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

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>Copyright &copy; Your Website 2020</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    {modals}

    <!-- Bootstrap core JavaScript-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/jquery/jquery.min.js"></script>
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/js/sb-admin-2.min.js"></script>

    <!-- Page level plugins -->
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/datatables/jquery.dataTables.min.js"></script>
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/datatables/dataTables.bootstrap4.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="https://codemation.github.io/easyadmin/easyadmin/js/demo/datatables-demo.js"></script>

</body>

</html>
"""