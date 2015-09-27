# The primary data structure will be a priority queue representing the destinations of a lift's occupants
# Priority will be based on which floor is the closest to the lift's current position


NUMFLOORS = 2
UP = True
DOWN = False


class Building:
    def __init__():
        self.pickups = [] # FIFO Queue
        self.lifts = []
        
    
class Lift:
    direction = UP
    location = 0
    dropoffs = [] # Priority queue based on elevator's location and direction 
    def __init__(direction, location):
        self.direction = direction
        self.location = location

    def pickup(person):
        self.dropoffs.append(person)
    
def main():
    building = Building()
    lift = Lift(UP,0)
    for i in range (NUMFLOORS):
        building.pickups.append((2,1)) # At floor 2, going to floor 1.
        lift.pickup(building.pickups[i])

    
