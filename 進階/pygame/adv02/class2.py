######################匯入模組######################
import pygame
import sys
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])
pygame.init()  # 啟動Pygame
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()  # 640
bg_y = bg.get_height()  # 400
######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))  # 建立視窗大小
pygame.display.set_caption("EZ snow")  # 設定視窗標題
####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)  # 音樂載入程式
pygame.mixer.music.play()  # 播放音樂
pygame.mixer.music.fadeout(600000)  # 設定音樂播放時間

####################設定文字######################
typeface = pygame.font.get_default_font()  # 取得系統字體
font = pygame.font.Font(typeface, 24)  # 設定字體和大小
title = font.render("Start", True, (0, 0, 0))  # 設定文字參數: 文字內容, 是否開啟反鋸齒, 文字顏色, 背景顏色
tit_w = title.get_width()  # 取得文字寬度
tit_h = title.get_height()  # 取得文字高度
####################設定雪花基本參數######################

####################新增fps######################

######################循環偵測######################
paint = False
while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果按下  [X] 就退出
            sys.exit()  # 離開遊戲

        if event.type == pygame.MOUSEBUTTONDOWN:  # 按下滑鼠按鍵時
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):  # 當滑鼠點擊特定區域
                paint = not paint  # 狀態相反

    if paint:
        title = font.render("Start", True, (0, 0, 0))

    else:
        title = font.render("Stop", True, (0, 0, 0))

    screen.blit(bg, (0, 0))  # 繪製畫布於視窗左上角
    screen.blit(title, (0, 0))  # 將文字畫在視窗的(0, 0)
    pygame.display.update()
