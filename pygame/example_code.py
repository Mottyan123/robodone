"""
pygameのサンプルコード

dependent library:
- pygame

@Author: Kazunori Hashimoto

2025robodone

"""

import pygame
from pygame.locals import * # pygame用の全ての定数をインポート
import sys #プログラムの終了処理を行うために必要

PLAYER_SPEED = 3
OBJECT_SPEED = 1

#************************************************************************************************************************************************************************************************************

def player_move():
    global player
    
    pressed_key = pygame.key.get_pressed() # キーの状態を取得
    
    if pressed_key[K_LEFT]: # 左キーが押されたら
        player.left -= PLAYER_SPEED # 左へ移動
    if pressed_key[K_RIGHT]: # 右キーが押されたら
        player.right += PLAYER_SPEED # 右へ移動
    if pressed_key[K_UP]: # 上キーが押されたら
        player.top -= PLAYER_SPEED # 上へ移動
    if pressed_key[K_DOWN]: # 下キーが押されたら
        player.bottom += PLAYER_SPEED # 下へ移動
    
    if player.left < 0: # プレイヤーの左端が画面の左端を超えたら
        player.left = 0 # プレイヤーの左端を画面の左端に固定
    if player.right > 720: # プレイヤーの右端が画面の右端を超えたら
        player.right = 720 # プレイヤーの右端を画面の右端に固定
    if player.top < 0: # プレイヤーの上端が画面の上端を超えたら
        player.top = 0 # プレイヤーの上端を画面の上端に固定
    if player.bottom > 480: # プレイヤーの下端が画面の下端を超えたら
        player.bottom = 480 # プレイヤーの下端を画面の下端に固定

#************************************************************************************************************************************************************************************************************

def object_move():
    global object
    
    object.centerx += OBJECT_SPEED
    
    if object.left > 720:
        object.left = 0

#************************************************************************************************************************************************************************************************************

def hit_check():
    global player
    
    if player.colliderect(object): # プレイヤーとオブジェクトの当たり判定
        player.bottomright = (720, 480)

#************************************************************************************************************************************************************************************************************

def timer():
    global time
    
    now_time = pygame.time.get_ticks() # 現在の時間を取得
    time = (now_time-reset_time)//1000 

#************************************************************************************************************************************************************************************************************

def reset():
    global background_image, object_image, object, player_image, player # Pygameのインスタンスをグローバル化
    global reset_time, time
    
    background_image = pygame.image.load(r"C:\Users\hkazu\OneDrive\ドキュメント\ロボ団\pygame\images\background.png") # 背景画像の読み込み
    background_image = pygame.transform.smoothscale(background_image, (720, 480)) # 背景画像のリサイズ
    object_image = pygame.image.load(r"C:\Users\hkazu\OneDrive\ドキュメント\ロボ団\pygame\images\nezubotto.png").convert_alpha() # オブジェクトの画像の読み込み(透過可能)
    object_image = pygame.transform.smoothscale(object_image, (90, 120)) # オブジェクトの画像のリサイズ
    object = object_image.get_rect() # オブジェクトの矩形を取得
    player_image = pygame.image.load(r"C:\Users\hkazu\OneDrive\ドキュメント\ロボ団\pygame\images\robonyan.png").convert_alpha() # プレイヤーの画像の読み込み(透過可能)
    player_image = pygame.transform.smoothscale(player_image, (90, 110)) # プレイヤーの画像のリサイズ
    player = player_image.get_rect() # プレイヤーの矩形を取得
    object.topleft = (0, 0) # オブジェクトの初期位置(矩形の左上座標)
    player.bottomright = (720, 480) # プレイヤーの初期位置(矩形の左下座標)
    reset_time = pygame.time.get_ticks() # 現在の時間を取得
    time = 0 # タイマーの初期化

#***********************************************************************************************************************************************************************************************************

def update():
    player_move()
    object_move()
    hit_check()
    timer()

    pressed_key = pygame.key.get_pressed() # キーの状態を取得
    if pressed_key[K_SPACE]: # SPACEキーが押されたら
        reset()

#************************************************************************************************************************************************************************************************************

def draw():
    screen.blit(background_image, (0, 0)) # 背景画像の描画
    text = font.render("pygameのプログラミングはじまるよぉ～!", True, (0, 0, 0)) # 文字の描画情報を変数に格納 (描画する文字，True，(0, 0, 0)はRGBの値)
    screen.blit(text, (110, 350)) # 文字の描画
    timer = font.render(str(time), True, (0, 0, 0)) # タイマーの描画情報を変数に格納 (描画する文字，True，(0, 0, 0)はRGBの値)
    screen.blit(timer, (10, 440)) # タイマーの描画
    screen.blit(object_image, object) # オブジェクトの描画
    screen.blit(player_image, player) # プレイヤーの描画

#************************************************************************************************************************************************************************************************************

def init():
    global screen, font # Pygameのインスタンスをグローバル化

    pygame.init() # Pygameの初期化
    pygame.display.set_caption("example") # タイトルバーの設定（表示する文字を指定）
    screen = pygame.display.set_mode((720, 480)) # 画面サイズの設定 (幅、高さ) , 第2引数にFULLSCREENを指定すると全画面表示
    screen.fill((255, 255, 255)) # 背景を指定色に塗りつぶし (0, 0, 0)はRGBの値
    font = pygame.font.SysFont("meiryo", 27) # フォントの設定（フォント名、サイズ）
    reset()

    while True:
        pygame.display.update() # 画面を更新
        pygame.time.Clock().tick(60) # FPSを60に固定
        update()
        draw()
        for event in pygame.event.get(): # イベント処理
            if event.type == QUIT: # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じる)
                sys.exit() # pythonプログラムの終了

#*************************************************************************************************************************************************************************************************************

init() # プログラムを実行