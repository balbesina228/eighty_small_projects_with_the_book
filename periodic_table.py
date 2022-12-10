from csv import reader
from re import sub
from sys import exit

elements_file = open('periodictable.csv', encoding='utf-8')
elements_csv_reader = reader(elements_file)
elements = list(elements_csv_reader)
elements_file.close()
all_columns = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               "Abundance in earth's crust"]
longest_column = 0
for key in all_columns:
    if len(key) > longest_column:
        longest_column = len(key)
print(longest_column)
elements_tab = {}
for line in elements:
    element = {
        'Atomic Number':              line[0],
        'Symbol':                     line[1],
        'Element':                    line[2],
        'Origin of name':             line[3],
        'Group':                      line[4],
        'Period':                     line[5],
        'Atomic weight':              line[6] + ' u',
        'Density':                    line[7] + ' g/cm^3',
        'Melting point':              line[8] + ' K',
        'Boiling point':              line[9] + ' K',
        'Specific heat capacity':     line[10] + ' J/(g*K)',
        'Electronegativity':          line[11],
        "Abundance in earth's crust": line[12] + ' mg/kg'
    }
    for key, value in element.items():
        element[key] = sub(r'\[(I|V|X)+\]', '', value)
    elements_tab[line[0]] = element
    elements_tab[line[1]] = element
print('Periodic table of elements by Al Sweigart\n')
while True:
    print('''
                 Periodic Table of Elements
  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
1 H                                                  He
2 Li Be                               B  C  N  O  F  Ne
3 Na Mg                               Al Si P  S  Cl Ar
4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

        Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
        Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
''')
    print('Enter a symbol or atomic number to examine or Quit:')
    print(elements_tab)
    response = input('> ').title()
    if response == 'Quit':
        exit()
    if response in elements_tab:
        for key in all_columns:
            key_justified = key.rjust(longest_column)
            print(key_justified + ': ' + elements_tab[response][key])
        input('Press Enter to continue...')
