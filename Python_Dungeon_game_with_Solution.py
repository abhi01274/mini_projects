# Dungeon Game

"""
Challenge 1
    It would be a 2 dimensional maze game 
    We would put the player in a random room in the grid 
    We would also put a monster in a random room in the grid
    We would out a door in a random room in the grid 
    The player would then move around the grid to find the door
    Don’t let he player go out of the edges of the grid 
    If they hit the monster room they are eaten by the monster 
    or if they reach the gate they win 
    Grid of Room = Collection of Coordinates 
    Player is a tuple, it contains two values  

"""



 
import random 

CELLS = [
(0,0),(0,1),(0,2) ,
(1,0),(1,1),(1,2) ,
(2,0),(2,1),(2,2)
]

def get_location() :
    # monster = random location 
    # door = random location 
    # start = random location 

    # if monster , door or start are the same , do it again 

    # return monster door and start 


def move_player ( player, move ):
    # player = (x,y)
    # Get the players current location 
    # If move is LEFT y - 1
    # if move is RIGHT y + 1
    # IF move is UP , x  - 1
    # IF move is DOWN , x  + 1

    # return player 


def get_moves ( player )
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    # If players y == 0 remove LEFT

    # If players x == 0 remove UP

    # If players y == 2 remove RIGHT

    # If players x == 2 remove DOWN

    return MOVES


while True:
    print("Welcome to my THE DUNGEON")
    print ("You are currently in room {} ") # fill with player position 
    print ("You can move {} ") # fill int with available moves 
    print ("Enter QUIT to quit")

    move = input( " > ")
    move = move.upper()
    if move == “QUIT” :
        break

#if its a good move change the players position 
# if it is a bad move don’t change anything

# if new player position is the door they win
# if new player position is the monster they loose

# other wise continue 



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random 

CELLS = [
(0,0),(0,1),(0,2) ,
(1,0),(1,1),(1,2) ,
(2,0),(2,1),(2,2)
]

def get_location() :
    # monster = random location 
    monster = random.choice(CELLS)
    # door = random location 
    door = random.choice(CELLS)

    # start = random location 
    start  = random.choice(CELLS)

    # if monster , door or start are the same , do it again 
    if monster == door or monster == start or door == start :
        return get_location() 

    # return monster door and start 
    return monster, door, start 



def get_moves ( player ):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    player = (x,y)

    # If players y == 0 remove LEFT
    if player[1] == 0:
        moves.remove('LEFT')

    # If players y == 2 remove RIGHT
    if player[1] == 2:
        moves.remove('RIGHT')

    # If players x == 0 remove UP
    if player[0] == 0:
        moves.remove('UP')


    # If players x == 2 remove DOWN
    if player[0] == 2:
        moves.remove('DOWN')

    return moves 

 

def move_player ( player, move ):
    # player = (x,y)
    x,y = player
    # Get the players current location 
    # If move is LEFT y - 1
    # if move is RIGHT y + 1
    # IF move is UP , x  - 1
    # IF move is DOWN , x  + 1

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP' :
        x -= 1
    elif move == 'DOWN':
        x += 1
    return x,y 


monster, door, player = get_location ()

while True:

    moves = get_moves(player)

    print("Welcome to my THE DUNGEON")
    print ("You are currently in room {} ".format(player)) # fill with player position 
    print ("You can move {} ".format(moves)) # fill int with available moves 
    print ("Enter QUIT to quit")

    move = input( " > ")
    move = move.upper()
    if move == "QUIT" :
        break

    #if its a good move change the players position 
    if move in moves :
        player = move_player(player, move)
        # if it is a bad move don’t change anything
    else :
        print ("Walls are hard, stop walking into it ")
        continue
    # if new player position is the door they win
    if player == door :
        print("You escaped")
        break
    # if new player position is the monster they loose
    elif player == monster :
        print ("You were eaten by the gruel monster ")
        break
# other wise continue 


"""
Challenge 2
Welcome message is getting printed every-time
Can we display the grid for the visual  

"""


def draw_map( player ):
    # Draw ASCII Map
    print( " _ _ _ ")
    tile = " | {}"

    for idx,cell in enumerate(CELLS)
    if idx in (0,2,3,4,6,7) :
        if cell == player :
            print ( tile.format('X'), end ='' )
        else :
            print ( tile.format("_", end='' )
    else :
        if cell == player :
            print ( tile.format('X |') ) 
        else:
            print ( tile.format('_ |') )


# call this draw function in the while true loop
draw_map(player)
 