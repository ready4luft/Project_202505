def get_together_games(anfisa_games, alisa_games):
# Напишите здесь код функции для поиска пересечений
    set1 = set(anfisa_games)
    set2 = set(alisa_games)
    together_games = set1.intersection(set2)
    return together_games

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)
# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print('👾', game)