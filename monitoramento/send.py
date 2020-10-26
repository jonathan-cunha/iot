import os
import sys

HOST = sys.argv[1]
PORT = sys.argv[2]

def send(msg):
  print("Sending number: {} ...".format(msg))
  os.system("mosquitto_pub -h {} -p {} -t raspberry/keyboard -q 1 -m {}".format(HOST, PORT, msg))
  print("Done!")
  
  
def main():
  while True:
    msg = input("Enter a number: ")
    if msg == "end": break
    send(msg)
    
main()
