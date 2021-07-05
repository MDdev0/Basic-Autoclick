import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

delay = 300.0
length = 2.0
button = Button.right
start_stop_key = Key.f6
exit_key = Key.f7

class ClickMouse(threading.Thread):
	def __init__(self, delay, length, button):
		super().__init__()
		self.delay = delay
		self.length = length
		self.button = button
		self.clicking = False
		self.program_running = True
	
	def start_clicking(self):
		self.clicking = True
	
	def stop_clicking(self):
		self.clicking = False
	
	def exit(self):
		self.stop_clicking()
		self.program_running = False
	
	def run(self):
		while self.program_running:
			while self.clicking:
				mouse.press(self.button)
				time.sleep(self.length)
				mouse.release(self.button)
				time.sleep(self.delay)
			time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, length, button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		if click_thread.clicking:
			click_thread.stop_clicking()
			print('Stopped clicking.')
		else:
			click_thread.start_clicking()
			print('Started clicking.')
	elif key == exit_key:
		print('Stopping...')
		click_thread.exit()
		listener.stop()

print('Startup complete. Starting listener.')

with Listener(on_press=on_press) as listener:
	listener.join()