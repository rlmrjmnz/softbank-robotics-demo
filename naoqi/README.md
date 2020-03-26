# NAOqi - qi API Demos
This directory contains demos for NAOqi and qi API. To run these demos is needed the IP and port of the robot platform to test.

These demos can be run using the virtual robot shown in Choregraphe

## Demos
* naoqi_basic: Uses Posture, Motion & TextToSpeech modules. Can be used with all Softbank robots.

## Requirements
* Choregraphe ver 2.5.10 or later
* Python 2
* NAOqi Python SDK ver 2.5

## Running the demos
If the demo is run using the virtual robot

```bash
python demo_name.py --port ####
```

If the demo is run against a real robot

```bash
python demo_name.py --ip www.xxx.yyy.zzz --port ####
```
