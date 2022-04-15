import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
HList = df["math score"].tolist()
WList = df["reading score"].tolist()

meanH = statistics.mean(HList)
meanW = statistics.mean(WList)

medianH = statistics.median(HList)
medianW = statistics.median(WList)

modeH = statistics.mode(HList)
modeW = statistics.mode(WList)

print("mean,median,mode of Height is {} , {} , {}".format(meanH,medianH,modeH))
print("mean,median,mode of Weight is {} , {} , {}".format(meanW,medianW,modeW))

stdH = statistics.stdev(HList)
stdW = statistics.stdev(WList)

stdHStart, stdHEnd = meanH - stdH , meanH + stdH
stdHStart2, stdHEnd2 = meanH - (2*stdH) , meanH + (2*stdH)
stdHStart3, stdHEnd3 = meanH - (3*stdH) , meanH + (3*stdH) 

stdWStart, stdWEnd = meanW - stdW , meanW + stdW
stdWStart2, stdWEnd2 = meanW - (2*stdW) , meanW + (2*stdW)
stdWStart3, stdWEnd3 = meanW - (3*stdW) , meanW + (3*stdW) 

Hlist1std = [result for result in HList if result > stdHStart and result < stdHEnd]
Hlist2std = [result for result in HList if result > stdHStart2 and result < stdHEnd2]
Hlist3std = [result for result in HList if result > stdHStart3 and result < stdHEnd3]

Wlist1std = [result for result in WList if result > stdWStart and result < stdWEnd]
Wlist2std = [result for result in WList if result > stdWStart2 and result < stdWEnd2]
Wlist3std = [result for result in WList if result > stdWStart3 and result < stdWEnd3]

print("{}% of data for math score lies within first standard deviation" . format(len(Hlist1std)* 100.0/len(HList)))
print("{}% of data for math score lies within second standard deviation" . format(len(Hlist2std)* 100.0/len(HList)))
print("{}% of data for math score within lies third standard deviation" . format(len(Hlist3std)* 100.0/len(HList)))\

print("{}% of data for reading score lies within first standard deviation" . format(len(Wlist1std)* 100.0/len(WList)))
print("{}% of data for reading score lies within second standard deviation" . format(len(Wlist2std)* 100.0/len(WList)))
print("{}% of data for reading score lies within third standard deviation" . format(len(Wlist3std)* 100.0/len(WList)))