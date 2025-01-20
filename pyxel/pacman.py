"""
パックマンゲームプログラム

dependent library:
- pyxel

@Author: Kazunori Hashimoto

2025robodone

"""

import pyxel
import random

PLAYER_SPEED = 3 # プレイヤーの移動速度
ENEMY_SPEED = 1.5 # 敵の移動速度
GAME_TIME = 60 # ゲームの制限時間

#*******************************************************************************************************************************************************************************************************

def limit_time():
    global game_time
    
    frame = pyxel.frame_count
    
    #*********制限時間処理*************
    if game_time > 0 and frame % 30 == 0:
        game_time -= 1

#************************************************************************************************************************************************************************************************************

def score_count():
    global score
    
    frame = pyxel.frame_count
    
    #*********スコア処理*************
    if game_time > 0 and frame % 30 == 0:
        score += 100

#****************************************************************************************************************************************************************************************************************

def object_move():
    global object_x, object_y
    
    frame = pyxel.frame_count
    
    #*********オブジェクト処理*************
    if game_time > 0 and frame % 60 == 0:
        object_x = random.randint(0, pyxel.width - 16)
        object_y = random.randint(0, pyxel.height - 16)

#*******************************************************************************************************************************************************************************************************
def enemy_move():
    global enemy_x, enemy_y
    
    #*********敵処理*************
    if game_time > 0:
        if enemy_x < player_x:
            enemy_x += ENEMY_SPEED
        elif enemy_x > player_x:
            enemy_x -= ENEMY_SPEED
        if enemy_y < player_y:
            enemy_y += ENEMY_SPEED
        elif enemy_y > player_y:
            enemy_y -= ENEMY_SPEED

#************************************************************************************************************************************************************************************************************

def hit_check():
    global game_time
    global player_effect_x, player_effect_y
    
    #*********オブジェクトとプレイヤーの当たり判定*************
    if player_x + 2 < object_x + 8 and player_x + 14 > object_x and player_y + 2 < object_y + 8 and player_y + 14 > object_y:
        game_time += 5

    #*********敵とプレイヤーの当たり判定*************
    if player_x + 2 < enemy_x + 8 and player_x + 14 > enemy_x and player_y + 2 < enemy_y + 8 and player_y + 14 > enemy_y:
        game_time = 0
        player_effect_x = 16
        player_effect_y = 16

#********************************************************************************************************************************************************************************************************

def player_move():
    global player_x, player_y, player_effect_x, player_effect_y
    global game_time
    
    frame = pyxel.frame_count    
    
    #*********プレイヤー処理********
    if (pyxel.btn(pyxel.KEY_RIGHT)) and game_time > 0:
        player_x += PLAYER_SPEED
        if frame % 8 == 0:
            player_effect_x = 0
            player_effect_y = 16
        else:
            player_effect_x = 0
            player_effect_y = 0
    elif (pyxel.btn(pyxel.KEY_LEFT)) and game_time > 0:
        player_x -= PLAYER_SPEED
        if frame % 8 == 0:
            player_effect_x = 0
            player_effect_y = 16
        else:
            player_effect_x = 32
            player_effect_y = 0
    elif (pyxel.btn(pyxel.KEY_UP)) and game_time > 0:
        player_y -= PLAYER_SPEED
        if frame % 8 == 0:
            player_effect_x = 0
            player_effect_y = 16
        else:
            player_effect_x = 16
            player_effect_y = 0
    elif (pyxel.btn(pyxel.KEY_DOWN)) and game_time > 0:
        player_y += PLAYER_SPEED
        if frame % 8 == 0:
            player_effect_x = 0
            player_effect_y = 16
        else:
            player_effect_x = 48
            player_effect_y = 0

    #*********プレイ画面制限処理*************
    if player_x < -3:
        player_x = -2
    if player_x > pyxel.width - 14:
        player_x = pyxel.width - 14
    if player_y < -3:
        player_y = -2
    if player_y > pyxel.height - 14:
        player_y = pyxel.height - 14

#*****************************************************************************************************************************************************************************************************

def game_start(): # ゲームスタート処理
    global game_ctl
    
    if pyxel.btnp(pyxel.KEY_SPACE):
        game_ctl = 1

#*****************************************************************************************************************************************************************************************************

def restart(): # 初期化(初期設定)
    global player_x, player_y, player_effect_x, player_effect_y, object_x, object_y, enemy_x, enemy_y
    global game_time
    global score
    global message
    
    game_time = GAME_TIME # 制限時間
    score = 0 # スコア
    player_x = 120 # プレイヤーの初期位置
    player_y = 120 # プレイヤーの初期位置
    player_effect_x = 0 # プレイヤーの画像の初期位置
    player_effect_y = 0 # プレイヤーの画像の初期位置
    object_x = -100 # オブジェクトの初期位置
    object_y = -100 # オブジェクトの初期位置
    enemy_x = -16 # 敵の初期位置
    enemy_y = -16 # 敵の初期位置
    message = ""

#***********************************************************************************************************************************************************************************************************

def game_over(): # ゲームオーバー判定
    global message
    
    if game_time == 0:
        message = "GAME OVER PRESS SPACE TO RESTART"
        if pyxel.btnp(pyxel.KEY_SPACE):
            restart()

#****************************************************************************************************************************************************************************************************

def update():
    if game_ctl == 0:
        game_start()
    else:
        limit_time()
        score_count()
        object_move()
        enemy_move()
        player_move()
        hit_check()
        game_over()

#**********************************************************************************************************************************************************************************************************

def draw():
    pyxel.cls(0) # 背景色
    frame = pyxel.frame_count
    
    if game_ctl == 0:
        pyxel.text(84, 84, "Welcome to PACMAN-GAME", 10)
        pyxel.text(88, 124, "PRESS SPACE TO START", frame % 16)
    else:
        pyxel.text(205, 5, "GAMETIME:", 7)
        pyxel.text(244, 5, str(game_time), 10)
        pyxel.text(5, 5, "SCORE:", 7)
        pyxel.text(30, 5, str(score), 10)
        pyxel.text(64, 64, message, frame % 16)
        pyxel.blt(object_x, object_y, 0, 0, 32, 16, 16, 0) # object
        pyxel.blt(enemy_x, enemy_y, 0, 0, 48, 16, 16, 0) # enemy
        pyxel.blt(player_x, player_y, 0, player_effect_x, player_effect_y, 16, 16, 0) # player

#*************************************************************************************************************************************************************************************************************

def __init__():
    global game_ctl
    game_ctl = 0 # ゲーム場面制御
    restart() # 初期化
    
    pyxel.init(256,256) # 画面サイズ
    pyxel.load("pacman.pyxres") # pyxresファイルを読み込む
    pyxel.run(update, draw) # update()とdraw()を呼び出す

#**********************************************************************************************************************************************************************************************************

__init__() #プログラム実行