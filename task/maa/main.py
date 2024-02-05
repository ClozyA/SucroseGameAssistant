# -*- coding:gbk -*-
import json
from ..default_task import Task
from tools.environment import *
from tools.software import get_pid, close, find_hwnd
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
            # def st():
            #     from win32process import CreateProcess, CREATE_NEW_CONSOLE, STARTUPINFO
            #     from win32event import WaitForSingleObject
            #     ifexistexe=os.system('tasklist|findstr "MAA.exe"')
            #     if ifexistexe==0:
            #         os.system('taskkill /f /im "MAA.exe"')
            #         wait(1000)
            #     handle=CreateProcess(_path, '', None , None , 0 ,CREATE_NEW_CONSOLE , None , os.path.split(_path)[0] ,STARTUPINFO())
            #     WaitForSingleObject(handle[0],2)
            #     self.indicate("MAA������...")
            _f = env.workdir + "/cache/maa_complete.txt"
            if os.path.exists(_f):
                os.remove(_f)
            def maa_run():
                [_dir, name] = os.path.split(_path)
                cmd = f"start /d \"{_dir}\" {name}"
                f = open("cache/MAA_start.bat", 'w', encoding='utf-8')
                f.writelines(cmd)
                f.close()
                _p = os.path.join(env.workdir, "assets/main_window/bat_scr/PsExec64.exe")
                for n in range(2):
                    cmd_run(f"start \"\" \"{_p}\" -i -s -d \"{_path}\"")
                    for i in range(30):
                        wait(1000)
                        self.hwnd = find_hwnd((False, "HwndWrapper[MAA", "MAA"))
                        if self.hwnd:
                            self.indicate("MAA������...")
                            return False
                return True
            if maa_run():
                raise RuntimeError("MAA������ʱ")
            # st()
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
