# -*- coding:gbk -*-
from tools.environment import *
from ..default_task import Task
import os


class Fight(Task):
    def __init__(self):
        super().__init__()
        
    def snow_fight(self):
        self.indicate("��ʼ��飺��֪ɨ��")
        if self.task["��֪����"] and find_color("yellow", (314, 350, 324, 359))[1]:
            click(286, 379)
            wait(2000)
            click(1780, 1030)
            wait(500)
            click(1780, 1030)
            wait(500)
            click(1780, 1030)
            wait(500)
            self.indicate(f"��֪�������")
            click(1674, 44)
            wait(2000)
        if self.task["ÿ�����"] and find_color("yellow", (186, 475, 196, 485))[1]:
            click(124, 508)
            wait(1500)
            click_pic(r"assets\snow\picture\supply.png", zone=(0, 251, 89, 624))
            wait(1500)
            if "ÿ�����������" in ocr((176, 621, 558, 676))[0]:
                click(365, 651)
                wait(2000)
                click(1355, 768)
                wait(2000)
                self.indicate(f"ÿ����������� ��ȡ���")
                click(1674, 44)
                wait(2000)
                click(1674, 44)
                wait(2000)
            else:
                self.indicate(f"ÿ����������� ����")
                click(1674, 44)
                wait(2000)
        if self.task["ʹ���Լ�"]:
            self.indicate(f"�����ʱ�Լ�")
            while 1:
                click(1052, 33)
                wait(2500)
                sc = screenshot()
                pt = ocr((293, 312, 511, 379), sc)[0]
                pn = int(ocr((340, 530, 474, 578), sc)[0].replace(" ", "").split("/")[-1])
                if "��" not in pt and pn > 0:
                    os.remove(sc)
                    click(401, 451)
                    wait(800)
                    click(1285, 729)
                    wait(800)
                    click(1356, 837)
                    wait(2000)
                    click(1383, 502)
                    wait(2000)
                    self.indicate(f"ʹ����ʱ�Լ�(��)")
                else:
                    yt = ocr((558, 309, 778, 378), sc)[0]
                    yn = int(ocr((602, 532, 735, 578), sc)[0].replace(" ", "").split("/")[-1])
                    os.remove(sc)
                    if "��" not in yt and yn > 0:
                        click(669, 454)
                        wait(800)
                        click(1285, 729)
                        wait(800)
                        click(1356, 837)
                        wait(2000)
                        click(1383, 502)
                        wait(2000)
                        self.indicate(f"ʹ����ʱ�Լ�(��)")
                    else:
                        click(770, 962)
                        wait(1500)
                        self.indicate(f"������ʱ�Լ�����")
                        break
        cons = int(ocr((901, 12, 1028, 60))[0].replace(" ", "")[:-4])
        if cons >= 40:
            if self.task["�ж�ѡ��"] == 6:
                if self.task["�����ж�"][0]:
                    self.fight_common(self.task["�����ж�"][1], True)
                    self.indicate(f"���һ�γ����ж�")
                cons = int(ocr((901, 12, 1028, 60))[0].replace(" ", "")[:-4])
                if cons >= 30:
                    click(1499, 538)
                    wait(4000)
                    click(669, 431)
                    wait(3000)
                    click(1622, 354)
                    wait(1500)
                    click(1489, 1006)
                    wait(2000)
                    click(1280, 711)
                    wait(1000)
                    click(955, 826)
                    wait(4000)
                    click(932, 993)
                    wait(1500)
                    for i in range(5):
                        if "��ս" in ocr((1438, 978, 1541, 1038))[0]:
                            break
                        else:
                            click(1670, 157)
                            wait(2000)
                    self.indicate(f"��֪ɨ������ؿ�")
                    click(1674, 44)
                    wait(2000)
                else:
                    self.indicate(f"��֪���㣺{cons}")
            else:
                self.fight_common(self.task["�ж�ѡ��"])
        else:
            self.indicate(f"��֪����40��{cons}")
        self.indicate("�����ɣ���֪ɨ��")

    def fight_common(self, common, once=False):
        click(1728, 531)
        wait(2500)
        click(1682, 599)
        wait(1500)
        if common == 0:
            click(267, 495)
            wait(2500)
        elif common == 1:
            click(707, 497)
            wait(2500)
        elif common == 2:
            click(1165, 478)
            wait(2500)
        elif common == 3:
            click(1617, 502)
            wait(2500)
        elif common == 4:
            roll(1002, 581, -55)
            wait(800)
            click(794, 508)
            wait(2500)
        elif common == 5:
            roll(1002, 581, -55)
            wait(800)
            click(1245, 515)
            wait(2500)
            if not self.task["����ѡ��"] in ocr((901, 12, 1028, 60))[0]:
                click(94, 935)
                wait(2000)
                click_text(self.task["����ѡ��"])
                wait(1000)
                click(1823, 52)
                wait(800)
        roll(1002, 581, -55)
        wait(500)
        click(872, 607)
        wait(1500)
        click(1489, 1006)
        wait(2000)
        if not once:
            click(1280, 711)
            wait(1000)
        click(955, 826)
        wait(4000)
        click(932, 993)
        wait(1500)
        for i in range(5):
            if "��ս" in ocr((1438, 978, 1541, 1038))[0]:
                break
            else:
                click(1670, 157)
                wait(2000)
        click(1674, 44)
        wait(2000)
