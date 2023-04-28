#!/usr/bin/env python3
import os

if __name__ == '__main__':
    for i in range(4):
        os.system(f"sudo chmod 666 /dev/ttyACM{i}")