# coding:utf-8
from PyQt5.QtCore import QThread, pyqtSignal
from tools.environment import *
import traceback
import os
import requests
import json
import time
import sys


class Update(QThread):
    send = pyqtSignal(str, int, bool, bool)

    def __init__(self, ui):  # mode true:集成运行 false:独立运行
        super(Update, self).__init__()
        self.ui = ui
        self.version = ui.state["version"]
        self.mode = None

    def indicate(self, msg: str, mode=2, his=True, log=True):
            self.send.emit(msg, mode, his, log)

    def run(self):
        if self.mode == 0:
            self.check()
        elif self.mode == 1:
            self.load_add_update()
        elif self.mode == 2:  # 自动检查并更新
            wait(500)
            if self.check():
                self.load_add_update()
            self.ui.overall.button_check.setEnabled(True)
            

    def check(self):
        # noinspection PyBroadException
        try:
             # cur_ver = "2.0.0"   ver_lit = [2, 0, 0]
            url = "https://gitee.com/huixinghen/sga_sucrose_game_assistant/raw/master/version.json"
        
            for i in range(3):
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = json.loads(response.text)
                    new_ver, self.url, intro = data["version"], data["url"], data["introduce"]
                    if not self.mode:
                            self.ui.overall.button_check.hide()
                            self.ui.overall.button_update.show()
                            self.ui.overall.button_update.setEnabled(True)
                    if self.version == data["version"]:
                        self.indicate(f"已为最新版本: {self.version}", 3)
                        return 0
                    else:
                        self.indicate(f"发现新版本: {self.version} -> {new_ver}")
                        self.indicate(f"可通过此链接进行手动更新:{self.url}")
                        self.indicate(intro, 3)
                        
                        return 1
                elif i < 2:
                    time.sleep(2)
                else:
                    raise ConnectionError("检查更新异常")
        except Exception:
            self.indicate("检查更新异常", 3)
            logger.error("检查更新异常:\n%s\n" % traceback.format_exc())
            return 0

    

    def load_add_update(self):
        self.indicate("开始更新,更新完成后将自动重启SGA")
        # noinspection PyBroadException
        try:
            _url = f"https://api.7585.net.cn/lanzou/api.php?url={self.url}"
            for i in range(3):
                response = requests.get(_url, timeout=10)
                if response.status_code == 200:
                    data = json.loads(response.text)
                elif i < 2:
                    time.sleep(2)
                else:
                    raise ConnectionError("直链获取异常")
        except Exception:
            self.indicate("直链获取异常", 3)
            logger.error("直链获取异常:\n%s\n" % traceback.format_exc())
            return 0
        # noinspection PyBroadException
        try:
            from urllib.request import urlretrieve
            import tempfile
            temp_path = tempfile.gettempdir()
            load_path = os.path.join(temp_path, data["name"])
            urlretrieve(data["down"], load_path)
            self.indicate("下载完成")
        except Exception:
            self.indicate("下载异常", 3)
            logger.error("下载异常:\n%s\n" % traceback.format_exc())
            return 0
        # noinspection PyBroadException
        try:
            from shutil import unpack_archive
            unpack_archive(load_path, temp_path)
        except Exception:
            self.indicate("解压异常", 3)
            logger.error("解压异常:\n%s\n" % traceback.format_exc())
            return 0
        # noinspection PyBroadException
        try:
            from shutil import copytree
            extract_folder = os.path.splitext(load_path)[0]
            cover_folder = env.workdir
            copytree(extract_folder, cover_folder, dirs_exist_ok=True)
        except Exception:
            self.indicate("替换异常", 3)
            logger.error("替换异常:\n%s\n" % traceback.format_exc())
            return 0
        # noinspection PyBroadException
        try:
            from shutil import rmtree
            os.remove(load_path)
            rmtree(extract_folder)
        except Exception:
            self.indicate("删除临时文件异常", 3)
            logger.error("删除临时文件异常:\n%s\n" % traceback.format_exc())
            return 0
        # 弹窗重启
        self.indicate("更新成功,进行重启", 3)
        if self.mode == 1:
            self.ui.overall.button_check.show()
            self.ui.overall.button_check.setEnabled(True)
            self.ui.overall.button_update.hide()
        cmd_run("start "" /d \"personal/bat\" restart.vbs")
        sys.exit(0)
        
            