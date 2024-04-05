import pygame #Импорирование библиотеки
import random
WHITE = (255,255,255)#Добавление базовых цветов
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
BLUE_LIGHT = (141,176,242)
BG_COLOR = (214,243,250)
COLOR_1 = (117,200,204)
COLOR_2 = (171,243,99)
COLOR_3 = (141,230,237)
SPAWN=()
num=1
global Turn#Обьявление глобальных переменных
Turn=1
global score_p1
global score_p2
score_p1 = 0
score_p2 = 0
clock=pygame.time.Clock()
turn=1
b1=1
b2=1
def button_create(text, rect, inactive_color, active_color, action):#Функция для создания кнопок

    font = pygame.font.Font(None, 40)
    button_rect = pygame.Rect(rect)
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    return [text, text_rect, button_rect, inactive_color, active_color, action, False]

def button_check(info, event):#Функция для проверки кнопки на нажатие

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if event.type == pygame.MOUSEMOTION:
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()


def button_draw(screen, info):#Прорисовка кнопки

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)

# ---

def on_click_button_1():#Функция если нажата кнопка игра
    global stage
    stage = 'game'

    print('You clicked Button Play')

def on_click_button_2():#Функция если нажата кнопка рестарт
    global stage
    stage = 'reset'

    print('You clicked Button Reset')

def on_click_button_Exit():#Функция если нажата кнопка выход
    global stage
    global running

    stage = 'exit'
    running = False

    print('You clicked Button Exit')

def on_click_button_return():#Функция если нажата кнопка назад
    global stage
    stage = 'menu'

    print('You clicked Button Return')

def on_click_button_help():#Функция если нажата кнопка помощь
    global stage
    stage = 'help'

    print('You clicked Button Return')

def error(er):#Функция для отображения ошибок на экран
    fontError = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceError = fontError.render(str(er), True, BLACK, BG_COLOR)
    textRectError = textSurfaceError.get_rect()
    textRectError.center = (400,30)

    screen.blit(textSurfaceError, textRectError)


def WIN(text_win):#Функция для отображения победы
    fontWIN = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceWIN = fontWIN.render(str(text_win), True, BLUE, BG_COLOR)
    textRectWIN = textSurfaceWIN.get_rect()
    textRectWIN.center = (410,200)

    screen.blit(textSurfaceWIN, textRectWIN)

def HELP(text,x,y,z):#Универсальная ффункция для отображения текста
    fontHELP = pygame.font.Font('freesansbold.ttf', z)
    textSurfaceHELP = fontHELP.render(str(text), True, BLUE, BG_COLOR)
    textRectHELP = textSurfaceHELP.get_rect()
    textRectHELP.center = (x,y)

    screen.blit(textSurfaceHELP, textRectHELP)


global game_space#Создания основного массива с фишками в углах
game_space=[[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
global game_numbers#Создания основного массива с фишками в углах
game_numbers=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
for i in range(0, len(game_numbers)):
    for i2 in range(0, len(game_numbers[i])):
        if game_space[i][i2]==1:
            game_numbers[i][i2]=0
        else:
            nn=random.randint(1,99)
            game_numbers[i][i2]=nn
def create_circles():#Создание кружков на местах цифр массива game_space
    x1 = 400
    x2 = 100
    w=40
    for i in range(0, len(game_space)):
        for i2 in range(0, len(game_space[i])):
            if game_space[i][i2]==0:
                col1=WHITE
            elif game_space[i][i2]==1:
                col1=RED
            elif game_space[i][i2]==2:
                col1=BLUE
            pygame.draw.circle(screen,col1, (x1, x2), w / 2)
            x1 = x1 + 50
        x1 = 400
        x2 = x2 + 50

def game_draw(game_space):#вывод на экран массива в формате 7 на 7
    fontGame = pygame.font.Font('freesansbold.ttf', 20)
    x1=400
    x2=100
    for i in range(0, len(game_space)):
        for i2 in range(0, len(game_space[i])):
            textSurfaceGame = fontGame.render(str(game_space[i][i2]), True, BLACK, BG_COLOR)
            textRectGame = textSurfaceGame.get_rect()
            textRectGame.center = (x1,x2)
            screen.blit(textSurfaceGame, textRectGame)
            x1=x1+50
        x1=400
        x2=x2+50
    b=0
    screen.blit(textSurfaceGame, textRectGame)

def create_numbers():#Создание цифр на местах цифр массива game_space
    fontGame = pygame.font.Font('freesansbold.ttf', 15)
    x1=400
    x2=100
    for i in range(0, len(game_space)):
        for i2 in range(0, len(game_space[i])):
            if game_numbers[i][i2]!=0:
                textSurfaceGame = fontGame.render(str(game_numbers[i][i2]), True, BLACK, WHITE)
                textRectGame = textSurfaceGame.get_rect()
                textRectGame.center = (x1,x2)
                screen.blit(textSurfaceGame, textRectGame)
            x1=x1+50
        x1=400
        x2=x2+50
    b=0
    screen.blit(textSurfaceGame, textRectGame)

def Input(input_box,text,color,active,done):#Создание поля ввода координат и вывод его на экран

    for event in pygame.event.get():#получение события
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:#проверна на нажания на поле ввода
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:#ввод теста
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:#стирание текста
                    text = text[:-1]
                else:
                    text += event.unicode
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))


def logic(text,b1,b2,turn,score_p1,score_p2):#Основная функция игры где находится логика

    #print('KUDA')
    con=True

    #print(text)
    p1p2 = str(text).replace(',', '')#Перераотка входных данных в 2 числа
    pp1 = p1p2[:len(p1p2) // 2]
    pp2 = p1p2[len(p1p2) // 2:]
    p1 = int(pp1)
    p2 = int(pp2)
    n = game_space[p1][p2]
    err=':)'
    if p1>=0 and p1<=7:
        if p2 >= 0 and p2 <= 7:
            if b1==p1 and b2==p2:
                err='Выберите другие координаты'
            else:
                if abs(b1 - p1) == abs(b2 - p2):
                    err='YES'
                    game_space[b1][b2]=0
                    game_space[p1][p2]=1

                    if turn==1:
                        score_p1 = score_p1 + game_numbers[p1][p2]
                        game_numbers[p1][p2]=0
                        game_numbers[b1][b2]=random.randint(1,99)
                        turn=2
                    else:
                        score_p2 = score_p2 + game_numbers[p1][p2]
                        game_numbers[p1][p2] = 0
                        game_numbers[b1][b2] = random.randint(1, 99)
                        turn=1
                    b1 = p1
                    b2 = p2
                else:
                    err='NO'
        else:
            err = '2 координата ложная'
    else:
        err='1 координата ложная'
    return b1,b2,err,turn,score_p1,score_p2


def SCORE_SHOW(Turn):#Отображение ходов и очередь
    HELP('Ходы:', 130, 340, 20)
    pygame.draw.circle(screen, BLUE, (180, 319), 10)
    pygame.draw.circle(screen, YELLOW, (180, 359), 10)
    if Turn == 1:
        pygame.draw.circle(screen, GREEN, (220, 319), 10)
    if Turn == 2:
        pygame.draw.circle(screen, GREEN, (220, 359), 10)




pygame.init()#Инициализация библиотеки
screen = pygame.display.set_mode((800,600))#Задание размеров окна
screen_rect = screen.get_rect()
font = pygame.font.Font(None, 32)

color_inactive = (120,80,1)
color_active = RED
color = color_inactive
active = False
text = ''

input_box = pygame.Rect(100, 100, 140, 32)#задание размеров поля ввода и его размещение
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

active = False
done = False

COLOR_INACTIVE = (120,80,1)
COLOR_ACTIVE =RED
FONT = pygame.font.Font(None, 32)



stage = 'menu'

button_play = button_create("Play", (300, 100, 200, 75), COLOR_1, COLOR_2, on_click_button_1)#создание кнопок, задание размера, цвета и текста
button_1 = button_create("Restart", (300, 200, 200, 75), COLOR_3, COLOR_2, on_click_button_2)
button_exit = button_create("Exit", (300, 300, 200, 75), COLOR_3, COLOR_2, on_click_button_Exit)
button_help = button_create("Help", (550, 500, 200, 75), COLOR_3, COLOR_2, on_click_button_help)
button_return = button_create("Return", (300, 500, 200, 75), COLOR_3, COLOR_2, on_click_button_return)

running = True
err=':)'
while running:#Цикл программы

    # - events -
    coordinat=0
    for event in pygame.event.get():#Получение события
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:#Проверка нажали ли на поле ввода
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive


        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:#Проверка нажатия на  ентер
                    #print(text)
                    try:
                        b1,b2,err,Turn,score_p1,score_p2=logic(text,b1,b2,Turn,score_p1,score_p2)#Запуск логики игры
                    except:
                        err='ОШИБКА'
                    text = ''
                    #print("--",Turn)
                elif event.key == pygame.K_BACKSPACE:#Стирание текста
                    text = text[:-1]
                else:
                    text += event.unicode
        if stage == 'menu':#проверки кнопок для меню
            button_check(button_play, event)
            button_check(button_1, event)
            button_check(button_exit, event)
            button_check(button_help, event)
        elif stage == 'game':#проверки кнопок для игры

            button_check(button_return, event)
        elif stage == 'reset':#проверки кнопок для рестарта и сам рестарт игры
            Turn = 1
            game_space = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            game_numbers = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            score_p2 = 0
            score_p1 = 0
            for i in range(0, len(game_numbers)):
                for i2 in range(0, len(game_numbers[i])):
                    if game_space[i][i2] == 1:
                        game_numbers[i][i2] = 0
                    else:
                        nn = random.randint(1, 99)
                        game_numbers[i][i2] = nn
            button_check(button_play, event)
            button_check(button_1, event)
            button_check(button_exit, event)
        elif stage == 'win1':#проверки кнопок для победы игрока 1
            print("1 player WIN")
            button_check(button_return, event)
        elif stage == 'win2':#проверки кнопок для победы игрока 1
            print("2 player WIN")
            button_check(button_return, event)
        elif stage == 'help':#проверки кнопок для помощи
            button_check(button_return, event)
        if score_p1>1000:
            stage='win1'
            print("1 player WIN")
            button_check(button_return, event)
            Turn = 1
            game_space = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            game_numbers = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            score_p2 = 0
            score_p1 = 0
            for i in range(0, len(game_numbers)):
                for i2 in range(0, len(game_numbers[i])):
                    if game_space[i][i2] == 1:
                        game_numbers[i][i2] = 0
                    else:
                        nn = random.randint(1, 99)
                        game_numbers[i][i2] = nn
        if score_p2 > 1000:
            stage = 'win2'
            print("2 player WIN")
            button_check(button_return, event)
            Turn = 1
            game_space = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            game_numbers = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            score_p2=0
            score_p1=0
            for i in range(0, len(game_numbers)):
                for i2 in range(0, len(game_numbers[i])):
                    if game_space[i][i2] == 1:
                        game_numbers[i][i2] = 0
                    else:
                        nn = random.randint(1, 99)
                        game_numbers[i][i2] = nn
        #print(Turn)
    pygame.display.flip()
    clock.tick(30)
    screen.fill(BG_COLOR)

    if stage == 'menu':#прорисовка кнопок и названия
        HELP("БЛОКАДА", 400, 50, 50)
        button_draw(screen, button_play)
        button_draw(screen, button_1)
        button_draw(screen, button_exit)
        button_draw(screen, button_help)
    elif stage == 'game':#прорисовка игры
        SCORE_SHOW(Turn)
        pygame.draw.circle(screen, BLUE, (50, 200), 20)
        HELP(score_p1, 250, 200, 20)
        pygame.draw.circle(screen,YELLOW , (50,250),20)
        HELP(score_p2, 250, 250, 20)
        HELP("Ввод", 200, 80, 20)
        HELP('- ИГРОК 1',130, 200,20)
        HELP('- ИГРОК 2', 130, 250, 20)
        HELP("0      1       2       3       4      5      6       7",580,60,20)#прорисовка координого угла
        HELP("0", 363, 100, 20)
        HELP("1", 363, 150, 20)
        HELP("2", 363, 200, 20)
        HELP("3", 363, 250, 20)
        HELP("4", 363, 300, 20)
        HELP("5", 363, 350, 20)
        HELP("6", 363, 400, 20)
        HELP("7", 363, 450, 20)
        error(err)
        pygame.draw.rect(screen, BLUE_LIGHT, [370, 70, 410, 410], 10, border_radius=15)
        #Input(input_box,text,color,active,done)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))#Прорисовка поля ввода
        pygame.draw.rect(screen, color, input_box, 2)
        game_draw(game_space)
        create_circles()
        create_numbers()

        button_draw(screen, button_return)
    elif stage == 'reset':#прорисовка рестарта
        HELP("БЛОКАДА", 350, 50, 50)
        button_draw(screen, button_play)
        button_draw(screen, button_1)
        button_draw(screen, button_exit)
        button_draw(screen, button_help)
    elif stage == 'win1':#прорисовка победы игрока 1
        WIN("1 player WIN")
        button_draw(screen, button_return)
    elif stage == 'win2':#прорисовка победы игрока 2
        WIN("2 player WIN")
        button_draw(screen, button_return)
    elif stage == 'help':#прорисовка помощи и обучения
        HELP('Обучение',400,50,50)
        HELP('Что бы начать игру нажмите играть.', 200, 100,20)
        HELP('Сначала ходит игрок 1. Что бы походить нажмите на поле ввода и введите', 400, 150, 20)
        HELP('двухзначное число первая цифра которого координата фишки по высоте, а', 400, 200, 20)
        HELP('вторая цифа координата по ширине.', 200, 250, 20)
        HELP('Затем нажмите ENTER и выберите направление куда фишка будет ходить.', 390, 300, 20)
        HELP('Нажмите соответственно коавишу на клавиатуре стрелочками', 320, 350, 20)
        button_draw(screen, button_return)
    pygame.display.update()#обновление кадра жкрана
pygame.quit()#Выход из игры