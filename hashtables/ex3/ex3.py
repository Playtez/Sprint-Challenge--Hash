def intersection(arrays):

    dictionary = {}
    all_values = []
    length = len(arrays)
    """
    YOUR CODE HERE
    set a cache
    if the inner list
    do we store each number in the cache?
    General case if number is in the cache

    [[-----0------], [------1------], [------2------]]
    [[1, 2, 3, 4, 5],[12, 7, 2, 9, 1], [99, 2, 7, 1,]]
    """

    for item in arrays:
        for value in item:
            if value in dictionary and value not in all_values:
                # cache[value] += 1
                all_values.append(value)
            else:
                dictionary[value] = 1
    # print(dictionary, "\n\n\n\n\n\n", all_values, "\n\n\n\n\n\n")

    return all_values

    # for item in all_values:
    # key will be number value will be number of instances

    # increment to 3
    # if the value is three then it exists in all three

    # for item in all_values:
    #     print(item)
    # for i, array in enumerate(arrays):
    #     cache[i] = array

    # for key, value in cache.items():
    #     print(key, "**** THIS IS KEY *****")

    # if the index is found in

    # for key, value in cache.items():
    #     print(key, value)
    #     # return result
    # for index in cache:
    #     print("===========", index)
    #     for i in arrays:
    #         print(i)
    # if cache[i] in i:


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
