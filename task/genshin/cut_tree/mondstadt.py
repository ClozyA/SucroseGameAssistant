from tools.environment import *
from task.genshin.genshin import Genshin


class Mondstadt(Genshin):
    # 桦木_萃华木
    def birch(self):
        self.indicate("采集：桦木×9 萃华木×3")
        self.home()
        self.tp_domain("忘却之峡")
        click((1875, 35))
        wait(800)
        click((1718, 814))
        wait(800)
        self.tp_point(3)
        keydown("A")
        wait(4900)
        keyup("A")
        wait(300)
        keydown("W")
        wait(2600)
        keyup("W")
        wait(300)
        press("Z")
        wait(300)

    # 萃华木_垂香木_孔雀木
    def cuihua(self):
        self.indicate("采集：萃华木×9 垂香木×3 孔雀木×6")
        self.home()
        self.tp_domain("仲夏庭园")
        click((619, 763))
        wait(800)
        self.tp_point(0)
        keydown("S")
        wait(2000)
        keyup("S")
        wait(300)
        keydown("A")
        wait(6800)
        keyup("A")
        wait(300)
        keydown("S")
        wait(1000)
        keyup("S")
        wait(300)
        press("Z")
        wait(300)

        self.home()
        self.tp_domain("砂流之庭")
        click((1675, 1011))
        wait(800)
        self.world()
        keydown("A")
        wait(2500)
        keyup("A")
        wait(300)
        keydown("W")
        wait(800)
        keyup("W")
        wait(300)
        press("Z")
        wait(300)

    # 松木
    def pine(self):
        self.indicate("采集：松木×12")
        self.home()
        self.tp_domain("仲夏庭园")
        click((426, 701))
        wait(800)
        self.tp_point(0)
        keydown("S")
        wait(2500)
        keyup("S")
        wait(300)
        keydown("D")
        wait(1500)
        keyup("D")
        wait(300)
        press("Z")
        wait(300)

    # 杉木
    def fir(self):
        self.indicate("采集：杉木×12")
        self.home()
        self.tp_domain("仲夏庭园")
        click((733, 353))
        wait(800)
        self.tp_point(0)
        keydown("A")
        wait(5500)
        keyup("A")
        wait(300)
        keydown("S")
        wait(1700)
        keyup("S")
        wait(300)
        keydown("A")
        wait(4500)
        keyup("A")
        wait(300)
        press("Z")
        wait(300)
        for i in range(4):
            press("F")
            wait(200)

    # 垂香木_萃华木
    def fragrant(self):
        self.indicate("采集：垂香木×15 萃华木×3")
        self.home()
        self.tp_domain("铭记之谷")
        click((742, 71))
        wait(800)
        self.tp_point(0)
        keydown("W")
        wait(4800)
        keyup("W")
        wait(300)
        press("Z")
        wait(300)
        keydown("W")
        wait(3000)
        keyup("W")
        wait(12800)
        press("Z")
        wait(300)
