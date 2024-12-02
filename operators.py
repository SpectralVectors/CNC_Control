import serial
from bpy.types import Operator


def serial_command(command):
    props = context.scene.cnccontrolprops
    port = props.port
    rate = int(props.rate)
    connection = serial.Serial(port=port, baudrate=rate)
    connection.write(command.encode("utf-8"))


# Connect/Disconnect Machine
class ConnectMachine(Operator):
    """Tooltip"""

    bl_idname = "cnc.connect_machine"
    bl_label = "Connect Machine"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        port = props.port
        rate = int(props.rate)
        connection = serial.Serial(port=port, baudrate=rate)
        props.connected = True
        return {"FINISHED"}


class DisconnectMachine(Operator):
    """Tooltip"""

    bl_idname = "cnc.disconnect_machine"
    bl_label = "Disconnect Machine"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        port = props.port
        rate = int(props.rate)
        connection = serial.Serial(port=port, baudrate=rate)
        connection.close()
        props.connected = False
        return {"FINISHED"}


# X Axis +/-
class JogXPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_plus"
    bl_label = "Jog X+"

    def execute(self, context):
        serial_command("G0 X5")
        return {"FINISHED"}


class JogXMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_minus"
    bl_label = "Jog X-"

    def execute(self, context):
        serial_command("G0 X-5")
        return {"FINISHED"}


# Y Axis
class JogYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_y_plus"
    bl_label = "Jog Y+"

    def execute(self, context):
        serial_command("G0 Y5")
        return {"FINISHED"}


class JogYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_y_minus"
    bl_label = "Jog Y-"

    def execute(self, context):
        serial_command("G0 Y-5")
        return {"FINISHED"}


# X/Y Combined Axes +/-
class JogXYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_xy_plus"
    bl_label = "Jog XY+"

    def execute(self, context):
        serial_command("G0 X5 Y5")
        return {"FINISHED"}


class JogXYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_xy_minus"
    bl_label = "Jog XY-"

    def execute(self, context):
        serial_command("G0 X-5 Y-5")
        return {"FINISHED"}


class JogXPlusYMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_plus_y_minus"
    bl_label = "Jog X+Y-"

    def execute(self, context):
        serial_command("G0 X5 Y-5")
        return {"FINISHED"}


class JogXMinusYPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_x_minus_y_plus"
    bl_label = "Jog X-Y+"

    def execute(self, context):
        serial_command("G0 X-5 Y5")
        return {"FINISHED"}


# Z Axis +/-
class JogZPlus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_z_plus"
    bl_label = "Jog Z+"

    def execute(self, context):
        serial_command("G0 Z5")
        return {"FINISHED"}


class JogZMinus(Operator):
    """Tooltip"""

    bl_idname = "cnc.jog_z_minus"
    bl_label = "Jog Z-"

    def execute(self, context):
        serial_command("G0 Z-5")
        return {"FINISHED"}
