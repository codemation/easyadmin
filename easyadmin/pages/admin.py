from easyadmin.elements import scripts

def get_admin_page(
    name: str, 
    sidebar: str,
    body: str,
    current_user: str,
    topbar_extra = "",
    modals: str = "",
    root_path = '',
    google = ''
):
    extra_scripts = ''
    extra_meta = ''
    if google:
        extra_meta = f"""
<meta name="google-signin-client_id" content="{google}">
"""
        extra_scripts = """
<script src="https://apis.google.com/js/platform.js?onload=onLoad" async defer></script>
"""
    navbar = sidebar
    submit_and_transform = scripts.get_onclick_form_submit_script(transform=True)

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    {extra_meta}

    <title>{name}</title>

    <!-- Custom fonts for this template -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/css/sb-admin-2.min.css" rel="stylesheet">

    <!-- Custom styles for this page -->
    <link href="https://codemation.github.io/easyadmin/easyadmin/vendor/datatables/dataTables.bootstrap4.min.css" rel="stylesheet">
</head>

<body id="page-top">
    {submit_and_transform}
    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        {sidebar}
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
                                <a class="dropdown-item" href="{root_path}/user/{current_user}">
                                    <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Profile
                                </a>
                                <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                    Logout
                                </a>
                            </div>
                        </li>
                    </ul>

                </nav>
                <!-- End of Topbar -->
                {topbar_extra}
                </div>

                <!-- Begin Page Content -->
                <div class="container-fluid" id="page-body">
                    {body}
                </div>
                <!-- /.container-fluid -->
            </div>
            <!-- End of Main Content -->

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

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    {extra_scripts}

</body>

</html>
"""