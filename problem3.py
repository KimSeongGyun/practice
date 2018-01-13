#import necessary module
import time

countdown = int(input("Enter Time: "))

# for loop in reverse
for i in range(countdown, -1, -1):
    print("{} seconds".format(i))
    time.sleep(1)       #delay 1 second

print("finish")