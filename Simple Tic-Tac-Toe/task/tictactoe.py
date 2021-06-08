# write your code here
user_field = list("         ")
player = "X"


def print_field():
    print("---------")
    print("|", user_field[0], user_field[1], user_field[2], "|")
    print("|", user_field[3], user_field[4], user_field[5], "|")
    print("|", user_field[6], user_field[7], user_field[8], "|")
    print("---------")


def is_player_win():
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
    if count_letter(" ") == 0:
        return True


def convert_xy(x, y):
    return int((x - 1) * 3 + y) - 1


def make_move():
    global user_field
    while True:
        print("Enter the coordinates: ")
        x, y = input().split()
        if int(x) < 0 or int(x) > 3 or int(y) < 0 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
        elif user_field[convert_xy(int(x), int(y))] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            user_field[convert_xy(int(x), int(y))] = player
            break


print_field()
while True:
    make_move()
    print_field()
    if is_player_win():
        print(player, "wins")
        break
    if is_draw():
        print("Draw")
        break
    player = "O" if player == "X" else "X"
