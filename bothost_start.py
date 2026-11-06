import os
import sys
from pathlib import Path

from first_setup import create_config_obj, default_config, hash_password

project_dir = Path(__file__).resolve().parent
config_path = project_dir / "configs" / "_main.cfg"

if not config_path.is_file() or config_path.stat().st_size == 0:
    config = create_config_obj(default_config)
    config["FunPay"]["golden_key"] = os.environ["FUNPAY_GOLDEN_KEY"].strip()
    config["Telegram"]["enabled"] = "1"
    config["Telegram"]["token"] = os.environ["BOT_TOKEN"].strip()
    config["Telegram"]["secretKeyHash"] = hash_password(
        os.environ["CARDINAL_PASSWORD"]
    )

    config_path.parent.mkdir(parents=True, exist_ok=True)
    with config_path.open("w", encoding="utf-8") as file:
        config.write(file)

os.chdir(project_dir)
os.execv(sys.executable, [sys.executable, str(project_dir / "main.py")])
