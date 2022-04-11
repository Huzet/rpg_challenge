map = [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', 'X', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]

def print_mini_map(map):
    for row in map:
        x = ""
        for elem in row:
            if elem == "*":
                x = x + " "
            else:
                x = x + elem
        print(x)

def update_map(map, direction):
    # update map location
    for row in range(0,len(map)):
        try:
            x = map[row].index("X")
            print(x)
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
        print("short space left")
        for row_extend in range(0, len(map)):
            print("extend Left")
            map[row_extend].insert(0, "*")
    # Check if running out of room on right
    elif x == len(map[0]) -2:
        for row_extend in range(0, len(map)):
                print("extend Right")
                map[row_extend].append("*")
    # check if running out of room top
    elif row == 1:
            print("extend top")
            map.insert(0, (["*"] * len(map[0])))
    # check if running out of room bottom
    elif row == len(map) -2:
        print("extend bottom")
        map.append((["*"] * len(map[0])))
    else:
        print("Something went wrong extending map")

    return map


while True:
    # print_mini_map(map)
    print_mini_map(map)
    user_input = input("Go? ")

    update_map(map, user_input)










