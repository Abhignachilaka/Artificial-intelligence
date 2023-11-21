import random
class VacuumCleaner:
    def __init__(self, position):
        self.position = position
    def move_left(self):
        self.position = max(0, self.position - 1)
    def move_right(self, world_size):
        self.position = min(world_size - 1, self.position + 1)
def generate_dirt(world_size, dirt_probability):
    return [random.random() < dirt_probability for _ in range(world_size)]
def clean(world, cleaner):
    cleaned_location = cleaner.position
    world[cleaned_location] = False
def print_world(world, cleaner):
    for i in range(len(world)):
        if cleaner.position == i:
            print("V", end=" ")  
        elif world[i]:
            print("D", end=" ")  
        else:
            print("_", end=" ")  
    print()
def main():
    world_size = 10
    dirt_probability = 0.3
    vacuum = VacuumCleaner(position=0)
    world = generate_dirt(world_size, dirt_probability)
    print("Initial state:")
    print_world(world, vacuum)
    steps = 0
    while any(world):
        vacuum.move_right(world_size)
        clean(world, vacuum)
        steps += 1
        print(f"Step {steps}:")
        print_world(world, vacuum)
    print(f"Cleaning completed in {steps} steps.")
if __name__ == "__main__":
    main()
