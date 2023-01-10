from colormapper import engine as widget_engine

from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DATASET_PATH = Path("data/skull.vti").absolute()


def initialize(server):
    widget_engine.initialize(server, DATASET_PATH)
