minute_ = int(input('minute is: '))
second_ = int(input('second is: '))
speed_ = int(input('speed is: '))

speed_m = (3600 / (minute_ * 60 + second_) * speed_) / 1.6
print('speed = {:.1f} 英哩/小時'.format(speed_m))