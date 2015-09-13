

import serial
import time
# needs to talk to 402 unit, typically slaved over RS422


class Gilson402(object):

	def __init__(self):
		self.unit='Gilson402 Syringe Pump'


	def connect(self, ser_port='/dev/ttyUSB0'):

		self.ser = serial.Serial(port=ser_port, baudrate=19200, bytesize=8, parity='E', stopbits=1, timeout=1 )
		status = self.ser.isOpen()

		return status


	def isConnected(self):

		connected = self.ser.isOpen()

		return connected



	def disconnect(self):

		self.ser.close()
		status = self.ser.isOpen()

		return status


	def deviceAcknowledge(self, device_id):

		if not self.isConnected():
			return 'not connected';
		ack_id = self._doImmediateCommand(chr(device_id), 2)

		return ack_id



###############################
# 402 Mode - Immediate Commands
###############################

	def reqModuleID(self):

		if not self.isConnected():
			return 'not connected';

		modInfo = self._doImmediateCommand('%', 8)

		return modInfo



	def masterReset(self):
		
		if not self.isConnected():
			return 'not connected';

		status = self._doImmediateCommand('$', 2)

		return status

	def getGlobalStatus(self):
		
		if not self.isConnected():
			return 'not connected';

		status = self._doImmediateCommand('S', 2)

		return status

		return globalStatus



	def getSyringeStatus(self):

		if not self.isConnected():
			return 'not connected';

		syringeStatus = self._doImmediateCommand('M',11)

		return syringeStatus



	def getValveStatus(self):

		if not self.isConnected():
			return 'not connected';

		valveStatus = self._doImmediateCommand('V',3)

		return valveStatus



##############################
# 402 Mode - Buffered Commands
##############################




	def initialiseSyringe(self, syringe):

		if not self.isConnected():
			return 'not connected';

		command = 'O' + syringe
		status = self._doBufferedCommand(command, 2)

		return status



	def aspirateVolume(self, syringe, volume):

		if not self.isConnected():
			return 'not connected';

		command = 'A' + syringe + volume

		status = self._doBufferedCommand(command, 2)

		return status





	def dispenseVolume(self, syringe, volume):

		if not self.isConnected():
			return 'not connected';

		command = 'D' + syringe + volume
		status = self._doBufferedCommand(command, 2)

		return status



	def startSyringe(self, syringe):

		if not self.isConnected():
			return 'not connected';

		command = 'B' + syringe
		status = self._doBufferedCommand(command, 2)

		return status



	def setSyringeMotorForce(self, syringe, amplitude):

		if not self.isConnected():
			return 'not connected';

		command = 'F' + syringe + amplitude
		status = self._doBufferedCommand(command, 2)

		return status




	def haltSyringeMotors(self, syringe):

		if not self.isConnected():
			return 'not connected';

		command = 'H' + syringe
		status = self._doBufferedCommand(command, 1)

		return status



	def setSyringeSize(self, syringe, volume):

		if not self.isConnected():
			return 'not connected';

		command = 'P' + syringe + volume
		status = self._doBufferedCommand(command, 6)

		return status



	def setSyringeFlow(self, syringe, volRate):

		if not self.isConnected():
			return 'not connected';

		command = 'S' + syringe + volRate
		status = self._doBufferedCommand(command, 1)


		return status



	def timelyStart(self, syringe):

		if not self.isConnected():
			return 'not connected';

		command = 'T' + syringe
		status = self._doBufferedCommand(command, 1)


		return status



	def valveConfigOption(self, valve):

		if not self.isConnected():
			return 'not connected';

		command = 'U' + valve
		status = self._doBufferedCommand(command, 1)

		return status



	def valveControl(self, valve, position):

		if not self.isConnected():
			return 'not connected';

		command = 'V' + valve + position
		status = self._doBufferedCommand(command, 1)

		return status



	def _doImmediateCommand(self, command_string, response_size):


		for c in command_string:
			self.ser.write(c)
			time.sleep(0.02)

		for i in range(1, response_size):
			self.ser.write(chr(6))
			time.sleep(0.02)

		ret = self.ser.readall()
		return ret


	def _doBufferedCommand(self, command_string, response_size):

		self.ser.write(chr(10))
		time.sleep(0.02)

		for c in command_string:
			self.ser.write(c)
			time.sleep(0.02)

		self.ser.write(chr(13))

		for i in range(1, response_size):
			self.ser.write(chr(6))
			time.sleep(0.02)

		ret = self.ser.readall()
		return ret

