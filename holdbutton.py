import time
import threading

from pynput import mouse, keyboard
from pynput.keyboard import Key

start_stop_key = Key.f12
exit_key = Key.f10

running = False
holding = []

kb = keyboard.Controller()
m = mouse.Controller()

def on_release(key):
	global running
	if key == start_stop_key:
		if running:
			for k in holding:
				kb.release(k)
			print('Will no longer hold keys. Released all keys.')
			running = False
		else:
			print('Will now hold all keys (except F10 and F12)')
			running = True
	elif key == exit_key:
		print('Stopping...')
		for k in holding:
			kb.release(k)
		print('Released all keys.')
		running = False
		kblistener.stop()
		mlistener.stop()
	elif running:
		if key not in holding:
			kb.press(key)
			holding.append(key)
			print('Holding ' + str(key))

def on_click(button):
	global running
	if running:
		if button not in holding:
			m.press(key)
			holding.append(key)
			print('Holding ' + str(button))

print('Startup complete. Starting listener.')

with keyboard.Listener(on_release=on_release) as kblistener:
	kblistener.join()
with mouse.Listener(on_click=on_click) as mlistener:
	mlistener.join()
