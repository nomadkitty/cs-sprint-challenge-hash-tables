#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    flights = {}
    # if source is none, it's the head
    # if des is none, it's the tail
    # bulid my ticket dictionary
    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    # initialize my router
    curr_flight = flights["NONE"]
    # while not the last flight
    # append the current fight
    while curr_flight != "NONE":
        route.append(curr_flight)
        curr_flight = flights[curr_flight]
    route.append(curr_flight)
    return route
