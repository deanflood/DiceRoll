import random

print("Dice Mean: 3.5")
mean = 0.0
for x in range(1, 1000000):
    mean += random.randint(1,6)
print("Mean after 1,000,000 rolls: " + str(mean / 1000000))
mean = 0.0
