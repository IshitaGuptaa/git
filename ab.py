#!/usr/bin/python3.6
import random
import os

from git import Repo
repo = Repo('/root/Desktop/workspace/GithubPush')  # if repo is CWD just do '.'

n1 = random.random()
n2 = random.random()
n3=random.random()

n4=n1*n2*n3


os.system("touch a")

repo.index.add(['a'])
print(1)
repo.index.commit('n4')
print(2)
origin = repo.remote('git')
print(11)
origin.push()



#os.system("git add .")

#os.system("git commit -m {}".format(n4)) 
#os.system("git push")


