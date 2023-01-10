from colormapper import engine as colormapper_engine

from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DATASET_PATH = Path("data/skull.vti").absolute()


def initialize(server):
    colormapper_engine.initialize(server, dataset_path=DATASET_PATH)
