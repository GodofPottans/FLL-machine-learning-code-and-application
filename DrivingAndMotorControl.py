from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
#Left motor Port:A
#Right motor Port:B
#AttachMotor1 Port:C
#AttachMotor2 Port:D
#ColorSensor1 Port:E
#ColorSensor2 Port:F

#Motor defining#
left_motor = Motor(Port.A, Direction=ANTICLOCKWISE) #Defined left_motor var. as a motor and at port A with an anitclockwise direction
right_motor = Motor(Port.B, Direction=CLOCKWISE) #Defined left_motor var. as a motor and at port A with an anitclockwise direction
attach_motor1 = Port.C
attach_motor2 = Port.D
ColorSensor1 = ColorSensor(Port.E)
ColorSensor2 = ColorSensor(Port.F)
hub.imu.heading(0)
wait(100)
Kp =   2.0                        #Set the kp as a different amount if necesary
Speed = 400                       #Set the Speed as a different amount if necesary
turnrate = 400                    #change the 400 into a different number if the robot is rapidly turning
Gyro_Drive = GyroDriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=150) #requires the left and right motr, the wheel diameter, and the distance from one wheel to another(mostly from ground touching point to the other)
while (Gyro_Drive.distance()<total_distance):
    x=Gyro_Drive.distance()
    target_angle =                 #Insert equation for navigation here
    attachment1_angle =            #Insert equation for attachment1 here
    attachment2_angle =            #Insert equation for attachment2 here
    error_turn = Kp*(target_angle - hub.imu.heading())
    if error_turn>turnrate:   
        error_turn=turnrate
    elif error_turn<-turnrate:
        error_turn=-turnrate
    await multitask(Gyro_Drive.drive(speed, error_turn), attach_motor1.run_angle(attach_motor1.angle(), attachment1_angle, then=Stop.HOLD, wait=TRUE), attach_motor2.run_angle(attach_motor2.angle(), attachment2_angle, then=Stop.HOLD, wait=TRUE))
    wait(100)
