def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    # for index, value in enumerate(weights):
    #     cache[value] = index
    #     target = limit - weights[index]

    # return target
    # does hash table of cache contain limit - weight

    # for key, value in cache.items():
    #     print(key, value)
    #     if target[value] == cache[key]:
    #         print("hello")

    # Pseudo code
    # General case what should happen most often?
    # iterate over the list of weights
    # while the limit is not equal to a + b
    # find two indices sum to the limit
    # return a tuple containing

    # store each weight in the input list as keys

    for index, v in enumerate(weights):
        cache.setdefault(v, []).append(index)

    for i in weights:
        target = limit - i
        if target in cache:
            if cache[target] > cache[i]:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[target][0], cache[i][1])
                return (cache[target][0], cache[i][0])
            else:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[i][1], cache[target][0])
                return (cache[i][0], cache[target][0])
    return None
