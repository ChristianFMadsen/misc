import re
file = open('aoc23_d2p1_data.txt', 'r')
max_red = 12
max_green = 13
max_blue = 14
ID_sum = 0
for string in file:
    game_ID = string.split(':')[0].split()[1]
    games_list = string.split(':')[1:][0].split(';')
    valid_game_counter = 0
    for game in games_list:
        valid_game = True
        entries = game.split(',')
        for entry in entries:
            amount = int(re.findall(r'\d+', entry)[0])
            if 'red' in entry and amount > max_red:
                valid_game = False
                break
            if 'green' in entry and amount > max_green:
                valid_game = False
                break
            if 'blue' in entry and amount > max_blue:
                valid_game = False
                break
        if valid_game:
            valid_game_counter += 1
    if valid_game_counter == len(games_list):
        ID_sum += int(game_ID)

print(ID_sum)
