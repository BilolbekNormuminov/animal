def input_int(message: str, error_message: str, predicate=lambda value: True):
    error_message = message if error_message is None else error_message

    while True:
        try:
            value = int(input(message))

            if not predicate(value):
                raise ValueError
        except ValueError:
            print(error_message)
        else:
            break

    return value


def input_str(message: str, error_message: str, predicate=lambda value: True):
    error_message = message if error_message is None else error_message

    while True:
        try:
            value = input(message)

            if not predicate(value):
                raise ValueError
        except ValueError:
            print(error_message)
        else:
            break

    return value
