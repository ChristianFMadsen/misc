import re
file = open('aoc23_d2p1_data.txt', 'r')
power_sum = 0
for string in file:
    game_ID = string.split(':')[0].split()[1]
    games_list = string.split(':')[1:][0].split(';')
    min_red = 0
    min_green = 0
    min_blue = 0
    for game in games_list:
        entries = game.split(',')
        for entry in entries:
            amount = int(re.findall(r'\d+', entry)[0])
            if 'red' in entry and amount > min_red:
                min_red = amount
            if 'green' in entry and amount > min_green:
                min_green = amount
            if 'blue' in entry and amount > min_blue:
                min_blue = amount
    power_sum += min_red*min_green*min_blue

print(power_sum)
