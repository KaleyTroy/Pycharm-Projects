from random import *
from icecream import ic

def ra(*args):
    print("shit")
    if len(args) == 1: return args[0]
    if len(args) == 2: return randint(args[0], args[1])
    return randint(args[0], args[1]) * choice([1, -1])

style = {
    "null":{
        "hori_drift":ra(0, 0),  # (Horizontal Drift)
        "vert_drift":ra(0, 0),  # (Vertical Drift)
        "radius_0":ra(0, 0),  # (Outer Cycle Radius)
        "rotation_0":ra(0, 0),  # (Number of Outer Cycles)
        "radius_1":ra(0, 0),  # (Inner Cycle Radius)
        "rotation_1":ra(0, 0),  # (Number of Inner Cycles)
        "hole_size":ra(0, 0),  # (Size of the inner hole)
        "growth":ra(0, 0),  # (Rate of Inner Cycle Size Change)
        },

    "control": {
        "hori_drift": ra(0, 0),  # (Horizontal Drift)
        "vert_drift": ra(0, 0),  # (Vertical Drift)
        "radius_0": ra(0, 0),  # (Outer Cycle Radius)
        "rotation_0": ra(3),  # (Number of Outer Cycles)
        "radius_1": ra(50, 300),  # (Inner Cycle Radius)
        "rotation_1": ra(16, 32),  # (Number of Inner Cycles)
        "hole_size": ra(100),  # (Number of Inner Cycles)
        "radius_2": ra(50, 200),  # (Size of the Circles)
        "growth": ra(50),  # (Rate of Inner Cycle Size Change)
    },
    "small_control": {
        "hori_drift": ra(-0),  # (Horizontal Drift)
        "vert_drift": ra(0, 0),  # (Vertical Drift)
        "radius_0": ra(0),  # (Outer Cycle Radius)
        "rotation_0": ra(3, 6),  # (Number of Outer Cycles)
        "radius_1": ra(50),  # (Inner Cycle Radius)
        "rotation_1": ra(12),  # (Number of Inner Cycles)
        "hole_size": ra(3),  # (Size of the inner hole)
        "growth": ra(-20),  # (Rate of Inner Cycle Size Change)
    },

    "mandela_plain": {
        "hori_drift": ra(0, 0),  # (Horizontal Drift)
        "vert_drift": ra(0, 0),  # (Vertical Drift)
        "radius_0": ra(0, 0),  # (Outer Cycle Radius)
        "rotation_0": ra(1, 1),  # (Number of Outer Cycles)
        "radius_1": ra(50, 300),  # (Inner Cycle Radius)
        "rotation_1": ra(16, 32),  # (Number of Inner Cycles)
        "hole_size": ra(1, 100),  # (Number of Inner Cycles)
        "radius_2": ra(50, 300),  # (Size of the Circles)
        "growth": ra(0, 0),  # (Rate of Inner Cycle Size Change)
    },
    "hypersphere": {
        "hori_drift": ra(-150, 150),  # (Horizontal Drift)
        "vert_drift": ra(-150, 150),  # (Vertical Drift)
        "radius_0": ra(0),  # (Outer Cycle Radius)
        "rotation_0": ra(5, 10),  # (Number of Outer Cycles)
        "radius_1": ra(5, 150),  # (Inner Cycle Radius)
        "rotation_1": ra(3, 30),  # (Number of Inner Cycles)
        "hole_size": ra(10, 50),  # (Size of the inner hole)
        "growth": ra(0, 100),  # (Rate of Inner Cycle Size Change)
    },
}
