import pickle

WIDTH = 416
HEIGHT = 300

s = 5
l = [[0,0]]
for i in range(0,300,2*s):
    l.extend([[416,i], [416, i+s], [s,i+s], [s,i+2*s]])

with open('test.eas', 'wb') as handle:
    pickle.dump(l, handle, protocol=pickle.HIGHEST_PROTOCOL)