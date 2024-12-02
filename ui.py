from bpy.types import Panel


class CAMControlPanel(Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "CNC Machine Control"
    bl_idname = "OBJECT_PT_cam_control"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "gControl"

    def draw(self, context):
        layout = self.layout

        props = context.scene.cnccontrolprops

        # Connection Panel
        header, connection_panel = layout.panel("connection", default_closed=False)
        header.label(text="Connection", icon="LINKED")
        if connection_panel:
            main_column = connection_panel.column(align=True)
            box = main_column.box()
            sub_box = box.box()
            row = sub_box.row()
            row.scale_y = 2
            connected = props.connected
            text = "Status: Connected" if connected else "Status: No Connection"
            icon = "SEQUENCE_COLOR_01" if not connected else "SEQUENCE_COLOR_04"
            row.label(text=text, icon=icon)
            icon = "UNLINKED" if not props.connected else "LINKED"
            row.label(text="", icon=icon)
            column = box.column(align=True)
            column.prop(props, "port")
            column.prop(props, "rate")
            operator = "cnc.connect_machine" if not props.connected else "cnc.disconnect_machine"
            row = main_column.row()
            row.scale_y = 2
            row.operator(operator=operator, icon="PLUGIN")

        # Gcode Panel
        header, gcode_panel = layout.panel("gcode", default_closed=False)
        header.label(text="Gcode", icon="FILEBROWSER")
        if gcode_panel:
            box = gcode_panel.box()
            box.prop(props, "jobfile")
            row = box.row(align=True)
            row.scale_x = row.scale_y = 2
            row.operator("render.render", text="Run", icon="PLAY")
            row.operator("render.render", text="Pause", icon="PAUSE")
            row.operator("render.render", text="Stop", icon="SNAP_FACE")

        # Position Panel
        header, position_panel = layout.panel("position", default_closed=False)
        header.label(text="Position", icon="ORIENTATION_LOCAL")
        if position_panel:
            column = position_panel.column(align=True)
            box = column.box()
            # box.alignment = "RIGHT"
            box.scale_x = box.scale_y = 2
            box.label(text="1.2321", icon="EVENT_X")
            box = column.box()
            # box.alignment = "RIGHT"
            box.scale_x = box.scale_y = 2
            box.label(text="1.0456", icon="EVENT_Y")
            box = column.box()
            # box.alignment = "RIGHT"
            box.scale_x = box.scale_y = 2
            box.label(text="1.7981", icon="EVENT_Z")
            row = column.row(align=True)
            row.scale_x = row.scale_y = 2
            row.label(text="Move To:")
            row.operator("render.render", text="X0")
            row.operator("render.render", text="Y0")
            row.operator("render.render", text="Z0")
            row = column.row(align=True)
            row.scale_x = row.scale_y = 2
            row.label(text="Set Current:")
            row.operator("render.render", text="X=0")
            row.operator("render.render", text="Y=0")
            row.operator("render.render", text="Z=0")

        # Jog Control Panel
        header, jog_panel = layout.panel("jog", default_closed=False)
        header.label(text="Jog Control", icon="DECORATE_DRIVER")
        if jog_panel:
            column = jog_panel.column(align=True)
            grid = column.grid_flow(
                columns=3,
                even_columns=True,
                even_rows=True,
                align=True,
            )
            grid.scale_x = grid.scale_y = 2

            grid.operator("cnc.jog_x_minus_y_plus", text="↖")
            grid.operator("cnc.jog_x_minus", text="← X-")
            grid.operator("cnc.jog_xy_minus", text="↙")

            grid.operator("cnc.jog_y_plus", text="↑ Y+")
            grid.operator("render.render", text="", icon="HOME")
            grid.operator("cnc.jog_y_minus", text="↓ Y-")

            grid.operator("cnc.jog_xy_plus", text="↗")
            grid.operator("cnc.jog_x_plus", text="X+ →")
            grid.operator("cnc.jog_x_plus_y_minus", text="↘")

            row = jog_panel.row()
            row.scale_x = row.scale_y = 2
            column = row.column(align=True)
            column.operator("cnc.jog_z_plus", text="Z+", icon="EXPORT")
            column.operator("cnc.jog_z_minus", text="Z-", icon="IMPORT")
            column = row.column(align=True)
            column.operator("render.render", text="A+", icon="LOOP_BACK")
            column.operator("render.render", text="A-", icon="LOOP_FORWARDS")
            column = jog_panel.column(align=True)
            box = column.box()
            column = box.column(align=True)
            column.label(text="Jog Speed: Fast")
            column.label(text="X / Y: 10")
            column.label(text="Z: 5")
            column.label(text="ABC: 3")
