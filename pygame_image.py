import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習8
    tmr = 0
    kk_img = pg.image.load("fig/3.png")  #練習3
    kk_img = pg.transform.flip(kk_img, True, False)#練習3左右反転
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr  #練習5
        screen.blit(bg_img, [-x, 0])  #練習5
        screen.blit(bg_img2, [-x + 1600, 0]) #練習7,8
        screen.blit(bg_img, [-x + 3200, 0]) #練習9
        screen.blit(kk_img, [300, 200])  #練習4
        # tmr は毎フレーム 1 ずつ増える
        # 背景の左上を、左へ x だけずらして貼る
        pg.display.update()
        tmr += 1
        if tmr == 3200:  #練習9
            tmr = 0       
        clock.tick(200)  #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()