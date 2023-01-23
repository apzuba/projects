class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.hints = {}

    def add_paths(self, paths):
        self.paths.update(paths)
    
    def add_hints(self, hints):
        self.hints.update(hints)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body. He's blocking the door to
the Armory and about to pull a weapon to blast you.
""")

def generic_death():
    print('gen')
def laser_weapon_armory():
    print('las')

central_corridor.add_paths({
    'central_corridor': central_corridor,
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

# central_corridor.add_hints(x for paths in central_corridor)

split
for i in central_corridor.paths:
    print(i[0])

# x for x[0] in 