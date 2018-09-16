
import random

neighbours = 0
num_rows = 20
num_cols = 20
world_change = True
ticks = 0

world = [[0 for row in range(num_rows + 2)] for row in range(num_cols + 2)]
n_world = [[0 for row in range(num_rows + 2)] for row in range(num_cols + 2)]

random.seed()

# Make the world 2 rows one top and 1 bottom bigger and
# two coloumns left and right bigger. we can then treat
# them as having no life.
# We only calculate row and col +1 to num_row / num_cols -1

#def generate_world() -> object: ?????
def generate_world():

    for row in range(1, num_rows + 1):
        for col in range(1, num_cols + 1):
            world[row][col] = random.randint(0,1)


    return world

def update_world(world):

    neighbours = 0


    for c_row in range(1, num_rows + 1):
        for c_col in range(1, num_cols + 1):
            if world[c_row - 1][c_col - 1] == 1:
                neighbours += 1
            if world[c_row - 1][c_col] == 1:
                neighbours += 1
            if world[c_row - 1][c_col + 1] == 1:
                neighbours += 1

            if world[c_row][c_col - 1] == 1:
                neighbours += 1
            if world[c_row][c_col + 1] == 1:
                neighbours += 1

            if world[c_row + 1][c_col - 1] == 1:
                neighbours += 1
            if world[c_row + 1][c_col] == 1:
                neighbours += 1
            if world[c_row + 1][c_col + 1] == 1:
                neighbours += 1

# If cell lives check to see if it lives on
            if world[c_row][c_col] == 1:
                if neighbours < 2:
                    n_world[c_row][c_col] = 0
                if neighbours == 2:
                    n_world[c_row][c_col] = 1
                if neighbours == 3:
                    n_world[c_row][c_col] = 1
                if neighbours > 3:
                    n_world[c_row][c_col] = 0

# If Cell is dead but has 3 Neighbours it lives
            if world[c_row][c_col] == 0:
                if neighbours == 3:
                    n_world[c_row][c_col] = 1

            neighbours = 0

    return n_world

def world_changed(world, n_world):

    for row in range(0, num_rows + 2):
        for col in range(0, num_cols + 2):
            if world[row][col] != n_world[row][col]:
                return True

    return False

def print_world(world):
    for row in range(0, num_rows + 2):
        for col in range(0, num_cols + 2):
            if world[row][col] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def copy_world(world, n_world):

    for row in range(0, num_rows + 2):
        for col in range(0, num_cols + 2):
            world[row][col] = n_world[row][col]
    return world


world = generate_world()

while world_change == True:
    ticks = ticks + 1
    n_world = update_world(world)
    world_change = world_changed(world, n_world)
    world = copy_world(world, n_world)

    print_world(world)


print("---------------------------------------")
print("Game Ticks ",ticks)
print_world(world)
