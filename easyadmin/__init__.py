from easyadmin.pages import (
    login, 
    errors, 
    admin, 
    admin_table,
    register
)
from easyadmin.elements import (
    buttons, modal, 
    sidebar, table, 
    forms, html_input,
    card, row, scripts
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
                    }
                ]
            }]
    ):
        self.sidebar = sidebar.get_side_bar(
            title={'name': title, 'brand_onclick': f"OnClickUpdate('/DEFAULT_ACTION', 'page-body', loadChart)"},
            sections=side_bar_sections
        )
        self.on_load_scripts = []
    def admin_page(self,
        name: str = 'DEFAULT ADMIN_PAGE NAME',
        body: str ='',
        current_user: str ='DEFAULT_USER',
        topbar_extra = "",
        modals: str = "",
        google: str = '',
    ):
        return admin.get_admin_page(
            name=name,
            sidebar=self.sidebar,
            body=body,
            current_user=current_user,
            topbar_extra=topbar_extra,
            modals=modals,
            google=google
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
        above: str = forms.get_form(transform_id="page-body", run_after='loadChartDefaultChartName'),
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
        ) +
        scripts.get_chart(),
        google='',
    ):
        
        return admin_table.get_table_page(
            name,
            data,
            self.sidebar,
            current_user,
            modals,
            above=above,
            below=below + scripts.get_onload_scripts(
                self.on_load_scripts
            ),
            google=google
        )
    def login_page(self,
        title: str = 'Login Title Page',
        identity_type: str = 'username', # 'email' also possible
        login_action: str = '/login',
        login_method: str = 'post',
        welcome_message: str = 'Welcome Back!',
        google: str = '',
        google_redirect_url: str =  '',
    ):
        return login.get_login_page(
            title,
            identity_type,
            login_action,
            login_method,
            welcome_message,
            google=google,
            google_redirect_url=google_redirect_url
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