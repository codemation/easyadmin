from easyadmin.pages import login, not_found, admin, admin_table
from easyadmin.elements import buttons, modal, sidebar, table, forms

class Admin:
    def __init__(self,
        title: str = 'EasyAdmin',
        title_link: str = '/',
        side_bar_sections: list = [
            {
                'items': [
                    {
                        'name':  'home',
                        'href': '/',
                        'items': []
                    }]
            }]
    ):
        self.sidebar = elements.sidebar.get_side_bar(
            title={'name': title, 'href': title_link},
            sections=side_bar_sections
        )

    def table_page(self,
        name: str = 'DEFAULT TABLE_NAME',
        data: list = [
            {
                'example_column1': i, 
                'example_column2': i+2,
                'actions': ( 
                    buttons.get_split_button(
                        f'button_{i}', 
                        modal='TEST_MODAL'
                    ) + 
                    buttons.get_split_button(
                        f'button_{i}', 
                        modal='TEST_MODAL', 
                        color='danger',
                        icon='trash',
                        size='lg'
                    )
                )
            } for i in range(20)],
        current_user: str = 'DEFAULT_USER',
        modals: str = modal.get_modal("TEST_MODAL"),
        above: str = forms.get_form(),
        below: str = ""
    ):
        
        return admin_table.get_table_page(
            name,
            data,
            self.sidebar,
            current_user,
            modals,
            above=above,
            below=below
        )
    def login_page(self,
        title: str = 'Login Title Page',
        identity_type: str = 'username', # 'email' also possible
        login_action: str = '/login',
        login_method: str = 'post',
        welcome_message: str = 'Welcome Back!'
    ):
        return login.get_login_page(
            title,
            identity_type,
            login_action,
            login_method,
            welcome_message
        )
    def not_found_page(self):
        return pages.not_found.get_404_page(
            'Page Not Found',
            self.sidebar,
            'DEFAULT_USER'
        )