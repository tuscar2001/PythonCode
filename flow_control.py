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




def ensure_has_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor


items = [2, 4, 36, 25, 9]
divisor = 5

dividend = ensure_has_divisible(items, divisor)
print ("{items} contains {dividend} which is a multiple of {divisor}".format(**locals()))