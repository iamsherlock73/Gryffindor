from subprocess import call
import RPi.GPIO as GPIO
from time import sleep   #test

#defining priorities
HIGH = 1
MID = 2
LOW = 3
GO = 0#use diff pin no
#expected object definition obtained
class information:
    status=0
    priority=0
    distance=0
    
    def writestatus( value ):
        status = value
    def getstatus( ):
        return status  
    def getdist():
        return distance
    def getprior():
        return priority
    

#halts process till condition turns false
def till_dist_halt(info):
    while info.getdist() != -1:         #false when veh crosses signal
        info.close()
        call ( "wget CLOUD_URL_HERE" )
        info = open("FILE_NAME", "rb")
        
info = information
while TRUE:
    while TRUE:                           # breaks when new object is available
        call ( "wget CLOUD_URL_HERE" )
        info = open("FILE_NAME", "wb+")
        if ( info.getstatus() == 1):
            info.writestatus(0)
            file.write(info)            # try closing file if needed (dev)
#           call("rm FILE_NAME")        if necessary(dev)          
            break
    
    if ( info.getprior() == HIGH):
        if(info.getdist() < 1 ):         #green lights , in 1km
            GPIO.OUTPUT( GO, TRUE )
       
    elif(info.getprior() == MID ):
        if(info.getdist() < .5 ):     #green lights , in .5km
            GPIO.OUTPUT( GO, TRUE )
        
    elif(info.getprior() == LOW):
        if(info.getdist() < .2 ):        #green lights , in .2km
            GPIO.OUTPUT(GO,TRUE)
        
    till_dist_halt()    
