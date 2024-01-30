# keyboard shifter by krussy
# ------------------------------
# Trying to read keyboard numpad inputs as a separate controller to use as an H-shifter
# Gonna need to package vJoy or ViGem, not sure yet
# ------------------------------

import sys
import ac
import acsys

# from third_party.sim_info import *

appName = "keyboard shifter"
appWindow = 0
lastgear = 0
label_gear = 0

# simInfo = SimInfo()

# Assetto Corsa initalizes this Main when the plugin app starts.
# Returns a string of appname, not sure if its used by the game.
def acMain(ac_version):
    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow, label_gear
    
    appWindow = ac.newApp(appName)
    # ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, 200, 200)

    ac.log("hello deez nutzs")
    ac.log(sys.path)
    label_gear = ac.addLabel(appWindow, 'N')
    ac.setPosition(label_gear, 100, 100)

    # ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function

    return appName

# def appGL(deltaT):
#     """
#     This is where you redraw your openGL graphics
#     if you need to use them .
#     """
#     pass

def acUpdate(deltaT):
    global lastgear, label_gear
    gear = ac.getCarState(0, acsys.CS.Gear)
    if gear != lastgear:
        lastgear = gear
        gear = "RN"[gear] if gear <= 1 else str(gear - 1)
        ac.log(gear)
        ac.setText(label_gear, gear)
