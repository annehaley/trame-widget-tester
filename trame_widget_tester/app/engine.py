from colormapper import engine as colormapper_engine
from filebrowser import engine as filebrowser_engine

from .vtk_pipeline import VtkPipeline
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DATASET_PATH = Path("data/skull.vti").absolute()


class VtkPipelineEngine:
    def initialize(self, server):
        self.vtk_pipeline = VtkPipeline(DATASET_PATH)
        state, ctrl = server.state, server.controller
        state.trame__title = "View skull.vti"
        self.state = state
        self.ctrl = ctrl

        @ctrl.set("get_render_window")
        def get_render_window():
            return self.vtk_pipeline.render_window


class WidgetTesterEngine(VtkPipelineEngine):
    def initialize(self, server):
        super().initialize(server)
        colormapper_engine.initialize(server, self.state, self.ctrl, self.vtk_pipeline)
        filebrowser_engine.initialize(server, self.state, self.ctrl, self.vtk_pipeline)


def initialize(server):
    WidgetTesterEngine().initialize(server)
