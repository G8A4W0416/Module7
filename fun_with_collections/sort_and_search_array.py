import array as arr
def sort_array(list_to_sort):
    pass


def search_array(array_to_search):
    user_input = input("What is the item you are searching for? ")

    try:
        index = array_to_search.index(user_input)
    except ValueError:
        index = -1

    return index
