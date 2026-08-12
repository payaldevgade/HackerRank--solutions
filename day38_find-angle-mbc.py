import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan2(AB, BC))

print(round(angle), chr(176), sep="")