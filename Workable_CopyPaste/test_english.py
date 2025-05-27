english = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'backend developer'
}

# Доступ по ключу: как по-английски рука?
# print(english['рука'])
# print(input(english))
# print(english(input()))

russian_enter = input('Введите русское слово: ').lower()

try:
    print(f'Перевод: {english[russian_enter]}')
except KeyError:
    print('Такого слова в словаре нет')

# translation = english.get(russian_word, "Перевод не найден")
# print(f"👾 {translation}")