import random

ran_list = []

for i in range(1, 21):
    ran_list.append(random.randint(1,100))

ran_list = sorted(ran_list, reverse=True)

print(ran_list)