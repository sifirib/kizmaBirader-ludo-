import pygame
import time
import random

pygame.init()
screenx, screeny = 600, 600
screen = pygame.display.set_mode((screenx, screeny))
board = pygame.image.load('board.png')
screen.blit(board, [15, 15])

points = [[40, 225], [88, 225], [136, 225], [184, 225], [232, 225],
          [232, 177], [232, 129], [232, 81], [232, 33],
          [280, 33], [328, 33],
          [328, 81], [328, 129], [328, 177], [328, 225],
          [376, 225], [424, 225], [472, 225], [520, 225],
          [520, 273], [520, 321],
          [472, 321], [424, 321], [376, 321], [328, 321],
          [328, 376], [328, 424], [328, 472], [328, 520],
          [280, 520], [232, 520],
          [232, 472], [232, 424], [232, 376], [232, 328],
          [184, 328], [136, 328], [88, 328], [40, 328],
          [40, 280]]


class Player:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + 24:
            if pos[1] > self.y and pos[1] < self.y + 24:
                return True

        return False

def draw_player(image, x, y):
    screen.blit(image, (x, y))

def roll_the_dice():
    return random.randint(1, 6)


def change_values():
    global players
    global color
    global bases
    global current_players
    global blues
    global reds
    global greens
    global yellows
    if color == 'blue':
        blues = current_players
        current_players = blues
        players = current_players + reds + greens + yellows
        bases = basepointsb
    if color == 'red':
        reds = current_players
        current_players = reds
        players = current_players + blues + greens + yellows
        bases = basepointsr
    if color == 'green':
        greens = current_players
        current_players = greens
        players = current_players + blues + reds + yellows
        bases = basepointsg
    if color == 'yellow':
        yellows = current_players
        current_players = yellows
        players = current_players + blues + reds + greens
        bases = basepointsy

def howmany_player_inbase(playerss, bases):
    quantity = 0
    for player in playerss:
        for i in range(4):
            if player.x == bases[i][0] and player.y == bases[i][1]:
                quantity += 1
                break
    return quantity


def choose_player():
    global running
    global current_players
    i = 0
    while True:
        player = current_players[i]
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            # MOUSE behaviours
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.isOver(pos):
                    return player, i
                    break

            if event.type == pygame.MOUSEMOTION:
                if player.isOver(pos):
                    pass
                else:
                    pass

        i += 1
        if i == len(current_players):
            i = 0

def get_current_point():
    global choosen_player
    global color
    global basepointsb
    global basepointsr
    global basepointsg
    global basepointsy
    for i in range(0, len(points)):
        if choosen_player.x == points[i][0] and choosen_player.y == points[i][1]:
            return i - 1
            break
    if color == "blue":
        for i in range(0, 4):
            if choosen_player.x == basepointsb[i][0] and choosen_player.y == basepointsb[i][1]:
                return  i - 4
                break
    if color == "red":
        for i in range(0, 4):
            if choosen_player.x == basepointsr[i][0] and choosen_player.y == basepointsr[i][1]:
                return  i - 4
                break
    if color == "green":
        for i in range(0, 4):
            if choosen_player.x == basepointsg[i][0] and choosen_player.y == basepointsg[i][1]:
                return  i - 4
                break
    if color == "yellow":
        for i in range(0, 4):
            if choosen_player.x == basepointsy[i][0] and choosen_player.y == basepointsy[i][1]:
                return  i - 4
                break

reds = []
blues = []
greens = []
yellows = []
blues.append(Player('blueplayer.png', 35, 30))
blues.append(Player('blueplayer.png', 85, 30))
blues.append(Player('blueplayer.png', 35, 85))
blues.append(Player('blueplayer.png', 85, 85))
reds.append(Player('redplayer.png', 480, 30))
reds.append(Player('redplayer.png', 530, 30))
reds.append(Player('redplayer.png', 480, 85))
reds.append(Player('redplayer.png', 530, 85))
greens.append(Player('greenplayer.png', 475, 475))
greens.append(Player('greenplayer.png', 525, 475))
greens.append(Player('greenplayer.png', 475, 525))
greens.append(Player('greenplayer.png', 525, 525))
yellows.append(Player('yellowplayer.png', 35, 475))
yellows.append(Player('yellowplayer.png', 85, 475))
yellows.append(Player('yellowplayer.png', 35, 525))
yellows.append(Player('yellowplayer.png', 85, 525))
players = blues + reds + greens + yellows
basepointsb = [[35, 30], [85, 30], [35, 85], [85, 85]]
basepointsr = [[480, 30], [530, 30], [480, 85], [530, 85]]
basepointsg = [[475, 475], [525, 475], [475, 525], [525, 525]]
basepointsy = [[35, 475], [85, 475], [35, 525], [85, 525]]


colors = ['blue', 'red', 'green', 'yellow']
j = 0
l = 0
run = True
while run:
    color = colors[j]
    if color == 'blue':
        current_players = blues
        bases = basepointsb
    if color == 'red':
        current_players = reds
        bases = basepointsr
    if color == 'green':
        current_players = greens
        bases = basepointsg
    if color == 'yellow':
        current_players = yellows
        bases = basepointsy
    j += 1
    if j == 4:
        j = 0
    value_of_dice = 6
    l += 1

    print(color)

    running = True
    while running:
        change_values()
        for player in players:
            draw_player(player.image, player.x, player.y)

        pygame.display.update()
        print(value_of_dice)
        print("Waiting for your choice...")
        choosen_player, place_inlist = choose_player()
        print(choosen_player)
        if howmany_player_inbase(current_players, bases) < 4:
            current_point = get_current_point()
            next_point = value_of_dice + current_point
            if next_point > 39:
                next_point = next_point - 40
        if l < 4:
            current_point = 1
        print("current point: ", current_point)

        if value_of_dice < 6:

            if howmany_player_inbase(current_players, bases) < 4:
                print(choosen_player.x, choosen_player.y)
                current_players[place_inlist].x, current_players[place_inlist].y = points[next_point][0], points[next_point][1]
                change_values()
                screen.blit(board, [15, 15])
                for player in players:
                    draw_player(player.image, player.x, player.y)
                pygame.display.update()
                running = False
                print("You cannot move. Time to play for other player")

            if howmany_player_inbase(current_players, bases) == 4:
                print(player.x, player.y)
                print("Try again next time.")
                change_values()
                screen.blit(board, [15, 15])
                for player in players:
                    draw_player(player.image, player.x, player.y)
                pygame.display.update()
                running = False

        if value_of_dice == 6:
            running = True

            if howmany_player_inbase(current_players, bases) < 4:
                next_point = current_point + value_of_dice
                print(choosen_player.x, choosen_player.y)
                current_players[place_inlist].x, current_players[place_inlist].y = points[next_point][0], points[next_point][1]
                change_values()
                screen.blit(board, [15, 15])
                for player in players:
                    draw_player(player.image, player.x, player.y)
                pygame.display.update()
                running = False
                print("hmm")
            if howmany_player_inbase(current_players, bases) == 4:
                if color == "blue":
                    print("WOW")
                    current_players[place_inlist].x, current_players[place_inlist].y = points[0][0], points[0][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)
                if color == "red":
                    print("WOW")
                    current_players[place_inlist].x, current_players[place_inlist].y = points[10][0], points[10][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)
                if color == "green":
                    print("WOW")
                    current_players[place_inlist].x, current_players[place_inlist].y = points[20][0], points[20][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)
                if color == "yellow":
                    print("WOW")
                    current_players[place_inlist].x, current_players[place_inlist].y = points[30][0], points[30][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)


        value_of_dice = 4
        pygame.display.update()
