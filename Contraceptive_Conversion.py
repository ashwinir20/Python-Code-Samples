def read_data():

    file=open("Output_Contraceptive.txt","w")

    for line in open("C:/data/Contraceptive.txt","r").readlines():

            line= line.split(',')
            _line=""

            #column 1
            #Wife's age (numerical)
            if float(line[0]) >= 32.5:
                 _line=_line+'0'
            else:
                 _line=_line+'1'

            _line+=','

            #column 2
            #Wife's education (categorical) 1=low, 2, 3, 4=high
            if line[1] == 1 or line[1] == 2:
                    _line=_line+'0'
            else:
                    _line+='1'
            _line+=','

            #column 3
            #Husband's education (categorical) 1=low, 2, 3, 4=high
            if line[2] == 1 or line[2] == 2:
                _line+='0'
            else:
                _line+='1'

            _line+=','

            #column 4
            #Number of children ever born (numerical)

            if int(line[3]) >= 2:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 5
            #Wife's religion (binary) 0=Non-Islam, 1=Islam

            if 'Islam' in line[4]:
                _line+='1'

            else:
                _line+='0'

            _line+=','

            #column 6
            #Wife's now working? (binary) 0=Yes, 1=No

            if 'No' in line[5]:
                _line+='0'
            else:
                _line+='1'

            _line+=','

            #column 7
            #Husband's occupation (categorical) 1, 2, 3, 4

            if line[6] == 1 or line[6] == 2:
                _line+='0'
            else:
                _line+='1'

            _line+=','

            #column 8
            #Standard-of-living index (categorical) 1=low, 2, 3, 4=high
            if line[7] == 1 or line[7] == 2:
                _line+='0'
            else:
                _line+='1'

            _line+=','

            #column 9
            #Media exposure (binary) 0=Good, 1=Not good
            if line[8] == 0:
                _line+='1'
            else:
                _line+='0'

            file.write(str(_line))
            file.write("\n")


read_data()