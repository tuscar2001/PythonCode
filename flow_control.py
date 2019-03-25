def is_comment(item):
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    """Execute a stack program.
    Args: Any stack like program containing where each item in the stack
    is a callable oprators or non callabel operands. The top most items
    on the stack may be strings beginning with # for the purposes of
    documentation. Stack like means support for:
    item=stack.poop(): remove and return the top item
    stack.append(item) puch an item to the top
    if stack   False in a boolean context when empty"""

    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:
        print ("Empty prograrm")
        return

    #evaluate the program
    pending = []

    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print ("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print ("Program successful. ")
        print ("Result: ", pending)

    print ("Finished")

if __name__ == '__main__':
    import operator

    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    execute(program)



######################################for else ###################################################################################




def go_north(position):
    i, j = position
    new_position = (i, j + 1)
    return new_position

def go_south(position):
    i, j = position
    new_position = (i, j - 1)
    return new_position


def go_east(position):
    i, j = position
    new_position = (i + 1, j)
    return new_position

def go_west(position):
    i, j = (position)
    new_position = (i - 1, j)
    return new_position

def look(position):
    return position

def quit(position):
    return None

def labyrinth(position, alive):
    print ("You are in a maze of twisty passages, all alike.")
    return position, alive

def dark_forest_road(position, alive):
    print ("You are on a roaf in a dark forest. To the north you can see a tower")
    return position, alive

def tall_tower(position, alive):
    print ("There is a tall tower here, with no obvious door. A path leads East")
    return position, alive

def rabbit_hole(position, alive):
    print ("You fall down a rabbit hole into a labyrinth")
    return (0, 0), alive

def lava_pit(position, alive):
    print ("You fall into a lava pit")
    return position, False


def play():

    position = (0, 0)
    alive = True

    while position:

        # if position == (0, 0):
        #     print ("You are in a maze of twisty passages, all alike")
        # elif position == (1, 0):
        #     print ("You are on a roaf in a dark forest. To the north you can see a tower")
        # elif position == (1, 1):
        #     print ("There is a tall tower here, with no obvious door. A path leads East")
        # else:
        #     print ("There is nothing here.")
        # the if else above can be converted into lambda functions as below:

        locations = {
            (0, 0): labyrinth,
            (1, 0): dark_forest_road,
            (1, 1): tall_tower,
            (2, 1): rabbit_hole,
            (1, 2): lava_pit,
        }

        try:
            location_action = locations[position]
        except KeyError:
            print ("There is nothing here.")
        else:
            position, alive = location_action(position, alive)

        if not alive:
            print ("Sorry, You're done")
            break

        command = input()

        # i, j = position
        # if command == "N":
        #     position = (i, j + 1)
        # elif command == "E":
        #     position = (i + 1, j)
        # elif command == "S":
        #     position == (i, j - 1)
        # elif command == "W":
        #     position = (i - 1, j)
        # elif command == "L":
        #     pass
        # elif command == "Q":
        #     position = None
        # else:
        #     print ("I don't understand")

       # the if else above can be converted into lambda functions as below:
        actions = {
            'N': go_north,
            'E': go_east,
            'S': go_south,
            'L': go_west,
            'L': look,
            'Q': quit,
        }

        try:
            command_action = actions[command]
        except keyError:
            print ("I don't understand")
        else:
            position = command_action(position)
    else:
        print ("You have chosen to leave the game")

    print ("Game Over")

if __name__ == '__main__':
    play()
