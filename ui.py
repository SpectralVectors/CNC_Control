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
            main_column = position_panel.column(align=True)
            main_column.scale_y = 2

            box = main_column.box()
            column = box.column(align=True)
            row = column.row(align=True)
            # row.alignment = "CENTER"
            row.label(text="", icon="SEQUENCE_COLOR_01")
            row.label(text=str(props.x_position), icon="EVENT_X")
            row = column.row(align=True)
            # row.alignment = "CENTER"
            row.label(text="", icon="SEQUENCE_COLOR_04")
            row.label(text=str(props.y_position), icon="EVENT_Y")
            row = column.row(align=True)
            # row.alignment = "CENTER"
            row.label(text="", icon="SEQUENCE_COLOR_05")
            row.label(text=str(props.z_position), icon="EVENT_Z")

            row = main_column.row(align=True)
            row.label(text="Move To:")
            row.operator("cnc.move_to_x_zero", text="X0")
            row.operator("cnc.move_to_y_zero", text="Y0")
            row.operator("cnc.move_to_z_zero", text="Z0")

            row = main_column.row(align=True)
            row.label(text="Set Current:")
            row.operator("cnc.current_x_to_zero", text="X=0")
            row.operator("cnc.current_y_to_zero", text="Y=0")
            row.operator("cnc.current_z_to_zero", text="Z=0")

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
            column.label(text="Step Size")
            column.use_property_split = True
            column.use_property_decorate = False
            column.prop(props, "xy_step", text="X/Y")
            column.prop(props, "z_step", text="Z")
