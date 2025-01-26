"""
パックマンゲームプログラム

dependent library:
- pyxel

@Author: Kazunori Hashimoto

2025robodone

"""

import pyxel

PLAYER_SPEED = 3 # プレイヤーの通常移動速度
ADD_SPEED = 2 # プレイヤーの加速時追加移動速度量
BOOST_TIME = 3 # プレイヤーの加速時間
ENEMY_SPEED = 1.3 # 敵の移動速度
GAME_TIME = 60 # ゲームの制限時間
ADD_TIME = 5 # object取得時のボーナス追加時間
EASY = 160 # 選択カーソル座標を難易度に変換
NORMAL = 175 # 選択カーソル座標を難易度に変換
HARD = 190 # 選択カーソル座標を難易度に変換

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
    global object1_x, object1_y, object2_x, object2_y
    global obj_flag,obj_flag1, obj_flag2, obj_flag3, obj_flag4, obj_flag5, obj_flag6
    
    frame = pyxel.frame_count
    
    #*********オブジェクト処理*************
    if game_time > 0 and frame % 60 == 0:
        object1_x = pyxel.rndi(0, pyxel.width - 16)
        object1_y = pyxel.rndi(0, pyxel.height - 16)
    
    if game_time > 0 and obj_flag1 == True:
        object2_x = _enemy1_x
        object2_y = _enemy1_y
        obj_flag = True
        obj_flag1 = False

    if game_time > 0 and obj_flag2 == True:
        object2_x = _enemy3_x
        object2_y = _enemy3_y
        obj_flag = True
        obj_flag2 = False

    if game_time > 0 and obj_flag3 == True:
        object2_x = _enemy1_x
        object2_y = _enemy1_y
        obj_flag = True
        obj_flag3 = False

    if game_time > 0 and obj_flag4 == True:
        object2_x = _enemy2_x
        object2_y = _enemy2_y
        obj_flag = True
        obj_flag4 = False

    if game_time > 0 and obj_flag5 == True:
        object2_x = _enemy4_x
        object2_y = _enemy4_y
        obj_flag = True
        obj_flag5 = False

    if game_time > 0 and obj_flag6 == True:
        object2_x = _enemy3_x
        object2_y = _enemy3_y
        obj_flag = True
        obj_flag6 = False

#*******************************************************************************************************************************************************************************************************
def enemy_move():
    global enemy1_x, enemy1_y, enemy2_x, enemy2_y, enemy3_x, enemy3_y, enemy4_x, enemy4_y
    
    #*********敵処理*************
    if game_time > 0:
        if enemy1_x < player_x:
            enemy1_x += ENEMY_SPEED
        elif enemy1_x > player_x:
            enemy1_x -= ENEMY_SPEED
        if enemy1_y < player_y:
            enemy1_y += ENEMY_SPEED
        elif enemy1_y > player_y:
            enemy1_y -= ENEMY_SPEED

        if enemy2_x < player_x and selecter >= NORMAL:
            enemy2_x += ENEMY_SPEED
        elif enemy2_x > player_x and selecter >= NORMAL:
            enemy2_x -= ENEMY_SPEED
        if enemy2_y < player_y and selecter >= NORMAL:
            enemy2_y += ENEMY_SPEED
        elif enemy2_y > player_y and selecter >= NORMAL:
            enemy2_y -= ENEMY_SPEED 

        if enemy3_x < player_x and selecter == HARD:
            enemy3_x += ENEMY_SPEED 
        elif enemy3_x > player_x and selecter == HARD:
            enemy3_x -= ENEMY_SPEED
        if enemy3_y < player_y and selecter == HARD:
            enemy3_y += ENEMY_SPEED
        elif enemy3_y > player_y and selecter == HARD:
            enemy3_y -= ENEMY_SPEED

        if enemy4_x < player_x and selecter == HARD:
            enemy4_x += ENEMY_SPEED
        elif enemy4_x > player_x and selecter == HARD:
            enemy4_x -= ENEMY_SPEED
        if enemy4_y < player_y and selecter == HARD:
            enemy4_y += ENEMY_SPEED
        elif enemy4_y > player_y and selecter == HARD:
            enemy4_y -= ENEMY_SPEED

#************************************************************************************************************************************************************************************************************

def hit_check():
    global game_time
    global timer_flag
    global player_effect_x, player_effect_y, speed_flag
    global object1_x, object1_y , object2_x, object2_y
    global enemy1_x, enemy1_y, enemy2_x, enemy2_y, enemy3_x, enemy3_y, enemy4_x, enemy4_y
    global _enemy1_x, _enemy1_y, _enemy2_x, _enemy2_y, _enemy3_x, _enemy3_y, _enemy4_x, _enemy4_y #敵同士が接触したときの座標を保存する変数
    global obj_flag, obj_flag1, obj_flag2, obj_flag3, obj_flag4, obj_flag5, obj_flag6
    
    #*********オブジェクトとプレイヤーの当たり判定*************
    if player_x + 3 < object1_x + 15 and player_x + 13 > object1_x + 1 and player_y + 3 < object1_y + 15 and player_y + 13 > object1_y:
        object1_x = -16 #objectの削除
        object1_y = -16 #objectの削除
        game_time += ADD_TIME
    
    if player_x + 3 < object2_x + 15 and player_x + 13 > object2_x + 1 and player_y + 3 < object2_y + 15 and player_y + 13 > object2_y + 1:
        object2_x = -16 #objectの削除
        object2_y = -16 #objectの削除
        speed_flag = True
        timer_flag = False
        obj_flag = False

    #*********敵とプレイヤーの当たり判定*************
    if player_x + 3 < enemy1_x + 15 and player_x + 13 > enemy1_x + 2 and player_y + 3 < enemy1_y + 14 and player_y + 13 > enemy1_y + 1:
        game_time = 0
        player_effect_x = 16
        player_effect_y = 16

    if player_x + 3 < enemy2_x + 15 and player_x + 13 > enemy2_x + 2 and player_y + 3 < enemy2_y + 14 and player_y + 13 > enemy2_y + 1:
        game_time = 0
        player_effect_x = 16
        player_effect_y = 16

    if player_x + 3 < enemy3_x + 15 and player_x + 13 > enemy3_x + 2 and player_y + 3 < enemy3_y + 14 and player_y + 13 > enemy3_y + 1:
        game_time = 0
        player_effect_x = 16
        player_effect_y = 16

    if player_x + 3 < enemy4_x + 15 and player_x + 13 > enemy4_x + 2 and player_y + 3 < enemy4_y + 14 and player_y + 13 > enemy4_y + 1:
        game_time = 0
        player_effect_x = 16
        player_effect_y = 16

    #*********敵と敵の当たり判定*************
    if enemy1_x + 2 < enemy2_x + 15 and enemy1_x + 15 > enemy2_x + 2 and enemy1_y + 1 < enemy2_y + 14 and enemy1_y + 14 > enemy2_y + 1:
        _enemy1_x = enemy1_x
        _enemy1_y = enemy1_y
        enemy1_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy1_y = -32 
        enemy2_x = 272 
        enemy2_y = pyxel.rndi(0, pyxel.height - 16)
        if obj_flag == False and speed_flag == False:
            obj_flag1 = True

    if enemy1_x + 2 < enemy3_x + 15 and enemy1_x + 15 > enemy3_x + 2 and enemy1_y + 1 < enemy3_y + 14 and enemy1_y + 14 > enemy3_y + 1:
        _enemy3_x = enemy3_x
        _enemy3_y = enemy3_y
        enemy1_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy1_y = -32 
        enemy3_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy3_y = 272
        if obj_flag == False and speed_flag == False:
            obj_flag2 = True

    if enemy1_x + 2 < enemy4_x + 15 and enemy1_x + 15 > enemy4_x + 2 and enemy1_y + 1 < enemy4_y + 14 and enemy1_y + 14 > enemy4_y + 1:
        _enemy1_x = enemy1_x
        _enemy1_y = enemy1_y
        enemy1_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy1_y = -32 
        enemy4_x = -32 
        enemy4_y = pyxel.rndi(0, pyxel.height - 16)
        if obj_flag == False and speed_flag == False:
            obj_flag3 = True

    if enemy2_x + 2 < enemy3_x + 15 and enemy2_x + 15 > enemy3_x + 2 and enemy2_y + 1 < enemy3_y + 14 and enemy2_y + 14 > enemy3_y + 1:
        _enemy2_x = enemy2_x
        _enemy2_y = enemy2_y
        enemy2_x = 272 
        enemy2_y = pyxel.rndi(0, pyxel.height - 16)
        enemy3_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy3_y = 272
        if obj_flag == False and speed_flag == False:
            obj_flag4 = True

    if enemy2_x + 2 < enemy4_x + 15 and enemy2_x + 15 > enemy4_x + 2 and enemy2_y + 1 < enemy4_y + 14 and enemy2_y + 14 > enemy4_y + 1:
        _enemy4_x = enemy4_x
        _enemy4_y = enemy4_y
        enemy2_x = 272 
        enemy2_y = pyxel.rndi(0, pyxel.height - 16)
        enemy4_x = -32 
        enemy4_y = pyxel.rndi(0, pyxel.height - 16)
        if obj_flag == False and speed_flag == False:
            obj_flag5 = True

    if enemy3_x + 2 < enemy4_x + 15 and enemy3_x + 15 > enemy4_x + 2 and enemy3_y + 1 < enemy4_y + 14 and enemy3_y + 14 > enemy4_y + 1:
        _enemy3_x = enemy3_x 
        _enemy3_y = enemy3_y
        enemy3_x = pyxel.rndi(0, pyxel.width - 16) 
        enemy3_y = 272
        enemy4_x = -32 
        enemy4_y = pyxel.rndi(0, pyxel.height - 16)
        if obj_flag == False and speed_flag == False:
            obj_flag6 = True

#********************************************************************************************************************************************************************************************************

def player_move():
    global player_x, player_y, player_effect_x, player_effect_y, speed_flag
    global timer_flag, time_set
    global game_time
    
    frame = pyxel.frame_count
    
    #********プレイヤー移動速度処理********
    if speed_flag == True:
        add_speed = ADD_SPEED

        if timer_flag == False:
            time_set = frame
            timer_flag = True

        if (frame - time_set)//30 > BOOST_TIME:
            speed_flag = False
    else:
        add_speed = 0    
    
    #*********プレイヤー処理********
    if (pyxel.btn(pyxel.KEY_RIGHT)) and not (pyxel.btn(pyxel.KEY_LEFT)) and not (pyxel.btn(pyxel.KEY_UP)) and not (pyxel.btn(pyxel.KEY_DOWN)) and game_time > 0:
        player_x += (PLAYER_SPEED + add_speed)
        if speed_flag == True:
            if frame % 8 == 0:
                player_effect_x = pyxel.rndi(0, 8)*16
                player_effect_y = 64
            else:
                player_effect_x = 0
                player_effect_y = 0
        else:
            if frame % 8 == 0:
                player_effect_x = 0
                player_effect_y = 16
            else:
                player_effect_x = 0
                player_effect_y = 0
    if (pyxel.btn(pyxel.KEY_LEFT)) and not (pyxel.btn(pyxel.KEY_RIGHT)) and not (pyxel.btn(pyxel.KEY_UP)) and not (pyxel.btn(pyxel.KEY_DOWN)) and game_time > 0:
        player_x -= (PLAYER_SPEED + add_speed)
        if speed_flag == True:
            if frame % 8 == 0:
                player_effect_x = pyxel.rndi(0, 8)*16
                player_effect_y = 64
            else:
                player_effect_x = 32
                player_effect_y = 0
        else:
            if frame % 8 == 0:
                player_effect_x = 0
                player_effect_y = 16
            else:
                player_effect_x = 32
                player_effect_y = 0
    if (pyxel.btn(pyxel.KEY_UP)) and not (pyxel.btn(pyxel.KEY_DOWN)) and not (pyxel.btn(pyxel.KEY_RIGHT)) and not (pyxel.btn(pyxel.KEY_LEFT)) and game_time > 0:
        player_y -= (PLAYER_SPEED + add_speed)
        if speed_flag == True:
            if frame % 8 == 0:
                player_effect_x = pyxel.rndi(0, 8)*16
                player_effect_y = 64
            else:
                player_effect_x = 16
                player_effect_y = 0
        else:
            if frame % 8 == 0:
                player_effect_x = 0
                player_effect_y = 16
            else:
                player_effect_x = 16
                player_effect_y = 0
    if (pyxel.btn(pyxel.KEY_DOWN)) and not (pyxel.btn(pyxel.KEY_UP)) and not (pyxel.btn(pyxel.KEY_RIGHT)) and not (pyxel.btn(pyxel.KEY_LEFT)) and game_time > 0:
        player_y += (PLAYER_SPEED + add_speed)
        if speed_flag == True:
            if frame % 8 == 0:
                player_effect_x = pyxel.rndi(0, 8)*16
                player_effect_y = 64
            else:
                player_effect_x = 48
                player_effect_y = 0
        else:
            if frame % 8 == 0:
                player_effect_x = 0
                player_effect_y = 16
            else:
                player_effect_x = 48
                player_effect_y = 0

    #*********プレイ画面制限処理*************
    if player_x < -3:
        player_x = -3
    if player_x > pyxel.width - 13:
        player_x = pyxel.width - 13
    if player_y < -3:
        player_y = -3
    if player_y > pyxel.height - 13:
        player_y = pyxel.height - 13

#*****************************************************************************************************************************************************************************************************

def game_start(): # ゲームスタート処理
    global game_ctl
    global selecter
    
    if pyxel.btnp(pyxel.KEY_SPACE):
        game_ctl = 1
    
    if pyxel.btnp(pyxel.KEY_UP) and selecter > EASY:
        selecter -= 15
    if pyxel.btnp(pyxel.KEY_DOWN) and selecter < HARD:
        selecter += 15

#*****************************************************************************************************************************************************************************************************

def restart(): # 初期化(初期設定)
    global player_x, player_y, player_effect_x, player_effect_y, speed_flag
    global object1_x, object1_y, object2_x, object2_y
    global obj_flag, obj_flag1, obj_flag2, obj_flag3, obj_flag4, obj_flag5, obj_flag6
    global enemy1_x, enemy1_y, enemy2_x, enemy2_y, enemy3_x, enemy3_y, enemy4_x, enemy4_y
    global game_time
    global score
    global message1, message2
    global game_ctl
    global selecter
    
    game_ctl = 0 # ゲーム場面制御
    selecter = NORMAL #選択カーソル位置
    game_time = GAME_TIME # 制限時間
    score = 0 # スコア
    player_x = 120 # プレイヤーの初期位置
    player_y = 120 # プレイヤーの初期位置
    player_effect_x = 0 # プレイヤーの画像の初期位置
    player_effect_y = 0 # プレイヤーの画像の初期位置
    speed_flag = False # プレイヤーの移動制御
    object1_x = -16 # オブジェクトの初期位置
    object1_y = -16 # オブジェクトの初期位置
    object2_x = -16 # オブジェクトの初期位置
    object2_y = -16 # オブジェクトの初期位置
    obj_flag = False # オブジェクトの出現制御
    obj_flag1 = False # オブジェクトの出現制御
    obj_flag2 = False # オブジェクトの出現制御
    obj_flag3 = False # オブジェクトの出現制御
    obj_flag4 = False # オブジェクトの出現制御
    obj_flag5 = False # オブジェクトの出現制御
    obj_flag6 = False # オブジェクトの出現制御
    enemy1_x = pyxel.rndi(0, pyxel.width - 16) # 敵の初期位置
    enemy1_y = -32 # 敵の初期位置
    enemy2_x = 272 # 敵の初期位置
    enemy2_y = pyxel.rndi(0, pyxel.height - 16) # 敵の初期位置
    enemy3_x = pyxel.rndi(0, pyxel.width - 16) # 敵の初期位置
    enemy3_y = 272 # 敵の初期位置
    enemy4_x = -32 # 敵の初期位置
    enemy4_y = pyxel.rndi(0, pyxel.height - 16) # 敵の初期位置
    message1 = ""
    message2 = ""

#***********************************************************************************************************************************************************************************************************

def game_over(): # ゲームオーバー判定
    global message1, message2
    
    if game_time == 0:
        message1 = "GAME OVER PRESS SPACE TO START MENU"
        message2 = "PRESS ESC TO QUIT..."
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
        pyxel.text(84, 64, "Welcome to PACMAN-GAME", 10)
        pyxel.text(88, 104, "PRESS SPACE TO START", frame % 16)
        pyxel.text(55, 140, "Select Difficulty level: UP/DOWN_key", 10)
        pyxel.text(125, EASY, "EASY", 7)
        pyxel.text(125, NORMAL, "NORMAL", 7)
        pyxel.text(125, HARD, "HARD", 7)
        pyxel.text(110, selecter, "->", 7)
        pyxel.text(175, 246, "PRESS ESC TO QUIT...", 7)
    else:
        pyxel.text(205, 5, "GAMETIME:", 7)
        pyxel.text(244, 5, str(game_time), 10)
        pyxel.text(5, 5, "SCORE:", 7)
        pyxel.text(30, 5, str(score), 10)
        pyxel.text(58, 64, message1, frame % 16)
        pyxel.text(175, 246, message2, 7)
        pyxel.blt(object1_x, object1_y, 0, 0, 32, 16, 16, 0) # object1
        pyxel.blt(object2_x, object2_y, 0, 16, 32, 16, 16, 0) # object2
        pyxel.blt(enemy1_x, enemy1_y, 0, 0, 48, 16, 16, 0) # enemy1
        pyxel.blt(enemy2_x, enemy2_y, 0, 16, 48, 16, 16, 0) # enemy2
        pyxel.blt(enemy3_x, enemy3_y, 0, 32, 48, 16, 16, 0) # enemy3
        pyxel.blt(enemy4_x, enemy4_y, 0, 48, 48, 16, 16, 0) # enemy4
        pyxel.blt(player_x, player_y, 0, player_effect_x, player_effect_y, 16, 16, 0) # player

#*************************************************************************************************************************************************************************************************************

def __init__(): 
    pyxel.init(256,256) # 画面サイズ
    pyxel.load("pacman.pyxres") # pyxresファイルを読み込む
    restart() # 初期化
    pyxel.run(update, draw) # update()とdraw()を呼び出す

#**********************************************************************************************************************************************************************************************************

__init__() #プログラム実行