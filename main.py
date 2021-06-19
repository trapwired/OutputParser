
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    with open("out.txt", "r") as f:
        nextLn = f.readline()
        values_loss = []
        values_perfM = []
        sums = 0
        count = 0
        sums_p = 0
        count_p = 0
        inEpoch = True
        inEval = False
        inTest = False
        while nextLn != '':
            if nextLn.startswith('Epoch: ') and sums != 0:
                inEpoch = True
                inEval = False
                f.readline()
                values_loss.append(sums / count)
                sums = 0
                count = 0
                values_perfM.append(sums_p / count_p)
                sums_p = 0
                count_p = 0
            elif nextLn.startswith('##### TRAINING'):
                inEpoch = True
                inEval = False
                inTest = False
            elif nextLn.startswith('##### EVAL'):
                inEpoch = False
                inEval = True
                inTest = False
            elif nextLn.startswith('##### TEST'):
                inEpoch = False
                inEval = False
                inTest = True
            elif nextLn.startswith('Iter:'):
                if inEpoch:
                    nextLnAr = nextLn.split(':')
                    loss = nextLnAr[2]
                    count += 1
                    sums += float(loss[1:6])
                elif inEval:
                    nextLnAr = nextLn.split(':')
                    perfM = nextLnAr[3]
                    count_p += 1
                    sums_p += float(perfM[1:6])
                elif inTest:
                    pass
            nextLn = f.readline()
        # add last value
        values_loss.append(sums / count)
        sums = 0
        count = 0
        values_perfM.append(sums_p / count_p)
        sums_p = 0
        count_p = 0
    #print(values_loss)
    #print(values_perfM)
    zmin = np.min(values_perfM)
    loc_min = values_perfM.index(zmin)
    print(f"min found in epoch: {loc_min}, is: {zmin}")
    plt.figure(1)
    plt.subplot(211)

    plt.plot(values_loss)
    plt.ylabel('loss in training')
    plt.subplot(212)
    plt.plot(values_perfM)
    plt.ylabel('perf_metric')
    plt.show()
