'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "Friends"
    elif to_member not in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "Followed by"
    elif to_member in social_graph[from_member]["following"] and from_member not in social_graph[to_member]["following"]:
        return "Follower"
    else:
        return "None"

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    horizontal_lists = []
    vertical_lists = []
    rdiagonal_lists = []
    ldiagonal_lists = []
    combination_list = []
    width = len(board)
    starting_element_limit = width - 2
    #Horizontal Combinations
    for a in range(len(board)):
        for b in range(len(board[a][0:starting_element_limit])):
            horizontal_lists.append([board[a][b], board[a][b+1], board[a][b+2]])
    #Vertical Combinations
    for c in range(len(board[0:starting_element_limit])):
        for d in range(len(board[c])):
            vertical_lists.append([board[c][d], board[c+1][d], board[b+2][d]])
    #Left-Leaning Diagonals
    for e in range(len(board[0:starting_element_limit])):
        for f in range(len(board[e][0:starting_element_limit])):
            ldiagonal_lists.append([board[e][f], board[e+1][f+1], board[e+2][f+2]])
    #Right-Leaning Diagonals
    for g in range(len(board[0:starting_element_limit])):
        for h in range(len(board[g][2:])):
            rdiagonal_lists.append([board[e][f], board[e+1][f-1], board[e+2][f-2]])
    combination_list = horizontal_lists + vertical_lists + rdiagonal_lists + ldiagonal_lists
    
    for i in combination_list:
        if i == ["X", "X", "X"]:
            return "X"
            break
        elif i == ["O", "O", "O"]:
            return "O"
            break
        else:
            pass
    return "None"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    for k, v in route_map.items():
        if k[0] == first_stop:
            travel_time = travel_time + v["travel_time_mins"]
            if k[1] == second_stop:
                break
            else:
                for l, m in route_map.items():
                    if l[1] == second_stop:
                        travel_time = travel_time + m["travel_time_mins"]
                        break
                    else:
                        travel_time = travel_time + m["travel_time_mins"]
                        
    return travel_time