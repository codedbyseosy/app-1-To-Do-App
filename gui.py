import functions
import  PySimpleGUI as sg

label = sg.Text("Type in a to-do") #Text is not a function but a type assocaited with pysimplegu
input_box = sg.InputText(tooltip="Enter todo", key="todo") #InputText is not a function but a type assocaited with pysimplegu
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]) #todos is the key for this dict, not to be confused
                                                                                                   #with the key for the input box
edit_button = sg.Button("Edit")

window = sg.Window('My TO-DO App', 
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20)) #Window is not a function but a type assocaited with pysimplegui, inside the bracket and quotes is an instance of window



while True: #this will keep the window open
    event, values = window.read() #read is a method i.e. like a list with .upper(), .capitalize() etc. It displays the window
                              #it also returns a tuple containing a string which describes the name of the button THAT IS PRESSED
                              #as well as a dictionary of which its key is defined in the input text class as "todo" and its value 
                              #is defined in as what the user enters in the input text class

    print(1, event) #print out the name of the button "Add"
    print(2, values) #print out the dictionary containing the key labelled "todo" and input value entered
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos() #call the function
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #'[todos]' represents the key for the inputbox, we are updating the Listbox

        case "Edit":
            todo_to_edit = values['todos'][0] #to get the string of the todo selected to be replaced/edited
            new_todo = values['todo'] #the new todo we want to replace/edit an old todo

            todos = functions.get_todos()
            index = todos.index(todo_to_edit) #gives us the index that the user selects
            todos[index] = new_todo #replace the old todo at its former index with the new todo
            functions.write_todos(todos) #write updated lust back into todos.txt
            window['todos'].update(values=todos) #update is a method of the type Listbox. update the Listbox in realtime
                                                 #after editing. '[todos]' represents the key for the Listbox

        case "todos":
            window['todo'].update(value=values['todos'][0]) #update the current selection as we move through the list
                                                            #and place it in the input textbox. We are updating the Listbox

        case sg.WIN_CLOSED:
            break

window.close()



#todos - what the user selects (listbox)
#todo - what user adds (inputbox)

