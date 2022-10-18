import time
import math
import stretch_body.robot

robot=stretch_body.robot.Robot()

def main():
  robot.base.translate_by(x_m=0.5, v_m = 0.4, a_m = 0.4)
  robot.push_command()
  time.sleep(4.0) #wait

  robot.base.rotate_by(x_r=math.pi)
  robot.push_command()
  time.sleep(4.0) #wait

  robot.base.translate_by(x_m=0.5, v_m = 0.4, a_m = 0.4)
  robot.push_command()
  time.sleep(4.0) #wait

  robot.base.rotate_by(x_r=-math.pi)
  robot.push_command()
  time.sleep(4.0) #wait

  robot.stow()
  robot.stop()

if __name__ == '__main__':
  robot.startup()
  main()
