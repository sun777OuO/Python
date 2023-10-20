######################匯入模組######################
import pygame
import sys


######################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


######################初始化######################
pygame.init()  # 啟動Pygame
width = 640  # 設定視窗的寬度
height = 320  # 設定視窗的高度
######################建立視窗及物件######################
screen = pygame.display.set_mode((width, height))  # 建立視窗大小
pygame.display.set_caption("EZ")  # 設定視窗標題

######################建立畫布######################
bg = pygame.Surface((width, height))  # 建立畫布
bg.fill((255, 255, 255))  # 畫布為白色(R, G, B)
######################繪製圖形######################
# # 畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
# pygame.draw.circle(screen, (0, 0, 255), (200, 100), 30, 0)
# pygame.draw.circle(screen, (0, 0, 255), (400, 100), 30, 0)

# # 畫矩形, (畫布, 顏色, [x, y, 寬, 高], 線寬)
# pygame.draw.rect(screen, (0, 255, 0), [270, 130, 60, 40], 5)

# # 畫橢圓, (畫布, 顏色, [x, y, 寬, 高], 線寬)
# pygame.draw.ellipse(screen, (255, 0, 0), [130, 160, 60, 35], 5)
# pygame.draw.ellipse(screen, (255, 0, 0), [400, 160, 60, 35], 5)

# # 畫線, (畫布, 顏色, 起點, 終點, 線寬)
# pygame.draw.line(screen, (255, 0, 255), (280, 220), (320, 220), 3)

# 畫多邊形, (畫布, 顏色, [[x1, y1], [x2, y2], [x3, y3]], 線寬)
# pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)

# 畫圓弧, (畫布, 顏色, [x, y, 寬, 高], 起始角度, 結束角度, 線寬)
# pygame.draw.arc(bg, (255, 10, 0), [100, 100, 100, 50], math.radians(180), math.radians(0), 2)

######################設定文字######################
typeface = pygame.font.get_default_font()  # 取得系統字體
font = pygame.font.Font(typeface, 24)  # 設定字體和大小
title = font.render("Start", True, (0, 0, 0))  # 設定文字參數: 文字內容, 是否開啟反鋸齒, 文字顏色, 背景顏色
tit_w = title.get_width()  # 取得文字寬度
tit_h = title.get_height()  # 取得文字高度

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
        # 畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
        pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
        pygame.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)

        # 畫矩形, (畫布, 顏色, [x, y, 寬, 高], 線寬)
        pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)

        # 畫橢圓, (畫布, 顏色, [x, y, 寬, 高], 線寬)
        pygame.draw.ellipse(bg, (255, 0, 0), [130, 160, 60, 35], 5)
        pygame.draw.ellipse(bg, (255, 0, 0), [400, 160, 60, 35], 5)

        # 畫線, (畫布, 顏色, 起點, 終點, 線寬)
        pygame.draw.line(bg, (255, 0, 255), (280, 220), (320, 220), 3)
    else:
        bg.fill((255, 255, 255))  # 畫布為白色(R, G, B)

    screen.blit(bg, (0, 0))  # 繪製畫布於視窗左上角
    screen.blit(title, (0, 0))  # 將文字畫在視窗的(0, 0)
    pygame.display.update()
