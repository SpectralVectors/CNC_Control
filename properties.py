from bpy_types import PropertyGroup
from bpy.props import StringProperty, IntProperty, BoolProperty, FloatProperty


class CNCControlProperties(PropertyGroup):

    port: StringProperty(
        name="Port",
        default="COM3",
        description="The port used for serial communication, often: Win: COM4, Linux: /dev/ttyACM0, Mac: /dev/tty.usbmodem...",
    )

    rate: StringProperty(
        name="Rate",
        default="115200",
        description="The rate at which comms are sent over the serial connection",
    )

    jobfile: StringProperty(
        name="Job File",
        default="",
        description="The gcode file for the job to be cut",
        subtype="FILE_PATH",
    )

    connected: BoolProperty(
        name="Connection Status",
        default=False,
        description="If Blender is connected to a CNC machine",
    )

    running_job: BoolProperty(
        name="Job Status",
        default=False,
        description="If a job is currently running from a gcode file",
    )

    xy_step: FloatProperty(
        name="X/Y Step Size",
        default=5,
        description="Length of the smallest movement along the X and Y axes",
    )

    z_step: FloatProperty(
        name="Z Step Size",
        default=1,
        description="Length of the smallest movement along the Z axis",
    )

    unit: StringProperty(
        name="Unit Type",
        default="G21",
        description="Metric or Imperial - Millimeter or Inch",
    )

    x_position: FloatProperty(
        name="X Position",
        default=0,
        description="Current position of the spindle along the X axis",
    )

    y_position: FloatProperty(
        name="Y Position",
        default=0,
        description="Current position of the spindle along the Y axis",
    )

    z_position: FloatProperty(
        name="Z Position",
        default=0,
        description="Current position of the spindle along the Z axis",
    )
