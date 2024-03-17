# -*- coding:gbk -*-
from tools.environment import *
from tools.software import find_hwnd
import traceback
import os
from .team import Team
from .dispatch import Dispatch
from .transformer import Transformer
from .crystalfly import CatchFly
from .condensed import Condensed
from .rambler import Rambler
from .cut_tree.main import CutTree
from .domain import Domain
from .mail import Mail
from .gpass import Pass


class TaskGenshin(Team, Dispatch, Transformer,
                  CatchFly, Condensed, Rambler,
                  Mail, CutTree, Domain, Pass):
    def __init__(self):
        super().__init__()

    def genshin_start(self, task: type[dir]):
        _k = False
        self.task = task
        env.OCR.enable()
        self.indicate("��ʼ����:ԭ��")
        self.task["resin"] = None
        self.genshin_launch()
        # noinspection PyBroadException
        try:
            self.genshin_log(60)
            if self.task["����0"]:
                self.indicate("��ʼ:�����л�")
                self.genshin_team()
                self.indicate("���:�����л�")
            if self.task["����1"]:
                self.indicate("��ʼ:̽����ǲ")
                if self.genshin_dispatch():
                    _k = True
                self.indicate("���:̽����ǲ")
            if self.task["����2"]:
                self.indicate("��ʼ:�����ʱ���")
                if self.genshin_transformer():
                    _k = True
                self.indicate("���:�����ʱ���")
            if self.task["����3"]:
                self.indicate("��ʼ:�Զ�����")
                if self.genshin_catch_fly():
                    _k = True
                self.indicate("���:�Զ�����")
            if self.task["����4"]:
                self.indicate("��ʼ:Ũ����֬")
                if self.genshin_make_condensed():
                    _k = True
                self.indicate("���:Ũ����֬")
            if self.task["����5"]:
                self.indicate("��ʼ:�����")
                self.genshin_rambler()
                self.indicate("���:�����")
            if self.task["����6"]:
                self.indicate("��ʼ:��ȡ�ʼ�")
                self.genshin_mail()
                self.indicate("���:��ȡ�ʼ�")
            if self.task["����7"]:
                self.indicate("��ʼ:�Զ���ľ")
                if self.genshin_cut_tree():
                    _k = True
                self.indicate("���:�Զ���ľ")
            if self.task["����8"]:
                self.indicate("��ʼ:�Զ��ؾ�")
                if self.genshin_domain():
                    _k = True
                self.indicate("���:�Զ��ؾ�")
            if self.task["����9"]:
                self.indicate("��ʼ:��ȡ����")
                self.genshin_pass()
                self.indicate("���:��ȡ����")
        except Exception:
            self.indicate("����ִ���쳣:ԭ��", log=False)
            logger.error("����ִ���쳣:ԭ��\n%s" % traceback.format_exc())
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
        self.indicate("�������:ԭ��")
        return _k

    def genshin_launch(self):
        # ·������
        env.set_soft(None, (0, "UnityWndClass", "ԭ��"))
        _path = self.task["����"]["game"]
        # print(_path)
        if os.path.isfile(_path):
            dire, name = os.path.split(_path)
            if name == "YuanShen.exe":
                env.soft.set_path(_path)
            elif name == "launcher.exe":
                path = dire + "/Genshin Impact Game/YuanShen.exe"
                if os.path.isfile(path):
                    env.soft.set_path(path)
                else:
                    self.indicate("ԭ��,��Ч����·��")
                    raise ValueError("ԭ��:��Ч����·��")
            else:
                self.indicate("ԭ��,��Ч����·��")
                raise ValueError("ԭ��:��Ч����·��")
        else:
            self.indicate("ԭ��,��Ч����·��")
            raise ValueError("ԭ��:��Ч����·��")
        # ������Ϸ
        env.soft.hwnd = find_hwnd(env.soft.mode_cls_tit)
        cond = env.soft.run()
        if cond == 1:
            self.indicate("��Ϸ��������")
            wait(1000)
        elif cond == 2:
            self.indicate("��Ϸ�����ɹ�")
            self.indicate("�ȴ�����,10���ʼʶ����Ϸ״̬")
            wait(10000)
        elif cond == 0:
            self.indicate("��Ϸ������ʱ")
            raise RuntimeError("ԭ��:��Ϸ������ʱ")
        for i in range(10):
            env.soft.foreground()
            wait(1000)
            if env.mode(1):
                break
            else:
                env.soft.foreground()
                wait(2000)
        
    def genshin_log(self, second: int):
        # ��¼&������Ϸ
        self.indicate("��ʼʶ����Ϸ״̬")
        server = self.task["����"]["server"]
        for i in range(second):
            sc = screenshot()
            if server == 0:
                if "�������" in ocr((897, 989, 1027, 1048))[0].replace(" ", ""):
                    server = 2
                    click((930, 630))
                    self.indicate("����")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            elif server == 1:
                if find_pic(r"assets\genshin\picture\login2.png", (863, 370, 1059, 467), sc)[1] >= 0.6:
                    click((953, 659))
                    self.indicate("��¼B���˺�")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
                if "�������" in ocr((897, 989, 1027, 1048))[0].replace(" ", ""):
                    server = 2
                    click((930, 630))
                    self.indicate("����")
                    wait(4000)
                    os.remove(sc)
                    sc = screenshot()
            if find_pic(r"assets\genshin\picture\sighin.png", (865, 240, 1060, 470), sc)[1] >= 0.6:
                click((930, 850))
                wait(800)
                click((930, 850))
                wait(100)
                click((930, 850))
                wait(1000)
                click((930, 850))
                wait(800)
                self.indicate("�����¿���ȡ�ɹ�")
                os.remove(sc)
                sc = screenshot()
            if find_pic(r"assets\genshin\picture\world.png", (57, 998, 179, 1075), sc)[1] >= 0.6:
                self.indicate("���ص�����")
                os.remove(sc)
                click((509, 313))
                wait(300)
                click((509, 313))
                wait(300)
                break
            if "����" in ocr((480, 442, 540, 481))[0]:
                self.indicate("���ص�������")
                os.remove(sc)
                click((509, 313))
                wait(300)
                click((509, 313))
                wait(300)
                break
            _p, val0 = find_pic(r"assets\genshin\picture\close0.png", (1683, 0, 1919, 236), sc)
            if val0 >= 0.6:
                click(_p)
                wait(2500)
            _p, val1 = find_pic(r"assets\genshin\picture\close1.png", (1609, 178, 1737, 293), sc)
            if val1 >= 0.6:
                click(_p)
                wait(2500)
            os.remove(sc)
            if i == second - 1:
                self.indicate(f"��¼��ʱ��{second * 2}s��")
                raise RuntimeError("ԭ��:ʶ����Ϸ״̬��ʱ")
            wait(2000)
            

if __name__ == '__main__':
    logger.enable_console()
    logger.hr("��ӭʹ�� ɰ�Ǵ���v1.1\n"
              "https://github.com/Kin-L/SGA-Sucrose_Game_Assistant\n"
              "�˳���Ϊ��ѿ�Դ��Ŀ ����㸶��Ǯ�������˿�", 0)
    pass
