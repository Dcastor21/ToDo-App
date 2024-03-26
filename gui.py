import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add_button = sg.Button("Add")

window = sg.Window("My ToDo App",
                   layout=[[label], [input_box,add_button]],
                   font= ('Helvetica',20))
window.read()
window.close()
