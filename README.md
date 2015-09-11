# Gilson402SyringePumpControl

library of gilson syringe pump control funcs



Usage:

import gilson402

machine = gilson402.Gilson402()
machine.connect()
machine.deviceAcknowledge(128)

machine.getSyringeStatus()
machine.getValveStatus()

machine.aspirateVolume('L', '02000')
machine.startSyringe('L')
machine.dispenseVolume('L', '01000')
machine.startSyringe('L')

machine.disconnect()



