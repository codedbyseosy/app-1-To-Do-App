import functions
import  PySimpleGUI as sg

label = sg.Text("Type in a to-do") #Text is not a function but a type assocaited with pysimplegu
input_box = sg.InputText(tooltip="Enter todo") #InputText is not a function but a type assocaited with pysimplegu
add_button = sg.Button("Add")

window = sg.Window('My To-DO App', layout=[[label], [input_box, add_button]]) #Window is not a function but a type assocaited with pysimplegui, inside the bracket and quotes is an instance of window
window.read() #read is a method i.e. like a list with .upper(), .capitalize() etc. It displays the window
#print("Hello")
window.close()



