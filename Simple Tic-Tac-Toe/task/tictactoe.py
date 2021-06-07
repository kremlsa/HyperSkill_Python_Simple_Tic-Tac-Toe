# write your code here
print("Enter cells:")
user_field = list(input())
print("---------")
print("|", user_field[0], user_field[1], user_field[2], "|")
print("|", user_field[3], user_field[4], user_field[5], "|")
print("|", user_field[6], user_field[7], user_field[8], "|")
print("---------")


def is_player_win(player):
    if user_field[0] == player and user_field[1] == player and user_field[2] == player:
        return True
    if user_field[3] == player and user_field[4] == player and user_field[5] == player:
        return True
    if user_field[6] == player and user_field[7] == player and user_field[8] == player:
        return True
    if user_field[0] == player and user_field[3] == player and user_field[6] == player:
        return True
    if user_field[1] == player and user_field[4] == player and user_field[7] == player:
        return True
    if user_field[2] == player and user_field[5] == player and user_field[8] == player:
        return True
    if user_field[0] == player and user_field[4] == player and user_field[8] == player:
        return True
    if user_field[2] == player and user_field[4] == player and user_field[6] == player:
        return True
    return False


def count_letter(letter):
    return len([i for i in user_field if i == letter])


def is_impossible():
    if count_letter("X") > count_letter("O") + 1:
        return True
    if count_letter("O") > count_letter("X") + 1:
        return True
    if is_player_win("X") and is_player_win("O"):
        return True


def is_draw():
    if count_letter("_") == 0:
        return True


if is_impossible():
    print("Impossible")
elif is_player_win("X"):
    print("X wins")
elif is_player_win("O"):
    print("O wins")
elif is_draw():
    print("Draw")
else:
    print("Game not finished")
