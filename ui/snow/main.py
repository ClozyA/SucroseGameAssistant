# -*- coding:gbk -*-
import os
import webbrowser
from .list import SnowList
from .stack import SnowStack
from ui.element.control import *
from tools.environment import env
from tools.system import check_path


# ���׽���ģ�����ô���
class Snow:
    def __init__(self, stack, icon, main):
        self.main = main
        self.widget_snow = Widget()
        stack.addWidget(self.widget_snow)
        self.button_snow = (
            PicButton(icon, (275, 0, 50, 50),
                      r"assets\snow\picture\snow-icon.png", (50, 50)))
        self.list = None
        self.set = None

    def load_window(self):
        self.list = SnowList(self.widget_snow, (0, 0, 215, 515))
        self.set = SnowStack(self.widget_snow, (225, 0, 410, 515))
        self.list.set_snow.clicked.connect(lambda: self.set.stack.setCurrentIndex(0))
        self.list.set_fight.clicked.connect(lambda: self.set.stack.setCurrentIndex(1))
        self.list.set_daily.clicked.connect(lambda: self.set.stack.setCurrentIndex(2))
        self.list.set_mail.clicked.connect(lambda: self.set.stack.setCurrentIndex(3))
        self.list.set_roll.clicked.connect(lambda: self.set.stack.setCurrentIndex(4))

        self.set.button_wiki.clicked.connect(self.open_wiki)
        self.set.button_arrange.clicked.connect(self.roll_arrange)
        self.set.button_open_roll.clicked.connect(self.open_roll_directory)
        Line(self.widget_snow, (215, 5, 3, 505), False)

    def load_run(self, run):
        _dir = {
            "server": 0,
            "snow_path": ""
        }
        _dir.update(run)
        self.set.combo_server.setCurrentIndex(_dir["server"])
        self.set.line_start.setText(_dir["snow_path"])
        self.set.line_start.setSelection(0, 0)

    def get_run(self):
        _dir = {
            "server": self.set.combo_server.currentIndex(),
            "snow_path": check_path(self.set.line_start.text())
        }
        return _dir

    def input_config(self, _dir):
        config = {
            "ģ��": 5,
            "Ԥ����": False,
            "����": False,
            "����": False,
            "�ر����": False,
            "��ɺ�": 0,
            "SGA�ر�": False,
            "�˺�ѡ��": "",
            "����0": False,
            "����1": False,
            "����2": False,
            "����3": False,
            "����4": False,
            "��֪����": False,
            "ÿ�����": False,
            "ʹ���Լ�": False,
            "�ж�ѡ��": 0,
            "����ѡ��": "�ױ�˹С��",
            "�����ѡ��": "����С��",
            "���˹���": [False, False, "δѡ��", "δѡ��", "δѡ��", "δѡ��"],
            "�⾳ɨ��": False,
            "�̵깺��": [False, "����ս����¼", "����ְ����֤"],
            "��������": False,
            "��ȡ�ճ�": False,
            "��ȡƾ֤": False,
            "�ÿ��": False
        }
        config.update(_dir)
        self.set.check_preload.setChecked(config["Ԥ����"])
        self.set.check_update.setChecked(config["����"])
        self.set.independent.check_mute.setChecked(config["����"])
        self.set.independent.check_kill_game.setChecked(config["�ر����"])
        self.set.independent.combo_after.setCurrentIndex(config["��ɺ�"])
        self.set.independent.check_kill_sga.setChecked(config["SGA�ر�"])
        self.set.line_account.setText(config["�˺�ѡ��"])
        self.set.line_account.setSelection(0, 0)

        self.list.check_fight.setChecked(config["����0"])
        self.list.check_daily.setChecked(config["����1"])
        self.list.check_mail.setChecked(config["����2"])
        self.list.check_roll.setChecked(config["����3"])

        self.set.check_share.setChecked(config["��֪����"])
        self.set.check_supply.setChecked(config["ÿ�����"])
        self.set.check_reagent.setChecked(config["ʹ���Լ�"])
        self.set.mat.setCurrentIndex(config["�ж�ѡ��"])
        self.set.logistics.setCurrentText(config["����ѡ��"])
        self.set.logistics1.setCurrentText(config["�����ѡ��"])

        self.set.check_character.setChecked(config["���˹���"][0])
        self.set.check_supplement.setChecked(config["���˹���"][1])
        self.set.character1.setCurrentText(config["���˹���"][2])
        self.set.character2.setCurrentText(config["���˹���"][3])
        self.set.character3.setCurrentText(config["���˹���"][4])
        self.set.character4.setCurrentText(config["���˹���"][5])

        self.set.check_imitate.setChecked(config["�⾳ɨ��"])
        self.set.check_market.setChecked(config["�̵깺��"][0])
        self.set.box_market1.setCurrentText(config["�̵깺��"][1])
        self.set.box_market2.setCurrentText(config["�̵깺��"][2])
        self.set.check_weapon.setChecked(config["��������"])
        self.set.check_daily.setChecked(config["��ȡ�ճ�"])
        self.set.check_daily2.setChecked(config["��ȡƾ֤"])
        self.set.check_daily3.setChecked(config["�ÿ��"])

    def output_config(self):
        config = dict()
        config["ģ��"] = 5

        config["Ԥ����"] = self.set.check_preload.isChecked()
        config["����"] = self.set.check_update.isChecked()
        config["����"] = self.set.independent.check_mute.isChecked()
        config["�ر����"] = self.set.independent.check_kill_game.isChecked()
        config["��ɺ�"] = self.set.independent.combo_after.currentIndex()
        config["SGA�ر�"] = self.set.independent.check_kill_sga.isChecked()
        config["�˺�ѡ��"] = self.set.line_account.text()

        config["����0"] = self.list.check_fight.isChecked()
        config["����1"] = self.list.check_daily.isChecked()
        config["����2"] = self.list.check_mail.isChecked()
        config["����3"] = self.list.check_roll.isChecked()

        config["��֪����"] = self.set.check_share.isChecked()
        config["ÿ�����"] = self.set.check_supply.isChecked()
        config["ʹ���Լ�"] = self.set.check_reagent.isChecked()
        config["�ж�ѡ��"] = self.set.mat.currentIndex()
        config["����ѡ��"] = self.set.logistics.currentText()
        config["�����ѡ��"] = self.set.logistics1.currentText()
        config["���˹���"] = [
            self.set.check_character.isChecked(),
            self.set.check_supplement.isChecked(),
            self.set.character1.currentText(),
            self.set.character2.currentText(),
            self.set.character3.currentText(),
            self.set.character4.currentText()]
        config["�⾳ɨ��"] = self.set.check_imitate.isChecked()
        config["�̵깺��"] = [
            self.set.check_market.isChecked(),
            self.set.box_market1.currentText(),
            self.set.box_market2.currentText()]
        config["��������"] = self.set.check_weapon.isChecked()
        config["��ȡ�ճ�"] = self.set.check_daily.isChecked()
        config["��ȡƾ֤"] = self.set.check_daily2.isChecked()
        config["�ÿ��"] = self.set.check_daily3.isChecked()
        return config

    def open_roll_directory(self):
        os.startfile(env.workdir + "/personal/snow/roll")
        self.main.indicate("���ļ���: ������¼", 1)

    def open_wiki(self):
        webbrowser.open("https://wiki.biligame.com/sonw/%E9%A6%96%E9%A1%B5")
        self.main.indicate("����ҳ: ���׽��� BWIKI", 1)

    def roll_arrange(self):
        import json
        with open("personal/snow/roll/history.json", 'r', encoding='utf-8') as m:
            _dir = json.load(m)
        from openpyxl import load_workbook
        from openpyxl.styles import Font, Alignment
        import time
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        import shutil
        src = r"assets\snow\default_snow_roll.xlsx"
        dst = f"personal/snow/roll/���׽���������¼ - {now}.xlsx"
        shutil.copyfile(src, dst)
        wb = load_workbook(dst)
        fon2 = Font(name='����', size=12)
        fon_three = Font(name='����', size=12, color="3374F8")
        fon_four = Font(name='����', size=12, color="7E30FF", bold=True)
        fon_five = Font(name='����', size=12, color="FFC332", bold=True)
        al = Alignment(horizontal='center', vertical='center')
        _count = []
        for i in ["��ѡ��ɫ����", "��ѡ��������", "�޶���ɫ����", "�޶���������", "����֮��", "��ͥ¯��", "���ֳ�"]:
            _sheet = wb[i]

            _list = _dir[i]
            n_row = 1
            n_four = 0
            n_five = 0
            count = [0, 0, 0, 0, 0, [], []]
            for [r, t] in _list:
                n_row += 1
                n_four += 1
                n_five += 1
                if "������" in r:
                    r = "��-��������"
                elif "����" in r:
                    if "��" in r:
                        r = "����-�̹�"
                elif "��ŵ" in r:
                    if "�" in r or "��" in r:
                        r = "��ŵ-���"
                elif "������ʾ" in r:
                    r = "����ϣ��-[������ʾ]"
                elif "�����" in r:
                    r = "�������"
                elif "������" in r:
                    r = "����-������"
                elif "��Ȩ��" in r:
                    r = "��Ȩ����"
                elif "��˹" in r and "��" in r:
                    r = "ɪ��˹-˲��"

                _a = _sheet[f"A{n_row}"]
                _b = _sheet[f"B{n_row}"]
                _c = _sheet[f"C{n_row}"]
                _d = _sheet[f"D{n_row}"]
                _sheet[f"A{n_row}"] = t
                _sheet[f"B{n_row}"] = r
                _sheet[f"C{n_row}"] = n_row - 1
                _sheet[f"D{n_row}"] = n_five
                _sheet[f"A{n_row}"].alignment = al
                _sheet[f"B{n_row}"].alignment = al
                _sheet[f"C{n_row}"].alignment = al
                _sheet[f"D{n_row}"].alignment = al
                if r in ["�����׵�", "��ѩ", "Ƥ˹��", "����",
                         "�������", "��Ĭ������", "���ǽ", "��ѵ",
                         "������", "����ɳ��", "�ҹ�", "��Ե��",
                         "Ⱥ�����", "��������", "����������", "��ȫ��",
                         "ƫͷʹ", "������ʿ", "����֮��", "���װ���",
                         "����ľ", "��ķ�籩", "��֮������", "����Ů��",
                         "�ش�"]:
                    _fon = fon_three
                    count[0] += 1
                elif r in ["����ϣ��-[������ʾ]", "��-����ר��", "����-�ƽ�ʨ��", "����-������",
                           "èϫ��-èè", "����-�۲���", "��ŵ-˫��", "����-����С��",
                           "��ܽ-������", "��-��������", "����-����", "ܽ����-С̫��",
                           "ɪ��˹-С����",
                           "����̾Ϣ", "СС����", "�ؼ���", "�ʺ����",
                           "������", "��Э����", "�󱦱���", "�޺�ƹ�",
                           "����ʱ��", "Ұ��װ��", "С��Ѽ", "���������",
                           "�ǣ��ǣ�������", "¥����è", "ŭ������", "��ݮ����",
                           "����Ȧ", "��е����", "������", "������",
                           "������", "������", "����ʩ��", "����",
                           "���ʯ", "�����", "�������", "���ҵ�˹��",
                           "����ˮĸ", "�߶�����2056", "�����ֳ�", "�������",
                           "ʪ�ع�԰", "ָʾ��"]:
                    _fon = fon_four
                    count[1] += 1
                    count[5] += [f"{r}({n_four})"]
                    n_four = 0
                elif r in ["����ϣ��-��ҹ", "����-��׭", "��-�ط�", "èϫ��-��Ӱ",
                           "̦˿-ħ��ʦ", "���ж�-����", "������-����", "��ŵ-���",
                           "����-����", "ɪ��˹-˲��",
                           "���ּ���", "�����а", "������16", "�Ͻ�����",
                           "���ƹֵ�", "������", "����绢", "��ҹ��ʫ",
                           "Ԩ��", "��Ȩ����",
                           "����-�̹�", "��-����", "��ܽ-����", "����-����", "ܽ����-��Ĭ",
                           "С��ʳ", "�ǳ���", "����ǰҹ", "���ҹ���",
                           "̫�����", "�����Ž�", "̫������", "��ս�ϱ�",
                           "����ƥ˹", "�ǳ�����"]:
                    _fon = fon_five
                    count[2] += 1
                    count[6] += [f"{r}({n_five})"]
                    n_five = 0
                else:
                    print(r, t)
                    self.main.indicate(f"ϡ�ж��쳣ʶ���쳣:{r}", 3)
                    return False
                _sheet[f"A{n_row}"].font = _fon
                _sheet[f"B{n_row}"].font = _fon
                _sheet[f"C{n_row}"].font = fon2
                _sheet[f"D{n_row}"].font = fon2
                _sheet.row_dimensions[n_row].height = 18
            count[3] = n_row-1
            count[4] = n_five
            _count += [count]
        sheet0 = wb["����"]
        sheet0["B3"] = _count[0][0]
        sheet0["C3"] = _count[0][1]
        sheet0["D3"] = _count[0][2]
        sheet0["E3"] = _count[0][3]
        sheet0["F3"] = _count[0][4]

        _list = _count[0][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I2"] = _str
        _list = _count[0][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I3"] = _str

        sheet0["B6"] = _count[1][0]
        sheet0["C6"] = _count[1][1]
        sheet0["D6"] = _count[1][2]
        sheet0["E6"] = _count[1][3]
        sheet0["F6"] = _count[1][4]
        _list = _count[1][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I5"] = _str

        _list = _count[1][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I6"] = _str

        sheet0["B9"] = _count[2][0]
        sheet0["C9"] = _count[2][1]
        sheet0["D9"] = _count[2][2]
        sheet0["E9"] = _count[2][3]
        sheet0["F9"] = _count[2][4]
        _list = _count[2][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I8"] = _str

        _list = _count[2][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I9"] = _str

        sheet0["B12"] = _count[3][0]
        sheet0["C12"] = _count[3][1]
        sheet0["D12"] = _count[3][2]
        sheet0["E12"] = _count[3][3]
        sheet0["F12"] = _count[3][4]
        _list = _count[3][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I11"] = _str

        _list = _count[3][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I12"] = _str

        sheet0["B15"] = _count[4][0]
        sheet0["C15"] = _count[4][1]
        sheet0["D15"] = _count[4][2]
        sheet0["E15"] = _count[4][3]
        sheet0["F15"] = _count[4][4]
        _list = _count[4][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I14"] = _str

        _list = _count[4][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I15"] = _str

        sheet0["B18"] = _count[5][0]
        sheet0["C18"] = _count[5][1]
        sheet0["D18"] = _count[5][2]
        sheet0["E18"] = _count[5][3]
        sheet0["F18"] = _count[5][4]
        _list = _count[5][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I17"] = _str

        _list = _count[5][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I18"] = _str

        sheet0["B21"] = _count[6][0]
        sheet0["C21"] = _count[6][1]
        sheet0["D21"] = _count[6][2]
        sheet0["E21"] = _count[6][3]
        sheet0["F21"] = _count[6][4]
        _list = _count[6][5]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I20"] = _str

        _list = _count[6][6]
        _str = ""
        for i in _list:
            _str += i + " "
        sheet0["I21"] = _str
        wb.save(dst)
        self.main.indicate("������¼�ѵ���", 3)
