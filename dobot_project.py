import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}


api = dType.load()

state = dType.ConnectDobot(api, "DOBOT_IP_HERE", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

    dType.SetQueuedCmdClear(api)

    dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
    #dType.SetHOMECmd(api, temp = 0, isQueued = 1)
    
    #dType.SetPTPJointParams(api, j1Velocity, j1Acceleration, j2Velocity, j2Acceleration, j3Velocity, j3Acceleration, j4Velocity, j4Acceleration, isQueued=1)
    dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)

    # Parameters:
    # v        - Velocity of the Dobots movements
    # a        - Acceleration of the Dobots movements.
    # isQueued - To queue the command or not.
    #dType.SetPTPCommonParams(api, v, a, isQueued)
    dType.SetPTPCommonParams(api, 80, 80, isQueued = 1) 

# Feding CNC 1 with row material � initiation
#M31 = Magazine of row material � CNC3
#M32 = Magazine of Finished product � CNC3
#M11 = Magazine of row material � CNC1
#M12 = Magazine of Finished product � CNC1
#M21 = Magazine of row material � CNC2
#M22 = Magazine of Finished product � CNC2
# Arms on move position = In a convenient position for the CNC to move

dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 780, isQueued=1) # moves CNC to M31
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -135, -214, 100,9, isQueued = 1) # A3 over M31
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -135, -214, -85, 9, isQueued = 1) # A3 ON M31 
dType.dSleep(2500) # wait 7seconds
dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1) # Closes gripper
dType.dSleep(7000) # wait 7seconds
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -135, -214, 100, 9, isQueued = 1) # A3 over M31
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued = 1) # arm on move position
dType.dSleep(2500)
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode ,190, -108, 49, 9, 761, isQueued=1) # Arm over M11
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode ,190, -108, -83, 9,  isQueued = 1) # Arm on M11
dType.dSleep(2500) # wait 7seconds
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500) # wait 7seconds
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 190, -108, 49, 9, isQueued = 1) # pull up arm
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued=1) # moves position
dType.dSleep(2500)
# Taking finished parts of M12
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 628, isQueued=1) # moves CNC to M12
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 277, -60, 100, 100, isQueued = 1) # A3 over M12
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 277, -60, -40, 100, isQueued = 1) # Gripper on M12
dType.dSleep(7000) # wait 7seconds
dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1) # Closes gripper
dType.dSleep(7000) # wait 7seconds
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 277, -60, 100, 100, isQueued = 1) # pull up arm
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued = 1) # arm on move position
dType.dSleep(2500)
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 583, isQueued = 1) # CNC TO M32
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -158, -233, 100, 14, isQueued = 1) # Arm over M32
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -158, -233, -88, 14, isQueued = 1) # Arm on M32
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -158, -233, 100, 14, isQueued = 1) # pull up arm
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued=1) # arm on move position
# Feeding CNC 2 with row material
dType.dSleep(2500)
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 780, isQueued=1) # moves CNC to M31
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -134, -261, 100,14, isQueued = 1) # A3 over M31
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -134, -261, -85, 14, isQueued = 1) # A3 ON M31 
dType.dSleep(5000) # wait 7seconds
dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1) # Closes gripper
dType.dSleep(9000) # wait 7seconds
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -134, -261, 100, 14, isQueued = 1) # A3 over M31
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41,isQueued=1) # moves Arms on move position
dType.dSleep(2500)
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 70, isQueued=1) # moves CNC to M21
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode ,144.74, -200.78, 63, 95.78, isQueued=1) # Arm over M21
dType.dSleep(2500)
dType.SetPTPCmd(api,1,144.74, -200.78, -91, 95.78, isQueued = 1) # Arm on M21
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode ,144.74, -200.78, 63, 95.78, isQueued = 1) # pull up arm
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued=1) # moves position
dType.dSleep(2500)
# Taking finished parts of M22
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 48, isQueued=1) # moves CNC to M22
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 140, -140, 100,103 , isQueued = 1) # A3 over M22
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 140, -140, -96,103, isQueued = 1) # Gripper on M22
dType.dSleep(5000) # wait 7seconds
dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1) # Closes gripper
dType.dSleep(5000) # wait 7seconds
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 140, -140, 100,103 , isQueued = 1) # A3 over M22
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41,isQueued=1) # moves Arms on move position
dType.dSleep(2500)
dType.SetPTPWithLCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, 598, isQueued = 1) # CNC TO M32
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -162, -263, 100, 9, isQueued = 1) # Arm over M32
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -162, -263, -88, 9, isQueued = 1) # Arm on M32
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1) # Opens gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , -162, -263, 100, 9, isQueued = 1) # Arm over M32
dType.dSleep(2500)
dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1) # disable gripper
dType.dSleep(2500)
dType.SetPTPCmd(api,dType.PTPMode.PTPMOVJXYZMode , 6, -204, 130, 41, isQueued=1) # moves position

#Start to Execute Command Queue
dType.SetQueuedCmdStartExec(api)

#Stop to Execute Command Queued
dType.SetQueuedCmdStopExec(api)
    
print('All processes finished')

#Disconnect Dobot
dType.DisconnectDobot(api)
