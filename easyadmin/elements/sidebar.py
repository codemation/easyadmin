def get_line_item(
    name: str = 'line_item name',
    href: str = '#',
    inside_header: str = 'inside_name name',
    items: list = None,
    icon: str = 'cog'
):
    inside_items = []
    inside_items_html = []
    for item in items:
        if 'href' in item:
            inside_name = item['name']
            inside_href = item['href']
            inside_item = f'<a class="collapse-item" href="{inside_href}">{inside_name}</a>'
        inside_items.append(
            inside_item
        )

    if inside_items:
        inside_items_html = '\n'.join(inside_items)
        inside_header = f'<h6 class="collapse-header">{inside_header}</h6>'

        inside_items_html = f"{inside_header}{inside_items_html}"

    if items:
        line_item = f"""
<!-- Nav Item - {name} Collapse Menu -->
<li class="nav-item">
    <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapse{name}" aria-expanded="true" aria-controls="collapse{name}">
        <i class="fas fa-fw fa-{icon}"></i>
        <span>{name}</span>
    </a>
    <div id="collapse{name}" class="collapse" aria-labelledby="heading{name}" data-parent="#accordionSidebar">
        <div class="bg-white py-2 collapse-inner rounded">
            {inside_items_html}
        </div>
    </div>
</li>
"""

    else:
        line_item = f"""
<!-- Nav Item - {name} -->
<li class="nav-item">
    <a class="nav-link" href="{href}">
        <i class="fas fa-fw fa-{icon}"></i>
        <span>{name}</span></a>
</li>
"""
    return line_item


def get_side_bar(
    title: dict,
    sections: dict
):
    divider = f"""
<!-- Divider -->
<hr class="sidebar-divider my-0">"""
    title_item = f"""
    <!-- Sidebar - Brand -->
<a class="sidebar-brand d-flex align-items-center justify-content-center" href="{title['href']}">
    <div class="sidebar-brand-text mx-3">{title['name']}</div>
</a>"""

    ## Get line items from sections config
    section_items = [divider]
    for section in sections:
        section_title = None
        if 'title' in section:
            section_title = f"""<div class="sidebar-heading">{section['title']}</div>"""
            section_items.append(section_title)
        for section_item in section['items']:
            section_items.append(
                get_line_item(
                    section_item['name'],
                    section_item['href'],
                    section_item['inside_header'] if 'inside_header' in section_item else None,
                    section_item['items'],
                    icon=section_item['icon'] if 'icon' in section_item else 'cog'
                )
            )
        # add divider between each section
        section_items.append(divider)

    sections_html = ''.join(section_items)
    side_bar = f"""
<!-- Sidebar -->

<ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">
    {title_item}
    {sections_html}
</ul"""

    return side_bar

def test():
    side_bar_config = {
        'title': {
            'name': 'EasyAuth',
            'href': '#'
        },
        'sections': [
            {
                'title': 'ADMIN',
                'items': [
                    {
                        'name':  'Users',
                        'href': 'index.html',
                        'items': []
                    },
                    {
                        'name':  'Groups',
                        'href': 'admin.html',
                        'items': []
                    },
                    {
                        'name':  'Roles',
                        'href': 'admin.html',
                        'items': []
                    },
                    {
                        'name':  'Actions',
                        'href': 'admin.html',
                        'items': []
                    }
                ]
            }
        ]
    }
    html = get_side_bar(
        side_bar_config['title'],
        side_bar_config['sections']
    )
    print(html)
    return html

if __name__ == '__main__':
    test()
