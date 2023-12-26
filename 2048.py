import random


def game_start(game_list):
    x_1, y_1 = random.randint(0, 3), random.randint(0, 3)
    x_2, y_2 = random.randint(0, 3), random.randint(0, 3)
    if x_1 == x_2 and y_1 == y_2:
        return game_start(game_list)
    else:
        game_list[x_1][y_1] = 2
        game_list[x_2][y_2] = 2 ** random.randint(1, 2)
        for i in game_list:print(i)
        return game_list


def push_right(game_list):
    for i in range(3, -1, -1):
        for j in range(2, -1, -1):
            if game_list[i][j] > game_list[i][j + 1] and game_list[i][j + 1] == 0:
                game_list[i][j + 1] = game_list[i][j]
                game_list[i][j] = 0
                return push_right(game_list)

            elif game_list[i][j] == game_list[i][j + 1] and game_list[i][j] != 0:
                game_list[i][j + 1] *= 2
                game_list[i][j] = 0
                return push_right(game_list)

    else:
        for i in game_list: print(i)
        return game_list


def push_left(game_list):
    for i in range(4):
        for j in range(3):
            if game_list[i][j] < game_list[i][j + 1] and game_list[i][j] == 0:
                game_list[i][j] = game_list[i][j + 1]
                game_list[i][j + 1] = 0
                return push_left(game_list)

            elif game_list[i][j] == game_list[i][j + 1] and game_list[i][j] != 0:
                game_list[i][j] *= 2
                game_list[i][j + 1] = 0
                return push_left(game_list)

    else:
        for i in game_list: print(i)
        return game_list


def push_up(game_list):
    for i in range(3):
        for j in range(4):
            if game_list[i][j] < game_list[i+1][j] and game_list[i][j] == 0:
                game_list[i][j] = game_list[i+1][j]
                game_list[i+1][j] = 0
                return push_up(game_list)

            elif game_list[i][j] == game_list[i+1][j] and game_list[i][j] != 0:
                game_list[i][j] *= 2
                game_list[i+1][j] = 0
                return push_up(game_list)

    else:
        for i in game_list: print(i)
        return game_list

def push_down(game_list):
    for i in range(2,-1,-1):
        for j in range(3,-1,-1):
            if game_list[i][j] > game_list[i+1][j] and game_list[i+1][j] == 0:
                game_list[i+1][j] = game_list[i][j]
                game_list[i][j] = 0
                return push_down(game_list)

            elif game_list[i][j] == game_list[i+1][j] and game_list[i+1][j] != 0:
                game_list[i+1][j] *= 2
                game_list[i][j] = 0
                return push_down(game_list)

    else:
        for i in game_list: print(i)
        return game_list

def random_number(game_list):
    r_x=random.randint(0, 3)
    r_y=random.randint(0, 3)
    if game_list[r_x][r_y]==0:
        game_list[r_x][r_y]=2
        return game_list
    else:
        return random_number(game_list)

def lost(game_list):
    count = len([item for row in game_list for item in row if item == 0])
    for i in range(0,3):
        for j in range(0,3):
            if count==0 and game_list[i][j]!=game_list[i][j+1] and game_list[i][j]!=game_list[i+1][j]:
                print("You LOST!!!" * 3)
                quit()
            else:pass

def win(game_list):
    for i in game_list:
        for win in i:
            if win==2048:
                print("You Win!!!"*3)
            else:pass

def choose(game_list):
    old_game_list = game_list.copy()
    h = input("选择:")
    if h == "w":
        new_game_list=push_up(game_list)
        print(old_game_list,new_game_list)
        if old_game_list==new_game_list:
            return choose(old_game_list)
        elif old_game_list!=new_game_list and len([item for row in game_list for item in row if item == 0]) > 0:
            return random_number(game_list)

    elif h == "s":
        new_game_list = push_down(game_list)
        print(old_game_list, new_game_list)
        if old_game_list == new_game_list:
            return choose(old_game_list)
        elif old_game_list != new_game_list and len([item for row in game_list for item in row if item == 0]) > 0:
            return random_number(game_list)

    elif h == "a":
        new_game_list = push_left(game_list)
        print(old_game_list, new_game_list)
        if old_game_list == new_game_list:
            return choose(old_game_list)
        elif old_game_list != new_game_list and len([item for row in game_list for item in row if item == 0]) > 0:
            return random_number(game_list)

    elif h == "d":
        new_game_list = push_right(game_list)
        print(old_game_list, new_game_list)
        if old_game_list == new_game_list:
            return choose(old_game_list)
        elif old_game_list != new_game_list and len([item for row in game_list for item in row if item == 0]) > 0:
            return random_number(game_list)

    elif h == "q":
        quit()

    else:
        print("What are you doing now?!!")
    print("-------------------------------------")
def main():
    game_list = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
    game_start(game_list)

    while True:
        win(game_list)
        lost(game_list)
        choose(game_list)

choose([[2, 3, 4, 5],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]])