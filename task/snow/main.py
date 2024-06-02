# -*- coding:gbk -*-
from tools.environment import *
from tools.software import find_hwnd
from .fight import Fight
from .daily import Daily
from .mail import Mail
from .roll import Roll
import os
import traceback


class TaskSnow(Fight, Daily, Mail, Roll):
    def __init__(self):
        super().__init__()

    def snow_start(self, task: type[dir]):
        _k = False
        self.task = task
        print(task)
        env.OCR.enable()
        self.indicate("��ʼ����:���׽���")
        self.snow_launch()
        # noinspection PyBroadException
        try:
            self.snow_log(60)
            click((829, 585))
            wait(500)
            click((829, 585))
            wait(500)
            if self.task["����0"]:
                self.snow_fight()
            if self.task["����1"]:
                self.snow_daily()
            if self.task["����2"]:
                self.snow_mail()
            if self.task["����3"]:
                self.snow_roll()
            self.indicate("ִ�����")
            env.OCR.disable()
        except Exception:
            self.indicate("����ִ���쳣:���׽���", log=False)
            logger.error("����ִ���쳣�����׽���\n%s" % traceback.format_exc())
            _k = True
        env.OCR.disable()
        if self.task["�ر����"]:
            self.indicate("���Թر���Ϸ")
            s, n = 15, 2
            if env.soft.kill(s, n):
                self.indicate("��Ϸ�ѹر�")
            else:
                self.indicate(f"error:��Ϸ�رճ�ʱ({s * n}s)")
                raise RuntimeError("genshin exit error")
        self.indicate("�������:���׽���")
        return _k

    def snow_launch(self):
        # ·������
        env.set_soft(None, (0, "UnrealWindow", "���׽���"))
        _path = self.task["����"]["snow_path"]
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "snow_launcher.exe":
                env.soft.set_path(_path)
                env.soft.set_hwnd_find(1, "wailsWindow", "���׽���������")
            elif name == "SeasunGame.exe":
                env.soft.set_path(_path)
                env.soft.set_hwnd_find(1, "Qt5159QWindowIcon", "��ɽ��������-���׽���")
            else:
                self.indicate("���׽�������Ч����·��")
                raise ValueError("���׽���:��Ч����·��")
        else:
            self.indicate("���׽�������Ч����·��")
            raise ValueError("���׽���:��Ч����·��")
        # ������Ϸ
        for u in range(2):
            if env.soft.find_hwnd():
                env.soft.foreground()
            else:
                if env.soft.run(fls=False):
                    self.indicate("�������򿪳ɹ�")
                else:
                    self.indicate("����������ʱ")
                    raise RuntimeError("���׽���:����������ʱ")
            wait(1000)

            if self.task["Ԥ����"]:
                _p, sim = find_pic(r"assets\snow\picture\pre-load.png")
                if sim:
                    click(_p)
                    wait(1500)
                    click_text("ȷ��")
                    wait(2000)
                else:
                    self.indicate("����Ԥ����")
            if self.lauch_prepare():
                for p in range(10):  # 0, "UnrealWindow", "���׽���"
                    _h = find_hwnd((1, None, "���׽���"))
                    if _h:
                        env.soft.set_hwnd_find(0, "UnrealWindow", "���׽���")
                        env.soft.hwnd = _h
                        if env.mode(1):
                            env.soft.set_pid(env.soft.hwnd)
                            self.indicate("��Ϸ������")
                            env.soft.foreground()
                            return True
                        else:
                            env.soft.foreground()
                            wait(3000)
                    else:
                        env.soft.foreground()
                        wait(1000)
                        click_text("��ʼ��Ϸ")
                        wait(2000)
            raise RuntimeError("���׽���:������ʱ")
        raise RuntimeError("���׽���:�����쳣")

    def lauch_prepare(self):
        for i in range(120):
            if find_hwnd((0, "UnrealWindow", "���׽���")):
                return True
            _list = ocr(mode=1)
            for o in _list:
                if res := text_match(o, "��ʼ��Ϸ"):
                    click(res)
                    return True
                elif res := text_match(o, "������"):
                    click(res)
                    wait(2000)
                    break
                elif res := text_match(o, "��ȡ����"):
                    if self.task["����"]:
                        click(res)
                        wait(2000)
                        click_text("ȷ��")
                        wait(2000)
                        break
                    else:
                        self.indicate("���׽���:��Ҫ����,��ǰδ��ѡ�Զ�����,��ֹ����")
                        raise RuntimeError("���׽���:��Ҫ����,��ǰδ��ѡ�Զ�����,��ֹ����")
                elif text_match(o, "�������"):
                    click_text("ȷ��")
                    wait(2000)
                    return False
                elif text_match(o, "������"):
                    self.indicate("������...")
                    for t in range(180):
                        wait(20000)
                        if not click_text("������"):
                            break
                        elif t == 179:
                            raise RuntimeError("���׽���:���³�ʱ")
                    break
        return False

    def snow_log(self, second: int):
        # ��¼&������Ϸ
        self.indicate("��ʼʶ����Ϸ״̬")
        server = self.task["����"]["server"]
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if "��ʼ��Ϸ" in ocr((883, 920, 1049, 989))[0]:
                    server = 2
                    wait(300)
                    if self.task["�˺�ѡ��"]:
                        click((1864, 222))
                        wait(1000)
                        click((1033, 38))
                        wait(800)
                        click((1152, 522))
                        wait(800)
                        click_text(self.task["�˺�ѡ��"], (703, 462, 1216, 715))
                        wait(800)
                        click((964, 607))
                        wait(800)
                    for r in range(3):
                        click((930, 630))
                        wait(800)
                    self.indicate("��¼��Ϸ")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic(r"assets\snow\picture\login2.png", (853, 369, 1055, 461), sc)[1] >= 0.6:
                    click((964, 679))
                    self.indicate("��¼B���˺�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            if "��õ���" in ocr((813, 45, 1099, 138), sc)[0]:
                click((967, 909))
                self.indicate("ǩ���ɹ�")
                os.remove(sc)
                sc = screenshot()
                wait(2500)
            if "ʱ��" in ocr((368, 217, 482, 249), sc)[0]:
                click((991, 123))
                os.remove(sc)
                sc = screenshot()
                wait(1500)
            if "ά��" in ocr((1003, 419, 1190, 513), sc)[0]:
                os.remove(sc)
                raise RuntimeError("���׽���:��Ϸά����")
            if "�汾����" in ocr((692, 414, 925, 513), sc)[0]:
                os.remove(sc)
                raise RuntimeError("���׽���:�汾����")
            if "��������δ����" in ocr((784, 418, 1148, 508), sc)[0]:
                os.remove(sc)
                raise RuntimeError("���׽���:��������δ����")
            if "����" in ocr((1552, 364, 1618, 409), sc)[0]:
                wait(300)
                os.remove(sc)
                sc = screenshot()
                if "����" in ocr((1552, 364, 1618, 409), sc)[0]:
                    self.indicate("���ص�������")
                    os.remove(sc)
                    return True
            if "�ȼ�����" in ocr((1076, 356, 1345, 448), sc)[0]:
                click((788, 1007))
                wait(8000)
            while 1:
                _p, sim = find_pic("assets/snow/picture/close.png", (1459, 122, 1805, 368), search_path=sc)
                if sim >= 0.6:
                    click(_p)
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                else:
                    break
            while 1:
                _p, sim = find_pic(r"assets\snow\picture\home.png", (1444, 0, 1921, 94), search_path=sc)
                if sim >= 0.6:
                    click(_p)
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                else:
                    break
            os.remove(sc)
            wait(1500)
        raise RuntimeError("���׽���:��¼��ʱ")


if __name__ == '__main__':
    pass
