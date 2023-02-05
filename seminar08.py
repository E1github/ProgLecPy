# **Задача:** Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# *(прямая отсылка [к первому семинару “введение в базы данных”](https://www.notion.so/ada887424df04be6b876ee8734aabcf1))*
# <aside>
# ❗ Решение каждой задачи начинается с обсуждения, только после этого пишется код.
# </aside>


def GetClasses():
    with open('Lesson_008\school\classes.txt', 'r') as file:
        temp = file.readlines()
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = element[element.index('[') + 1:-2].split(', ') 
            print(classes)