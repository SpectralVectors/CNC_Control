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
    MoveToX0,
    MoveToY0,
    MoveToZ0,
    MoveToXYZ0,
    SetCurrentXTo0,
    SetCurrentYTo0,
    SetCurrentZTo0,
    SetCurrentXYZTo0,
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
    MoveToX0,
    MoveToY0,
    MoveToZ0,
    MoveToXYZ0,
    SetCurrentXTo0,
    SetCurrentYTo0,
    SetCurrentZTo0,
    SetCurrentXYZTo0,
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
