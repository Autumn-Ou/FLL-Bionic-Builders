from spike import PrimeHub, MotorPair, Motor
from math import pi, radians

hub = PrimeHub()

# turn function for degrees
def turn_degrees(drive_wheel_spread, degrees):
    output = (drive_wheel_spread * pi / radians(degrees))
    return output

# estimated wheel base for turn function, measure the bot
wheel_base = 8.1

# creates drive motor pair
drive_motors = MotorPair('A', 'B')

# creates arm motor
arm_motor = Motor('C')

# raises arm with plow
arm_motor.run_for_degrees(-45)

# drives to target powercell
drive_motors.move_tank(45, 'cm', 50, 50)
drive_motors.move(turn_degrees(wheel_base, -90), 'cm', 100)
drive_motors.move_tank(25, 'cm', 50, 50)

# lowers arm to ground with plow
arm_motor.run_for_degrees(90)

# returns to home backwards to drag powercell
drive_motors.move_tank(25, 'cm', -50, -50)
drive_motors.move(turn_degrees(wheel_base, 90), 'cm', 100)
drive_motors.move_tank(45, 'cm', -50, -50)