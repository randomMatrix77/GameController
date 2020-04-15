def calibrator(board, iter, gas, brake):
    iter.start()
    board.pass_time(0.2)

    gas_arr = []
    brake_arr = []
    print('Begining calibration process:')
    for i in range(15):
        gas_arr.append(gas.read())
        brake_arr.append(brake.read())
        print('gas: {}, brake: {}'.format(gas.read(), brake.read()))
        board.pass_time(2)

    gas_calib = [max(gas_arr), min(gas_arr)]
    brake_calib = [max(brake_arr), min(brake_arr)]

    print('Gas - Max: {}, Min: {}'.format(gas_calib[0], gas_calib[1] - 0.09))
    print('Brake - Max: {}, Min: {}'.format(brake_calib[0], brake_calib[1] - 0.09))

    return gas_calib[1], brake_calib[1]
