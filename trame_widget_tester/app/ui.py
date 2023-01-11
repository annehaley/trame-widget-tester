from trame.ui.vuetify import SinglePageWithDrawerLayout
from trame.widgets import vuetify
from trame.widgets import vtk
from trame.app import get_server

from colormapper.widget import ColormapEditor
from filebrowser.widget import FileBrowser

server = get_server()
state, ctrl = server.state, server.controller


def initialize(server):
    ctrl = server.controller

    with SinglePageWithDrawerLayout(server) as layout:
        layout.title.set_text("Trame Widget Tester")

        with layout.toolbar:
            vuetify.VSwitch(
                v_model="$vuetify.theme.dark",
                hide_details=True,
                dense=True,
            )

        with layout.drawer as drawer:
            drawer.width = 450
            with vuetify.VContainer(classes="pa-5"):
                ColormapEditor(
                    histogram_data=("histogram_data",),
                    colors=("colormap_points",),
                    opacities=("opacity_points",),
                    update_colors="colormap_points = $event",
                    update_opacities="opacity_points = $event",
                )
                FileBrowser(
                    attribute=("attribute",)
                )

        # Main content
        with layout.content:
            with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                html_view = vtk.VtkRemoteView(ctrl.get_render_window())
                ctrl.on_server_ready.add(html_view.update)
                ctrl.view_update = html_view.update

        # Footer
        layout.footer.hide()
