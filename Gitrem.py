#!/usr/bin/python3.6
import random
import os
n1 = random.random()
n2 = random.random()
n3=random.random()

n4=n1*n2*n3


os.system("rm -rf a")
os.system("git add .")

os.system("git commit -m {}".format(n4))
os.system("git push")
