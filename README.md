# ac-kbShifter
An Assetto Corsa app to use your keyboard as an H-shifter. Intended to use your numpad as a controller input for various H-shifter patterns e.g., 4R, 6R, direct select 9.
## Installation
Drag .zip file into Content Manager and click install, or manually paste the contents of the .zip in the root folder of your Assetto Corsa installation. After install, the app must be activated in your AC settings.
## Configuration
bottom text
## Why?
The closest thing I found for this purpose is [levamak's Keyboard H-Shifter][1] which uses vJoy to emulate the controller. But, it stores its input settings in text format, so only alphanumerics are supported. No special keys, and with the pynput implementation, digits only correspond to number row keys.

At first I was going to fork and change its input to use positional keycodes, but since AC supports Python scripts I decided to make a new app that's more integrated with the game.
Going with ViGEmBus becuase the script can create an emulated controller seamlessly, no extra setup steps needed like with vJoy.
## Notes
- ViGEmBus is deprecated as of v1.22 Nov 2023 but I will continue to use its framework until it doesn't work anymore or a successor is released.
- Interested in AC app development? [Here's my resources](https://github.com/kr1spyK/ac-kbShifter/wiki)
## Credits
- levamak, for creating a universal [keyboard H-shifter][1] app.

- Nefarious, for [Virtual Gamepad Emulation Bus Driver](https://github.com/nefarius/ViGEmBus)

[1]:https://github.com/levamak/Keyboard-H-Shifter
