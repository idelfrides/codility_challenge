""" Main module of QuintoAndar test """

from textwrap import dedent
from task_lib import TaskLibSolution
from task_lib.task_lib_help import  HelpSolutionLib


def main(*args):
    print(dedent("""
        
        THIS IS CODILITY CHALLENGE
    
    """))
    
    tls = TaskLibSolution()
    hsl = HelpSolutionLib()

    
    data = hsl.read_data2()
    listData = hsl.setup_list(data[0])

    tls.solution_gz_not_inarray(listData)
    
    N, S = hsl.generate_seat(8)
    print('\n ROWS: {} \n\n RESERVED SEATS:  {}'
        .format(N, S)
    )
    seats = tls.solution_numbeur_of_seats(N, S)

    print('\n\n AVAILABLE SEATS:  {}'.format(seats))

    print('\n\n\n')


if __name__ =='__main__':
    main()

