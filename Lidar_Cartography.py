import PyLidar3
import matplotlib.pyplot as plt
import math    
import time

x=[]
y=[]
for _ in range(360):
    x.append(0)
    y.append(0)
port = "COM10" # à compléter

#port =  "Enter port name 
# which lidar is connected:"
# for instance /dev/ttyUSB0
Obj = PyLidar3.YdLidarX4(port)

if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    plt.figure(1)

    t = time.time() # start time 
    data = next(gen)
    delta = time.time() - t
    while (delta) < 15: #scan for 30 seconds
        xmax = 0
        ymax = 0
        xmin = 0
        ymin = 0

        delta = time.time() - t
        print(delta)
        data = next(gen)
        for angle in range(0,360):
            if(data[angle]>50):
                x[angle] = data[angle] * math.cos(math.radians(angle))
                y[angle] = data[angle] * math.sin(math.radians(angle))
        plt.cla()
        plt.ylim(-500,500)
        plt.xlim(-500,500)
        plt.scatter(x,y,c='r',s=8)
        
        plt.pause(0.05)
        
    plt.close("all")
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")


plt.figure(1)
plt.cla()

plt.ylim(-500,500)
plt.xlim(-500,500)
plt.scatter(x,y,c='r',s=8)
plt.pause(20) 
plt.close()