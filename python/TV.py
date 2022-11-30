from spike import PrimeHub, MotorPair

hub = PrimeHub()

# creates drive motor pair
drive_motors = MotorPair('A', 'B')

# drives into the TV & backs up
drive_motors.move_tank(35, 'cm', 50, 50)
drive_motors.move_tank(35, 'cm', -50, -50)