# numpad H-shifter by krussy
# ------------------------------
# Trying to read keyboard numpad inputs as a separate controller to use as an H-shifter
# Gonna need to package vJoy or ViGem, not sure yet
# ------------------------------

import sys
import ac
import acsys

from third_party.sim_info import *

appName = "keyboard shifter"
appWindow = 0
lastgear = 0
label_gear = 0

# simInfo = SimInfo()


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version):
    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow, label_gear # <- you'll need to update your window in other functions.
    
    appWindow = ac.newApp(appName)
    # ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, 200, 200)

    ac.log("hello deez nutzs")
    label_gear = ac.addLabel(appWindow, 'N')
    ac.setPosition(label_gear, 100, 100)

    # ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function

    return appName


def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    """
    This is where you redraw your openGL graphics
    if you need to use them .
    """
    pass # -> Delete this line if you do something here !

def acUpdate(deltaT):#-------------------------------- AC UPDATE
    global lastgear, label_gear
    gear = ac.getCarState(0, acsys.CS.Gear)
    if gear != lastgear:
        lastgear = gear
        gear = "RN"[gear] if gear <= 1 else str(gear - 1)
        ac.log(gear)
        ac.setText(label_gear, gear)

    pass # -> Delete this line if you do something here !
