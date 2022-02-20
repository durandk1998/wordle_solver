from collections import defaultdict

def default_val(val):
    def default():
        return val
    return default

def get_default_dict(val):
    return defaultdict(default_val(val))
