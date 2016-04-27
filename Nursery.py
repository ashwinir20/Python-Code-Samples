import numpy as np


def read_data():

        file=open("Output_Nursery.txt","w")

        for line in open("C:/data/nursery_dataset.txt","r").readlines():

            line= line.split(',')

            print("line",line)

            _line=""

            #column 1
            if 'usual' or 'pretentious' in line[0]:
                 _line=_line+'1'
            else:
                 _line=_line+'0'

            _line+=','

            #column 2
            if 'great_pret' in line[0]:
                 _line=_line+'1'
            else:
                 _line=_line+'0'

            _line+=','

            #column 3

            if 'proper' or 'less_proper' or 'improper' in line[1]:
                    _line=_line+'1'
            else:
                    #critical and greatyl critical is 1
                    _line+='0'

            _line+=','

            #column 4

            if 'critical' or 'very_crit'  in line[1]:
                    _line=_line+'1'
            else:
                    _line+='0'

            _line+=','

            #column 5

            #complete, completed, incomplete

            if 'complete' or 'completed' or 'incomplete' in line[2]:
                    _line =_line+'1'
            else:
                    _line+='0'

            _line+=','

            #column 6

            #foster

            if 'foster' in line[2]:
                    _line=_line+'1'
            else:
                    _line+='0'

            _line+=','

            #column 7

            #1, 2,

            if line[3] == 1 or line[3] == 2:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 8
            #3, more

            if line[3] == 3 or line[3] == 'more':
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 9
            #convenient - housing

            if 'convenient' in line[4]:
                _line+='1'

            else:
                #else housing is critical
                _line+='0'

            _line+=','

            #column 10
            #convenient - finance

            if 'convenient' in line[5]:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 11
            #inconv
            if 'inconv' in line[5]:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 12

            #social: non-prob,
            if 'non-prob' in line[6]:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 13

            #social - slightly_prob, problematic
            if 'slightly_prob' or 'problematic' in line[6]:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 14

            #health: recommended, priority,
            if 'recommended' or 'priority' in line[7]:
                _line+='1'
            else:
                _line+='0'

            _line+=','

            #column 15

            #non_recom

            if 'not_recom' in line[7]:
                _line+='1'
            else:
                _line+='0'

            file.write(str(_line))
            file.write("\n")


read_data()