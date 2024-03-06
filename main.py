while True:
    users_action = input(" Type add, show, edit or exit:")
    users_action = users_action.strip()

    match users_action:
        case 'add':
            todo = input('Enter a Todo:') + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            with open('todos.txt', 'r') as file:
                file.writelines(todos)

        case "show":
            with  open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("number of the todo to edit: "))
            number = number - 1

            with  open('todos.txt', 'r') as file:
                todos = file.readlines()
            print(f"Here is existing todos, {todos}")

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo

            print(f"Here is how it will be, {todos}")
            file.writelines(todos)

        case 'complete':
            number = int(input("number of the todo to complete"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todos_to_remove = todos[index]

            todos.pop(index)

            with open('todos.txt', 'r') as file:
                file.writelines(todos)

        case 'exit':
            break

print("bye!")
