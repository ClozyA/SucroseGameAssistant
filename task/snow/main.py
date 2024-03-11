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
            click(829, 585)
            wait(500)
            click(829, 585)
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
        if self.task["�ر�����"]:
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
            else:
                self.indicate("���׽�������Ч����·��")
                raise ValueError("���׽���:��Ч����·��")
        else:
            self.indicate("���׽�������Ч����·��")
            raise ValueError("���׽���:��Ч����·��")
        # ������Ϸ
        for u in range(2):
            launch = find_hwnd((1, "wailsWindow", "���׽���������"))
            if launch:
                foreground(launch)
            else:
                env.soft.set_hwnd_find(1, "wailsWindow", "���׽���������")
                if env.soft.run(fls=False):
                    self.indicate("�������򿪳ɹ�")
                else:
                    self.indicate("����������ʱ")
                    raise RuntimeError("���׽���:����������ʱ")
            wait(1000)

            if self.task["Ԥ����"]:
                (x, y), sim = find_pic(r"assets\snow\picture\pre-load.png")
                if sim:
                    click(x, y)
                    wait(1500)
                    click_text("ȷ��")
                    wait(2000)
                else:
                    self.indicate("����Ԥ����")
            if self.lauch_prepare():
                for p in range(10):
                    _h = find_hwnd((0, "UnrealWindow", "���׽���"))
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
                    x, y = res
                    click(x, y)
                    return True
                elif res := text_match(o, "������"):
                    x, y = res
                    click(x, y)
                    wait(2000)
                    break
                elif text_match(o, "��ȡ����"):
                    if self.task["����"]:
                        x, y = res
                        click(x, y)
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
                    click(930, 630)
                    self.indicate("��¼��Ϸ")
                    wait(5000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic(r"assets\snow\picture\login2.png", (863, 370, 1059, 467), sc)[1] >= 0.6:
                    click(953, 659)
                    self.indicate("��¼B���˺�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
                if "��ʼ��Ϸ" in ocr((883, 920, 1049, 989))[0]:
                    server = 2
                    click(930, 630)
                    self.indicate("����")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            if "��õ���" in ocr((813, 45, 1099, 138), sc)[0]:
                click(967, 909)
                wait(3500)
                click(991, 123)
                self.indicate("ǩ���ɹ�")
                wait(2500)
                os.remove(sc)
                sc = screenshot()
            if "ά��" in ocr((1003, 419, 1190, 513), sc)[0]:
                raise RuntimeError("���׽���:��Ϸά����")
            if "�汾����" in ocr((692, 414, 925, 513), sc)[0]:
                raise RuntimeError("���׽���:��Ϸά����")
            if "����" in ocr((1552, 364, 1618, 409))[0]:
                # wait(500)
                os.remove(sc)
                sc = screenshot()
                if "����" in ocr((1552, 364, 1618, 409))[0]:
                    self.indicate("���ص�������")
                    os.remove(sc)
                    break
            while 1:
                (x, y), sim = find_pic("assets/snow/picture/close.png", (1459, 122, 1805, 368), search_path=sc)
                if sim >= 0.6:
                    click(x, y)
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                else:
                    break
            while 1:
                (x, y), sim = find_pic(r"assets\snow\picture\home.png", (1444, 0, 1921, 94), search_path=sc)
                if sim >= 0.6:
                    click(x, y)
                    wait(1500)
                    os.remove(sc)
                    sc = screenshot()
                else:
                    break
            os.remove(sc)
            wait(1500)


if __name__ == '__main__':
    pass