class Moon:

    def __init__(self, id, x ,y, z):

        self.id = id

        self.x = x
        self.y = y
        self.z = z

        self.v_x = 0
        self.v_y = 0
        self.v_z = 0

    def pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kin(self):
        return abs(self.v_x) + abs(self.v_y) + abs(self.v_z)

    @staticmethod
    def correct(a, b):
        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return -1

    def update_velocity(self, moons):
        v_x = 0
        v_y = 0
        v_z = 0
        for moon in moons:
            if moon.id == self.id:
                v_x += self.v_x
                v_y += self.v_y
                v_z += self.v_z
            else:
                v_x += self.correct(self.x, moon.x)
                v_y += self.correct(self.y, moon.y)
                v_z += self.correct(self.z, moon.z)
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z


moons = [
        Moon(1, -2, 9, -5),
        Moon(2, 16, 19, 9),
        Moon(3, 0, 3, 6),
        Moon(4, 11, 0, 11)
        ]

# moons = [
#         Moon(1, -1, 0, 2),
#         Moon(2, 2, -10, -7),
#         Moon(3, 4, -8, 8),
#         Moon(4, 3, 5, -1)
#         ]


step = 0
while True:
    print(step)
    moons[0].update_velocity(moons)
    moons[1].update_velocity(moons)
    moons[2].update_velocity(moons)
    moons[3].update_velocity(moons)

    moons[0].move()
    moons[1].move()
    moons[2].move()
    moons[3].move()

    step += 1
    if moons[0].v_z == 0 \
        and moons[1].v_z == 0 \
        and moons[2].v_z == 0 \
        and moons[3].v_z == 0:

        break

print("Ans = {}".format(step))
