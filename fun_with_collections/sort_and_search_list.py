def sort_list():
    pass


def search_list(list_to_search):
    user_input = input("What is the item you are searching for? ")

    try:
        index = list_to_search.index(user_input)
    except ValueError:
        index = -1

    return index
