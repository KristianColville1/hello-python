class Wolf:
    """Creates an instance of a Wolf"""
    
    def __init__(self, speed, strength, teeth, height, weight, habitat):
        self.speed = speed
        self.strength = strength
        self.teeth = teeth
        self.height = height
        self.weight = weight
        self.habitat = habitat

    def description(self):
        described = f'The Wolf has a top speed of {self.speed}.\nIts lives in a {self.habitat} habitat and can grow to a height of {self.height} and weight {self.weight}.'
        return described

wolf_one = Wolf(25, 70, 55, '1.2 meters', '35Kg', 'forest')
print(wolf_one)

print(wolf_one.description())