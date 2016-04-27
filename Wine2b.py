import scipy.spatial as sp
import numpy as np

class WineDistance:

    closestExampleDict={}

    def closestNeighbourPercentage(self):
        rowClass=[]
        for lines in open("C:/data/Wine.txt","r").readlines():
            line=lines.split(',')
            rowClass.append(int(line[0]))
        closestNeighbour=0
        closestNeighbourClass1=0
        closestNeighbourClass2=0
        closestNeighbourClass3=0
        for k,v in WineDistance().closestExampleDict.items():
            if rowClass[k] == rowClass[v-1]:
                closestNeighbour=closestNeighbour+1
            if (rowClass[k] == rowClass[v-1] ==1):
                closestNeighbourClass1+=1
            if (rowClass[k] == rowClass[v-1] ==2):
                closestNeighbourClass2+=1
            if (rowClass[k] == rowClass[v-1] ==3):
                closestNeighbourClass3+=1
        print("Closest Neighbour Percentage:",float("{0:.2f}".format(100.0*closestNeighbour/178)))
        print("Class 1 Percentage:",float("{0:.2f}".format(100.0*closestNeighbourClass1/59)))
        print("Class 2 Percentage:",float("{0:.2f}".format(100.0*closestNeighbourClass2/71)))
        print("Class 3 Percentage:",float("{0:.2f}".format(100.0*closestNeighbourClass3/48)))

    def printClosestExample(self):

        for key,value in WineDistance.closestExampleDict.items():
            print("Closest row to",key,"is",value)


    def EuclideanDistance(self,example1,example2):

        return sp.distance.euclidean(example1,example2)

    def loadWineExamples(self):
            WineArray=np.loadtxt("C:/data/Wine.txt",delimiter=',',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))

            (rows,columns) =WineArray.shape
            #print("rows",rows)

            for i in range(0,rows):
                distDict={}
                for j in range(i+1,rows):
                    euclideanDist=WineDistance().EuclideanDistance(WineArray[i],WineArray[j])
                    if i in distDict.keys():
                        distDict[i].append((j,euclideanDist))
                    else:
                        distDict[i]=[(j,euclideanDist)]
                for k,v in distDict.items():
                    streamlist=[]
                    for val in v:
                        streamlist.append(val[1])
                    result=min(tuple(streamlist))
                    for val in v:
                        if val[1]==result:
                            WineDistance().closestExampleDict[k]=val[0]


WineDistance().loadWineExamples()
WineDistance().printClosestExample()
WineDistance().closestNeighbourPercentage()