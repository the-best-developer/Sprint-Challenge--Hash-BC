#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """

    for tick in tickets:
        hash_table_insert(hashtable, tick.source, tick.destination)
    
    # Pull the ticket with the source of NONE, this is our first flight
    start = hash_table_retrieve(hashtable, 'NONE')

    flight = start

    # while our next flight is NOT none, keep searching for the end
    while flight != 'NONE':
        # Add flight and set flight to the destination of the current flight
        route.append(flight)
        flight = hash_table_retrieve(hashtable, flight)

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA"]
result = reconstruct_trip(tickets, 3)