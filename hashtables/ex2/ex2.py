#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    # iterate over tickets list and create our cache (key = source, value = destination)
    for i in tickets:
        cache[i.source] = i.destination
    # Set our starting point to the cache with key set to None (first location)
    current_value = cache['NONE']
    # While the length of our route is less than the number of tickets
    while len(route) < length:
        # Add the current destination to the route list
        route.append(current_value)
        # Change current_value to the current key's destination (starting point for the next flight)
        current_value = cache[current_value]

    # for t in cache:
    #     current_value = cache[t]
    #     # print(cache[t])
    #     # print(current_value)
    #     route.append(current_value)
    return route
