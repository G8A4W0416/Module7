import array as arr


def sort_array(array_to_sort):
    len_of_arr = len(array_to_sort)

    for i in range(len_of_arr):
        for j in range(i + 1, len_of_arr):
            if array_to_sort[i] > array_to_sort[j]:
                temp = array_to_sort[i]
                array_to_sort[i] = array_to_sort[j]
                array_to_sort[j] = temp

    return array_to_sort
    # this is returning the sorted array. I included the return to be able to assert that the expected array and the
    # actual array are equal


def search_array(array_to_search):
    user_input = input("What is the item you are searching for? ")

    try:
        index = array_to_search.index(user_input)
    except ValueError:
        index = -1

    return index


if __name__ == '__main__':
    print(sort_array(arr.array('I', [99, 1, 4, 5, 36])))
