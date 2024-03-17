# -*- coding:gbk -*-
from tools.environment import *
from .fight import Fight
from .dispatch import Dispatch
from .review import Review
from .market import Market
from .recruit import Recruit
from .reward import Reward
from .network import Network
from .mail import Mail
from .roll import Roll
import os
import traceback


class TaskKleins(Fight, Dispatch, Review, Market, Recruit, Reward, Network, Mail, Roll):
    def __init__(self):
        super().__init__()

    def kleins_start(self, task: type[dir]):
        _k = False
        self.task = task
        env.OCR.enable()
        self.indicate("��ʼ����:��������")
        self.kleins_launch()
        # noinspection PyBroadException
        try:
            self.kleins_log(60)
            # �������ѻ���
            click((969, 374))
            wait(500)
            click((969, 374))
            wait(500)
            if self.task["����0"]:
                self.indicate("��ʼ:��ս")
                if self.kleins_fight():
                    _k = True
                self.indicate("���:��ս")
            if self.task["����1"]:
                self.indicate("��ʼ:���²ɹ�")
                self.kleins_dispatch()
                self.indicate("���:���²ɹ�")
            if self.task["����2"]:
                self.indicate("��ʼ:ս���ع�")
                self.kleins_review()
                self.indicate("���:ս���ع�")
            if self.task["����3"]:
                self.indicate("��ʼ:������ȡ")
                self.kleins_get_market()
                self.indicate("���:������ȡ")
            if self.task["����4"]:
                self.indicate("��ʼ:���ѷ�ļ")
                self.kleins_recruit()
                self.indicate("���:���ѷ�ļ")
            if self.task["����5"]:
                self.indicate("��ʼ:���չ���")
                self.kleins_reward()
                self.indicate("���:���չ���")
            if self.task["����6"]:
                self.indicate("��ʼ:��������")
                self.kleins_market_network()
                self.indicate("���:��������")
            if self.task["����7"]:
                self.indicate("��ʼ:��ȡ�ʼ�")
                self.kleins_get_mail()
                self.indicate("���:��ȡ�ʼ�")
            if self.task["����8"]:
                self.indicate("��ʼ:�鿨��ʷ")
                self.kleins_get_roll()
                self.indicate("���:�鿨��ʷ")
        except Exception:
            self.indicate("����ִ���쳣:��������", log=False)
            logger.error("����ִ���쳣:��������\n%s" % traceback.format_exc())
            _k = True
        env.OCR.disable()
        if self.task["�ر����"]:
            self.indicate("���Թر���Ϸ")
            s, n = 15, 2
            if env.soft.kill(s, n):
                self.indicate("��Ϸ�ѹر�")
            else:
                self.indicate(f"error:��Ϸ�رճ�ʱ��{s * n}s��")
                raise RuntimeError("kleins exit error")
        self.indicate("�������:��������")
        return _k

    def kleins_launch(self):
        # ·������
        env.set_soft(None, (1, "UnityWndClass", "��������"))
        _path = self.task["����"]["game"]
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "��������.exe":
                env.soft.set_path(_path)
            elif name == "kleins.exe":
                path = dire + "/Games/��������.exe"
                if os.path.isfile(path):
                    env.soft.set_path(path)
                else:
                    self.indicate("�������ᣬ��Ч����·��")
                    return 3
            else:
                self.indicate("�������ᣬ��Ч����·��")
                return 3
        else:
            self.indicate("�������ᣬ��Ч����·��")
            return 3
        # ������Ϸ
        cond = env.soft.run()
        if cond == 2:
            self.indicate("��Ϸ�����ɹ�")
            self.indicate("�ȴ�����,10���ʼʶ����Ϸ״̬")
            wait(1000)
            env.soft.foreground()
            wait(9000)
        elif cond == 1:
            self.indicate("��Ϸ��������")
            env.soft.foreground()
            wait(1000)
        elif cond == 0:
            self.indicate("��Ϸ������ʱ")
            return 3
        env.mode(1)

    def kleins_log(self, second: int):
        # ��¼&������Ϸ
        self.indicate("��ʼʶ����Ϸ״̬")
        server = self.task["����"]["server"]
        net = 1
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if "��ʼ��Ϸ" in ocr((870, 611, 1050, 655), sc)[0].replace(" ", ""):
                    wait(300)
                    click((930, 630))
                    self.indicate("��¼��Ϸ")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if "��¼�˺�" in ocr((870, 611, 1050, 655), sc)[0].replace(" ", ""):
                    wait(300)
                    click((960, 633))
                    self.indicate("��¼�˺�")
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                if find_pic(r"assets\kleins\picture\login2.png", (853, 369, 1055, 461), sc)[1] >= 0.6:
                    click((958, 679))
                    self.indicate("��¼��Ϸ")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            if "ǩ������" in ocr((832, 211, 1090, 313), sc)[0].replace(" ", ""):  # ǩ������
                click((1469, 551))
                wait(1500)
                click((1789, 120))
                self.indicate("ǩ���ɹ�")
                wait(1000)
                os.remove(sc)
                sc = screenshot()
            _p, sim = find_pic("assets/kleins/picture/close/close2.png", search_path=sc)
            if sim >= 0.6:
                click(_p)
                wait(1500)
                os.remove(sc)
                sc = screenshot()
            if find_pic("assets/kleins/picture/home.png", (1739, 37, 1814, 98), sc)[1] >= 0.7:
                wait(1500)
                os.remove(sc)
                sc = screenshot()
                if find_pic("assets/kleins/picture/home.png", (1739, 37, 1814, 98), sc)[1] >= 0.7:
                    self.indicate("���ص�������")
                    os.remove(sc)
                    return 0
            if find_pic("assets/kleins/picture/rehome.png", (238, 27, 355, 105), sc)[1] >= 0.7:
                click((295, 69))
                wait(1500)
                os.remove(sc)
                self.indicate("���ص�������")
                return 0
            if "�������ӳ�ʱ" in ocr((748, 448, 1183, 524), sc)[0].replace(" ", ""):
                self.indicate(f"error: �������ӳ�ʱ({net}��)")
                if net < 4:
                    net += 1
                    click((1063, 710))
                    wait(10000)
                else:
                    os.remove(sc)
                    raise RuntimeError("��������:�������ӳ�ʱ���")
            os.remove(sc)
            wait(1500)
        raise RuntimeError("��������:ʶ����Ϸ״̬��ʱ")


if __name__ == '__main__':
    pass
