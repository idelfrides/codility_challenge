""" Task helping to build solutions module """

from random import randint, choice


class HelpSolutionLib(object):
        
    def __init__(self):
        pass

    def positives(self, sorted_A):
        smallest = sorted_A[0]
        if smallest > 1:
            return  1

        i = 1
        for x in sorted_A:
            if x + 1 == sorted_A[i]:
                smallest = sorted_A[i]
                i += 1
                continue
            if x + 1 < sorted_A[i]:
                smallest = x + 1
                break
            
        return smallest

    def setup_list(self, data_list):
        new_list = []
        print('-'*40)
        print('\n\n Entring data \n\n', data_list)
        list_len = len(data_list)
        i = 0
        while True:
            j = i + 1
            if j == list_len:
                break
            value1 =  data_list[i].strip()
            value2 =  data_list[j].strip()
            if value1.isnumeric() and value2.isnumeric():
                real_value = value1 + value2
                new_list.append(int(real_value))
                i = j + 1
                continue
            if value1.isnumeric() and value2 == ',':
                new_list.append(int(value1))
                i += 1
            
            i += 1
        
        return new_list

    def read_data(self):
        print("""
            
            THIS IS read_data 1 
        
        """)
        return open('./file_inputdata.txt', 'r', encoding='utf-8')

    def read_data2(self):
        with open('./file_inputdata.txt', 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        return content

    def remove_negative(self, mylist):
        i = 0
        while True:
            x = mylist[i]
            if x < 0:
                mylist.remove(x)
            else:
                break

        return mylist

    def generate_seat(self, max_rows):
        row = randint(1, max_rows)
        seat_code = ''
        myspace = ' '

        seat_letter_list = [
            'A','B','C',
            'D','E','F','G',
            'H','J','K'
        ]

        for i in range(3):
            seat_num = randint(1, row)
           
            seat_letter = choice(seat_letter_list)
            
            seat_code = seat_code + str(seat_num) + seat_letter + myspace

        seat_code.strip()

        return row, seat_code

