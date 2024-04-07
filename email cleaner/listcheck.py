import keyboard
import re
import pyperclip
import pandas
from io import StringIO

def list_check():
    headers = "l1\tl2\tl3\tl4\n"
    table = pandas.read_csv(StringIO(headers + pyperclip.paste()), delimiter='\t', skipinitialspace=True, dtype='str')
    for first_row, row in table.iterrows():
        second_row = table.index[row['l1'] == table['l3']].to_list()
        if second_row: table.loc[first_row, 'l2'] = table.loc[second_row[0], 'l4']
    tsv_output = table.to_csv(sep='\t', index=False, header=False)
    print(tsv_output)
    pyperclip.copy(tsv_output)
# hello
list_check()