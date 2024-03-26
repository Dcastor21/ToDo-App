import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")

window = sg.Window("My ToDo App", layout=[[label, input_box]])
window.read()
window.close()
