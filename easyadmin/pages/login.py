def get_google_oauth_login(redirect_url='admin'):
    return f"""
<div class="g-signin2" data-onsuccess="onSignIn">
<script>
function onSignIn(googleUser) {{
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    console.log('Token: '+ id_token)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/auth/token/oauth/google');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('X-Google-OAuth2-Type', 'client');
    xhr.onload = function() {{
        console.log('Signed in as: ' + xhr.responseText);
        window.location.href = '{redirect_url}';
    }};
    xhr.send(id_token);

}}

</script>
"""

def get_login_page(
    title: str = 'Login Title Page',
    identity_type: str = 'username', # 'email' also possible
    login_action: str = '/login',
    login_method: str = 'post',
    welcome_message: str = 'Welcome Back!',
    google: str = '',
    google_redirect_url = ''
):
    meta_extras = ''
    oauth_login = ''
    if google:
        meta_extras = f"""
<meta name="google-signin-client_id" content="{google}">
<script src="https://apis.google.com/js/platform.js" async defer></script>
"""
        google_login = get_google_oauth_login(google_redirect_url)
        oauth_login = f"{oauth_login}{google_login}"
        
    placeholder = 'Username...'
    if identity_type == 'email':
        placeholder = f'Enter Email Address...'

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>{title}</title>

    <!-- Custom fonts for this template-->
    <link href="https://codemation.github.io/easyadmin/easyadmin/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="https://codemation.github.io/easyadmin/easyadmin/css/sb-admin-2.min.css" rel="stylesheet">
    {meta_extras}
</head>

<body class="bg-gradient-primary">

    <div class="container">

        <!-- Outer Row -->
        <div class="row justify-content-center">

            <div class="col-xl-6 col-lg-6 col-md-6">
                <div class="card o-hidden border-0 shadow-lg my-5">
                    <div class="card-body p-0">
                        <!-- Nested Row within Card Body -->
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h1 class="h4 text-gray-900 mb-4">{welcome_message}</h1>
                                    </div>
                                    <form class="user" action="{login_action}" method="{login_method}">
                                        <div class="form-group">
                                            <input type="{identity_type}" name="username" class="form-control form-control-user"
                                                id="exampleInputEmail" aria-describedby="emailHelp"
                                                placeholder="{placeholder}">
                                        </div>
                                        <div class="form-group">
                                            <input type="password" name="password" class="form-control form-control-user"
                                                id="exampleInputPassword" placeholder="Password" value="None">
                                        </div>
                                        <button class="btn btn-primary btn-user btn-block" type="submit">
                                            Login
                                        </button
                                    </form>
                                    <hr>
                                    <div class="text-center">
                                        <a class="small" href="/register">New User - Register / </a>
                                        <a class="small" href="forgot-password.html">Forgot Password?</a>
                                    </div>
                                    {oauth_login}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/jquery/jquery.min.js"></script>
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="https://codemation.github.io/easyadmin/easyadmin/js/sb-admin-2.min.js"></script>

</body>

</html>
    """