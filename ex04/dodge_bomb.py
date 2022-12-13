# 逃げろ!こうかとん のゲームを作成(追加機能まで)

import pygame as pg
import sys
from random import randint as rd

# 追加
import tkinter.messagebox as tkm
from pygame.locals import *

screen = pg.display.set_mode((128, 128))
clock = pg.time.clock()


# 練習7
def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock = pg.time.Clock()
    # 練習1
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("../fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習3
    tori_sfc = pg.image.load("../fig/6.png")    # Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()              # Rect(Surface作ったらRectもつくっておくと良い.)
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って, tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct)           # blit

    # 練習5
    bomb_sfc = pg.Surface((20, 20))             # 正方形の空Surface
    bomb_sfc.set_colorkey((0, 0, 0))            # 四隅の黒を排除
    # pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # Surfaceの半分の値の10を代入.

    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # Surfaceの半分の値の10を代入.
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = rd(0, scrn_rct.width)
    bomb_rct.centery = rd(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = +1, +1
    # bomb_rct.centerx, bomb_rct.centery = rd()

    # 練習2
    
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                tkm.showwarning("警告", "マウスボタンのクリックは禁止だよ!!")
            if event.type == pg.QUIT :
                return
            # カウントダウンタイマーの処理..

        key_dct = pg.key.get_pressed()         # 辞書型(True or False)

        centery_mem = [key_dct[pg.K_UP], key_dct[pg.K_w], key_dct[pg.K_DOWN], key_dct[pg.K_s]]
        centerx_mem = [key_dct[pg.K_LEFT], key_dct[pg.K_a], key_dct[pg.K_RIGHT], key_dct[pg.K_d]]

        if centery_mem:
            if centery_mem[0] or centery_mem[1]:
                tori_rct.centery -= 1
            elif centery_mem[2] or centery_mem[3] :
                tori_rct.centery += 1
        if centerx_mem:
            if centerx_mem[0] or centerx_mem[1]:
                tori_rct.centerx -= 1
            elif centerx_mem[2] or centerx_mem[3]:
                tori_rct.centerx += 1


        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出していたら
            if centery_mem:
                if centery_mem[0] or centery_mem[1]:
                    tori_rct.centery += 1
                elif centery_mem[2] or centery_mem[3] :
                    tori_rct.centery -= 1
            if centerx_mem:
                if centerx_mem[0] or centerx_mem[1]:
                    tori_rct.centerx += 1
                elif centerx_mem[2] or centerx_mem[3]:
                    tori_rct.centerx -= 1


        scrn_sfc.blit(tori_sfc, tori_rct)           # blit

       # 練習6
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        if (vx < 0):
            vx -= 0.001
        else :
            vx += 0.001
        if (vy < 0):
            vy -= 0.001
        else :
            vx += 0.001
        pg.display.update()
        clock.tick(1000)

        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            # 追加(失敗時の処理)
            ti = pg.time.get_ticks()
            scrn_sfc.fill((0,0,0))
            fonto = pg.font.Font(None, 200)
            text = fonto.render("Game Over...", True, (255,255,255))
            scrn_sfc.blit(text, [425, 400])
            pg.display.update()
            tkm.showinfo("残念!", f'記録は{ti//1000}秒だったよ!')
            return 

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()