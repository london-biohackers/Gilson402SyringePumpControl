

import serial
# needs to talk to 402 unit, typically slaved over RS422


class Gilson402(object):

	def __init__(self):





	def connect(self, port, baud=19200, bytesize=8, timeout=1):

		self.ser = serial.Serial( port, baud, bytesize, timeout )
	

		return status


	def isConnected(self):


		return connected  #bool




	def disconnect(self):

		self.ser.close()

		return status






###############################
# 402 Mode - Immediate Commands
###############################

	def reqModuleID(self):
		#check connected
		if( ! self.isConnected() ):
			return 0;
		#clear read buffer

		#write command
		self.ser.write('%')
		#send ack
		self.ser.write(chr(6))

		#read returned bytes

		#process returned bytes

		return format



	def masterReset(self):
		#check connected
		if( ! self.isConnected() ):
			return 0;
		#clear read buffer

		#write command
		self.ser.write('$')
		#send ack
		self.ser.write(chr(6))

		#read returned bytes
		
		#process returned bytes

		return status

	def getGlobalStatus(self):
		#check connected
		if( ! self.isConnected() ):
			return 0;
		#clear read buffer

		#write command
		self.ser.write('')
		#send ack
		self.ser.write(chr(6))

		#read returned bytes
		
		#process returned bytes

		return globalStatus



	def getSyringeStatus(self):
		#check connected
		if( ! self.isConnected() ):
			return 0;
		#clear read buffer

		#write command
		self.ser.write('M')
		#send ack
		self.ser.write(chr(6))

		#read returned bytes
		
		#process returned bytes

		return syringeStatus



	def getValveStatus(self):
		#check connected
		if( ! self.isConnected() ):
			return 0;
		#clear read buffer

		#write command
		self.ser.write('V')
		#send ack
		self.ser.write(chr(6))

		#read returned bytes
		
		#process returned bytes

		return valveStatus



##############################
# 402 Mode - Buffered Commands
##############################


	def aspirateVolume(self, syringe, volume):



		return status



	def startSyringe(self, syringe):



		return status




	def dispenseVolume(self, syringe, volume):



		return status


	def setSyringeMotorForce(self, syringe, amplitude):




		return status:




	def haltSyringeMotors(self, syringe):


		return status



	def initialiseSyringe(self, syringe):




		return status



	def setSyringeSize(self, syringe, volume):




		return status



	def setSyringeFlow(self, syringe, volRate):




		return status



	def timelyStart(self, syringe):




		return status



	def valveConfigOption(self, valve):



		return status





	def valveControl(self, valve, position):



		return status












# % Request module identification
# Response format:
# 402SVa.bc
# where
# Va.bc
# is the software version.
# $ Master reset
# Response format:
# $
# where
# The returned
# $
# indicates that the machine has been reset in its power-
# up state.
# M Read syringe status
# Response format:
# fnnnnnngmmmmmm
# where
# f
# is the left syringe status. It can have one of the following values:
# N
# for no errors.
# R
# for motor running.
# O
# for overload error (motor has lost steps ; the syringe must be re-
# initialized.
# I
# for a syringe not initialized or being initialized.
# M
# for a syringe motor missing ; either it is not installed (single
# syringe 402) or the syringe drive is defective or locked because
# of a software error.
# H
# for an uncompleted motion ; either the motion has been specified
# by a buffered
# A
# or
# D
# command but not started yet, or the syringe
# has been halted by a buffered
# H
# command.
# W
# for a syringe waiting for the other syringe as set by the buffered
# command
# W
# .
# nnnnnn
# is the left syringe contents volume. The unit is the microliter,
# or the step if syringe 39000 is used.
# g
# is the right syringe status, identical to f (see above).
# In the case of an O error, the syringe must be reinitialized before normal
# operation can resume.
# S Return global status
# Response format:
# ab
# where
# a
# is the command status buffer
# a
# =
# 0
# for buffer empty,
# a
# =
# 1
# for buffer occupied.
# When the buffer is empty, the commands previously sent are being
# processed ; when it is occupied, they are not necessarily being
# processed, and it is not possible to send more buffered commands.
# b
# is the error flag status
# b
# =
# 0
# for no error, all commands have been accepted.
# b
# =
# 1
# for one or more rejected buffered commands since the last
# immediate $ command.
# This flag is reset to 0 just after the immediate
# $
# command has been executed.

# V Valve status
# Response format:
# ab
# where
# a
# is the left valve status
# b
# is the right valve status.
# R
# for valve to reservoir.
# N
# for valve to needle.
# X
# for valve running..
# O
# for valve overload error (the motor has lost steps) or failure to
# detect one or both rest positions. May happen on initialization.
# M
# for valve absent.






##############################
# 402 Mode - Buffered Commands
##############################


# A Aspirate volume
# Syntax:
# Anvvvvv
# where
# n
# is the syringe identification.
# n
# =
# L
# for left syringe,
# n
# =
# R
# for right syringe.
# vvvvv.v
# is the aspirated volume in microliters (0 up to syringe volume), or
# in steps if syringe 39000 is used.
# This command sets the next aspiration but does not initiate liquid flow.
# To begin aspiration, use the buffered
# B
# command.
# Volume range
# Syringe (μl) 100 250 500
# 1000 5000 10000 25000 39000
# Vol. min (ml) 0.1 0.1 1 1 1 1 1 0*
# Vol. max (ml) 100 250 500
# 1000 5000 10000 25000 39000*
# Increment (ml) 0.1 0.1 1 1 1 1 1 1*
# This command will be rejected if the syringe involved has not been defined and
# successfully initialized or if it is an error. Use the immediate M command to see if
# there no error after initialization. If the volume is greater than the volume that can
# be aspirated by the syringe, the command will be rejected. Rejection is flagged by
# the immediate
# S
# command.
# * These units are in steps, not μl.
# B Start syringe
# Syntax:
# Bn
# where
# n
# is the syringe identification
# n
# =
# L
# for left syringe,
# n
# =
# R
# for right syringe,
# n
# =
# B
# for both syringe.
# Send the designated syringe(s) to the destination defined by the previous
# buffered A or D commands if any. If both syringes are
# selected, they start
# simultaneously. If the destination is not defined for a syringe, this command
# has no effect. The syringe(s) will not start until the valve on the same side
# (if any) is at rest. Furthermore, the start of the syringe can be delayed
# under more conditions, using the buffered command
# T
# .
# D Dispense volume
# Syntax:
# Dnvvvvv
# n
# is the syringe identification
# n
# =
# L
# for lrft syringe,
# n
# =
# R
# for right syringe.
# vvvvv
# is the dispensed volume in microliters (0 up to syringe volume),
# or in steps if syringe 39000 is used.
# This command sets the next dispense but does not initiate liquid flow.

# o
# begin
# dispense,
# use
# the
# buffered
# B
# command.
# Volume
# range:
# see
# buffered
# A
# command
# above.
# If the volume is greater than the volume currently held by the syringe, the
# command will be rejected. This is flagged by the immediate
# S
# command. This
# command will be rejected until the syringe involved has been defined and
# successfully initialized or it is an error. Use the immediate
# M
# command to check if
# there is no error after initialization.
# F Set syringe motor force Syntax: Fna where n is the syringe identification n = L for left syringe, n = R for right syringe.
#  a selects the amplitude of the motor current: 0 = 0% of nominal current (the motor is unpowerd) 1 = 25%, 2 = 37.
# 5%, 3 = 50%, 4 = 75%, 5 = 100%.

# The current level is automatically set according to the syringe type, as follows:
# 100, 250, 500, 1000 μl: level 3 ;
# 5000, 10000, 25000 μl, 39000 steps: level 5.
# Use this command to set the syringe motor force to a different value if the need arises.
#  Send it after defining the syringe using the buffered P command, and before to send the first motion command.
#  If a motion is already in progress, this command will only take effect at the next motion.
#  After a delay of about ten seconds of idling, the current will be automatically reduced to level 1 to reduce temperature rise, but it will be restored to the specified value at the beginning of every motion without the need to issue this command each time.
#  N Halt syringe motors Syntax: Hn where n is the syringe identification n = L for left syringe, n = R for right syringe, n = B for both syringe.
#  If the specified syringe is at rest, the command is ignored.
#  No error is flagged.
#  O Initialize syringe Syntax: On where n is the syringe identification n = L for left syringe, n = R for right syringe, n = B for both syringe.
#  This command sends the piston to the topmost position, until the plunger touches the valve body; then the piston moves down by a small amount to provide a clearance between the piston and the syringe top.
#  The motor force is set automatically according to the syringe selected.
#  If necessary the force may be adjusted with the buffered F command before initializing the syringe.
#  Care must be taken that some liquid will be dispensed during initialization.
#  If the syringe motor is missing, this command has no effect.
#  This command acts immediately, even if a motion is already in progress.
#  After successful initialization, the immediate M command returns a N for no error and the contents of the syringe are set to zero.
#  If the initialization failed, the M error is returned.
#  The syringe must be initialized prior to any syringe movement command.

# P Set syringe size Syntax: Pnvvvvv where n is the syringe identification n = L for left syringe, n = R for right syringe, n = B for both syringe.
#  vvvvv is the syringe volume, in microliters.
#  The syringe size for both syringes must be taken in the following list: 100, 250, 500, 1000, 5000, 10000, 25000.
#  The value 39000 is also accepted to indicate that the commands A, D and S will be expressed in steps or steps/s.
#  S Set syringe flow Syntax: Snvvvvv where n is the syringe identification n = L for left syringe, n = R for right syringe.
#  vvvvv is the flow in ml/min, or in steps/s if the syringe 39000 is used.
#  Volume range Syringe (μl) 100 250 500 1000 5000 10000 25000 39000 Flow min (ml/min) 0.
# 001 0.
# 001 0.
# 001 0.
# 01 0.
# 01 0.
# 02 0.
# 04 1* Flow max (ml/min) 6 15 30 60 120 240 240 39000* Increment (ml/min) 0.
# 001 0.
# 001 0.
# 001 0.
# 01 0.
# 01 0.
# 01 0.
# 01 1* If the parameter flow is out of range, the flow rate will be set to either the maximum or the minimum possible.
#  This event will be flagged by the immediate S command.
#  The new syringe flow rate will be effective at the next aspirate or dispense command.
#  The syringe flow cannot be changed while the syringe is running.
#  * These units are in steps, not ml.
#  T Timely start Syntax: Tn where n is the syringe identification n = L for left syringe, n = R for right syringe.
#  This command delays the motion of the specified syringe to synchronize it with the other syringe.
#  It must be sent before the buffered B command, and may be sent before or after the buffered A or D command that defines the next motion.
#  For a single syringe, single valve 402, it does not apply.
#  For a dual syringe, single valve 402, the syringe waits until the other syringe and the valve are at rest.
#  For a dual syringe, dual valve, the syringe waits both the other syringe and the other valve.
#  Even if this command is not sent, the syringe will not start until the valve on the same side is at rest.
#  U Valve configuration option Syntax: Un where n is 1 or 2 .
#  For a 402 dilutor fitted with two valve drives, sending U1 forces the right-hand valve to be missing as though the motor had not been installed.
#  This is necessary to allow a proper sequencing of the syringes in case the functions that are specific to a single valve, dual syringe configuration are used with a dual valve dilutor.
#  Sending U2 or the immediate $ command restores the dual syringe configuration.
#  This command has no effect in single-syringe, or dual-syringe and single valve configurations.


# V Valve control
# Syntax:
# Vnp
# where
# n
# is the syringe identification:
# n
# =
# L
# for left syringe.
# n
# =
# R
# for right syringe.
# p
# is the desired valve position:
# R
# for valve to reservoir.
# N
# for valve to needle.
# If the valve is already at the desired position or if the valve is missing, this command
# has no effect.


