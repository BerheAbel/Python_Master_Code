from getter import Player

tim = Player("Tim")
print(tim.name)
print(tim._level)
tim._level += 1

print(tim._level)

tim.level = 2
print(tim)

# tim.lives -= 1
# print(tim)

# tim.lives -= 1
# print(tim)
