# NAOqi - qiBullet Integration Demos
This directory contains demos using NAOqi and qiBullet together. To run these demos is needed the IP and port of the robot platform to test.

These demos can be run using the virtual robot shown in Choregraphe.

## Demos
* **pepper_shadowing**: Simulated Pepper mimics the movement of the real robot. Can be used with the virtual robot shown in Choregraphe.

## Requirements
* Choregraphe ver 2.5.10 or later
* Python 2
* NAOqi Python SDK ver 2.5
* qiBullet for Python 2

## Running the demos
If the demo is run using the virtual robot

```bash
python demo_name.py --port ####
```

If the demo is run against a real robot

```bash
python demo_name.py --ip www.xxx.yyy.zzz --port ####
```
