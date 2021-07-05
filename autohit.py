import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

delay = 1.1
button = Button.left
start_stop_key = Key.f9
auto_scroll_key = Key.f8
exit_key = Key.f10

class ClickMouse(threading.Thread):
	def __init__(self, delay, button):
		super().__init__()
		self.delay = delay
		self.button = button
		self.clicking = False
		self.scrolling = False
		self.program_running = True
	
	def start_clicking(self):
		self.clicking = True
	
	def stop_clicking(self):
		self.clicking = False
	
	def start_scrolling(self):
		self.scrolling = True
	
	def stop_scrolling(self):
		self.scrolling = False
	
	def exit(self):
		self.stop_clicking()
		self.stop_scrolling()
		self.program_running = False
	
	def run(self):
		while self.program_running:
			while self.clicking:
				mouse.click(self.button)
				if self.scrolling:
					mouse.scroll(0, 1)
				time.sleep(self.delay)
			time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
	if key == start_stop_key:
		if click_thread.clicking:
			click_thread.stop_clicking()
			print('Stopped clicking.')
		else:
			click_thread.start_clicking()
			print('Started clicking.')
	elif key == auto_scroll_key:
		if click_thread.scrolling:
			click_thread.stop_scrolling()
			print('Stopped scrolling.')
		else:
			click_thread.start_scrolling()
			print('Started scrolling.')
	elif key == exit_key:
		print('Stopping...')
		click_thread.exit()
		listener.stop()

print('Startup complete. Starting listener.')

with Listener(on_press=on_press) as listener:
	listener.join()