import serial
import bpy
import time
from bpy.types import Operator


def serial_command(context, command):
    command = f"{command} \n".encode("utf-8")
    context.scene.connection.write(command)


# Connect/Disconnect Machine
class ConnectMachine(Operator):
    """Tooltip"""

    bl_idname = "cnc.connect_machine"
    bl_label = "Connect Machine"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        port = props.port
        rate = int(props.rate)
        bpy.types.Scene.connection = serial.Serial(port=port, baudrate=rate)
        context.scene.connection.write("\r\n\r\n".encode("utf-8"))
        time.sleep(2)
        context.scene.connection.flushInput()
        props.connected = True
        return {"FINISHED"}


class DisconnectMachine(Operator):
    """Tooltip"""

    bl_idname = "cnc.disconnect_machine"
    bl_label = "Disconnect Machine"

    def execute(self, context):
        context.scene.connection.close()
        props = context.scene.cnccontrolprops
        props.connected = False
        return {"FINISHED"}


# X Axis +/-
class JogXPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_plus"
    bl_label = "Jog X+"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X{step}")
        return {"FINISHED"}


class JogXMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_minus"
    bl_label = "Jog X-"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X-{step}")
        return {"FINISHED"}


# Y Axis
class JogYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_y_plus"
    bl_label = "Jog Y+"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 Y{step}")
        return {"FINISHED"}


class JogYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_y_minus"
    bl_label = "Jog Y-"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 Y-{step}")
        return {"FINISHED"}


# X/Y Combined Axes +/-
class JogXYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_xy_plus"
    bl_label = "Jog XY+"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X{step} Y{step}")
        return {"FINISHED"}


class JogXYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_xy_minus"
    bl_label = "Jog XY-"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X-{step} Y-{step}")
        return {"FINISHED"}


class JogXPlusYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_plus_y_minus"
    bl_label = "Jog X+Y-"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X{step} Y-{step}")
        return {"FINISHED"}


class JogXMinusYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_minus_y_plus"
    bl_label = "Jog X-Y+"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.xy_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 X-{step} Y{step}")
        return {"FINISHED"}


# Z Axis +/-
class JogZPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_z_plus"
    bl_label = "Jog Z+"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.z_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 Z{step}")
        return {"FINISHED"}


class JogZMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_z_minus"
    bl_label = "Jog Z-"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        step = props.z_step
        unit = props.unit
        serial_command(context, f"{unit}G91 G0 Z-{step}")
        return {"FINISHED"}


# Move to 0 - XYZ
class MoveToX0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_x_zero"
    bl_label = "Move to X Zero"

    def execute(self, context):
        serial_command(context, "G90 G0 X0")
        return {"FINISHED"}


class MoveToY0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_y_zero"
    bl_label = "Move to Y Zero"

    def execute(self, context):
        serial_command(context, "G90 G0 Y0")
        return {"FINISHED"}


class MoveToZ0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_z_zero"
    bl_label = "Move to Z Zero"

    def execute(self, context):
        serial_command(context, "G90 G0 Z0")
        return {"FINISHED"}


# Set current position to 0 - XYZ
class SetCurrentXTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_x_to_zero"
    bl_label = "Set current X position to X Zero"

    def execute(self, context):
        serial_command(context, "G10 L20 P1 X0")
        return {"FINISHED"}


class SetCurrentYTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_y_to_zero"
    bl_label = "Set current Y position to Y Zero"

    def execute(self, context):
        serial_command(context, "G10 L20 P1 Y0")
        return {"FINISHED"}


class SetCurrentZTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_z_to_zero"
    bl_label = "Set current Z position to Z Zero"

    def execute(self, context):
        serial_command(context, "G10 L20 P1 Z0")
        return {"FINISHED"}
