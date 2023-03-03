# Win Automation 
# pip install ahk
import ahk
auto = ahk.AHK()
# Mouse actions
auto.mouse_move(100, 100)
auto.mouse_click()
auto.mouse_drag(100, 100, 200, 200)
auto.mouse_wheel(1)
auto.get_mouse_position()
# Keyboard actions
auto.key_press('p')
auto.key_down('p')
auto.key_up('p')
auto.key_toggle('CapsLock', True)
auto.type('Hello World')
auto.key_press('Ctrl + Shift + P')
# Window actions
auto.run_script("chrome.exe")
app  = auto.find_window(title="Google Chrome")
app.activate()
app.maximize()
app.minimize()
app.send("Python")
app.kill()
