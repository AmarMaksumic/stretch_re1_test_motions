import time
import stretch_body.robot

robot=stretch_body.robot.Robot()

def main():

  # Extend all robot joints
  robot.arm.move_by(0.75)
  robot.lift.move_by(0.8)
  robot.end_of_arm.move_to('wrist_yaw', 0)
  robot.end_of_arm.move_to('stretch_gripper',50)
  robot.push_command()
  time.sleep(4)

  # Retract all robot joints to stowed position
  robot.stow()

  # Set camera cluster head to look ahead
  robot.head.pose('ahead')
  robot.push_command()
  time.sleep(1.5)

  # Set camera cluster head to look backwards
  robot.head.pose('back')
  robot.push_command()
  time.sleep(1.5)

  # Set camera cluster head to look at its tools
  robot.head.pose('tool')
  robot.push_command()
  time.sleep(1.5)

  # Set camera cluster head to look at its wheels
  robot.head.pose('wheels')
  robot.push_command()
  time.sleep(1.5)

  # Set camera cluster head to look left
  robot.head.pose('left')
  robot.push_command()
  time.sleep(1.5)

  # Set camera cluster head to look up
  robot.head.pose('up')
  robot.push_command()
  time.sleep(1.5)

  robot.stow()
  robot.stop()

if __name__ == '__main__':
  robot.startup()
  main()
