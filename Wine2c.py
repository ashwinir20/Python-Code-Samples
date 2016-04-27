import scipy.spatial as sp
import numpy as np

class Wine:


    closestExampleDict_01={}
    closestExampleDict_zscore={}

    def calcDistance(self,point1,point2):

        return sp.distance.euclidean(point1,point2)

    def closestNeighbourPercentage(self):
        rowClass=[]
        for lines in open("C:/data/Wine.txt","r").readlines():
            line=lines.split(',')
            rowClass.append(int(line[0]))

        i=0
        closestNeighbour=0
        closestNeighbourClass1=0
        closestNeighbourClass2=0
        closestNeighbourClass3=0
        for k,v in Wine().closestExampleDict_01.items():
            if rowClass[i] == rowClass[v-1]:
                #print("row class of i",rowClass[i],"row class of v",rowClass[v])
                #print("here",i)
                closestNeighbour=closestNeighbour+1
            if (rowClass[i] == rowClass[v-1] ==1):
                    closestNeighbourClass1=closestNeighbourClass1+1
            if (rowClass[i] == rowClass[v-1] ==2):
                    closestNeighbourClass2=closestNeighbourClass2+1
            if (rowClass[i] == rowClass[v-1] ==3):
                    closestNeighbourClass3=closestNeighbourClass3+1
            i=i+1
        print("Closest Neighbour Percentage after 0-1 normalization:",float("{0:.2f}".format(100.0*closestNeighbour/178)))
        print("Class 1 Percentage after 0-1 normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass1/59)))
        print("Class 2 Percentage after 0-1 normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass2/71)))
        print("Class 3 Percentage after 0-1 normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass3/48)))

        i=0
        closestNeighbour=0
        closestNeighbourClass1=0
        closestNeighbourClass2=0
        closestNeighbourClass3=0

        for k,v in Wine().closestExampleDict_zscore.items():
            if rowClass[i] == rowClass[v-1]:
                #print("row class of i",rowClass[i],"row class of v",rowClass[v])
                #print("here",i)
                closestNeighbour=closestNeighbour+1
            if (rowClass[i] == rowClass[v-1] ==1):
                    closestNeighbourClass1=closestNeighbourClass1+1
            if (rowClass[i] == rowClass[v-1] ==2):
                    closestNeighbourClass2=closestNeighbourClass2+1
            if (rowClass[i] == rowClass[v-1] ==3):
                    closestNeighbourClass3=closestNeighbourClass3+1
            i=i+1
        print(closestNeighbour)
        print("Closest Neighbour Percentage after z-score normalization:",float("{0:.2f}".format(100.0*closestNeighbour/178)))
        print("Class 1 Percentage after z-score normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass1/59)))
        print("Class 2 Percentage after z-score normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass2/71)))
        print("Class 3 Percentage after z-score normalization:",float("{0:.2f}".format(100.0*closestNeighbourClass3/48)))


    def EuclideanDistance(self,data,rows,type):

        for i in range(0,rows):
            distDict={}
            for j in range(i+1,rows):
                euclideanDist=Wine().calcDistance(data[i],data[j])
                if i in distDict.keys():
                    distDict[i].append((j,euclideanDist))
                else:
                    distDict[i]=[(j,euclideanDist)]
                for k,v in distDict.items():
                    streamlist=[]
                    for val in v:
                        streamlist.append(val[1])
                    result=min(streamlist)
                    for val in v:
                        if val[1]==result:
                            if type == "zerone":
                                Wine().closestExampleDict_01[k]=val[0]
                            elif type == "zscore":
                                Wine().closestExampleDict_zscore[k]=val[0]

    def findStats_01(self,data):

        newList=[]
        minimum=min(data)
        maximum=max(data)


        #0-1 Normalization
        for each in data:
            new_val=(each-minimum)/(maximum-minimum)
            newList.append(new_val)

        return newList

    def findStats_znorm(self,data):

        newList=[]
        std_dev=np.std(data)
        mean=np.mean(data)

        #z-score Normalization
        for each in data:
            val=(each-mean)/std_dev
            newList.append(val)

        return newList

    def loadData(self):

        WineArray=np.loadtxt("C:/data/Wine.txt",delimiter=',',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
        (rows,cols)=WineArray.shape
        print(rows,cols)
        zero_one=np.empty(shape=[rows, cols])
        z_norm=np.empty(shape=[rows, cols])

        WineArray=np.loadtxt("C:/data/Wine.txt",delimiter=',',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13))
        #print(WineArray[:,12])
        #calculate minimum, maximum standard deviation for each attribute
        for i in range(0,13):
          list=WineArray[:,i]
          zeroOneList=Wine().findStats_01(list)
          zscoreList=Wine().findStats_znorm(list)
          zero_one[:,i]=zeroOneList
          z_norm[:,i]=zscoreList

        Wine().EuclideanDistance(zero_one,rows,"zerone")
        Wine().EuclideanDistance(z_norm,rows,"zscore")


Wine().loadData()
Wine().closestNeighbourPercentage()