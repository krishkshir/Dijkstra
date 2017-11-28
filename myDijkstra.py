#!/usr/bin/python
""" Implement Dijkstra's algorithm to find the shortest path between a start 
vertex on an undirected graph and every other vertex.

"""

def Dijkstra(a_G, a_s, a_d = None):
    """ Implement Dijkstra's algorithm
    : param a_G: Dictionary with vertices of graph as keys and the
        corresponding value being a dictionary with neighboring
        vertices as keys and distance to them from the original vertex as 
        values.
    : param a_s: Source vertex
    : param a_e: Destination vertex
    : returns D: A dictionary with vertices as keys and corresponding value
        is a list with the first element being a list of the shortest
        path to the vertex from a_s and the second element being the shortest
        distance to that vertex
    """
    # extract vertices from a_G and mark them all as unvisited
    unvisited = a_G.keys()
    # Initialize dictionary of shortest distances
    D = dict()
    for v in unvisited:
        D[v] = [[],float('inf')]
    # endfor #
    # Zero out distance to start vertex
    D[a_s][1] = 0.0
    # While all vertices haven't been yet visited
    while len(unvisited) > 0:
        # Select current node as min. of shortest distances so far computed
        minD, curr = min([(D[n][1],n) for n in unvisited])
        # Add current node to its path
        D[curr][0].append(curr)
        # We're at the destination already
        if curr == a_d:
            return a_d, D[a_d]
        # endif #
        # Loop over all neighboring vertices
        for n, d in a_G[curr].items():
            # make sure we haven't visited n already
            if n in unvisited:
                # compute distance to this neighbor through current vertex
                currd = minD + d
                # check if this distance is less than currently assigned
                # tentative distance
                if currd < D[n][1]:
                    # re-assign shortest distance
                    D[n][1] = currd
                    # shortest path to this vertex is shortest path to current
                    # vertex + the current vertex
                    D[n][0] = D[curr][0] + [curr]
                # endif #
            # endif #
        # endfor #
        # Remove current node from unvisited ones
        unvisited.remove(curr)
    # endwhile #
    return D
# enddef Dijkstra() #
if __name__ == "__main__":
    #sub = {'SF':{'Boston':110},'NY':{'LA':96},'Seattle':{'Jacksonville':94},'LA':{'Chicago':67},'Phoenix':{'Jacksonville':65,'Seattle':37},'Medford':{'Minneapolis':63,'Omaha':57},'Great Falls':{'Minneapolis':39,'Omaha'}}
    sub = dict()
    for city in ['San Francisco','Seattle','Medford','Los Angeles',
            'Great Falls','Salt Lake City','Phoenix','Denver','Albuquerque',
            'Minneapolis','Omaha','Dallas','Chicago','Memphis','Detroit',
            'Boston','New York','Washington','Charlotte','Jacksonville']:
        sub[city] = {}
    # endfor #
    sub['San Francisco'].update({'Boston':100})
    sub['Boston'].update({'San Francisco':100})
    sub['New York'].update({'Los Angeles':96})
    sub['Los Angeles'].update({'New York':96})
    sub['Seattle'].update({'Jacksonville':92})
    sub['Jacksonville'].update({'Seattle':92})
    sub['Los Angeles'].update({'Chicago':67})
    sub['Chicago'].update({'Los Angeles':67})
    sub['Phoenix'].update({'Jacksonville':65})
    sub['Jacksonville'].update({'Phoenix':65})
    sub['Medford'].update({'Minneapolis':63})
    sub['Minneapolis'].update({'Medford':63})
    sub['Omaha'].update({'Medford':57})
    sub['Medford'].update({'Omaha':57})
    sub['Great Falls'].update({'Minneapolis':49})
    sub['Minneapolis'].update({'Great Falls':49})
    sub['Phoenix'].update({'Seattle':37})
    sub['Seattle'].update({'Phoenix':37})
    sub['Great Falls'].update({'Omaha':35})
    sub['Omaha'].update({'Great Falls':35})
    sub['San Francisco'].update({'Great Falls':32})
    sub['Great Falls'].update({'San Francisco':32})
    sub['Washington'].update({'Memphis':29})
    sub['Memphis'].update({'Washington':29})
    sub['Seattle'].update({'Great Falls':24})
    sub['Great Falls'].update({'Seattle':24})
    sub['Denver'].update({'Dallas':23})
    sub['Dallas'].update({'Denver':23})
    sub['San Francisco'].update({'Salt Lake City':23})
    sub['Salt Lake City'].update({'San Francisco':23})
    sub['Minneapolis'].update({'Memphis':52})
    sub['Memphis'].update({'Minneapolis':52})
    sub['Detroit'].update({'Minneapolis':22})
    sub['Minneapolis'].update({'Detroit':22})
    sub['Albuquerque'].update({'Dallas':21})
    sub['Dallas'].update({'Albuquerque':21})
    sub['Denver'].update({'Great Falls':21})
    sub['Great Falls'].update({'Denver':21})
    sub['Chicago'].update({'Charlotte':20})
    sub['Charlotte'].update({'Chicago':20})
    sub['Memphis'].update({'Jacksonville':20})
    sub['Jacksonville'].update({'Memphis':20})
    sub['Detroit'].update({'New York':20})
    sub['New York'].update({'Detroit':20})
    sub['Memphis'].update({'Charlotte':19})
    sub['Charlotte'].update({'Memphis':19})
    sub['Denver'].update({'Omaha':19})
    sub['Omaha'].update({'Denver':19})
    sub['Chicago'].update({'Omaha':18})
    sub['Omaha'].update({'Chicago':18})
    sub['Omaha'].update({'Dallas':18})
    sub['Dallas'].update({'Omaha':18})
    sub['Salt Lake City'].update({'Albuquerque':16})
    sub['Albuquerque'].update({'Salt Lake City':16})
    sub['Detroit'].update({'Washington':15})
    sub['Washington'].update({'Detroit':15})
    sub['Memphis'].update({'Dallas':15})
    sub['Dallas'].update({'Memphis':15})
    sub['Chicago'].update({'Memphis':15})
    sub['Memphis'].update({'Chicago':15})
    sub['Denver'].update({'Salt Lake City':15})
    sub['Salt Lake City'].update({'Denver':15})
    sub['Minneapolis'].update({'Chicago':14})
    sub['Chicago'].update({'Minneapolis':14})
    sub['Great Falls'].update({'Salt Lake City':14})
    sub['Salt Lake City'].update({'Great Falls':14})
    sub['Los Angeles'].update({'Phoenix':13})
    sub['Phoenix'].update({'Los Angeles':13})
    sub['Phoenix'].update({'Albuquerque':12})
    sub['Albuquerque'].update({'Phoenix':12})
    sub['San Francisco'].update({'Los Angeles':12})
    sub['Los Angeles'].update({'San Francisco':12})
    sub['Charlotte'].update({'Washington':11})
    sub['Washington'].update({'Charlotte':11})
    sub['Jacksonville'].update({'Charlotte':11})
    sub['Charlotte'].update({'Jacksonville':11})
    sub['Seattle'].update({'Medford':11})
    sub['Medford'].update({'Seattle':11})
    sub['Minneapolis'].update({'Omaha':10})
    sub['Omaha'].update({'Minneapolis':10})
    sub['Chicago'].update({'Detroit':10})
    sub['Detroit'].update({'Chicago':10})
    sub['Denver'].update({'Albuquerque':10})
    sub['Albuquerque'].update({'Denver':10})
    sub['Medford'].update({'San Francisco':10})
    sub['San Francisco'].update({'Medford':10})
    sub['Washington'].update({'New York':8})
    sub['New York'].update({'Washington':8})
    sub['Boston'].update({'New York':7})
    sub['New York'].update({'Boston':7})
    print "US cities map:-"
    print sub
    # Perform Dijkstra's algorithm
    D = Dijkstra(sub,'San Francisco')
    #D = Dijkstra(sub,'San Francisco','Chicago')
    print "Shortest paths and minimum distances from San Francisco to:-"
    print D
# endif #
