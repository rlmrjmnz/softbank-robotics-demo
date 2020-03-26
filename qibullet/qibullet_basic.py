# coding: utf-8

from __future__ import print_function

from qibullet import SimulationManager
from qibullet import PepperVirtual

from time import sleep


def main(sim, client):
    robot = sim.spawnPepper(client, spawn_ground_plane=True)

    print("Hi! I'm Peeper")
    sleep(2)
    print("I show you my postures")
    sleep(2)

    robot.goToPosture("StandInit", 1.0)
    robot.goToPosture("StandZero", 1.0)
    robot.goToPosture("Crouch", 1.0)
    robot.goToPosture("StandInit", 1.0)

    print("Thank you!")

    head_pos = robot.getAnglesPosition("HeadPitch")
    robot.setAngles("HeadPitch", 0.25, 0.5)
    sleep(2)
    robot.setAngles("HeadPitch", head_pos, 0.5)

    while True:
        pass


if __name__ == "__main__":
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)

    main(simulation_manager, client)
