# -*- coding:gbk -*-
import json
from ..default_task import Task
from tools.environment import *
from tools.software import get_pid, close
import os
import traceback


class TaskMAA(Task):
    def __init__(self):
        super().__init__()

    def maa_start(self, task: type[dir]):
        _k = False
        self.task = task
        self.indicate("��ʼ����:MAA")
        # noinspection PyBroadException
        try:
            # MAA�رղ���ʼ��
            pid = get_pid("MAA.exe")
            if pid is not None:
                self.indicate("MAA��������,��������")
                close(pid)
            env.set_soft(None, (1, "HwndWrapper[MAA.exe", "MAA"))
            _path = self.task["����"]["maa_path"]
            if os.path.isfile(_path):
                dire, name = os.path.split(_path)
                if name == "MAA.exe":
                    env.soft.set_path(_path)
                else:
                    self.indicate("MAA,��Ч����·��")
                    raise ValueError("MAA,��Ч����·��")
            else:
                self.indicate("MAA,��Ч����·��")
                raise ValueError("MAA,��Ч����·��")
            # �޸�MAA��������
            gui_path = os.path.split(_path)[0] + "/config/gui.json"
            with open(gui_path, 'r', encoding='utf-8') as g:
                maa = json.load(g)
            import copy
            setcurrent = self.task["����"]
            _sga = copy.deepcopy(maa["Configurations"][setcurrent])
            if self.task["�ر����"]:
                after_completed = "ExitEmulatorAndSelf"
            else:
                after_completed = "ExitSelf"
            current = maa["Current"]
            _sga["Start.EndsWithScript"] = env.workdir + "/personal/bat/maa_create.bat"
            _sga["MainFunction.ActionAfterCompleted"] = after_completed
            _sga["Start.RunDirectly"] = "True"
            maa["Configurations"]["SGA-cache"] = _sga
            maa["Current"] = "SGA-cache"
            with open(gui_path, 'w', encoding='utf-8') as g:
                json.dump(maa, g, ensure_ascii=False, indent=1)
            _f = env.workdir + "/cache/maa_complete.txt"
            if os.path.exists(_f):
                os.remove(_f)
            env.soft.run()
            self.indicate("MAA������...")
            # ����-����
            while 1:
                wait(10000)
                if os.path.exists(_f):
                    os.remove(_f)
                    break
            with open(gui_path, 'r', encoding='utf-8') as g:
                maa = json.load(g)
            maa["Current"] = current
            with open(gui_path, 'w', encoding='utf-8') as g:
                json.dump(maa, g, ensure_ascii=False, indent=1)
        except Exception:
            self.indicate("����ִ���쳣:MAA", log=False)
            logger.error("����ִ���쳣:MAA\n%s" % traceback.format_exc())
            _k = True
        self.indicate("�������:MAA")
        return _k


if __name__ == '__main__':
    pass
