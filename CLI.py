from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f" It is {now}")

while True:
    users_action = input(" Type add, show, edit or exit:")
    users_action = users_action.strip()

    if users_action.startswith("add"):
        todo = users_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos( todos)

    elif users_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif users_action.startswith('edit'):
        try:
            number = int(users_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            write_todos(todos,"todos.txt")
        except ValueError:
            print(f"your command isn't Valid")
            continue

    elif users_action.startswith('complete'):
        try:
            number = int(users_action[9:])

            todos = get_todos()
            index = number - 1
            todos_to_remove = todos[index]

            todos.pop(index)

            write_todos =(todos)
            message = f'Todo {todos_to_remove} was removed from the list'
            print(message)

        except IndexError:
            print(" there is no item with that number")
            continue
    elif 'exit':
        break

else:
    print("command not valid.")

print("bye!")
