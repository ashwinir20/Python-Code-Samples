import scipy.stats as sp
import heapq as hp
import matplotlib.pyplot as plot
import matplotlib as mat

class Wine:

    master_dict={}
    alcohol=[]
    malic_acid=[]
    ash=[]
    alcaline_ash=[]
    magnesium=[]
    total_phenols=[]
    flavanoids=[]
    nonflavanoid_phenols=[]
    cyanins=[]
    intensity=[]
    hue=[]
    od=[]
    proline=[]


    def ScatterPlot(self,key,value):


        fig=plot.figure(figsize=(6,6))

        ax=fig.add_subplot(1,1,1)

        ax.scatter(value[0],value[1],c='yellow',marker='*')

        ax.set_xlabel(key[0])
        ax.set_ylabel(key[1])

        name=key[0]+key[1]
        fig.savefig(name+".png")

    def dataDictPlot(self):

        dataDict={}

        dataDict[("Total Phenols","Od")]=[Wine.total_phenols,Wine.od]
        dataDict["Flavanoids","Od"]=[Wine.flavanoids,Wine.total_phenols]
        dataDict["Cyanins","Flavanoids"]=[Wine.flavanoids,Wine.od]
        dataDict["Total Phenols","Flavanoids"]=[Wine.total_phenols,Wine.flavanoids]
        dataDict["Non-Flavanoid Phenols","Flavanoids"]=[Wine.nonflavanoid_phenols,Wine.flavanoids]
        dataDict["Malic Acid","Hue"]=[Wine.malic_acid,Wine.hue]
        dataDict["Non-Flavanoid Phenols","Od"]=[Wine.nonflavanoid_phenols,Wine.od]
        dataDict["Hue","Itensity"]=[Wine.hue,Wine.intensity]

        for k,v in dataDict.items():
            Wine().ScatterPlot(k,v)


    def find_four_maxmin(corr_dict):

        val_list=[]
        val_list=corr_dict.values()

        maxlist=[]
        minlist=[]
        maxlist.append(hp.nlargest(4,val_list))
        minlist.append(hp.nsmallest(4,val_list))

        print("====================================================================")

        for item in maxlist:
            for key,value in corr_dict.items():
                if (item==value).any():
                    print("Maximum Correlation Pair:",key,value)

        print("====================================================================")

        for item in minlist:
            for key,value in corr_dict.items():
                if (item==value).any():
                    print("Minimum Correlation Pair:",key,value)

        print("====================================================================")


    def PearsonCorrelation(self):

        correlation_dict={}
        for key1,val in Wine.master_dict.items():
            for key2,valother in Wine.master_dict.items():
                if key1==key2: continue
                elif (key2,key1) in correlation_dict.keys(): continue
                else:
                    #print(sp.pearsonr(val,valother)[0])
                    correlation_dict[(key1,key2)]=sp.pearsonr(val,valother)[0]


        #for key,val in correlation_dict.items():
            #print("key:",key,"val:",val)

        Wine.find_four_maxmin(correlation_dict)


    def loadWineData(self):

        for lines in open("C:/data/Wine.txt","r").readlines():
            line=lines.split(',')
            Wine.alcohol.append(float(line[1]))
            Wine.malic_acid.append(float(line[2]))
            Wine.ash.append(float(line[3]))
            Wine.alcaline_ash.append(float(line[4]))
            Wine.magnesium.append(float(line[5]))
            Wine.total_phenols.append(float(line[6]))
            Wine.flavanoids.append(float(line[7]))
            Wine.nonflavanoid_phenols.append(float(line[8]))
            Wine.cyanins.append(float(line[9]))
            Wine.intensity.append(float(line[10]))
            Wine.hue.append(float(line[11]))
            Wine.od.append(float(line[12]))
            Wine.proline.append(float(line[13]))


        Wine.master_dict['alcohol']=Wine.alcohol
        Wine.master_dict['malic_acid']=Wine.malic_acid
        Wine.master_dict['ash']=Wine.ash
        Wine.master_dict['alcaline_ash']=Wine.alcaline_ash
        Wine.master_dict['magnesium']=Wine.magnesium
        Wine.master_dict['total_phenols']=Wine.total_phenols
        Wine.master_dict['flavanoids']=Wine.flavanoids
        Wine.master_dict['nonflavanoid_phenols']=Wine.nonflavanoid_phenols
        Wine.master_dict['cyanins']=Wine.cyanins
        Wine.master_dict['itensity']=Wine.intensity
        Wine.master_dict['hue']=Wine.hue
        Wine.master_dict['od']=Wine.od
        Wine.master_dict['proline']=Wine.proline


Wine().loadWineData()
Wine().PearsonCorrelation()
Wine().dataDictPlot()