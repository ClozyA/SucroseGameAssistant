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
                break
            elif i == 2:
                self.indicate("�ϳ���֬δ֪����,���Զ��")
                return True
            else:
                self.indicate(f"error:�ϳ���֬δ֪����,��ʼ���Ե�{i+1}/2��") #
        pressto("F", 1000, ("�ϳ�", (124, 18, 215, 79), 0))
        if "Ũ����֬" in ocr((1270, 103, 1417, 158))[0]:
            fly = int(ocr((1025, 917, 1134, 941))[0].split("/")[0])
            cons = int(ocr((1162, 917, 1269, 941))[0].split("/")[0])
            clickto((1339, 408), 600, ("Ũ����֬", (739, 178, 882, 227), 0))
            num = int(ocr((996, 887, 1028, 924))[0].strip(" "))
            clickto((1618, 497), 600, ("�ϳ�", (823, 740, 938, 788), 0))
            self.indicate(f"��ǰ����:\n"
                          f"  ����:{fly}��\n"
                          f"  ԭ����֬:{cons}/160\n"
                          f"  Ũ����֬:{num}��")
            _n = min(int(cons/40), fly, 5-num)
            if _n:
                for i in range(_n-1):
                    click((1611, 671))
                    wait(400)
                ori = cons-_n*40
                cond = num+_n
                self.task["resin"] = [ori, cond]
                self.indicate(f"���κϳ�Ũ����֬{_n}��\n"
                              f"  ԭ����֬: {cons} -> {ori}\n"
                              f"  Ũ����֬: {num} -> {cond}")
                click((1727, 1019))
                wait(800)
                click((1180, 755))
                wait(500)
            else:
                self.indicate("Ũ����֬�����ﵽ����")
        else:
            self.indicate("�޷��ϳ�Ũ����֬:ȱ����֬�򾧺�")
        self.home()
        return False
