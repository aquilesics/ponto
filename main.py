import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("acao", help = "ex: entrada ou saida")
parser.add_argument("path", help = "path of file.")


args = parser.parse_args()


def format_row(*values, size = 12,delimiter = '|'):
    for value in values:
        spaces = (size - len(value) ) * ' '
        yield value + spaces  + delimiter


def punching_the_clock (acao = args.acao, path = args.path ):
    with open (path,'a') as file:
        current_date, current_time = datetime.datetime.now().__format__("%d/%m/%Y %H:%M").split(' ')

        row = [ x for x in format_row( current_date, acao, current_time ) ]
        row.append('\n')

        file.writelines( row )


def read_last_row():
    with open('ponto.txt','r') as file:
        for line in file:
            pass
        last_line = line

    return last_line.replace(' ','')



today = datetime.datetime.now().__format__("%d/%m/%Y")
check =  all( map( lambda x:x in read_last_row().split('|'), [today,args.acao]))

if check == True:
    pass
else:
    punching_the_clock()


