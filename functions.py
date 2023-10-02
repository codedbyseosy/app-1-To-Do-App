FILEPATH = "todos_item.txt" #constant

def get_todos(filepath=FILEPATH): #default argument
    """ Read a text file and return the list 
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local 

def write_todos(todos_arg, filepath=FILEPATH): #default arguments come after non-default arguments
    """Write the to-do items list 
    in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
#this function retuns nothing

if __name__ == "__main__":
    print("Hello")
    print(get_todos())