import numpy as np
import math
from math import sqrt

def calcrk(distance_list,k):

    r_k=[]
    tup = tuple(distance_list)
    #print "tup:",tup

    d_max=max(tup)
    d_min=min(tup)

    return math.log((d_max-d_min)/d_min,10)

def CalculateEuclidean(list1,list2,k):

        var1=[]
        var2=[]
        sum=0

        if k==1:
                var1.append(list1[0])
                var2.append(list2[0])

        else:
            for j in range(0,k-1):
                var1.append(list1[0][j])
                var2.append(list2[0][j])

        for i in range(0,len(var1)):
            sum+=math.pow(var2[i]-var1[i],2)

        return sqrt(sum)


def extractPoint(input,k,n):

        #we have to compute distance between every pair of points
        #print "data points:",n
        #print "dimension:",k
        distance=[]
        if k==1:
            for i in range(0,n-1):
                for j in range(i+1,n):
                    point1=input[i]
                    #print "point1:",point1
                    point2=input[j]
                    #print "point2:",point2
                    distance.append(CalculateEuclidean(point1,point2,k))

        else:
            for i in range(0,n-1):
                for j in range(i+1,n):
                    point1=input[[i][0:k-1]]
                    #print "point1:",point1
                    point2=input[[j][0:k-1]]
                    #print "point2:",point2
                    distance.append(CalculateEuclidean(point1,point2,k))

        #for i in range(0,len(distance)):
            #print "distance:",distance[i]

        return calcrk(distance,k)

def writetofile(dimension,r_k,data_point):

        if(data_point == 100):
            file=open("Output_100.csv","a")
        elif(data_point==1000):
            file=open("Output_1000.csv","a")
        else:
            file=open("Output_10000.csv","a")
        file.write(str(dimension))
        file.write(",")
        file.write(str(r_k))
        file.write("\n")

def dimesionality():

        limit=[100,1000,1000]
        for n in limit:
            for k in range(1,100):
                 #print "k:",k
                 result=np.random.uniform(0,1,size=(n,k))
                 r_k=extractPoint(result,k,n)
                 writetofile(k,r_k,n)

dimesionality()
