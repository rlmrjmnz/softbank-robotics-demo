# coding: utf-8

import cv2

from qibullet import SimulationManager
from qibullet import PepperVirtual

import time


def main():
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True)
    pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=True)

    pepper.goToPosture("Crouch", 0.6)
    time.sleep(1)
    pepper.goToPosture("Stand", 0.6)
    time.sleep(1)
    pepper.goToPosture("StandZero", 0.6)
    time.sleep(1)
    pepper.subscribeCamera(PepperVirtual.ID_CAMERA_BOTTOM)

    while True:
        img = pepper.getCameraFrame()
        cv2.imshow("bottom camera", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
