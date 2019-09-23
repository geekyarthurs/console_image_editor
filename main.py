from init import *
from signal import signal, SIGINT
from sys import exit
from controllers.InputController import InputController


def handler(signal_received, frame):
    # Handle any cleanup here
    print("")
    ColorPrint().print_warn("Exiting... Have a nice day..")
    os.system("clear")
    exit(0)

if __name__ == "__main__":
    os.system("clear")
    signal(SIGINT, handler) # to capture exit on keyboard.
    sys.stderr.write('\x1b[1;31m' + """


             ____                        _           _____       _   _   _                  
            / ___|    __ _   _ __ ___   ( )  ___    | ____|   __| | (_) | |_    ___    _ __ 
            \___ \   / _` | | '_ ` _ \  |/  / __|   |  _|    / _` | | | | __|  / _ \  | '__|
             ___) | | (_| | | | | | | |     \__ \   | |___  | (_| | | | | |_  | (_) | | |   
            |____/   \__,_| |_| |_| |_|     |___/   |_____|  \__,_| |_|  \__|  \___/  |_|   
                                                                                 
                                                                            ---Developer 0x255
    """)

    if(len(sys.argv) <= 1):
        ColorPrint.print_fail(
            "Error !! " + error_messages["argument-length-error"])
        exit()

    inputController = InputController(sys.argv[1])

    ColorPrint.print_pass(messages["console-start"])

    while True:
        inputController.getInput()

# End of The code