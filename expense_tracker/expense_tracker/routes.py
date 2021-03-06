"""Configuration for this app's routes."""


def includeme(config):
    """Configuration for this app's routes."""
    config.add_static_view('static', 'expense_tracker:static')
    config.add_route('list', '/')
    config.add_route('detail', '/expense/{id:\d+}')
    config.add_route('create', '/new-expense')
    config.add_route('edit', '/expense/{id:\d+}/edit')
    config.add_route('category', '/expense/{cat:\w+}')
