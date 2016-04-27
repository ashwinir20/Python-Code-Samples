from nltk.compat import raw_input
import numpy as np

class AprioriSolution:


    attribute_names=[]

    candidate_master_dict={}

    #dictionary to store 1-frequent itemsets
    attribute_column={}
    candidate_one_itemsets={}
    candidate_one_support={}
    candidate_one_support_pruned={}
    candidate_two={}
    candidate_two_support={}
    candidate_two_support_pruned={}

    def  calculate_candidate_one_itemsets(self,column,no_of_rows,attribute_name):

        #read each column of the transaction matrix and create a dictionary that has the count of the occurence of 1
        for each in column:
            if each == 1:
                if attribute_name in AprioriSolution.candidate_one_itemsets.keys():
                    AprioriSolution.candidate_one_itemsets[attribute_name]+=1
                else:
                    AprioriSolution.candidate_one_itemsets[attribute_name]=1

    def calculate_candidate_one_support(self,rows,support):

        #creating a dictionary that has the 1-itemset and its support count
        for key,value in AprioriSolution.candidate_one_itemsets.items():
            calc_support=value/rows;
            AprioriSolution.candidate_one_support[key]=round(calc_support,2);

        #for key,val in AprioriSolution.candidate_one_support.items():
            #print("candidate-one-before",key,"support",val);

        #pruning the candidate one itemsets that do not satisfy the minimum support
        for key,val in AprioriSolution.candidate_one_support.items():
            if val >= float(support):
                AprioriSolution.candidate_one_support_pruned[key]=val

        #after pruning
        #for key,val in AprioriSolution.candidate_one_support_pruned.items():
            #print("candidate-one-pruned",key,"support",val);

        number=1
        AprioriSolution.candidate_master_dict[number]=AprioriSolution.candidate_one_support_pruned;

    def calculate_candidate_two_support(self,row,support,DataMatrix):

         candidate_one_pruned=[]
         #generating candidate itemsets of length 2 from frequent one candidate itemset
         for key in AprioriSolution.candidate_one_support_pruned.keys():
            candidate_one_pruned.append(key)

         for i in range(0,len(candidate_one_pruned)):
             for j in range(i+1,len(candidate_one_pruned)):
                 AprioriSolution.candidate_two[candidate_one_pruned[i],candidate_one_pruned[j]]=0


         for key,val in AprioriSolution.candidate_two.items():
            column_first=AprioriSolution.attribute_column.get(key[0])
            column_second=AprioriSolution.attribute_column.get(key[1])
            list_one=DataMatrix[:,column_first]
            list_second=DataMatrix[:,column_second]
            count=0
            for i in range(0,len(list_one)):
                if list_one[i] == list_second[i] == 1:
                    count+=1
            AprioriSolution.candidate_two_support[key[0],key[1]]=count

         for key,value in AprioriSolution.candidate_two_support.items():
            calc_support=value/row;
            AprioriSolution.candidate_two_support[key]=round(calc_support,2);

         #for key,val in AprioriSolution.candidate_two_support.items():
            #print("candidate-two-before",key,"support",val);

         #pruning the candidate two itemsets that do not satisfy the minimum support
         for key,val in AprioriSolution.candidate_two_support.items():
            if val >= float(support):
                AprioriSolution.candidate_two_support_pruned[key]=val

         #after pruning
         #for key,val in AprioriSolution.candidate_two_support_pruned.items():
            #print("candidate-two-pruned",key,"support",val);

         number=2
         AprioriSolution.candidate_master_dict[number]=AprioriSolution.candidate_two_support_pruned;

    def calculate_candidate_k_1(self,rows,support,DataMatrix,num):

        #for key,value in AprioriSolution.candidate_master_dict.items():
            #print("master key",key,"value",value)

        #get k-1 dictionary from the master dictionary

        dict_k_1={}
        dict_k_1=AprioriSolution.candidate_master_dict.get(num-1)

        #generate candidate-k itemset by joining k-1 with k-1 only if first k-2 itemes match

        itemset_list=[]
        for itemset in dict_k_1.keys():
            itemset_list.append(itemset)

        dict_k={}
        j=num-2
        print("j",j)
        for each in itemset_list:
            for other in itemset_list:
                if each == other: continue
                else:
                    itemset_i=each
                    itemset_j=other
                    count=0
                for k in range(0,j):
                    if itemset_i[k] == itemset_j[k]:
                        count+=1
                if count == j:
                    dict_k[tuple(set(itemset_i).union(set(itemset_j)))]=0
                    #print(list(set(itemset_i).union(set(itemset_j))))

          #pruning the k-candidate itemset using the support count
        dict_k_pruned_support={}
        for key in dict_k.keys():
            list_of_key=[]
            for each in key:
                list_of_key.append(AprioriSolution().attribute_column.get(each))

            list_of_data_columns=[]
            for i in range(0,len(list_of_key)):
                list_of_data_columns.append(DataMatrix[:,list_of_key[i]])

            support_count=0
            for i in range(0,rows):
                count=0
                for j in range(0,len(list_of_data_columns)):
                    if list_of_data_columns[j][i] == 1:
                       count+=1
                    if count == num:
                        support_count+=1

            dict_k_pruned_support[key]=support_count

        dict_k_support_final={}
        for key,val in dict_k_pruned_support.items():
            calc_support=val/rows
            rounded_support=round(calc_support,2)
            #print("support value",rounded_support)
            if  rounded_support >= float(support):
                dict_k_support_final[key]=rounded_support

        AprioriSolution.candidate_master_dict[num]=dict_k_support_final;
        if len(dict_k_support_final) == 0:
            return 0
        else: return 1


    def start_apriori(self):
        #First, ask the user to input support and confidence
        support=raw_input("Enter the support for the dataset:");
        #confidence=raw_input("Enter the confidence for the dataset:");

        number_of_attributes=raw_input("Enter the number of attributes for this dataset:");
        for i in range(0,int(number_of_attributes)):
            label=raw_input("Enter the attribute label:");
            AprioriSolution.attribute_names.append(label)
            AprioriSolution.attribute_column[label]=i

        for key,val in AprioriSolution.attribute_column.items():
            print("column name",key,"column no",val)

        #reading the file into numpy array
        DataMatrix=np.loadtxt("C:/Users/dell/PycharmProjects/Homework4/Output_Contraceptive.txt",delimiter=',')
        (row,column)=DataMatrix.shape

        #reading each column one by one
        for i in range(0,9):
            column=DataMatrix[:,i]
            AprioriSolution().calculate_candidate_one_itemsets(column,row,AprioriSolution.attribute_names[i]);

        for key,val in AprioriSolution.candidate_one_itemsets.items():
            print(key,val);

        AprioriSolution.calculate_candidate_one_support(self,row,support)

        AprioriSolution.calculate_candidate_two_support(self,row,support,DataMatrix)

        m=number_of_attributes
        for i in range(3,int(m)+1):
            val=AprioriSolution.calculate_candidate_k_1(self,row,support,DataMatrix,i)
            if val == 0:
                break

        for k,frequent_item in AprioriSolution.candidate_master_dict.items():
            print("k",k,"itemset frequent",frequent_item)

AprioriSolution().start_apriori()