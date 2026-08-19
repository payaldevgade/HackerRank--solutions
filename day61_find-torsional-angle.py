import math


class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    def dot(self, no):
        return (
            self.x * no.x +
            self.y * no.y +
            self.z * no.z
        )

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2
        )


# Input
A = Points(*map(float, input("Enter point A (x y z): ").split()))
B = Points(*map(float, input("Enter point B (x y z): ").split()))
C = Points(*map(float, input("Enter point C (x y z): ").split()))
D = Points(*map(float, input("Enter point D (x y z): ").split()))

# Create vectors
AB = B - A
BC = C - B
CD = D - C

# Cross products
X = AB.cross(BC)
Y = BC.cross(CD)

# Calculate angle
cos_theta = X.dot(Y) / (X.absolute() * Y.absolute())

theta = math.acos(cos_theta)

# Convert radians to degrees
angle = math.degrees(theta)

print("Torsional angle:", f"{angle:.2f}")