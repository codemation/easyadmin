from easyadmin.pages import (
    login, 
    errors, 
    admin, 
    admin_table
)
from easyadmin.elements import (
    buttons, modal, 
    sidebar, table, 
    forms, html_input,
    card, row
)

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
    def admin_page(self,
        name: str = 'DEFAULT ADMIN_PAGE NAME',
        body: str ='',
        current_user: str ='DEFAULT_USER',
        modals: str = ""
    ):
        return admin.get_admin_page(
            name=name,
            sidebar=self.sidebar,
            body=body,
            current_user=current_user,
            modals=modals
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
        below: str = row.get_row(
            card.get_card(
                "default_card_name",
                buttons.get_split_button(),
                size=3
            )+
            card.get_card(
                "default_card_name",
                buttons.get_split_button(),
                size=3
            )+
            card.get_card(
                "default_card_name",
                buttons.get_split_button(),
                size=3
            )
        )
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
        return errors.get_404_page(
            'Page Not Found',
            self.sidebar,
            'DEFAULT_USER'
        )
    def forbidden_page(self):
        return errors.get_formidden_page(
            'Forbidden',
            self.sidebar,
            ''
        )