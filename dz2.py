# HELP="""
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи."""

# tasks=[]

# run=True

# while run:
#   command=input("Введите команду: ")
#   if command=="help":
#     print(HELP)
#   elif command=="add":
#     task=input("Введите задачу: ")
#     tasks.append(task)
#     print("Задача добавлена")
#   elif command=="show":
#     print(tasks)
#   elif command =="exit":
#     print("Спасибо за использование! До свидания!")
#     break
#   else:
#     print("Неизвестная команда")
#     print("До свидания!")
#     break

HELP="""
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today=[]
tomorrow=[]
other=[]

run=True

while True:
    command=input("Введите команду: ")
    if command=="help":
      print(HELP)
    elif command=="add":
        task=input("Введите задачу")
        data=input("Введите дату: ")
        if data=="today":
          today.append("task")
        elif data=="tomorrow":
          tomorrow.append("task")
        else: 
          other.append("task")
        print(f'Задача {task} добавлена.')
    elif command=="show":
      print(today)
      print(tomorrow)
      print(other)
    elif command =="exit":
      print("Спасибо за использование! До свидания!")
      break
    else:
      print("Неизвестная команда")
      print("До свидания!")
      break
