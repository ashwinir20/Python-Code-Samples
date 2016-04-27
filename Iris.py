import statistics as stat
import matplotlib as mp
import matplotlib.pyplot as pl

class StatPlot:

    master_list=[]
    setosa_s_l=[]
    versicolor_s_l=[]
    virginica_s_l=[]
    setosa_s_w=[]
    versicolor_s_w=[]
    virginica_s_w=[]
    setosa_p_l=[]
    versicolor_p_l=[]
    virginica_p_l=[]
    setosa_p_w=[]
    versicolor_p_w=[]
    virginica_p_w=[]

    def BoxPlot(self):

        index=[0,3,6,9]
        label=['Sepal Length','Sepal Width','Petal Length','Petal Width']
        j=0

        for i in index:
            data=[StatPlot.master_list[i],StatPlot.master_list[i+1],StatPlot.master_list[i+2]]
            pl.boxplot(data)
            pl.xlabel("Iris Dataset")
            pl.ylabel(label[j])
            pl.xticks([1, 2, 3], ['Iris-Setosa', 'Iris-Versicolor', 'Iris-Virginica'])
            pl.show()
            j+=1

        print("done")

    def SummaryStatisticsOverall(self):

        sepal_length=[]
        sepal_width=[]
        petal_length=[]
        petal_width=[]
        for line in open("C:/data/Iris.txt","r").readlines():
            list = line.split(',')
            sepal_length.append(float(list[0]))
            sepal_width.append(float(list[1]))
            petal_length.append(float(list[2]))
            petal_width.append(float(list[3]))

        print("Average of Sepal Length:",stat.mean(sepal_length),"Standard Deviation:",stat.stdev(sepal_length))
        print("Average of Sepal Width:",stat.stdev(sepal_width),"Standard Deviation:",stat.stdev(sepal_width))
        print("Average of Petal Length:",stat.mean(petal_length),"Standard Deviation:",stat.stdev(petal_length))
        print("Average of Petal Width:",stat.mean(petal_width),"Standard Deviation:",stat.stdev(petal_width))


    def SummaryStatisticsIndividual(self):

        setosa_sepal_width=[]
        setosa_petal_length=[]
        setosa_petal_width=[]
        versicolor_sepal_width=[]
        versicolor_petal_length=[]
        versicolor_petal_width=[]
        virginica_sepal_width=[]
        virginica_petal_length=[]
        virginica_petal_width=[]
        setosa_sepal_length=[]
        versicolor_sepal_length=[]
        virginica_sepal_length=[]
        for lines in open("C:/data/Iris.txt","r").readlines():
            line= lines.split(',')
            if 'setosa' in line[4]:
                setosa_sepal_length.append(float(line[0]))
                setosa_sepal_width.append(float(line[1]))
                setosa_petal_length.append(float(line[2]))
                setosa_petal_width.append(float(line[3]))
            elif 'versicolor' in line[4]:
                versicolor_sepal_length.append(float(line[0]))
                versicolor_sepal_width.append(float(line[1]))
                versicolor_petal_length.append(float(line[2]))
                versicolor_petal_width.append(float(line[3]))
            else:
                virginica_sepal_length.append(float(line[0]))
                virginica_sepal_width.append(float(line[1]))
                virginica_petal_length.append(float(line[2]))
                virginica_petal_width.append(float(line[3]))

        print("Average of Setosa sepal length:",stat.mean(setosa_sepal_length),"Standard Dev:",stat.stdev(setosa_sepal_length))
        print("Average of Setosa sepal width:",stat.mean(setosa_sepal_width),"Standard Dev:",stat.stdev(setosa_sepal_width))
        print("Average of Setosa petal length:",stat.mean(setosa_petal_length),"Standard Dev:",stat.stdev(setosa_petal_length))
        print("Average of Setosa petal width:",stat.mean(setosa_petal_width),"Standard Dev:",stat.stdev(setosa_petal_width))
        print("Average of Versicolor sepal length:",stat.mean(versicolor_sepal_length),"Standard Dev:",stat.stdev(versicolor_sepal_length))
        print("Average of Versicolor sepal width:",stat.mean(versicolor_sepal_width),"Standard Dev:",stat.stdev(versicolor_sepal_width))
        print("Average of Versicolor petal length:",stat.mean(versicolor_petal_length),"Standard Dev:",stat.stdev(versicolor_petal_length))
        print("Average of Versicolor petal width:",stat.mean(versicolor_petal_width),"Standard Dev:",stat.stdev(versicolor_petal_width))
        print("Average of Virginica sepal length:",stat.mean(virginica_sepal_length),"Standard Dev:",stat.stdev(virginica_sepal_length))
        print("Average of Virginica sepal width:",stat.mean(virginica_sepal_width),"Standard Dev:",stat.stdev(virginica_sepal_width))
        print("Average of Virginica petal length:",stat.mean(virginica_petal_length),"Standard Dev:",stat.stdev(virginica_petal_length))
        print("Average of Virginica petal width:",stat.mean(virginica_petal_width),"Standard Dev:",stat.stdev(virginica_petal_width))

        StatPlot.setosa_s_l=setosa_sepal_length
        StatPlot.versicolor_s_l=versicolor_sepal_length
        StatPlot.virginica_s_l=virginica_sepal_length
        StatPlot.setosa_s_w=setosa_sepal_width
        StatPlot.versicolor_s_w=versicolor_sepal_width
        StatPlot.virginica_s_w=virginica_sepal_width
        StatPlot.setosa_p_l=setosa_petal_length
        StatPlot.versicolor_p_l=versicolor_petal_length
        StatPlot.virginica_p_l=virginica_petal_length
        StatPlot.setosa_p_w=setosa_petal_width
        StatPlot.versicolor_p_w=versicolor_petal_width
        StatPlot.virginica_p_w=virginica_petal_width
        StatPlot.master_list.append(StatPlot.setosa_s_l)
        StatPlot.master_list.append(StatPlot.versicolor_s_l)
        StatPlot.master_list.append(StatPlot.virginica_s_l)
        StatPlot.master_list.append(StatPlot.setosa_s_w)
        StatPlot.master_list.append(StatPlot.versicolor_s_w)
        StatPlot.master_list.append(StatPlot.virginica_s_w)
        StatPlot.master_list.append(StatPlot.setosa_p_l)
        StatPlot.master_list.append(StatPlot.versicolor_p_l)
        StatPlot.master_list.append(StatPlot.virginica_p_l)
        StatPlot.master_list.append(StatPlot.setosa_p_w)
        StatPlot.master_list.append(StatPlot.versicolor_p_w)
        StatPlot.master_list.append(StatPlot.virginica_p_w)



StatPlot().SummaryStatisticsIndividual()
StatPlot().SummaryStatisticsOverall()
StatPlot().BoxPlot()






