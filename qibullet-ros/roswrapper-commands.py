# coding: utf-8

from __future__ import print_function
from builtins import input

import rospy

from qibullet import SimulationManager
from qibullet import PepperRosWrapper

from time import sleep


def main(sim, client):
    robot = sim.spawnPepper(client, spawn_ground_plane=True)
    wrap = PepperRosWrapper()
    wrap.launchWrapper(robot, '/naoqi_driver')

    input('Wait for a key')

    sleep(2)
    robot.goToPosture('StandInit', 1.0)
    sleep(2)
    robot.goToPosture('Crouch', 1.0)
    sleep(2)
    robot.goToPosture('StandInit', 1.0)

    rospy.spin()
    wrap.stopWrapper()


if __name__ == "__main__":
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=False,
                                                 use_shared_memory=True)

    main(simulation_manager, client)

    simulation_manager.stopSimulation(client)
