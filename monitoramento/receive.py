import os
import sys

HOST = sys.argv[1]
PORT = sys.argv[2]

def receive():
  os.system("mosquitto_pub -v -h {} -p {} -t raspberry/keyboard".format(HOST, PORT))
  print("Done!")
  
  
def main():
  receive()
    
main()
