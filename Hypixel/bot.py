import keyboard
import mouse
import time

# COLOR IN TERMINAL
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"Script has been launch {bcolors.OKGREEN}successful !{bcolors.ENDC}\n   - Press {bcolors.OKGREEN}Q{bcolors.ENDC} to launch it\n   - Press {bcolors.FAIL}F{bcolors.ENDC} to stop it")

def check(sec):
    tic = time.perf_counter()
    while int(time.perf_counter() - tic) < sec:
        if keyboard.is_pressed("f"):
            return False
            break
        time.sleep(0.01)
    return True

def release_all():
    keyboard.release("z")
    keyboard.release("q")
    keyboard.release("d")

def move(key,time):
    print(f"Pressing {key} key", end="")
    keyboard.press(key)
    if not check(time):
        release_all()
        return False
    else:
        keyboard.release(key)
        print(f": Success pressing {key}")
        return True


while True:
    if keyboard.is_pressed("g"):

        #Lauch Timer
        print("Launching in ", end="")
        for i in [i for i in range(4)][::-1]:
            print(f"{bcolors.WARNING}{i}{bcolors.ENDC}", end=".")
            time.sleep(1)

        netherwartRows = [("ctrl+z",1),("q", 29.5),("ctrl+z", 1),("d", 29.5)]
        # Moving
        flag = False
        for row in range(500):
            print(f"Making the row {bcolors.OKGREEN}#{row}{bcolors.ENDC}")

            for index in range(len(netherwartRows)):
                i = netherwartRows[index]
                result = move(i[0],i[1])
                if not result:
                    print(f"\n{bcolors.FAIL}Task Break{bcolors.ENDC}")
                    flag = True
                    break
                elif i == len(netherwartRows) and row == 1:
                    print(f"{bcolors.OKGREEN}Task done succesfull{bcolors.ENDC}")

            if flag == True:
                break

    time.sleep(0.05)
