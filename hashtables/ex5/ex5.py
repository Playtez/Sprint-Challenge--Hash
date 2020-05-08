def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    results = []

    for f in files:
        # slice the path and set the last item as the key in the cache and the path as the value
        key = f.split('/')
        cache.setdefault(key[-1], []).append(f)
    # if my query is in the cache, add the value to a list
    for q in queries:
        if 'nofile' in q:
            continue
        if q in cache:
            if len(cache[q]) > 1:
                for i in cache[q]:
                    results.append(i)
            else:
                results.append(cache[q][0])
        else:
            continue
    return results

    # query_str = [q_str for q_str in queries]
    # i = 0
    # j = len(query_str)
    # # loop through the queries and take out individual strings
    # for path in files:
    #     if i < j:
    #         if query_str[i] in path:
    #             cache[query_str[i]] = path
    #             i = i + 1
    #         else:
    #             i = i + 1
    #     else:
    #         return
    # for q in queries:
    #     if q in cache:
    #         results.append(cache[q])
    #     else:
    #         return results
    # return results

    # for query_str in queries:
    #     for path in files:
    #         if query_str in path:
    #             cache[query_str] = path

    # for q in queries:
    #     if q in cache:
    #         results.append(cache[q])

    # return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
