# Gilson402SyringePumpControl

library of gilson syringe pump control funcs



Usage:


import gilson402

machine = gilson402.Gilson402()

# connect port
machine.connect()

#acknowledge (this will correspond to the device ID settings on the back of the 402)
machine.deviceAcknowledge(128)

#the 402 homes the syringes to initialise and allow further commands
#L = left syringe, R = right, B = both
machine.initialiseSyringe('B')

#read the status of the Syringes
machine.getSyringeStatus()

#read the status of the valves
machine.getValveStatus()

#set a volume to aspirate (need to then call startSyringe to run)
machine.aspirateVolume('L', '02000')

#run buffered syringe command
machine.startSyringe('L')

#set the flowrate ml/min
machine.setSyringeFlow('L', '00010')

#set the syringe force 1 - 5
machine.setSyringeMotorForce('L', '2')

#set a volume to dispense (need to the call startSyringe to run)
machine.dispenseVolume('L', '01000')

#run buffered syringe command
machine.startSyringe('L')

#halt moving syringe
machine.haltSyringeMotors('L')


machine.disconnect()




TODO:

demonstrate continual flow 
e.g for chromatography mobile phase

parse raw return vals


