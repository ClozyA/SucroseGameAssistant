# -*- coding:gbk -*-
from tools.environment import *
from .genshin import Genshin


class Condensed(Genshin):
    def genshin_make_condensed(self):
        for i in range(3):
            self.tp_fontaine1()
            keydown("W")
            wait(4300)
            keyup("W")
            wait(300)
            keydown("D")
            wait(500)
            keyup("D")
            wait(300)
            keydown("W")
            wait(1000)
            keyup("W")
            wait(300)
            if "�ϳ�" in ocr((1205, 502, 1315, 578))[0]:
                self.indicate("����ϳ�̨")
            elif i == 2:
                self.indicate("�ϳ���֬δ֪����,���Զ��")
                return True
            else:
                self.indicate(f"error:�ϳ���֬δ֪����,��ʼ���Ե�{i+1}/2��")
        press("F")
        wait(1000)
        click(960, 950)
        wait(1500)
        click(107, 188)
        wait(500)
        click(1339, 408)
        wait(600)
        if "Ũ����֬" in ocr((739, 178, 882, 227))[0]:
            num = int(ocr((996, 887, 1028, 924))[0].strip(" "))
            click(1618, 497)
            wait(600)
            fly = int(ocr((1025, 917, 1134, 941))[0].split("/")[0])
            cons = int(ocr((1162, 917, 1269, 941))[0].split("/")[0])
            self.indicate(f"��ǰ����:\n"
                          f"  ����:{fly}��\n"
                          f"  ԭ����֬:{cons}/160\n"
                          f"  Ũ����֬:{num}��")
            _n = min(int(cons/40), fly, 5-num)
            if _n:
                for i in range(_n-1):
                    click(1611, 671)
                    wait(400)
                ori = cons-_n*40
                cond = num+_n
                self.task["resin"] = [ori, cond]
                self.indicate(f"���κϳ�Ũ����֬{_n}��\n"
                              f"  ԭ����֬: {cons} -> {ori}\n"
                              f"  Ũ����֬: {num} -> {cond}")
                click(1727, 1019)
                wait(800)
                click(1173, 786)
                wait(200)
            else:
                self.indicate("Ũ����֬�����ﵽ����")
        else:
            click(1618, 497)
            wait(600)
            self.indicate("�޷��ϳ�Ũ����֬:ȱ����֬�򾧺�")
        self.turn_world()
        return False
