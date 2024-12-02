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
        props.x_position += step
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
        props.x_position -= step
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
        props.y_position += step
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
        props.y_position -= step
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
        props.x_position += step
        props.y_position += step
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
        props.x_position -= step
        props.y_position -= step
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
        props.x_position += step
        props.y_position -= step
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
        props.x_position -= step
        props.y_position += step
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
        props.z_position += step
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
        props.z_position -= step
        return {"FINISHED"}


# Move to 0 - XYZ
class MoveToX0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_x_zero"
    bl_label = "Move to X Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G90 G0 X0")
        props.x_position = 0
        return {"FINISHED"}


class MoveToY0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_y_zero"
    bl_label = "Move to Y Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G90 G0 Y0")
        props.y_position = 0
        return {"FINISHED"}


class MoveToZ0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_z_zero"
    bl_label = "Move to Z Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G90 G0 Z0")
        props.z_position = 0
        return {"FINISHED"}


class MoveToXYZ0(Operator):
    """Tooltip"""

    bl_idname = "cnc.move_to_xyz_zero"
    bl_label = "Move to XYZ Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G90 G0 X0 Y0 Z0")
        props.x_position = props.y_position = props.z_position = 0
        return {"FINISHED"}


# Set current position to 0 - XYZ
class SetCurrentXTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_x_to_zero"
    bl_label = "Set current X position to X Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G10 L20 P1 X0")
        props.x_position = 0
        return {"FINISHED"}


class SetCurrentYTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_y_to_zero"
    bl_label = "Set current Y position to Y Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G10 L20 P1 Y0")
        props.y_position = 0
        return {"FINISHED"}


class SetCurrentZTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_z_to_zero"
    bl_label = "Set current Z position to Z Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G10 L20 P1 Z0")
        props.z_position = 0
        return {"FINISHED"}


class SetCurrentXYZTo0(Operator):
    """Tooltip"""

    bl_idname = "cnc.current_xyz_to_zero"
    bl_label = "Set current XYZ position to Z Zero"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        serial_command(context, "G10 L20 P1 X0 Y0 Z0")
        props.x_position = props.y_position = props.z_position = 0
        return {"FINISHED"}


class RunJobFile(Operator):
    """Tooltip"""

    bl_idname = "cnc.run_job_file"
    bl_label = "Run the currently loaded gcode file"

    def execute(self, context):
        props = context.scene.cnccontrolprops
        running_job = props.running_job
        if not running_job:
            jobfile = open(props.jobfile, "r")
            for line in jobfile:
                serial_command(context, line)
                grbl_out = context.scene.connection.readline()
                print(grbl_out)
        else:
            serial_command(context, "~")

        return {"FINISHED"}


class PauseJobFile(Operator):
    """Tooltip"""

    bl_idname = "cnc.pause_job_file"
    bl_label = "Pause the currently running job"

    def execute(self, context):
        serial_command(context, "!")

        return {"FINISHED"}


class StopJobFile(Operator):
    """Tooltip"""

    bl_idname = "cnc.stop_job_file"
    bl_label = "Stop the currently running job"

    def execute(self, context):
        serial_command(context, "\x18")

        return {"FINISHED"}
