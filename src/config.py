import toml
import shutil
import os.path


def load_config(config_path="./config.toml"):
    if not os.path.exists(config_path):
        shutil.copyfile("config.toml.example", "config.toml")
        raise RuntimeError(
            f"Config file {config_path} does not exist. A default file has been generated.")

    with open(config_path, "r") as config:
        return toml.loads(config.read())
