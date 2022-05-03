import sys
k = sys.getrecursionlimit()
sys.setrecursionlimit(100000000)
print (k)

def chik():
    print(k)
    chik()

chik()