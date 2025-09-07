from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch, DataLog

hub = PrimeHub()

#Left motor Port:A
#Right motor Port:B
#AttachMotor1 Port:C
#AttachMotor2 Port:D
#ColorSensor1 Port:E
#ColorSensor2 Port:F

#Motor defining#
left_motor = Motor(Port.A, Direction.ANTICLOCKWISE) #Defined left_motor var. as a motor and at port A with an anitclockwise direction
right_motor = Motor(Port.B, Direction.CLOCKWISE) #Defined left_motor var. as a motor and at port A with an anitclockwise direction
attach_motor1 = Motor(Port.C)
attach_motor2 = Motor(Port.D)
ColorSensor1 = ColorSensor(Port.E)
ColorSensor2 = ColorSensor(Port.F)

Gyro_Drive = GyroDriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=150) #requires the left and right motr, the wheel diameter, and the distance from one wheel to another(mostly from ground touvhing point to the other)
navigation_data = DataLog('time', 'angle')
Attachment1_data = DataLog('time', 'attachement1 angle')
Attachment2_data = DataLog('time', 'attachement2 angle')
watch = StopWatch()
for i in range(1000):
    Gyro_angle= hub.imu.heading()
    Attachment1_angle = attach_motor1.angle()
    Attachment2_angle = attach_motor2.angle()
    time = watch.time()
    distance = GyroBaseDrive.distance()
    navigation_data.log(time, distance, Gyro_angle) #Logging navigation data for moving around
    Attachment1_data.log(time, distance, Attachment1_angle) #logging the first motor for attachments
    Attachment2_data.log(time, distance, Attachment2_angle) #logging the first motor for attachments
    print(time, "|", distance, "|", Gyro_angle, "|", Attachment1_angle, "|", Attachment2_angle)
    wait(150)
