def print_list_models(model_name: str, iterable):
    print(model_name)
    for item in iterable:
        print(item.get_string())