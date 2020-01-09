""" Module olds solutions method """

from task_lib import HelpSolutionLib
from textwrap import dedent
import time


class TaskLibSolution(object):

    def __init__(self):
        self.hsl = HelpSolutionLib()

    def solution_gz_not_inarray(self, A):

        if len(A) == 0:
            print("""
                Invalid Array! 
                The task will be ended.
            """)
            exit(1)
        
        sorted_A = sorted(set(A))
        smallest =  sorted_A[0]
        greatlest = sorted_A[len(sorted_A)-1]
        
        if greatlest <= 0:
            response = 1
            print('\n\n Response:  ', response)
            print('\n\n')
            print('-'*40)
        
        if smallest > 0 and greatlest > 0:
            response = self.hsl.positives(sorted_A)
            print('\n\n Response:  ', response)
            print('\n\n')
            print('-'*40)

        if smallest < 0 and greatlest > 0:
       
            sorted_A2 = self.hsl.remove_negative(sorted_A)
            response =  self.hsl.positives(sorted_A2)
            print('\n\n Response:  ', response)
            print('\n\n')
            print('-'*40)

    def solution_numbeur_of_seats(self, N, S):

        if N < 1 or N > 50:
            print('INVALID NUMBER OF ROWS')
            exit(1)
        
        if len(S) < 0 or len(S) > 1909:
            print('INVALID LENGHT OF MNUMBER OF SEATS')
            exit(1)
        
        if N >= 1:
            row = 0
            num_seat =  0
            seats = N * 3
            num_seat_help = 0
            code_goup_help = 'I'

            while True:
                if row >= len(S):
                    break
                
                num_seat =  S[row]
                code_goup =  S[row+1]
                num_seat = int(num_seat)

                if num_seat > N:
                    print(dedent(""" 
                        -------------------------------                   
                                   WARNING
                        -------------------------------
                         The number of row is INVALID!
                         The app gonna be quited!
                         check S --> {}
            
                    """.format(num_seat)))
                    time.sleep(7)
                    exit(1)

                if num_seat == num_seat_help  and code_goup == code_goup_help:
                    print(dedent(""" 
                        -------------------------------                   
                                   WARNING
                        -------------------------------
                         The code of a seat is INVALID!
                         Code of a seat can not REPEAT. 
                         The app gonna be quited!
                         check Seat --> {}
            
                    """.format(str(num_seat) + code_goup)))
                    time.sleep(7)
                    exit(1)

                if code_goup in ['A', 'B', 'C']:
                    if num_seat != num_seat_help:
                        seats -= 1
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                    else:
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                if code_goup in ['E', 'F']:
                    if num_seat != num_seat_help:
                        seats -= 1
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help == code_goup
                        continue
                    else:
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                if code_goup in ['D', 'G']:
                    if num_seat_help == num_seat:
                        seats -= 1
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                    else:
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                if code_goup in ['H', 'J', 'K']:
                    if num_seat != num_seat_help:
                        seats -= 1
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue
                    else:
                        row += 3
                        num_seat_help = num_seat
                        code_goup_help = code_goup
                        continue

            return seats

