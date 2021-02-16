import time

def countdown():
    for i in range(0,1):
        tmp = 10000
        try:
            when_to_stop = abs(int(tmp))
        except KeyboardInterrupt:
            break
        except:
            print('Not a number')
        while when_to_stop > -1:
            s, ms = divmod(when_to_stop, 1000)
            time_left = str(s).zfill(2) + ':' + str(ms).zfill(3)
            print(time_left + '\r', end = '')
            time.sleep(0.001)
            when_to_stop -= 1
    return time_left

print(countdown())













def timer():
    tmp = int(10000)
    while tmp > -1:
        s, ms = divmod(tmp, 1000)
        time_left = str(s).zfill(2) + ':' + str(ms).zfill(3)
        print(time_left + '\r', end = '')
        time.sleep(1)
        tmp -= 1
    return time_left

print(timer())






    