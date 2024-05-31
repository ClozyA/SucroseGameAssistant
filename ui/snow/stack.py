# -*- coding:gbk -*-
from ui.element.ui_part import Independent
from ui.element.control import *


class Local:
    def __init__(self, stack):
        # ��ʼ������
        self.page_local = Widget(stack)
        stack.addWidget(self.page_local)
        # ��ӿؼ�
        self.label_local = Label(self.page_local, (0, 12, 180, 18), "����ҳ�棺���׽��� ���з�ʽ")
        Line(self.page_local, (0, 42, 395, 3))

        self.label_snow_overall = Label(self.page_local, (0, 50, 180, 27), "ȫ�����ã�")
        self.label_start = Label(self.page_local, (0, 90, 80, 27), "������")  # ����·�� /
        self.combo_server = Combobox(self.page_local, (80, 90, 100, 32))
        self.combo_server.addItems(["�ٷ�", "B��"])
        self.label_start = Label(self.page_local, (0, 130, 80, 27), "����·��")
        self.line_start = Lineedit(self.page_local, (0, 160, 385, 33))

        Line(self.page_local, (0, 202, 395, 3))

        self.label_team_tip = Label(self.page_local, (0, 210, 220, 27), "�����������ã�")
        self.check_preload = Check(self.page_local, (0, 245, 140, 22), "�Զ�Ԥ����")
        self.check_update = Check(self.page_local, (205, 245, 140, 22), "�Զ�����")
        self.independent = Independent(self.page_local, (0, 285, 350, 70))
        self.label_tools = Label(self.page_local, (0, 365, 220, 27), "ʵ�ù��ߣ�")
        self.button_wiki = Button(self.page_local, (0, 400, 100, 30), "������ͼ��")

        self.label_account = Label(self.page_local, (0, 433, 220, 27), "�˺�ѡ��")
        self.line_account = Lineedit(self.page_local, (0, 467, 200, 33))


class Fight:
    def __init__(self, stack):
        # ��ʼ������
        self.page_fight = Widget(stack)
        stack.addWidget(self.page_fight)
        # ��ӿؼ�
        self.label_fight = Label(self.page_fight, (0, 12, 220, 18), "����ҳ�棺��֪ɨ��")

        self.check_share = Check(self.page_fight, (15, 50, 140, 22), "��֪����")
        self.check_supply = Check(self.page_fight, (15, 80, 140, 22), "ÿ�����")
        self.check_reagent = Check(self.page_fight, (15, 110, 140, 22), "����ʹ����ʱ�Լ�")

        self.label_mat = Label(self.page_fight, (15, 195, 80, 18), "ʣ���֪")
        self.mat = Combobox(self.page_fight, (15, 225, 180, 40))
        self.mat.addItems(
            ["ͨ����", "��ɫ�����ز�", "���������ز�",
             "����ͻ���ز�", "��ɫ���ز�", "���ڻ�ȡ",
             "����ڻ�ȡ", "�������ȡ",
             "��ؿ�-���ֻù�"])

        self.label_logistics = Label(self.page_fight, (15, 275, 80, 18), "����ѡ��")
        self.logistics = Combobox(self.page_fight, (15, 305, 160, 40))
        self.logistics.addItems(
            ["�ױ�˹С��",
             "������С��",
             "Ħ����С��",
             "���һ�С��",
             "���С��",
             "��ҶС��",
             "��ĦС��",
             "������С��"])
        self.logistics1 = Combobox(self.page_fight, (185, 305, 160, 40))
        self.logistics1.addItems(
            ["����С��",
             "���С��",
             "������С��",
             "��԰С��",
             "����С��",
             "����С��",
             "����С��",
             "ɳҶС��"])


class Daily:
    def __init__(self, stack):
        # ��ʼ������
        self.page_debris = Widget(stack)
        stack.addWidget(self.page_debris)
        # ��ӿؼ�
        self.label_debris = Label(self.page_debris, (0, 12, 180, 18), "����ҳ�棺�ճ��ܳ�")

        self.check_character = Check(self.page_debris, (15, 50, 140, 22), "���˹���")
        self.check_supplement = Check(self.page_debris, (15, 80, 250, 22), "ǶƬΪ0ʱ,����2����Ƕ��")
        self.character1 = Combobox(self.page_debris, (15, 110, 120, 40))
        self.character2 = Combobox(self.page_debris, (145, 110, 120, 40))
        self.character3 = Combobox(self.page_debris, (15, 155, 120, 40))
        self.character4 = Combobox(self.page_debris, (145, 155, 120, 40))
        chara = ["δѡ��", "˲��", "����", "���", "����", "����", "ħ��ʦ", "�ط�", "��Ӱ", "��׭", "��ҹ",
                 "�̹�", "����", "����", "����", "��Ĭ",
                 "С����", "С̫��", "�۲���", "�ƽ�ʨ��", "����ר��",
                 "èè", "������", "������", "˫��", "��������",
                 "����С��", "������ʾ", "����"]
        self.character1.addItems(chara)
        self.character2.addItems(chara)
        self.character3.addItems(chara)
        self.character4.addItems(chara)

        self.check_imitate = Check(self.page_debris, (15, 210, 140, 22), "�⾳ɨ��")

        self.check_market = Check(self.page_debris, (15, 255, 220, 22), "ͨ���̵깺��һ�����ÿ��")
        self.box_market1 = Combobox(self.page_debris, (15, 285, 160, 40))
        self.box_market2 = Combobox(self.page_debris, (180, 285, 160, 40))
        self.box_market1.addItems(["����ս����¼", "����ְ����֤", "��������", "�������ϡ�3"])
        self.box_market2.addItems(["����ս����¼", "����ְ����֤", "��������", "�������ϡ�3"])
        self.check_weapon = Check(self.page_debris, (15, 340, 220, 22), "ͨ����������һ�����ÿ��")

        self.check_daily = Check(self.page_debris, (15, 375, 140, 22), "��ȡ�ճ�")
        self.check_daily2 = Check(self.page_debris, (15, 410, 140, 22), "��ȡƾ֤")
        self.check_daily3 = Check(self.page_debris, (15, 445, 180, 22), "��ȡ�ÿ��-���ֻù�")


class Mail:
    def __init__(self, stack):
        # ��ʼ������
        self.page_mail = Widget(stack)
        stack.addWidget(self.page_mail)
        # ��ӿؼ�
        self.label_mail = Label(self.page_mail, (0, 12, 180, 18), "����ҳ�棺��ȡ�ʼ�")
        self.label_mail_tip = Label(self.page_mail, (90, 80, 220, 27), "��ȡ�ʼ� ����������Ŀ��")


class Roll:
    def __init__(self, stack):
        # ��ʼ������
        self.page_roll = Widget(stack)
        stack.addWidget(self.page_roll)
        # ��ӿؼ�
        self.label_roll = Label(self.page_roll, (0, 12, 180, 18), "����ҳ�棺������¼")
        self.button_arrange = Button(self.page_roll, (0, 45, 180, 30), "����������¼ΪExcel")
        self.button_open_roll = (
            TransPicButton(self.page_roll, (185, 45, 30, 30),
                           "assets/main_window/ui/directory.png", (25, 25)))
        self.label_roll_tip = Label(self.page_roll, (90, 100, 220, 27), "������¼ ����������Ŀ��")


class SnowStack(Local, Fight, Daily, Mail, Roll):
    def __init__(self, widget, location):
        # ���ܶѵ�����
        self.stack = Stack(widget, location)
        Local.__init__(self, self.stack)
        Fight.__init__(self, self.stack)
        Daily.__init__(self, self.stack)
        Mail.__init__(self, self.stack)
        Roll.__init__(self, self.stack)
