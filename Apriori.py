from nltk.compat import raw_input
import numpy as np
from itertools import combinations

class Apriori:

    attribute_names=[]

    candidate_master_dict={}
    candidate_master_dict_before_pruning={}


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
                if attribute_name in Apriori.candidate_one_itemsets.keys():
                    Apriori.candidate_one_itemsets[attribute_name]+=1
                else:
                    Apriori.candidate_one_itemsets[attribute_name]=1

    def calculate_candidate_one_support(self,rows,support):

        #creating a dictionary that has the 1-itemset and its support count
        for key,value in Apriori.candidate_one_itemsets.items():
            calc_support=value/rows;
            Apriori.candidate_one_support[key]=round(calc_support,2);

        number=1
        Apriori.candidate_master_dict_before_pruning[1]=Apriori.candidate_one_itemsets

        count_freq_before=0
        for key in Apriori.candidate_one_support.keys():
            count_freq_before+=1
            #print("candidate-one-before",key,"support",val);

        print("Frequent itemsets of length 1 before pruning",count_freq_before)

        #pruning the candidate one itemsets that do not satisfy the minimum support
        for key,val in Apriori.candidate_one_support.items():
            if val >= float(support):
                Apriori.candidate_one_support_pruned[key]=val

        #after pruning
        count_after=0
        for key,val in Apriori.candidate_one_support_pruned.items():
            count_after+=1
            print("candidate-one-pruned",key,"support",val);

        print("Frequent itemsets of length 1 before pruning",count_after)


        Apriori.candidate_master_dict[number]=Apriori.candidate_one_support_pruned;

    def calculate_candidate_two_support(self,row,support,DataMatrix):

         candidate_one_pruned=[]
         #generating candidate itemsets of length 2 from frequent one candidate itemset
         for key in Apriori.candidate_one_support_pruned.keys():
            candidate_one_pruned.append(key)

         for i in range(0,len(candidate_one_pruned)):
             for j in range(i+1,len(candidate_one_pruned)):
                 Apriori.candidate_two[candidate_one_pruned[i],candidate_one_pruned[j]]=0


         for key,val in Apriori.candidate_two.items():
            column_first=Apriori.attribute_column.get(key[0])
            column_second=Apriori.attribute_column.get(key[1])
            list_one=DataMatrix[:,column_first]
            list_second=DataMatrix[:,column_second]
            count=0
            for i in range(0,len(list_one)):
                if list_one[i] == list_second[i] == 1:
                    count+=1
            Apriori.candidate_two_support[key[0],key[1]]=count

         for key,value in Apriori.candidate_two_support.items():
            calc_support=value/row;
            Apriori.candidate_two_support[key]=round(calc_support,2);

         count_before_second=0
         for key,val in Apriori.candidate_two_support.items():
            count_before_second+=1

         number=2
         Apriori.candidate_master_dict_before_pruning[number]=Apriori.candidate_two_support


         print("Frequent itemsets of length 2 before pruning",count_before_second)


         #pruning the candidate two itemsets that do not satisfy the minimum support
         for key,val in Apriori.candidate_two_support.items():
            if val >= float(support):
                Apriori.candidate_two_support_pruned[key]=val

         #after pruning
         count_after=0
         for key,val in Apriori.candidate_two_support_pruned.items():
            count_after+=1

         print("Frequent itemsets of length 2 after pruning",count_after)

         Apriori.candidate_master_dict[number]=Apriori.candidate_two_support_pruned;

    def calculate_candidate_k(self,rows,support,DataMatrix,num):

        #generate candidate-k itemsets by joining k-1 and 1

        for key,value in Apriori.candidate_master_dict.items():
            print("master key",key,"value",value)

        #get k-1 dictionary from the master dictionary

        dict_k_1={}
        dict_k_1=Apriori.candidate_master_dict.get(num-1)

        dict_k={}
        #Join the k-1 keys with the 1 candidate itemsets
        for key in Apriori.candidate_one_support_pruned.keys():
           for k in dict_k_1.keys():
               length=len(k)
               new_key=[]
               new_key.append(key)
               for i in range(0,length):
                   new_key.append(k[i])
               if np.unique(new_key).size == len(new_key):
                   tup=tuple(new_key)
                   dict_k[tup]=0


        count_before_k=0
        for k in dict_k.keys():
            count_before_k+=1

        print("Number of candidate itemsets before pruning of k=",num,"is",count_before_k)

        #candidate pruning:  every item in the k candidate should occur k-1 times in  k-1 candidate itemsets
        #using the hueristic to minimize

        dict_count={}
        for k,value in dict_k_1.items():
            #print("key",k)
            for each in k:
                if each in dict_count.keys():
                    val=dict_count.get(each)
                    val=val+1
                    dict_count[each]=val
                else:
                    dict_count[each]=1


        dict_k_pruned={}
        for key in dict_k.keys():
            for each in key:
                if dict_count.get(each) >= num-1:
                    dict_k_pruned[key]=0


        #pruning the k-candidate itemset using the support count
        dict_k_pruned_support={}
        for key in dict_k.keys():
            list_of_key=[]
            for each in key:
                list_of_key.append(Apriori().attribute_column.get(each))

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
            dict_k_pruned_support[key]=rounded_support

        for key,val in dict_k_pruned_support.items():
            if  val >= float(support):
                dict_k_support_final[key]=val

        Apriori.candidate_master_dict_before_pruning[num]=dict_k_pruned_support

        count_after=0
        for freq_itemset in dict_k_support_final.keys():
            count_after+=1

        print("Number of frequent itemsets after pruning using support is",count_after)

        Apriori.candidate_master_dict[num]=dict_k_support_final;

        if len(dict_k_support_final) == 0:
            return 0
        else:
            return 1



    def calc_support(self,tuple_s,DataMatrix):


        list_of_key=[]
        for each in tuple_s:
            list_of_key.append(Apriori().attribute_column.get(each))

        list_of_data_columns=[]
        for i in range(0,len(list_of_key)):
            list_of_data_columns.append(DataMatrix[:,list_of_key[i]])

        support_count=0
        rows,cols=DataMatrix.shape
        for i in range(0,rows):
            count=0
            for j in range(0,len(list_of_data_columns)):
                    if list_of_data_columns[j][i] == 1:
                       count+=1
                    if count == len(tuple_s):
                        support_count+=1


        calc_support=support_count/rows
        rounded_support=round(calc_support,2)

        return rounded_support


    def count_maximal(self,master_dict):


        dict_maximal={}

        total_count_maximal=0
        for k,itemset in master_dict.items():
            list_of_maximal=[]
            #go through each immediate frequent itemset
            i=k+1
            if len(master_dict) < i:
                break
            else:
                super_set=master_dict.get(i)
                super_set_frequent=Apriori.candidate_master_dict.get(i)
                for freq_itemset,sup in itemset.items():
                    for super_itemset,super_sup in super_set.items():
                        if freq_itemset in super_itemset:
                            if super_itemset in super_set_frequent.keys():
                                #print("comparing if",freq_itemset,"is a subset of",super_itemset,"is present in",super_set_frequent)
                                #print("true")
                                continue
                            else:
                                #it is maximal
                                list_of_maximal.append(freq_itemset)
                                total_count_maximal+=1

            dict_maximal[k]=list_of_maximal


        #for val_k,maximal_set in dict_maximal.items():
            #for each in maximal_set:


        print("total number of maximal",total_count_maximal)



    def count_closed_frequent(self,master_dict):

        closed_dict={}
        total_count_closed=0
        for k,itemset in master_dict.items():
            list_of_closed=[]
            print("starting with k equal to",k)
            #go through each immediate frequent itemset
            i=k+1
            if len(master_dict) < i:
                break
            else:
                super_set_closed=master_dict.get(i)
                for freq_itemset_closed,support in itemset.items():
                    count=0
                    for super_itemset_closed,super_support in super_set_closed.items():
                        if freq_itemset_closed in super_itemset_closed:
                            if support == super_support:
                                count=count+1
                            if count == 0:
                                total_count_closed+=1
                                if freq_itemset_closed not in list_of_closed:
                                    list_of_closed.append(freq_itemset_closed)

            closed_dict[k]=list_of_closed

        print("closed itemsets",closed_dict)
        print("total closed",total_count_closed)

    def generate_rules(self,itemset_dict,DataMatrix,min_confidence):

        dict_of_subsets={}
        for key in itemset_dict.keys():
            s=set(key)
            subset=sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), [])
            dict_of_subsets[key]=subset

        rule_dict_pruned={}
        temp_rule={}
        for each,subset in dict_of_subsets.items():
            #print("each",each,"subset",subset)
            #GENERATING RULES
            for val_subset in subset:
                set_minus=set(each).difference(set(val_subset))
                if len(set_minus) ==0: continue
                else:
                    temp_rule[tuple(each)]=[val_subset,set_minus]

        # got the rules, now prune them based on confidence min_con >= support(each)/support(s)
        rules_pruned={}
        for superset,rule in temp_rule.items():
            support_count_sup=Apriori().calc_support(superset,DataMatrix)
            support_count_s=Apriori().calc_support(rule[0],DataMatrix)
            confidence=support_count_sup/support_count_s
            rounded_confidence=round(confidence,2)
            if rounded_confidence >= float(min_confidence):
                rules_pruned[rule[0]]=rule[1]

        for subse,conse in rules_pruned.items():
            print("subsequent",subse,"consequent=========>",conse)

    def generate_rules_lift(self,itemset_dict,DataMatrix,lift):

        dict_of_subsets={}
        for key in itemset_dict.keys():
            s=set(key)
            subset=sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), [])
            dict_of_subsets[key]=subset

        rule_dict_pruned={}
        temp_rule={}
        for each,subset in dict_of_subsets.items():
            #print("each",each,"subset",subset)
            #GENERATING RULES
            for val_subset in subset:
                set_minus=set(each).difference(set(val_subset))
                if len(set_minus) ==0: continue
                else:
                    temp_rule[tuple(each)]=[val_subset,set_minus]

        # got the rules, now prune them based on confidence min_con >= support(each)/support(s)
        rules_pruned={}
        for superset,rule in temp_rule.items():
            support_count_sup=Apriori().calc_support(superset,DataMatrix)
            support_count_s=Apriori().calc_support(rule[0],DataMatrix)
            confidence=support_count_sup/support_count_s
            rounded_confidence=round(confidence,2)
            support_count_c=Apriori().calc_support(rule[1],DataMatrix)
            calc_lift=confidence/support_count_c
            if calc_lift >= float(lift):
                rules_pruned[rule[0]]=rule[1]

        for subse,conse in rules_pruned.items():
            print("LHS of Rule",subse,"RHS of Rule",conse)

        print("using lift")


    def Apriori_1_kminus1(self):

        #First, ask the user to input support and confidence
        support=raw_input("Enter the support for the dataset:");
        confidence=raw_input("Enter the confidence for the dataset:");
        lift=raw_input("Enter the lift measure for the dataset:")
        check=raw_input("Would you like to use lift to generate the rules- enter Y or N, N implies confidence")

        number_of_attributes=raw_input("Enter the number of attributes for this dataset:");
        for i in range(0,int(number_of_attributes)):
            label=raw_input("Enter the attribute label:");
            Apriori.attribute_names.append(label)
            Apriori.attribute_column[label]=i

        for key,val in Apriori.attribute_column.items():
            print("column name",key,"column no",val)

        #reading the Tic Tac Toe file into numpy array
        DataMatrix=np.loadtxt("C:/Users/dell/PycharmProjects/Homework4/Output_Contraceptive.txt",delimiter=',')
        (row,column)=DataMatrix.shape
        #print(row,column)
        #reading each column one by one
        for i in range(0,column):
            column=DataMatrix[:,i]
            Apriori().calculate_candidate_one_itemsets(column,row,Apriori.attribute_names[i]);

        #for key,val in Apriori.candidate_one_itemsets.items():
            # print(key,val);

        Apriori.calculate_candidate_one_support(self,row,support)

        Apriori.calculate_candidate_two_support(self,row,support,DataMatrix)

        m=number_of_attributes
        for i in range(3,m+1):
            val=Apriori.calculate_candidate_k(self,row,support,DataMatrix,i)
            if val == 0:
                break

        print("done with itemset generation")

        #for k,itemset in Apriori.candidate_master_dict.items():
            #

        # print("finally")
            #print(k,itemset)

        print("counting maximal itemsets")

        Apriori.count_maximal(self,Apriori.candidate_master_dict_before_pruning)

        Apriori.count_closed_frequent(self,Apriori.candidate_master_dict_before_pruning)

        for key,itemset_dict in Apriori.candidate_master_dict.items():
            if key != 1:
                if check == 'N':
                    Apriori.generate_rules(self,itemset_dict,DataMatrix,confidence)
                else:
                    Apriori.generate_rules_lift(self,itemset_dict,DataMatrix,lift)
                    #print("commented rule gen")


Apriori().Apriori_1_kminus1()
