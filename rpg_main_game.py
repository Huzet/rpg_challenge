#!/usr/bin/python3

import math

'''
Code added by Tomas
'''
def compass():
    location = rooms[currentRoom]
    print(f'''Compass:
    
                 ("north"){location.get("north", "")}
                     
        ("west"){location.get("west", "")} -- <+> -- ("east"){location.get("east", "")}
                     
                 ("south"){location.get("south", "")}
    ''') 

def mini_map(x_length, y_heigth):
    # create box
    my_box = []
    for y in range(0, y_heigth):
        row = []
        for x in range(0, x_length):
            row.append('*')
        my_box.append(row)
    # place starting point in middle of matrix: X is were user is at
    my_box[math.floor(y_heigth / 2)][math.floor(x_length / 2)] = "X"
    return my_box

def print_mini_map(map):
    for row in map:
        x = ""
        for elem in row:
            if elem == "*":
                x = x + " "
            else:
                x = x + elem
        print(x)

def update_mini_map(map, direction):
    # update map location
    for row in range(0,len(map)):
        try:
            x = map[row].index("X")
            map[row][x] = "+"
            if direction == "east":
                map[row][x + 1] = "X"
            elif direction == "west":
                map[row][x - 1] = "X"
            elif direction == "north":
                map[row - 1][x] = "X"
            elif direction == "south":
                map[row + 1][x] = "X"
            else:
                print("something went wrong finding X or placing new X marker")
            break
        except:
            continue

    print("Previous Grid: "+ str(x) + "  " + str(row))
    # extend map so we dont run out of space if needed
    # check if running out of room on left
    if x == 1:
        for row_extend in range(0, len(map)):
            map[row_extend].insert(0, "*")
    # Check if running out of room on right
    elif x == len(map[0]) -2:
        for row_extend in range(0, len(map)):
                map[row_extend].append("*")
    # check if running out of room top
    elif row == 1:
            map.insert(0, (["*"] * len(map[0])))
    # check if running out of room bottom
    elif row == len(map) -2:
        map.append((["*"] * len(map[0])))

    return map

# lets create map
current_map = mini_map(5,5)

'''
Original code writen by Chad
'''
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
    go [direction]
    get [item]
''')

def showStatus():
    # print the player's current status
    compass()
    print("-----------MAP-------------")
    print_mini_map(current_map)
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            # update mini map
            print(f"Going {move[1]}")
            update_mini_map(current_map, move[1])
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break


'''
Tomas changes

    Homework goal per Chad:
        add 3 additional changes
    ideas:
        -Chads game will serve as intro, once player gets into garden thats when I will add my stuff.



TODO
[X] Add compass
[X] Add miniMap
[ ] Add HUD with miniMap, Items, health, some other cool stuff
[ ] Add screen wipe betwee turns
[ ] Add my level with maybe three rooms or something.....
'''

