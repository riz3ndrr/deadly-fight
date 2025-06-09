import pygame as pyg
from fighter import Fighter
from button import Button
import ast

pyg.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FLOOR_HEIGHT = 40

# colours
YELLOW = (255, 255, 0)
RED = (255, 0 , 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Game Variables
ROUND_NUM = 1
TEXT_ON_SCREEN_DURATION = 100


# Font
BIG_FONT = pyg.font.Font('assets/images/fonts/VT323-Regular.ttf', 150)
MED_FONT = pyg.font.Font('assets/images/fonts/VT323-Regular.ttf', 100)
font = pyg.font.Font('assets/images/fonts/VT323-Regular.ttf', 60)


screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pyg.display.set_caption('Deadly Fight')


# load sfx
skull_img = pyg.image.load("assets/images/misc/skull.png").convert_alpha()


# Load the game icon
pyg.display.set_icon(skull_img)

# set framerate
clock = pyg.time.Clock()
FPS = 60

# Score hashmap format:
# player : score
score = {1 : 0, 2 : 0}

def display_skull(x):
     # Skull
    scaled_skull = pyg.transform.scale(skull_img, (65,65))
    screen.blit(scaled_skull, (x, 150))


def display_score():
    global score
    # Display player 1 score
    if score[1] == 1:
        display_skull(10)
    if score[1] == 2:
        display_skull(10)
        display_skull(70)

    # Display player 2 score
    if score[2] == 1:
        display_skull(SCREEN_WIDTH - 80)
    if score[2] == 2:
        display_skull(SCREEN_WIDTH - 80)
        display_skull(SCREEN_WIDTH - 80 - 60)


def extract_fighter_sheet(fighter_id):
    """sdfds"""
    filename = 'assets/images/fighters/' + fighter_id + '.png'
    return pyg.image.load(filename)


def extract_fighter_data(fighter_id):
    """sdfds"""
    filename = f"fighter_data/fighter_info/{fighter_id}_DATA.txt"
    
    data = []
    infile = open(filename)
    lines = infile.read().splitlines()
    for line in lines:
        data.append(line)
    
    name, steps, indeces, size, scale, offset, fighter_id, can_transform = data
    indeces = ast.literal_eval(indeces)
    offset = ast.literal_eval(offset)

    can_transform_dict = {"True" : True, "False" : False}
    can_transform = can_transform_dict[can_transform]


    
    return [int(size), int(scale), offset, int(steps), indeces, name, fighter_id, can_transform]


# 
bg_image = pyg.image.load("assets/images/background/bg-sakura1.png").convert_alpha()
menu_image = pyg.image.load("assets/images/background/bg-img.jpg")

# function for drawing health bar
def draw_health_bar(health, x, y):
    ratio = health / 100
    pyg.draw.rect(screen, BLACK, (x - 5, y - 5 + 40, 410, 40))

    pyg.draw.rect(screen, RED, (x, y + 40, 400, 30))
    pyg.draw.rect(screen, YELLOW, (x, y + 40, 400 * ratio, 30))

def draw_meter_bar(meter, x, y):
    ratio = meter / 100
    pyg.draw.rect(screen, BLACK, (x - 5, y - 5 + 90, 410, 40))
    pyg.draw.rect(screen, BLUE, (x, y + 90, 400 * ratio, 30))

player1_index = 0
player2_index = 0

down_btn1 = Button(100, 440, screen, False, 'assets/images/misc/arrow.png', (100,100))
up_btn1 = Button(100, 350, screen, True, 'assets/images/misc/arrow.png', (100,100))

down_btn2 = Button(720, 440, screen, False, 'assets/images/misc/arrow.png', (100,100))
up_btn2 = Button(720, 350, screen, True, 'assets/images/misc/arrow.png', (100,100))

start_btn = Button(320, 200, screen, False, 'assets/images/misc/fight_btn.png', (300,150))

def draw_bg():
    
    """Draw background"""
    img = bg_image
    # if display_menu is False:
    #     img = bg_image
    # else:
    #     img = menu_image
    scaled_bg = pyg.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

    if display_menu:
        show_select_screen()


def show_select_screen():
    global player1_index, player2_index, fighter_2, fighter_1, display_menu, game_on
    player_names = [("The Puncher", "PNR"), 
                    ("The Stick", "STK"),
                    ("The Transformer", "TRN"),
                    ("The Volt", "VLT"),
                    ("The Boomer", "BMR")]
    player1 = player_names[player1_index]
    player2 = player_names[player2_index]

    # title screen:
    game_title_shadow = BIG_FONT.render("DEADLY FIGHT", True, BLACK)
    screen.blit(game_title_shadow, (140, 75))
    game_title = BIG_FONT.render("DEADLY FIGHT", True, WHITE)
    screen.blit(game_title, (135, 70))

    # Buttons for player 1
    if down_btn1.draw():
        player1_index += 1
        if player1_index == len(player_names):
            player1_index = 0
    if up_btn1.draw():
        if player1_index == 0:
            player1_index = len(player_names) - 1
        else:
            player1_index -= 1
    # Buttons for player 2
    if down_btn2.draw():
        player2_index += 1
        if player2_index == len(player_names):
            player2_index = 0
    if up_btn2.draw():
        if player2_index == 0:
            player2_index = len(player_names) - 1
        else:
            player2_index -= 1
   # Player 1's currently selected character
    player1_title_shadow = font.render("Player 1:", True, BLACK)
    screen.blit(player1_title_shadow, (35, 285))
    player1_title = font.render("Player 1:", True, WHITE)
    screen.blit(player1_title, (40, 280))

    player1_name_shadow = font.render(player1[0], True, BLACK)
    screen.blit(player1_name_shadow, (25, 405))
    player1_name = font.render(player1[0], True, WHITE)
    screen.blit(player1_name, (30, 400))

    # Player 2's currently selected character
    player2_title_shadow = font.render("Player 2:", True, BLACK)
    screen.blit(player2_title_shadow, (665, 285))
    player2_title = font.render("Player 2:", True, WHITE)
    screen.blit(player2_title, (670, 280))

    player2_name_shadow = font.render(player2[0], True, BLACK)
    screen.blit(player2_name_shadow, (625, 405))
    player2_name = font.render(player2[0], True, WHITE)
    screen.blit(player2_name, (630, 400))

    if start_btn.draw():
        fighter_1_data = extract_fighter_data(player1[1])
        fighter_2_data = extract_fighter_data(player2[1])

        # create two fighter instances
        fighter_1 = Fighter(200, 380, 1, False, fighter_1_data, extract_fighter_sheet(fighter_1_data[6]))
        fighter_2 = Fighter(700, 380, 2, True, fighter_2_data, extract_fighter_sheet(fighter_2_data[6]))
        display_menu = False
        game_on = True



def display_title(player, x):
    """Display fighter names"""
    text = font.render(player.name, True, BLACK)
    screen.blit(text, (x + 5, 0))
    bg_text = font.render(player.name, True, WHITE)
    screen.blit(bg_text, (x, -5))

def check_for_winner(fighter):
    """Check (if there is) who the winner is"""
    winner = None
    winner_player_num = None

    if fighter.health <= 0 or fighter.target.health <= 0:
        if fighter.health <= 0:
            winner = fighter.target.name
            winner_player_num = fighter.target.player
        else:
            winner = fighter.name
            winner_player_num = fighter.player
    return winner, winner_player_num


def display_intro():
    """Display the introduction"""
    global TEXT_ON_SCREEN_DURATION, INTRO_ON
    texts = [[f"ROUND {ROUND_NUM}", WHITE], ["FIGHT!", RED], ["", WHITE]]
    if INTRO_ON:
        if TEXT_ON_SCREEN_DURATION > 30:
            i = 0
        elif TEXT_ON_SCREEN_DURATION >= 0 and TEXT_ON_SCREEN_DURATION <= 30:
            i = 1
        else:
            # When the intro is over
            i = 2
            INTRO_ON = False
            TEXT_ON_SCREEN_DURATION = 110
            
    
    
        TEXT_ON_SCREEN_DURATION -= 1

        text = BIG_FONT.render(texts[i][0], True, BLACK)
        screen.blit(text, (300, 200))
        bg_text = BIG_FONT.render(texts[i][0], True, texts[i][1])
        screen.blit(bg_text, (300 - 5, 200- 5))


def update_score(winner_player_num):
    """update score"""
    global score
    score[winner_player_num] += 1

    

def display_winner(winner, winner_player_num):
    global TEXT_ON_SCREEN_DURATION, INTRO_ON, ROUND_NUM, BIG_FONT, run, fighter_1, fighter_2
    texts = [[f"{winner} wins!", WHITE], ["", WHITE],[f"Player {winner_player_num} wins!", WHITE]]

    if len(winner) >= 12:
        # font size is changed if character name too long
        used_font = MED_FONT
    else:
        used_font = BIG_FONT


    if TEXT_ON_SCREEN_DURATION > 0:
        i = 0
    else:
        update_score(winner_player_num)
        if score[1] == 2 or score[2] == 2:
            i = 2
        else:
            i = 1
            INTRO_ON = True
            
            # The 4th index is the fighter's data
            fighter_1.reset(200, False, fighter_1.data)
            fighter_2.reset(700, True, fighter_2.data)
            ROUND_NUM += 1
        TEXT_ON_SCREEN_DURATION = 110
            
            
    text = used_font.render(texts[i][0], True, BLACK)
    screen.blit(text,  (70, 200))
    bg_text = used_font.render(texts[i][0], True, texts[i][1])
    screen.blit(bg_text, (70 - 5, 200 - 5))
    TEXT_ON_SCREEN_DURATION -= 1







# Game Loop
run = True

INTRO_ON = True
# game_on = True
# display_menu = False
#CHANGE TO FALSE
display_menu = True
game_on = False

while run:
    clock.tick(FPS)
    #draw background
    draw_bg()
    if display_menu is False:
        display_intro()

        # Show health bars
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

        # Update fighters' meter
        fighter_1.update_meter()
        fighter_2.update_meter()

        # Draw meter bars
        draw_meter_bar(fighter_1.meter, 20, 20)
        draw_meter_bar(fighter_2.meter, 580, 20)

        # Display fighter names:
        display_title(fighter_1, 15)
        display_title(fighter_2, SCREEN_WIDTH - 430)

        # Display scores
        display_score()

        # draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # update fighter animation
        fighter_1.update()
        fighter_2.update()


    if INTRO_ON is False and game_on is True:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, FLOOR_HEIGHT)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, FLOOR_HEIGHT)

        fighter_1.update_projectile(screen, SCREEN_WIDTH)
        fighter_2.update_projectile(screen, SCREEN_WIDTH)

        fighter_1.misc_attack(SCREEN_WIDTH)
        fighter_2.misc_attack(SCREEN_WIDTH)
        
        # Check for a winner
        winner, winner_player_num = check_for_winner(fighter_1)
        if winner != None:
            display_winner(winner, winner_player_num)
            if score[1] == 2 or score[2] == 2:
                game_on = False
                display_menu = True
                score = {1 : 0, 2 : 0}
                ROUND_NUM = 1
    
    elif display_menu is True:
        draw_bg()
            

    # event handler
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    # update display
    pyg.display.update()

# Exit pygame
pyg.quit()