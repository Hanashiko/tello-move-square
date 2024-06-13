from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()
print(drone.get_battery())
drone.move_up(50)

for j in range(2):
    for i in range(4):
        drone.move_forward(200)
        drone.rotate_clockwise(90)

print(drone.get_battery())
drone.land()

drone.end()
