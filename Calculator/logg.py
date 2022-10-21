from datetime import datetime


def logger(op_str, data, res):
    time_now = datetime.now().strftime('%H:%M')
    date_now = datetime.now().strftime('%d.%m')
    with open('log.csv', 'a') as log:
        log.write('\n{}; {}; {}; {}; {}'.format(time_now, date_now, op_str, data, res))
