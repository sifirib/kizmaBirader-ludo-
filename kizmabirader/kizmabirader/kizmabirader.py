import pygame
import time
import random

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 20)
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

parks = [[85, 277],[133, 277 ],[181, 277],[229, 277],
         [280, 80],[280, 128],[280, 178],[280, 228],
         [480, 277],[430, 277],[380, 277],[330, 277],
         [280, 480],[280, 430],[280, 380],[280, 330]]

parkb = [[85, 277],[133, 277 ],[181, 277],[229, 277]]
parkr = [[280, 80],[280, 128],[280, 178],[280, 228]]
parkg = [[480, 277],[430, 277],[380, 277],[330, 277]]
parky = [[280, 480],[280, 430],[280, 380],[280, 330]]

class Player:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + 40:
            if pos[1] > self.y and pos[1] < self.y + 40:
                return True

        return False

def draw_player(image, x, y):
    screen.blit(image, (x, y))

def roll_the_dice():
    return random.randint(1, 6)

def draw_dice():
    global value_of_dice
    if value_of_dice == 1:
        image = pygame.image.load("dice_1.png")
    if value_of_dice == 2:
        image = pygame.image.load("dice_2.png")
    if value_of_dice == 3:
        image = pygame.image.load("dice_3.png")
    if value_of_dice == 4:
        image = pygame.image.load("dice_4.png")
    if value_of_dice == 5:
        image = pygame.image.load("dice_5.png")
    if value_of_dice == 6:
        image = pygame.image.load("dice_6.png")
    screen.blit(image, (275, 275))


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
            pygame.display.update()

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

    for i in range(0, len(points)):
        if choosen_player.x == points[i][0] and choosen_player.y == points[i][1]:
            return i
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

def can_park():
    if color == 'blue':
        i = 39
        k = 6
    if color == 'red':
        i = 9
        k = 15
    if color == 'green':
        i = 19
        k = 25
    if color == 'yellow':
        i = 29
        k = 35
    j = False
    for i in range(0, len(points)):
        if choosen_player.x == points[i][0] and choosen_player.y == points[i][1]:
            j = True
            break

    if j:
        x, y = choosen_player.x, choosen_player.y
        index = points.index([x, y])

        if value_of_dice > i - index and value_of_dice < i - index + 5 and index <= i and index > k:
            print("You can park :)")
            return True, value_of_dice - (i - index) - 1

        else:
            print("You can't park!")
            return False, 0
    else:
        print("You can't park!")
        return False, 0


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
basepoints = basepointsb + basepointsr + basepointsg + basepointsy


colors = ['blue', 'red', 'green', 'yellow']
j = 0
l = 0
run = True
for player in players:
    draw_player(player.image, player.x, player.y)

pygame.display.update()
while run:
    color = colors[j]
    if color == 'blue':
        text_color = (0, 0, 255)
        text_place = [70, 180 ]
        current_players = blues
        bases = basepointsb
        parkpoints = parkb
    if color == 'red':
        text_color = (255, 0, 0)
        text_place = [400, 180 ]
        current_players = reds
        bases = basepointsr
        parkpoints = parkr
    if color == 'green':
        text_color = (0, 255, 0)
        text_place = [400, 400]
        current_players = greens
        bases = basepointsg
        parkpoints = parkg
    if color == 'yellow':
        text_color = (200, 200, 0)
        text_place = [60, 390]
        current_players = yellows
        bases = basepointsy
        parkpoints = parky
    j += 1
    if j == 4:
        j = 0
    l += 1
    print(color)
    text = font.render("YOUR TURN", True, text_color)
    text_rect = text.get_rect()
    screen.blit(board, [15, 15])
    screen.blit(text, text_place)
    for player in players:
        draw_player(player.image, player.x, player.y)
    pygame.display.update()

    running = True
    while running:
        value_of_dice = roll_the_dice()
        draw_dice()
        pygame.display.update()
        print("Value of the dice: ", value_of_dice)
        change_values()

        print(value_of_dice)
        print("Waiting for your choice...")
        if howmany_player_inbase(current_players, bases) == 4 and value_of_dice < 6:
            print("Try at the next time")
            running = False
            time.sleep(1)

        else:
            ok = True
            while ok:
                m = 0
                choosen_player, place_inlist = choose_player()
                if value_of_dice < 6:
                    for k in range(0, len(basepoints)):
                        if choosen_player.x == basepoints[k][0] and choosen_player.y == basepoints[k][1]:
                            print("Try to choose another one!")
                            ok = True
                            break
                        ok = False
                        current_point = get_current_point()
                        next_point = value_of_dice + current_point
                        canpark, parkstep_no = can_park()
                        if canpark:
                            next_point = parkstep_no - 1
                if value_of_dice == 6:
                    ok = False
                    for k in range(0, len(basepoints)):
                        if choosen_player.x == basepoints[k][0] and choosen_player.y == basepoints[k][1]:
                            if color == "blue":
                                current_point = 0
                            if color == "red":
                                current_point = 10
                            if color == "green":
                                current_point = 20
                            if color == "yellow":
                                current_point = 30
                            next_point = current_point
                            break
                        else:
                            current_point = get_current_point()
                            next_point = value_of_dice + current_point
                            canpark, parkstep_no = can_park()
                            if canpark:
                                next_point = parkstep_no - 1
            if next_point > 39:
                next_point = next_point - 40
            print("current point: ", current_point)

            if value_of_dice < 6:
                running = False
                for k in range(0, len(basepoints)):
                    if choosen_player.x == basepoints[k][0] and choosen_player.y == basepoints[k][1]:
                        running = False
                if howmany_player_inbase(current_players, bases) < 4:

                    print(choosen_player.x, choosen_player.y)
                    if canpark:
                        current_players[place_inlist].x, current_players[place_inlist].y = parkpoints[next_point][0], parkpoints[next_point][1]
                    current_players[place_inlist].x, current_players[place_inlist].y = points[next_point][0], points[next_point][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)
                    print("You cannot move. Time to play for other player")

            if value_of_dice == 6:
                running = True
                print("Huh u got the 6")

                if howmany_player_inbase(current_players, bases) < 4:
                    if next_point > 39:
                        next_point = next_point - 40
                    print(choosen_player.x, choosen_player.y)
                    if canpark:
                        current_players[place_inlist].x, current_players[place_inlist].y = parkpoints[next_point][0], parkpoints[next_point][1]
                    current_players[place_inlist].x, current_players[place_inlist].y = points[next_point][0], points[next_point][1]
                    change_values()
                    screen.blit(board, [15, 15])
                    for player in players:
                        draw_player(player.image, player.x, player.y)
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

        pygame.display.update()
