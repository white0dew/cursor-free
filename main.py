import os
import json
import uuid
from datetime import date
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    if not is_admin():
        print("请以管理员权限运行此脚本！")
        input("按Enter键退出...")
        sys.exit()

    try:
        # 获取用户配置文件路径
        user_profile = os.environ['USERPROFILE']
        config_path = os.path.join(user_profile, "AppData", "Roaming", "Cursor", "User", "globalStorage")

        # 生成新的设备ID
        device_id = str(uuid.uuid4())

        # 创建基础JSON对象
        json_object = {
            "telemetry.devDeviceId": device_id,
            "telemetry.deviceId": device_id,
            "telemetry.firstWebInstall": date.today().isoformat(),
            "telemetry.webInstallId": device_id,
            "update.lastCheckDate": date.today().isoformat(),
            "update.updateChannel": "stable",
            "workbench.hasSeenOnboarding": True,
            "workbench.theme": "Monokai Pro",
            "workbench.colorTheme": "Monokai Pro",
            "telemetry.machineId": device_id,
            "settingsVersion": 2,
            "sync.machineId": device_id
        }

        # 确保目录存在
        os.makedirs(config_path, exist_ok=True)

        # 将JSON对象保存到文件
        storage_file = os.path.join(config_path, "storage.json")
        with open(storage_file, 'w', encoding='utf-8') as f:
            json.dump(json_object, f, indent=2)

        print(f"已重置 storage.json: {storage_file}")
        print("重置完成！")
        print("请重新启动 Cursor 以应用更改。")

    except Exception as e:
        print(f"发生错误: {e}")

    input("按Enter键退出...")

if __name__ == "__main__":
    main()
