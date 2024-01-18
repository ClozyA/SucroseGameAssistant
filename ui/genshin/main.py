# -*- coding:gbk -*-
from .list import GenshinList
from .stack import GenshinStack
from ui.element.control import Line, Widget, PicButton


class Genshin:
    def __init__(self, stack, icon, main):
        self.widget_genshin = Widget()
        stack.addWidget(self.widget_genshin)
        self.button_genshin = (
            PicButton(icon, (110, 0, 50, 50),
                      r"assets\genshin\picture\genshin-icon.png", (50, 50)))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = GenshinList(self.widget_genshin, (0, 0, 215, 515))
        self.set = GenshinStack(self.widget_genshin, (225, 0, 410, 515))
        self.list.set_genshin.clicked.connect(lambda: self.set.stack.setCurrentIndex(0))
        self.list.set_team.clicked.connect(lambda: self.set.stack.setCurrentIndex(1))
        self.list.set_disp.clicked.connect(lambda: self.set.stack.setCurrentIndex(2))
        self.list.set_trans.clicked.connect(lambda: self.set.stack.setCurrentIndex(3))
        self.list.set_fly.clicked.connect(lambda: self.set.stack.setCurrentIndex(4))
        self.list.set_comp.clicked.connect(lambda: self.set.stack.setCurrentIndex(5))
        self.list.set_pot.clicked.connect(lambda: self.set.stack.setCurrentIndex(6))
        self.list.set_mail.clicked.connect(lambda: self.set.stack.setCurrentIndex(7))
        self.list.set_tree.clicked.connect(lambda: self.set.stack.setCurrentIndex(8))
        self.list.set_domain.clicked.connect(lambda: self.set.stack.setCurrentIndex(9))
        Line(self.widget_genshin, (215, 5, 3, 505), False)

    def load_run(self, run):
        _dir = {
            "server": 0,
            "game": "",
            "BGI": ""
        }
        _dir.update(run)
        self.set.combo_server.setCurrentIndex(_dir["server"])
        self.set.line_start.setText(_dir["game"])
        self.set.line_start.setSelection(0, 0)
        self.set.line_bgi.setText(_dir["BGI"])

    def get_run(self):
        _dir = {
            "server": self.set.combo_server.currentIndex(),
            "game": self.set.line_start.text(),
            "BGI": self.set.line_bgi.text()
        }
        return _dir

    def input_config(self, _dir):
        config = {
            "ģ��": 2,
            "����": False,
            "�ر����": False,
            "��ɺ�": 0,
            "SGA�ر�": False,
            "����0": False,
            "����1": False,
            "����2": False,
            "����3": False,
            "����4": False,
            "����5": False,
            "����6": False,
            "����7": False,
            "����8": False,
            "��ǲ0": [0, 0],
            "��ǲ1": [0, 0],
            "��ǲ2": [0, 0],
            "��ǲ3": [0, 0],
            "��ǲ4": [0, 0],
            "�ٴ���ǲ": False,
            "�����ʱ���0": "",
            "�����ʱ���1": "",
            "�����ʱ���2": "",
            "�����ʱ���3": "",
            "�����ʱ���4": "",
            "����0": False,
            "����1": False,
            "����2": False,
            "����3": False,
            "����4": False,
            "��������": 0,
            "����0": False,
            "����1": False,
            "����2": False,
            "����3": False,
            "����4": False,
            "����5": False,
            "����6": False,
            "����7": False,
            "����8": False,
            "����9": False,
            "����10": False,
            "����11": False,
            "����12": False,
            "����13": False,
            "����14": False,
            "����15": False,
            "����16": False,
            "����17": False,
            "����18": False,
            "�ؾ�": ["ʥ����", "����ͥԺ"]
        }
        config.update(_dir)
        self.set.independent.check_mute.setChecked(config["����"])
        self.set.independent.check_kill_game.setChecked(config["�ر����"])
        self.set.independent.combo_after.setCurrentIndex(config["��ɺ�"])
        self.set.independent.check_kill_sga.setChecked(config["SGA�ر�"])
        self.list.check_team.setChecked(config["����0"])
        self.list.check_disp.setChecked(config["����1"])
        self.list.check_trans.setChecked(config["����2"])
        self.list.check_fly.setChecked(config["����3"])
        self.list.check_comp.setChecked(config["����4"])
        self.list.check_pot.setChecked(config["����5"])
        self.list.check_mail.setChecked(config["����6"])
        self.list.check_tree.setChecked(config["����7"])
        self.list.check_domain.setChecked(config["����8"])

        self.set.area0.setCurrentIndex(config["��ǲ0"][0])
        self.set.area1.setCurrentIndex(config["��ǲ1"][0])
        self.set.area2.setCurrentIndex(config["��ǲ2"][0])
        self.set.area3.setCurrentIndex(config["��ǲ3"][0])
        self.set.area4.setCurrentIndex(config["��ǲ4"][0])
        self.set.list_change(self.set.area0, self.set.mat0)
        self.set.list_change(self.set.area1, self.set.mat1)
        self.set.list_change(self.set.area2, self.set.mat2)
        self.set.list_change(self.set.area3, self.set.mat3)
        self.set.list_change(self.set.area4, self.set.mat4)
        self.set.mat0.setCurrentIndex(config["��ǲ0"][1])
        self.set.mat1.setCurrentIndex(config["��ǲ1"][1])
        self.set.mat2.setCurrentIndex(config["��ǲ2"][1])
        self.set.mat3.setCurrentIndex(config["��ǲ3"][1])
        self.set.mat4.setCurrentIndex(config["��ǲ4"][1])

        self.set.LineEdit0.setText(config["�����ʱ���0"])
        self.set.LineEdit1.setText(config["�����ʱ���1"])
        self.set.LineEdit2.setText(config["�����ʱ���2"])
        self.set.LineEdit3.setText(config["�����ʱ���3"])
        self.set.LineEdit4.setText(config["�����ʱ���4"])
        self.set.fly0.setChecked(config["����0"])
        self.set.fly1.setChecked(config["����1"])
        self.set.fly2.setChecked(config["����2"])
        self.set.fly3.setChecked(config["����3"])
        self.set.fly4.setChecked(config["����4"])

        self.set.CompactSpinBox.setValue(config["��������"])
        self.set.tree0.setChecked(config["����0"])
        self.set.tree1.setChecked(config["����1"])
        self.set.tree2.setChecked(config["����2"])
        self.set.tree3.setChecked(config["����3"])
        self.set.tree4.setChecked(config["����4"])
        self.set.tree5.setChecked(config["����5"])
        self.set.tree6.setChecked(config["����6"])
        self.set.tree7.setChecked(config["����7"])
        self.set.tree8.setChecked(config["����8"])
        self.set.tree9.setChecked(config["����9"])
        self.set.tree10.setChecked(config["����10"])
        self.set.tree11.setChecked(config["����11"])
        self.set.tree12.setChecked(config["����12"])
        self.set.tree13.setChecked(config["����13"])
        self.set.tree14.setChecked(config["����14"])
        self.set.tree15.setChecked(config["����15"])
        self.set.tree16.setChecked(config["����16"])
        self.set.tree17.setChecked(config["����17"])
        self.set.tree18.setChecked(config["����18"])
        self.set.domain_type.setCurrentText(config["�ؾ�"][0])
        self.set.domain_change(self.set.domain_type, self.set.domain)
        self.set.domain.setCurrentText(config["�ؾ�"][1])

    def output_config(self):
        config = dict()
        config["ģ��"] = 2

        config["����"] = self.set.independent.check_mute.isChecked()
        config["�ر����"] = self.set.independent.check_kill_game.isChecked()
        config["��ɺ�"] = self.set.independent.combo_after.currentIndex()
        config["SGA�ر�"] = self.set.independent.check_kill_sga.isChecked()

        config["����0"] = self.list.check_team.isChecked()
        config["����1"] = self.list.check_disp.isChecked()
        config["����2"] = self.list.check_trans.isChecked()
        config["����3"] = self.list.check_fly.isChecked()
        config["����4"] = self.list.check_comp.isChecked()
        config["����5"] = self.list.check_pot.isChecked()
        config["����6"] = self.list.check_mail.isChecked()
        config["����7"] = self.list.check_tree.isChecked()
        config["����8"] = self.list.check_domain.isChecked()

        config["��ǲ0"] = [self.set.area0.currentIndex(), self.set.mat0.currentIndex()]
        config["��ǲ1"] = [self.set.area1.currentIndex(), self.set.mat1.currentIndex()]
        config["��ǲ2"] = [self.set.area2.currentIndex(), self.set.mat2.currentIndex()]
        config["��ǲ3"] = [self.set.area3.currentIndex(), self.set.mat3.currentIndex()]
        config["��ǲ4"] = [self.set.area4.currentIndex(), self.set.mat4.currentIndex()]
        config["�ٴ���ǲ"] = self.set.redisp.isChecked()

        config["�����ʱ���0"] = self.set.LineEdit0.text()
        config["�����ʱ���1"] = self.set.LineEdit1.text()
        config["�����ʱ���2"] = self.set.LineEdit2.text()
        config["�����ʱ���3"] = self.set.LineEdit3.text()
        config["�����ʱ���4"] = self.set.LineEdit4.text()

        config["����0"] = self.set.fly0.isChecked()
        config["����1"] = self.set.fly1.isChecked()
        config["����2"] = self.set.fly2.isChecked()
        config["����3"] = self.set.fly3.isChecked()
        config["����4"] = self.set.fly4.isChecked()

        config["��������"] = self.set.CompactSpinBox.value()
        config["����0"] = self.set.tree0.isChecked()
        config["����1"] = self.set.tree1.isChecked()
        config["����2"] = self.set.tree2.isChecked()
        config["����3"] = self.set.tree3.isChecked()
        config["����4"] = self.set.tree4.isChecked()
        config["����5"] = self.set.tree5.isChecked()
        config["����6"] = self.set.tree6.isChecked()
        config["����7"] = self.set.tree7.isChecked()
        config["����8"] = self.set.tree8.isChecked()
        config["����9"] = self.set.tree9.isChecked()
        config["����10"] = self.set.tree10.isChecked()
        config["����11"] = self.set.tree11.isChecked()
        config["����12"] = self.set.tree12.isChecked()
        config["����13"] = self.set.tree13.isChecked()
        config["����14"] = self.set.tree14.isChecked()
        config["����15"] = self.set.tree15.isChecked()
        config["����16"] = self.set.tree16.isChecked()
        config["����17"] = self.set.tree17.isChecked()
        config["����18"] = self.set.tree18.isChecked()
        config["�ؾ�"] = [self.set.domain_type.currentText(),
                        self.set.domain.currentText()]
        return config
