import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
readingList = df["reading score"].to_list()
writingList = df["writing score"].to_list()

rmean = statistics.mean(readingList)
wmean = statistics.mean(writingList)

rmedian = statistics.median(readingList)
wmedian = statistics.median(writingList)

rmode = statistics.mode(readingList)
wmode = statistics.mode(writingList)

rstdev = statistics.stdev(readingList)
wstdev = statistics.stdev(writingList)

print("mean,median,mode,stdev of Reading is {},{},{},{} respectively".format(rmean,rmedian,rmode,rstdev))
print("mean,median,mode,stdev of Writing is {},{},{},{} respectively".format(wmean,wmedian,wmode,wstdev))

rfirststdevstart,rfirststdevend = rmean - rstdev,rmean + rstdev
wfirststdevstart,wfirststdevend = wmean - wstdev,wmean + wstdev

rsecondstdevstart,rsecondstdevend = rmean - (2*rstdev),rmean + (2*rstdev)
wsecondstdevstart,wsecondstdevend = wmean - (2*wstdev),wmean + (2*wstdev)

rthirdstdevstart,rthirdstdevend = rmean - (3*rstdev),rmean + (3*rstdev)
wthirdstdevstart,wthirdstdevend = wmean - (3*wstdev),wmean + (3*wstdev)

rdatafirststdev = [result for result in readingList if result > rfirststdevstart and result < rfirststdevend]
wdatafirststdev = [result for result in writingList if result > wfirststdevstart and result < wfirststdevend]

rdatasecondstdev = [result for result in readingList if result > rsecondstdevstart and result < rsecondstdevend]
wdatasecondstdev = [result for result in writingList if result > wsecondstdevstart and result < wsecondstdevend]

rdatathirdstdev = [result for result in readingList if result > rthirdstdevstart and result < rthirdstdevend]
wdatathirdstdev = [result for result in writingList if result > wthirdstdevstart and result < wthirdstdevend]

print("{}% data for reading lies within firststdev".format(len(rdatafirststdev)*100.0/len(readingList)))
print("{}% data for reading lies within secondstdev".format(len(rdatasecondstdev)*100.0/len(readingList)))
print("{}% data for reading lies within thirdstdev".format(len(rdatathirdstdev)*100.0/len(readingList)))

print("{}% data for writing lies within firststdev".format(len(wdatafirststdev)*100.0/len(writingList)))
print("{}% data for writing lies within secondstdev".format(len(wdatasecondstdev)*100.0/len(writingList)))
print("{}% data for writing lies within thirdstdev".format(len(wdatathirdstdev)*100.0/len(writingList)))

