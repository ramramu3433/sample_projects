from subprocess import Popen,PIPE

t=Popen(["ls"],stdout=PIPE)
print([ line for line in t.stdout])
