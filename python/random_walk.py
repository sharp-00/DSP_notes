import random

def random_walk(n):

    position = 0
    path = [position]

    for i in range(n):

        position += random.choice([-1,+1])

        path.append(position)

    return path

n =1000
p=500
total_disp = []

for _ in range(p):
    total_path = random_walk(n)
    total_disp.append(total_path[-1])


avg_disp = sum(total_disp) / len(total_disp)


print(avg_disp)

