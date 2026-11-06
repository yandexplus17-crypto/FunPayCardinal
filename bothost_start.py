import os
import runpy
from pathlib import Path

from first_setup import create_config_obj, default_config, hash_password

path = Path("configs/_main.cfg")

if not path.exists():
    config = create_config_obj(default_config)
    config["FunPay"]["golden_key"] = os.environ["FUNPAY_GOLDEN_KEY"].strip()
    config["Telegram"]["enabled"] = "1"
    config["Telegram"]["token"] = os.environ["BOT_TOKEN"].strip()
    config["Telegram"]["secretKeyHash"] = hash_password(
        os.environ["CARDINAL_PASSWORD"]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        config.write(file)

runpy.run_path("main.py", run_name="__main__")
