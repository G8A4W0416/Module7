def get_input():
    pass


def make_list():
    inputs = []

    for i in range(3):
        try:
            value = int(get_input())
            inputs.insert(i, value)
        except ValueError:
            print("Invalid type.")

    return inputs
