# while True:
#     print("Hello")

user_prompt = "Enter todo: "

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)
