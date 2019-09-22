import os



print('hello again world!')


def bip():
    if os.name == 'nt':  # Windows
        import winsound
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    else:
        print('\a')

