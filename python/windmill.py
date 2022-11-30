from spike import PrimeHub, MotorPair

hub = PrimeHub()

# creates drive motor pair
drive_motors = MotorPair('A', 'B')

# drives to windmill & turns to face it
drive_motors.move_tank(74, 'cm', 50, 50)
drive_motors.move_tank(4.3, 'cm', 50, 0)

# pushes into the windmill
i = 0
while i < 4:
  # this runs 4 times
  drive_motors.move_tank(45, 'cm', 10, 10)
  drive_motors.move_tank(5, 'cm', -25, -25)
  i += 1

# turns towards home & drives into it
drive_motors.move_tank(17, 'cm', 25, 0)
drive_motors.move_tank(74, 'cm', 50, 50)