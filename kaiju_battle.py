# python3
# coding: utf-8

import cv2

import pybullet
import pybullet_data

from qibullet import SimulationManager
from qibullet import NaoVirtual
from qibullet import PepperVirtual
from qibullet import RomeoVirtual

def main():
    sim_manager = SimulationManager()
    client = sim_manager.launchSimulation(gui=True)
    # client_direct_1 = sim_manager.launchSimulation(gui=False)

    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

    pybullet.loadURDF('plane.urdf')

    duck = pybullet.loadURDF(
        'duck_vhacd.urdf',
        basePosition = [0, 0, 0],
        globalScaling = 5.0,
        physicsClientId = client)
    
    # r2d2 = pybullet.loadURDF(
    #     "r2d2.urdf",
    #     basePosition = [-2, 0, 0],
    #     globalScaling = 5.0,
    #     physicsClientId = client_direct_1)
  
    nao = sim_manager.spawnNao(
        client, 
        translation=[2, 0, 0],
        quaternion=pybullet.getQuaternionFromEuler([0, 0, 3]))
    pepper = sim_manager.spawnPepper(
        client, 
        translation=[0, -2, 0],
        quaternion=pybullet.getQuaternionFromEuler([0, 0, 1.5]))
    romeo = sim_manager.spawnRomeo(
        client, 
        translation=[0, 2, 0],
        quaternion=pybullet.getQuaternionFromEuler([0, 0, -1.5]))

    nao.goToPosture('StandInit', 1)
    pepper.goToPosture('StandInit', 1)
    romeo.goToPosture('StandInit', 1)

    nao.subscribeCamera(NaoVirtual.ID_CAMERA_TOP)
    pepper.subscribeCamera(PepperVirtual.ID_CAMERA_TOP)
    romeo.subscribeCamera(RomeoVirtual.ID_CAMERA_DEPTH)

    nao.setAngles('HeadPitch', 0.25, 1)    

    while True:
        nao_cam = nao.getCameraFrame()
        cv2.imshow('Nao Cam', nao_cam)
        pepper_cam = pepper.getCameraFrame()
        cv2.imshow('Pepper Cam', pepper_cam)
        romeo_cam = romeo.getCameraFrame()
        cv2.imshow('Romeo Cam', romeo_cam)
        cv2.waitKey(1)
        pass

if __name__ == "__main__":
    main()
