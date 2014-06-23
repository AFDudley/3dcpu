class honeycomb(ordereddict):
    """when polyhedra are inserted, returns position."""
    # Either all polyhedra are the same, or polyhedra with different internals
    # are inserted into matrix at random, given some distribution.
    # At start matrix is "full" and fully connected


class Polyhedra():
    def __init__(self, sides=12, honeycomb):
        self.sides = {key: Side(self, key) for key in xrange(0, sides - 1)}
        self.honeycomb = honeycomb
        self.position = honeycomb.insert(self)
                
class Side():
    """Assumes Rhombic dodecahedron."""
    def set_connections(self):
        """sets the connections at init."""
        connections = {"left": None, "right": None}
        if self.index < 6: # this is an input side
            # There is some elegant way to do this...
            connections["right"] = self.index + 6
            if self.index == 0:
                connections["left"] = 11
            else:
                connections["left"] = self.index + 5
        else: #  This is an output side
            connections["left"] = self.index - 6
            if self.index == 11:
                connections["right"] = index - 5
            else:
                connections["right"] = 0
        return connections
    
    def __init__(self, polyhedron, index):
        self.polyhedron = polyhedron
        self.index = index
        self.conenctions = self.set_connections()
    