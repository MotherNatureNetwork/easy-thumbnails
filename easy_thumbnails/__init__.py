VERSION = (2, 3, 0, 'post', 1)


def get_version(*args, **kwargs):
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from .get_version import get_version
    return get_version(*args, **kwargs)
