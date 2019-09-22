import os



print('hello again world!')


def bip():
    if os.name == 'nt':  # Windows
        import winsound
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 100  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    else:
        print('\a')

