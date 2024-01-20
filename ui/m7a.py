# -*- coding:gbk -*-
from ui.element.control import *
from ui.element.ui_part import Independent
from tools.system import check_path


class M7AList:
    def __init__(self, widget, location):
        # �����б���
        self.scroll_list = Widget(widget, location)
        self.label_m7a = Label(self.scroll_list, (70, 10, 120, 20), "����������", 18)
        Line(widget, (215, 5, 3, 505), False)


class M7AStack:
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        # ���ܶѵ�����
        self.stack = Widget(self.stack, (0, 0, 395, 515))
        self.label_local = Label(self.stack, (0, 12, 220, 18), "����ҳ�棺���������� ���з�ʽ")
        Line(self.stack, (0, 41, 395, 3))
        
        self.label_m7a_overall = Label(self.stack, (0, 45, 180, 27), "ȫ�����ã�")
        self.label_start = Label(self.stack, (0, 80, 80, 27), "����·��")
        self.line_start = Lineedit(self.stack, (0, 110, 385, 33))
        Line(self.stack, (0, 152, 395, 3))

        self.label_team_tip = Label(self.stack, (0, 160, 220, 27), "�����������ã�")
        self.independent = Independent(self.stack, (0, 200, 350, 70), False)


class M7A:
    def __init__(self, stack, icon, main):
        # ����������
        self.widget_m7a = Widget()
        stack.addWidget(self.widget_m7a)
        self.button_m7a = (
            PicButton(icon, (220, 0, 50, 50), 
                      r"assets\m7a\picture\M7A-icon.png", (50, 50)))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = M7AList(self.widget_m7a, (0, 0, 215, 515))
        self.set = M7AStack(self.widget_m7a, (225, 0, 395, 515))
        Line(self.widget_m7a, (215, 5, 3, 505), False)

    def load_run(self, run):
        _dir = {
            "m7a_path": ""
        }
        _dir.update(run)
        self.set.line_start.setText(_dir["m7a_path"])
        self.set.line_start.setSelection(0, 0)

    def get_run(self):
        return {"m7a_path": check_path(self.set.line_start.text())}

    def input_config(self, _dir):
        config = {
            "ģ��": 4,
            "����": False,
            "�ر����": False,
            "��ɺ�": 0,
            "SGA�ر�": False
        }
        config.update(_dir)
        self.set.independent.check_mute.setChecked(config["����"])
        self.set.independent.combo_after.setCurrentIndex(config["��ɺ�"])
        self.set.independent.check_kill_sga.setChecked(config["SGA�ر�"])

    def output_config(self):
        config = dict()
        config["ģ��"] = 4
        config["����"] = self.set.independent.check_mute.isChecked()
        config["�ر����"] = True
        config["��ɺ�"] = self.set.independent.combo_after.currentIndex()
        config["SGA�ر�"] = self.set.independent.check_kill_sga.isChecked()
        return config
