# -*- coding:gbk -*-
from tools.environment import *
from ..default_task import Task
import json


class Roll(Task):
    def __init__(self):
        super().__init__()

    def snow_roll(self):
        self.indicate("��ʼ��ȡ�鿨��¼")
        click(1731, 678)
        for i in range(10):
            wait(1000)
            if "����" in ocr((1686, 940, 1843, 1006))[0]:
                break
            elif i < 9:
                wait(1000)
            else:
                self.indicate("���׽���: ��ȡ������¼�ȴ���ʱ")
                raise RuntimeError("���׽���: ��ȡ������¼�ȴ���ʱ")
        wait(1200)
        current = {
            "�޶���ɫ����": [],
            "�޶���������": [],
            "����֮��": [],
            "��ͥ¯��": []
        }
        with open("personal/snow/roll/history.json", 'r', encoding='utf-8') as m:
            _dir = json.load(m)
        current.update(_dir)
        for i in ["�޶���ɫ����", "�޶���������", "����֮��", "��ͥ¯��"]:
            if i == "�޶���ɫ����":
                if "��" in ocr((192, 68, 277, 120))[0]:
                    click(167, 143)
                else:
                    continue
            elif i == "�޶���������":
                if "��" in ocr((197, 217, 279, 262))[0]:
                    click(131, 281)
                else:
                    continue
            else:
                if click_text(i, (3, 67, 280, 1066)):
                    pass
                else:
                    continue
            wait(800)
            click(1877, 141)
            wait(2000)
            click(1081, 84)
            for o in range(20):
                wait(1000)
                if "����" in ocr((865, 133, 970, 191))[0]:
                    break
                elif o < 19:
                    pass
                else:
                    self.indicate("���׽���: ��ȡ������¼�ȴ���ʱ")
                    raise RuntimeError("���׽���: ��ȡ������¼�ȴ���ʱ")

            _l = current[i]
            _nl = []
            _p = 0
            while 1:
                _list1 = ocr((357, 185, 685, 866), mode=1)
                _list2 = ocr((1357, 185, 1561, 866), mode=1)
                num = 0
                _p += 1
                _line = []
                for row in _list1:
                    row = row[0].strip(" ")
                    if row:
                        _line = [row, _list2[num][0]]
                        if _p != 1:
                            if _line == _nl[9]:
                                break
                        if _line not in _l:
                            _nl = [_line] + _nl
                            _line = []
                        else:
                            break
                        num += 1
                    else:
                        break
                if num < 10:
                    break
                else:
                    click(1666, 602)
                    wait(500)
            current[i] += _nl
            click(1851, 81)
            wait(2000)
        with open("personal/snow/roll/history.json", 'w', encoding='utf-8') as x:
            json.dump(current, x, ensure_ascii=False, indent=1)
        click(1674, 46)
        wait(2000)
        self.indicate("��ȡ�鿨��¼���")
