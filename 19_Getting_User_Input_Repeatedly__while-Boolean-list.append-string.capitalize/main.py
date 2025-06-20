user_prompt = "Enter todo: "

# while 2 > 1:
#     todo = input(user_prompt)

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)
