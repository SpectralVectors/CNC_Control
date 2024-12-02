import bpy

from .ui import CAMControlPanel
from .operators import (
    ConnectMachine,
    DisconnectMachine,
    JogXPlus,
    JogXMinus,
    JogYPlus,
    JogYMinus,
    JogXYPlus,
    JogXYMinus,
    JogXPlusYMinus,
    JogXMinusYPlus,
    JogZPlus,
    JogZMinus,
)
from .properties import CNCControlProperties

classes = [
    # .ui
    CAMControlPanel,
    # .operators
    ConnectMachine,
    DisconnectMachine,
    JogXPlus,
    JogXMinus,
    JogYPlus,
    JogYMinus,
    JogXYPlus,
    JogXYMinus,
    JogXPlusYMinus,
    JogXMinusYPlus,
    JogZPlus,
    JogZMinus,
    # .properties
    CNCControlProperties,
]


def register() -> None:
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.cnccontrolprops = bpy.props.PointerProperty(type=CNCControlProperties)


def unregister() -> None:
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
