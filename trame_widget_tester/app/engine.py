from .vtk_pipeline import VtkPipeline
from pathlib import Path
import logging

from .filebrowser_functions import (
    get_applicable_file_types,
    get_dir_contents,
    save_file,
    open_file,
)
from .default_states import (
    DEFAULT_COLOR_MAP,
    DEFAULT_OPACITY_MAP,
    DEFAULT_FILEBROWSER_STATE,
)

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


class ColorMapperEngine(VtkPipelineEngine):
    def initialize(self, server, **kwargs):
        super().initialize(server)
        state, ctrl = server.state, server.controller
        state.colormap_points = DEFAULT_COLOR_MAP
        state.opacity_points = DEFAULT_OPACITY_MAP
        state.histogram_data = self.vtk_pipeline.get_histogram_data(buckets=10)

        @state.change("colormap_points")
        def update_colors(colormap_points, **kwargs):
            self.vtk_pipeline.update_colors(colormap_points)
            ctrl.view_update()

        @state.change("opacity_points")
        def update_opacity(opacity_points, **kwargs):
            self.vtk_pipeline.update_opacity(opacity_points)
            ctrl.view_update()

        @ctrl.set("reset_colormap_points")
        def reset_colormap_points(self):
            self._server.state.colormap_points = DEFAULT_COLOR_MAP


class FileBrowserEngine():
    def initialize(self, server):
        state, ctrl = server.state, server.controller
        for key, value in DEFAULT_FILEBROWSER_STATE.items():
            setattr(state, key, value)
        state.current_local_dir_contents = get_dir_contents(state.current_local_dir)
        state.current_remote_dir_contents = get_dir_contents(state.current_remote_dir)
        state.file_types = get_applicable_file_types()
        ctrl.save_file = save_file
        ctrl.open_file = open_file

        @state.change('current_local_dir')
        def update_local_dir(current_local_dir, **kwargs):
            state.current_local_dir_contents = get_dir_contents(current_local_dir)

        @state.change('current_remote_dir')
        def update_remote_dir(current_remote_dir, **kwargs):
            state.current_remote_dir_contents = get_dir_contents(current_remote_dir)


class WidgetTesterEngine():
    def initialize(self, server):
        ColorMapperEngine().initialize(server)
        FileBrowserEngine().initialize(server)


def initialize(server):
    WidgetTesterEngine().initialize(server)
