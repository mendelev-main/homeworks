# Создать список учеников подобной структуры. Определить средний балл каждого студента по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.
pupils = [
    {
        "firstname": "Masha",
        "group": 42,
        "physics": 7,
        "informatics": 6,
        "history": 8,
    },
    {
        "firstname": "Sasha",
        "group": 42,
        "physics": 3,
        "informatics": 4,
        "history": 5,
    },
    {
        "firstname": "Nikita",
        "group": 38,
        "physics": 8,
        "informatics": 8,
        "history": 6,
    },
]
for pupil in pupils:
    average = (pupil["physics"] + pupil["informatics"] + pupil["history"]) / 3
    if average > 4:
        print(pupil)
