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
