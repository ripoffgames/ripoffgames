class AI:
  def _init_(self):
    pass
  def turn(self):
    if self.robot.lookInFront() == "bot":
      self.robot.attack()
    else:
      self.goTowards(self.robot.locateEnemy () [0] )
  def goTowards (self, enemyLocation):
    myLocation = self.robot.position
    delta = (enemyLocation[0]-myLocation[0],enemyLocation[1]-myLocation[1])
    if abs(delta[0]) > abs(delta[1]):
      if delta[0] < 0:
        targetOrientation = 3
      else:
        targetOrientation = 1
    else:
      if delta[1] < 0:
        targetOrientation = 0
      else:
        targetOrientation = 2
    if self.robot.rotation == targetOrientation:
      self.robot.goForth()
    else:
      leftTurnsNeeded  = (self.robot.rotation - targetOrientation) % 4
      if leftTurnsNeeded <= 2:
        self.robot.turnLeft()
      else:
        self.robot.turnRight()
