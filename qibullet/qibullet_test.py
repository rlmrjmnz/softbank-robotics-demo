# coding: utf-8

from qibullet import SimulationManager

if __name__ == "__main__":
    simulation_manager = SimulationManager()

    # Launch a simulation instances, with using a graphical interface.
    # Please note that only one graphical interface can be launched at a time
    client_id = simulation_manager.launchSimulation(gui=True)

    # Selection of the robot type to spawn (True : Pepper, False : NAO)
    pepper_robot = True

    if pepper_robot:
        # Spawning a virtual Pepper robot, at the origin of the WORLD frame, and a
        # ground plane
        pepper = simulation_manager.spawnPepper(
            client_id,
            translation=[0, 0, 0],
            quaternion=[0, 0, 0, 1],
            spawn_ground_plane=True)
    else:
        # Or a NAO robot, at a default position
        nao = simulation_manager.spawnNao(
            client_id,
            spawn_ground_plane=True)
