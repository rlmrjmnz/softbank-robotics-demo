# coding: utf-8

from __future__ import print_function

import rospy

from qibullet import SimulationManager
from qibullet import PepperVirtual
from qibullet import PepperRosWrapper


def main(sim, client):
    robot = sim.spawnPepper(client, spawn_ground_plane=True)
    wrap = PepperRosWrapper()
    wrap.launchWrapper(robot, '/naoqi_driver')

    robot.subscribeCamera(PepperVirtual.ID_CAMERA_TOP)
    rospy.spin()

    wrap.stopWrapper()


if __name__ == "__main__":
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True,
                                                 use_shared_memory=False)

    main(simulation_manager, client)

    simulation_manager.stopSimulation(client)
