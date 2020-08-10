#!/usr/bin/python3.6
import random
import os
n1 = random.random()
n2 = random.random()
n3=random.random()

n4=n1*n2*n3

os.system("rm -f /root/Desktop/workspace/GithubPush/a")


os.system("git --git-dir=/root/Desktop/workspace/GithubPush/.git --work-tree=/root/Desktop/workspace/GithubPush/ add .")

os.system("git --git-dir=/root/Desktop/workspace/GithubPush/.git --work-tree=/root/Desktop/workspace/GithubPush/ commit -m {}".format(n4))
os.system("git --git-dir=/root/Desktop/workspace/GithubPush/.git --work-tree=/root/Desktop/workspace/GithubPush/ push HEAD:master")

