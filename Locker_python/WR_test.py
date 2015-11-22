import serial

ser = serial.Serial('/dev/ttyACM0',115200)
check=""
print ser.readline()


ser.write("write")

check=ser.readline()
while check[:-2]!="write":
	print str(check)+"   2"
ser.write("test")

print ser.readline()

print "r"
ser.write("read")

while check[:-2]!="read":
	check=ser.readline()
t=ser.readline()
print t
ser.readline()

