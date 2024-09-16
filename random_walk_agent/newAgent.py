# This agent has a tendency to walk back to the source the further it gets away from the source.
# That would mean that I need to calculate which angle the agent is at with respect to the origin
# and bias the turns. This agent will walk in squares

import numpy as np

class NewAgent():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = np.random.randint(0,4) * np.pi/2
        self.vel = 1

    def closestAngle(self, angle):
        return round(angle / (np.pi / 2)) * (np.pi / 2)
    
    # Calculates distance
    def dist(self):
        return np.sqrt(self.x**2 + self.y**2)
    
    #Calculates distance to origin
    def ang(self):
        return np.arctan2(-self.y, -self.x)

    
    
    def step(self):
        distance = self.dist()
        if distance > 100:
            if np.random.random() < 0.8:
                targetAngle = self.ang()
                self.orientation = self.closestAngle(targetAngle)
            else:
                self.orientation = np.random.randint(0,4) * np.pi/2
        else:
            self.orientation += np.random.randint(0,4) * np.pi/2

        self.x += self.vel * np.cos(self.orientation)
        self.y += self.vel * np.sin(self.orientation)


