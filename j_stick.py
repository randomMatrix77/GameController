import pyvjoy
import time
from pyfirmata import Arduino, util
from scipy.interpolate import interp1d
import calibration

board = Arduino('COM5')
ster = board.get_pin('a:0:p')
gas = board.get_pin('a:1:i')
brake = board.get_pin('a:2:i')
iter = util.Iterator(board)

min_gas, min_brake = calibration.calibrator(board, iter, gas, brake)

interpol_gas = interp1d([min_gas, 1], [0, 16384*2])
interpol_brake = interp1d([min_brake, 1], [0, 16384*2])
interpol_steer = interp1d([0, 1], [0, 16384*2])

j = pyvjoy.VJoyDevice(1)

board.pass_time(0.2)

while True:
    if gas.read() >= min_gas and brake.read() >= min_brake:
    # if gas.read() >= 0.52:
    # if brake.read() >= 0.52:
        gas_val = int(interpol_gas(gas.read()))
        brake_val = int(interpol_brake(brake.read()))
        j.data.wAxisZRot = brake_val
        j.data.wAxisZ = gas_val
        print('Gas: {}, Brake: {}'.format(gas_val, brake_val), end = '\r')
    steer_val = int(interpol_steer(ster.read()))
    j.data.wAxisX = steer_val
    j.update()
    time.sleep(0.05)
