# 逃げろ!こうかとん のゲームを作成

import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    # 練習1
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    pgbg_sfc = pg.image.load("../fig/pg_bg.jpg")

    
    clock.tick(0.5)
    pg.display.update()



if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()