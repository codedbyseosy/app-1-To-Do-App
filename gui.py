import functions
import  PySimpleGUI as sg

label = sg.Text("Type in a to-do") #Text is not a function but a type assocaited with pysimplegu
input_box = sg.InputText(tooltip="Enter todo", key="todo") #InputText is not a function but a type assocaited with pysimplegu
add_button = sg.Button("Add")

window = sg.Window('My To-DO App', 
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20)) #Window is not a function but a type assocaited with pysimplegui, inside the bracket and quotes is an instance of window



while True: #this will keep the window open
    event, values = window.read() #read is a method i.e. like a list with .upper(), .capitalize() etc. It displays the window
                              #it also returns a tuple containing a string which describes the name of the button THAT IS PRESSED
                              #as well as a dictionary of which its key is defined in the input text class as "todo" and its value is defined in as what the user enters in
                              #the input text class

    print(event) #print out the name of the button "Add"
    print(values) #print out the dictionary containing the key labelled "todo" and input value entered

    match event:
        case "Add":
            todos = functions.get_todos() #call the function
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

window.close()



