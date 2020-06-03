import pkgutil


def clear_database_info(data):
    for key, value in data.items():
        value.pop('PASSWORD')
        value.pop('USER')
    return data


def get_package_list():
    return [x[1] for x in list(pkgutil.iter_modules()) if not x[1].startswith('_')]
