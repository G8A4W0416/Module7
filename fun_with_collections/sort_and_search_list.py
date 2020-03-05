def sort_list(list_to_sort):
    list_to_sort.sort()
    return list_to_sort
    # this is returning the sorted array. I included the return to be able to assert that the expected array and the
    # actual array are equal



def search_list(list_to_search):
    user_input = input("What is the item you are searching for? ")

    try:
        index = list_to_search.index(user_input)
    except ValueError:
        index = -1

    return index
