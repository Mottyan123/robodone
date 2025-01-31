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

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
PLAYER_SPEED = 3
OBJECT_SPEED = 2

#************************************************************************************************************************************************************************************************************

def player_move():
    global player
    
    pressed_key = pygame.key.get_pressed() # キーの状態を取得
    
    if pressed_key[K_LEFT]: # 左キーが押されたら
        player.x -= PLAYER_SPEED # 左へ移動
    if pressed_key[K_RIGHT]: # 右キーが押されたら
        player.x += PLAYER_SPEED # 右へ移動
    if pressed_key[K_UP]: # 上キーが押されたら
        player.y -= PLAYER_SPEED # 上へ移動
    if pressed_key[K_DOWN]: # 下キーが押されたら
        player.y += PLAYER_SPEED # 下へ移動
    
    player.clamp_ip((0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) # プレイヤーの移動範囲を制限

#************************************************************************************************************************************************************************************************************

def object_move():
    global object1
    
    object1.x += OBJECT_SPEED
    
    if object1.left > 720:
        object1.right = 0

#************************************************************************************************************************************************************************************************************

def hit_check():
    global player
    
    if player.colliderect(object1): # プレイヤーとオブジェクトの当たり判定
        player.bottomright = (720, 480)

#************************************************************************************************************************************************************************************************************

def timer():
    global time
    
    now_time = pygame.time.get_ticks() # 現在の時間を取得
    time = (now_time-reset_time)//1000 

#************************************************************************************************************************************************************************************************************

def reset():
    global screen, font, background_image, object_image, object1, player_image, player # Pygameのインスタンスをグローバル化
    global reset_time, time
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 画面サイズの設定 (幅、高さ) , 第2引数にFULLSCREENを指定すると全画面表示
    screen.fill((255, 255, 255)) # 背景を指定色に塗りつぶし (0, 0, 0)はRGBの値
    font = pygame.font.SysFont("meiryo", 27) # フォントの設定（フォント名、サイズ）
    background_image = pygame.image.load("images/background.png") # 背景画像の読み込み(絶対パスでも相対パスでも可)
    background_image = pygame.transform.smoothscale(background_image, (720, 480)) # 背景画像のリサイズ
    object_image = pygame.image.load("images/nezubotto.png").convert_alpha() # オブジェクトの画像の読み込み(透過可能)
    object_image = pygame.transform.smoothscale(object_image, (90, 120)) # オブジェクトの画像のリサイズ
    object1 = object_image.get_rect() # オブジェクトの矩形を取得
    player_image = pygame.image.load("images/robonyan.png").convert_alpha() # プレイヤーの画像の読み込み(透過可能)
    player_image = pygame.transform.smoothscale(player_image, (90, 110)) # プレイヤーの画像のリサイズ
    player = player_image.get_rect() # プレイヤーの矩形を取得
    object1.topleft = (0, 0) # オブジェクトの初期位置(矩形の左上座標)
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
    screen.blit(object_image, object1) # オブジェクトの描画
    screen.blit(player_image, player) # プレイヤーの描画

#************************************************************************************************************************************************************************************************************

def init():
    pygame.init() # Pygameの初期化
    pygame.display.set_caption("example") # タイトルバーの設定（表示する文字を指定）
    reset()

    while True:
        update()
        draw()
        pygame.display.update() # 画面を更新
        pygame.time.Clock().tick(60) # FPSを30に固定
        
        for event in pygame.event.get(): # イベント処理
            if event.type == QUIT: # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じる)
                sys.exit() # pythonプログラムの終了

#*************************************************************************************************************************************************************************************************************

init() # プログラムを実行