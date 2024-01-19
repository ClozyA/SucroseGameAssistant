# -*- coding:gbk -*-
from ui.element.control import *
from ui.element.ui_part import *
import time
from tools.environment import logger


# ������
class MainWindow:  # FramelessWindow
    def __init__(self):
        # �����ڳ�ʼ��
        self.main_window = MWindow()
        self.button_set_home = OverallButton(self.main_window)  # ȫ��/ģ�� ���ð�ť
        self.button_history = PicButton(self.main_window, (693, 0, 56, 56),  # ��ʷ��Ϣ��ť
                                        r"assets\main_window\ui\history.png", (25, 25))
        self.button_sponsor = PicButton(self.main_window, (751, 0, 56, 56),  # ���Ͱ�ť
                                        r"assets\main_window\ui\support.png", (25, 25))
        self.window_support = Support()
        self.button_statement = Button(self.main_window, (809, 0, 96, 27), "ʹ����֪")
        self.button_instructions = Button(self.main_window, (809, 29, 96, 27), "ʹ��˵��")
        self.label_status = Picture(self.main_window, (485, 430, 150, 150),   # ָʾͼ��
                                    r"assets\main_window\ui\ico\0.png")
        self.box_info = InfoBox(self.main_window)  # ָʾ��Ϣ����
        self.stack_setting = Stack(self.main_window, (5, 0, 620, 570))
        self.state = \
            {"name": ["mix", "kleins", "genshin", "maa", "m7a"],
             "prefix": ["00", "01", "02", "03", "04"],
             "mix":     {"load": False, "prefix": "00"},
             "kleins":   {"load": False, "prefix": "01"},
             "genshin": {"load": False, "prefix": "02"},
             "maa":     {"load": False, "prefix": "03"},
             "m7a":     {"load": False, "prefix": "04"},
             "plan":    {},    "serial": [],   "single":    [],
             "stack":   None,  "locked": None, "hwnd":      None,
             "text":    None,  "index":  None, "wait_time": 1}
        self.config = None
        self.task = {}
        self.overall = None

        # ��Ϣ����ʾ��Ϣ
    def indicate(self, msg, mode=2, his=True, log=True):
        if mode == 0:  # �����Ϣ��
            self.box_info.clear()
        elif mode == 1:  # ʱ��ǰ׺����Ϣͷ��׷��
            now_time = time.strftime("%Y-%m-%d", time.localtime())
            self.box_info.append(now_time)
            if his:
                txt = open(r"personal\history.txt", 'a+', encoding='utf-8')
                txt.write(now_time + "\n")
        elif mode == 2:  # ʱ��ǰ׺����Ϣ����׷��
            _t = time.strftime("%H:%M:%S ", time.localtime()) + msg
            _t = _t.replace("\n", "\n         ")
            self.box_info.append(_t)
            self.box_info.ensureCursorVisible()
            if his:
                txt = open(r"personal\history.txt", 'a+', encoding='utf-8')
                txt.write(_t + "\n")
            if log:
                logger.info(msg.replace("\n", "\n                   "))
        elif mode == 3:  # ��Ϣ�����β
            _t = time.strftime("%H:%M:%S ", time.localtime()) + msg
            _t = _t.replace("\n", "\n         ")
            self.box_info.append(_t + "\n------------------------------")
            self.box_info.ensureCursorVisible()
            if his:
                txt = open(r"personal\history.txt", 'a+', encoding='utf-8')
                txt.write(_t + "\n------------------------------\n")
            if log:
                logger.info(msg.replace("\n", "\n                   ") +
                            "\n-------------------------------------")
        elif mode == 4:  # ֱ��׷����Ϣ
            self.box_info.append(msg)
            self.box_info.ensureCursorVisible()
            if his:
                txt = open(r"personal\history.txt", 'a+', encoding='utf-8')
                txt.write("msg" + "\n")
        else:
            print("��Ϣ���,��Чģʽ")
