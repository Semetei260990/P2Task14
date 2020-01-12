import random
my_list = []
for x in range(20):
    my_list.append(random.randint(1, 1000))
    if my_list[x] % 2 == 0:
        print(my_list[x])