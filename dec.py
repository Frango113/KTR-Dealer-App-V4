import datetime


def timestamp_submit(func):
    def wrapper(*args, **kwargs):
        current_time =datetime.datetime.now()
        print(f"{current_time} A registry has been added ")
        return func(*args, **kwargs)
    return wrapper

def timestamp_delete(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()
        print(f"{current_time} A registry has been deleted ")
        return func(*args, **kwargs)

    return wrapper

def timestamp_modify(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()
        print(f"{current_time} A registry has been modified ")
        return func(*args, **kwargs)

    return wrapper
