from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class DumbRegistryConfig(BaseModel):
    name: str = "localhost"
    url: str = "http://localhost:5000"
    version: str = "v2"


class DumbConfig(BaseModel):
    registry: DumbRegistryConfig = Field(default_factory=DumbRegistryConfig)


def load_config():
    config_path = Path("/config/dumb.yml")
    config = {}
    if config_path.exists():
        with config_path.open() as fp:
            config = yaml.safe_load(fp)
    return DumbConfig(**config)


def get_config(reload=True):
    global global_config
    if not global_config or reload:
        global_config = load_config()
    return global_config


global_config = load_config()
