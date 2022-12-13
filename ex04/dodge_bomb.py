# 逃げろ!こうかとん のゲームを作成

import pygame as pg
import sys
from random import randint as rd

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
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # Surfaceの半分の値の10を代入.
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = rd(0, scrn_rct.width)
    bomb_rct.centery = rd(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    # bomb_rct.centerx, bomb_rct.centery = rd()

    # 練習2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT :
                return

        key_dct = pg.key.get_pressed()         # 辞書型(True or False)

        if key_dct[pg.K_UP] :
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN] :
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT] :
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT] :
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct)           # blit

        # 練習6
        vx, vy = +1, +1
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        pg.display.update()
        clock.tick(1000)




if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()