# -*- coding:gbk -*-
from tools.environment import *
from .mondstadt import Mondstadt
from .liyue import LiYue
from .sumeru import Sumeru
from .inazuma import Inazuma
from .fontaine import Fontaine


class CutTree(Mondstadt, LiYue, Inazuma, Sumeru, Fontaine):
    def genshin_cut_tree(self):
        _freq = self.task["��������"]
        if not _freq:
            self.indicate("ѭ������Ӧ����0")
            return True
        _num = 0
        for i in range(19):
            if self.task[f"����{i}"]:
                _num += 1
        if _num < 5:
            self.indicate("ѡ���λ��Ӧ>=5�Ա���ľ��ˢ��ѭ��")
            return True
        self.home()
        self.indicate("����������ӡ�")
        self.open_sub("����")
        wait(2000)
        self.check_overdue()
        click((1053, 48))
        wait(800)
        _p, val = find_pic(r"assets\genshin\picture\lit_tools\boon_elder_tree.png",
                               (110, 112, 1273, 805))
        if val < 0.75:
            self.indicate("û���ҵ����ߣ���������")
            return True
        else:
            click(_p)
            wait(800)
            if find_pic(r"assets\genshin\picture\lit_tools\unload.png",
                        (1637, 972, 1765, 1068))[1] >= 0.75:
                self.indicate("����������װ����")
                click((1840, 47))
                wait(1500)
            else:
                self.indicate("װ���������ӡ�")
                click((1694, 1013))
                wait(1500)
        self.indicate(f"�ɼ�ľ�ļƻ���ʼ��\n"
                      f"  ��λ{_num}��\n"
                      f"  ѭ��������{_freq}")
        for f in range(_freq):
            if self.task["����0"]:
                self.birch()
            if self.task["����1"]:
                self.cuihua()
            if self.task["����2"]:
                self.pine()
            if self.task["����3"]:
                self.sand_bearer()
            if self.task["����4"]:
                self.bamboo()
            if self.task["����5"]:
                self.fragrant()
            if self.task["����6"]:
                self.fir()
            if self.task["����7"]:
                self.yumemiru()
            if self.task["����8"]:
                self.maple()
            if self.task["����9"]:
                self.aralia_otogi()
            if self.task["����10"]:
                self.otogi()
            if self.task["����11"]:
                self.karmaphala_bright()
            if self.task["����12"]:
                self.adhigama()
            if self.task["����13"]:
                self.mountain_date()
            if self.task["����14"]:
                self.mallow()
            if self.task["����15"]:
                self.linden()
            if self.task["����16"]:
                self.ash()
            if self.task["����17"]:
                self.cypress()
            if self.task["����18"]:
                self.torch()
        return False
