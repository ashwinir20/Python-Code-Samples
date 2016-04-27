import numpy as np


def read_data():

    file=open("Output_Car.txt","w")

    for line in open("C:/data/CarEvaluation.txt","r").readlines():

            line= line.split(',')
            _line=""
            if 'vhigh' or 'high' in line[0]:
                    #new_line.append('1')
                 _line=_line+'1'
            elif 'med' or 'low' in line[0]:
                    #new_line.append('0')
                    _line=_line+'0'
            _line+=','

            if 'vhigh' or 'high' in line[1]:
                    #new_line.append('1')
                    _line=_line+'1'

            elif 'med' or 'low' in line[1]:
                    #new_line.append('0')
                    _line+='0'

            _line+=','


            if line[2] == 2 or line[2] == 3:
                #new_line.append('0')
                _line+='0'
            else:
                #new_line.append('1')
                _line+='1'

            _line+=','

            if line[3] == 2 or line[3] == 4:
                #new_line.append('0')
                _line+='0'

            else:
                #new_line.append('1')
                _line+='1'

            _line+=','

            if 'small' in line[4]:
                #new_line.append('0')
                _line+='0'

            else:
                #new_line.append('1')
                _line+='1'

            _line+=','

            if 'low' in line[5]:
                #new_line.append('0')
                _line+='0'

            else:
                #new_line.append('1')
                _line+='1'

            file.write(str(_line))
            file.write("\n")


read_data()