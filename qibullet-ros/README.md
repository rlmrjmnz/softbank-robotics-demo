# qiBullet - ROS Demos
This directory contains demos for qiBullet ROSWrapper and its connection to ROS.

Each directory contains the files related to the specific demo.

## Demos
* **roswrapper-basic**: Launch a GUI simulation with a Pepper and in RViz show its camera.
* **roswrapper-postures**: Launch a Direct simulation with a Pepper and in RViz show its movements.

## Requirements
* Python 2
* qiBullet
* ROS Melodic or Kinetic

## Running the demos
To run the demos follow the next instructions for each demo

* Run roscore
```bash
source /opt/ros/version/setup.bash
roscore
```
* In another terminal, run the qiBullet simulation
```bash
source /opt/ros/version/setup.bash
cd /path/to/example-directory
python example.py
```
* In another terminal, run RViz with the example configuration
```bash
source /opt/ros/version/setup.bash
cd /path/to/example-directory
rosrun rviz rviz -d example.rviz
```
