import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面サイズの設定
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ラストワン")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 駒の管理用リスト(7*)
pieces = [
    [-1,-1,0,0,0,-1,-1],
    [-1,-1,0,0,0,-1,-1],
    [ 0, 10,10,0,10,10, 0],
    [ 0, 0,0,10,0, 0, 0],
    [ 0, 0,0,0,0, 0, 0],
    [-1,-1,0,0,0,-1,-1],
    [-1,-1,0,0,0,-1,-1]
]

# 移動可能なマスを判定する
# (x,y)は選択された駒の座標
# 移動可能なマスには5を入れる
def check_piece(x,y):
    if y - 1 >= 0:#上    
        if pieces[y-1][x] == 10:
            if pieces[y-2][x] == 0:
                pieces[y-2][x] = 5
    
    if y + 1 <= 6:#下
        if pieces[y+1][x] == 10:
            if pieces[y+2][x] == 0:
                pieces[y+2][x] = 5
    
    if x - 1 >= 0:#左
        if pieces[y][x-1] == 10:
            if pieces[y][x-2] == 0:
                pieces[y][x-2] = 5
    
    if x + 1 <= 6:#右
        if pieces[y][x+1] == 10:
            if pieces[y][x+2] == 0:
                pieces[y][x+2] = 5

def move_piece(x,y):
    if y - 2 >= 0:#上
        if pieces[y - 2][x] == 20:
            pieces[y - 1][x] = 15
    
    if y + 2 <= 6:#下
        if pieces[y + 2][x] == 20:
            pieces[y + 1][x] = 15

    if x - 2 >= 0:#左
        if pieces[y][x - 2] == 20:
            pieces[y][x - 1] = 15
       
    if x + 2 <= 6:#右
        if pieces[y][x + 2] == 20:
            pieces[y][x + 1] = 15

    for i in range(7):
        for j in range(7):
            if pieces[i][j] == 20:
                pieces[i][j] = 0
            elif pieces[i][j] == 15:
                pieces[i][j] = 0
            elif pieces [i][j] == 5:
                pieces[i][j] = 10



# ゲームのループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画面を白で塗りつぶす
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (300,50,300,700), 2)

    pygame.draw.rect(screen, BLACK, (100,250,700,300), 2)

    pygame.draw.rect(screen, BLACK, (400,50,100,700), 2)

    pygame.draw.rect(screen, BLACK, (100,350,700,100), 2)

    pygame.draw.line(screen, BLACK, (300, 150), (600, 150), 2)

    pygame.draw.line(screen, BLACK, (300, 650), (600, 650), 2)

    pygame.draw.line(screen, BLACK, (200, 250), (200, 550), 2)

    pygame.draw.line(screen, BLACK, (700, 250), (700, 550), 2)

    if event.type == pygame.MOUSEBUTTONDOWN:
        (x,y) = pygame.mouse.get_pos()
        x = int((x - 100) / 100)
        y = int((y - 50) / 100)
        if x > 6 or y > 6:
            continue

        if pieces[y][x] == 5:
            move_piece(x,y)
        
        for i in range(7):
            for j in range(7):
                if pieces[i][j] == 20:
                    pieces[i][j] = 10
                elif pieces[i][j] == 15:
                    pieces[i][j] = 10
                elif pieces[i][j] == 5:
                    pieces[i][j] = 0
        
        if pieces[y][x] == 10:
            pieces[y][x] = 20
            check_piece(x,y)
        # print(x,y)


    for i in range(7):
        for j in range(7):
            if pieces[i][j] >= 10:
                pygame.draw.circle(screen, BLACK, (150 + 100 * j, 100 + 100 * i), 40)
            elif pieces[i][j] == 5:
                pygame.draw.circle(screen, RED, (150 + 100 * j, 100 + 100 * i), 40)
            print(pieces[i][j], end=',')
        print("\n")

    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    pygame.time.Clock().tick(60)
