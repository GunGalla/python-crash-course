# Упражнение 6.6

people = {
    'viktor': 'java',
    'pavel': 'rust',
    'jen': 'python',
    'evgenia': 'kotlin',
    'edward': 'ruby',
}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for taken the poll, {person.title()}!")
    else:
        print(f"Please, take a poll, {person.title()}!")
