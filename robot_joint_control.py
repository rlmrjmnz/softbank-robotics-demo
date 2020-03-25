# coding: utf-8

from __future__ import print_function
from builtins import input

import pybullet as p
from qibullet import SimulationManager
from qibullet import PepperVirtual
from qibullet import NaoVirtual
from qibullet import RomeoVirtual

import sys
from time import sleep

if __name__ == "__main__":
    simulation_manager = SimulationManager()

    rob = input("Which robot should be spawned? (pepper/nao/romeo): ")

    client = simulation_manager.launchSimulation(gui=True)

    if rob.lower() == "nao":
        robot = simulation_manager.spawnNao(client, spawn_ground_plane=True)
    elif rob.lower() == "pepper":
        robot = simulation_manager.spawnPepper(client, spawn_ground_plane=True)
    elif rob.lower() == "romeo":
        robot = simulation_manager.spawnRomeo(client, spawn_ground_plane=True)
    else:
        print("You have to specify a robot, pepper, nao or romeo.")
        simulation_manager.stopSimulation(client)
        sys.exit(1)

    sleep(1.0)
    joint_parameters = list()

    for name, joint in list(robot.joint_dict.items()):
        if "Finger" not in name and "Thumb" not in name:
            joint_parameters.append((
                p.addUserDebugParameter(
                    name,
                    joint.getLowerLimit(),
                    joint.getUpperLimit(),
                    robot.getAnglesPosition(name)),
                name))

    while True:
        for joint_parameter in joint_parameters:
            robot.setAngles(
                joint_parameter[1],
                p.readUserDebugParameter(joint_parameter[0]), 1.0)
