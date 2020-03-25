# python 2
# coding: utf-8

"""Example: Use goToPosture Method"""

from __future__ import print_function

import qi

import argparse
import sys
from time import sleep


def main(session):
    """
    This example uses the goToPosture method.
    """
    # Get the service ALRobotPosture.
    posture_service = session.service("ALRobotPosture")

    # Get the service ALTextToSpeech.
    text_service = session.service("ALTextToSpeech")

    # Get the service ALMotion.
    motion_service = session.service("ALMotion")

    text_service.say("Hi! I'm Peeper")
    sleep(2)
    text_service.say("I show you my postures")
    sleep(2)

    posture_service.goToPosture("StandInit", 1.0)
    posture_service.goToPosture("StandZero", 1.0)
    posture_service.goToPosture("Crouch", 1.0)
    posture_service.goToPosture("StandInit", 1.0)

    text_service.say("Thank you!")

    head_pos = motion_service.getAngles("HeadPitch", True)
    motion_service.setAngles("HeadPitch", 0.25, 0.5)
    sleep(2)
    motion_service.setAngles("HeadPitch", head_pos, 0.5)
    sleep(2)

    print(posture_service.getPostureFamily())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
