import numpy as np

def fillSeq(selectedSeqName):
    seqFile = open("./auxiliary2023/" + selectedSeqName + ".txt", "r")
    seq = []
    lines = seqFile.readlines()[1:]
    for line in lines:
        for letter in line:
            seq.append(letter)
    seqFile.close()
    return seq

seq1 = fillSeq(input("Select first sequence to use (brain, liver or muscle)"))
seq2 = fillSeq(input("Select second sequence to use (brain, liver or muscle)"))

print(str(len(seq1)) + " seq1 length")
print(str(len(seq2)) + " seq2 length")

canWin = np.ones((len(seq1)+1, len(seq2)+1), dtype=bool)
wasRemovedFromI = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)
wasRemovedFromJ = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)
for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        if (i-1>=0 and j-2>=0) or (i>=2 and j>=1):
            if i-1>=0 and j-2>=0:
                if canWin[i-1][j-2]:
                    canWin[i][j] = False
                else:
                    canWin[i][j] = True
                wasRemovedFromI[i][j] = -1
                wasRemovedFromJ[i][j] = -2
            if i>=2 and j>=1:
                if not(canWin[i][j]):
                    if canWin[i-2][j-1]:
                        canWin[i][j] = False
                    else:
                        canWin[i][j] = True
                    wasRemovedFromI[i][j] = -2
                    wasRemovedFromJ[i][j] = -1
        else:
            canWin[i][j] = True

if canWin[-1][-1]:
    print("Player A won.")
else:
    print("Player A lost.")

for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        print("["+str(i)+", "+str(j)+"]" +str(canWin[i][j]))
        print("["+str(wasRemovedFromI[i][j])+", "+str(wasRemovedFromJ[i][j])+"]")