from sys import exit

bitmap = """
...................................................................
                                     **
                                    ****
                                   *******
                                  ***********
                                 **************
        *********      *********  **************
      *************** **************************
    *******     *******************************
   *****    *************************** *****
  *****  *******************************
 ***************************************
 ***************************************
 ***************************************
 ***************************************
 ***************************************
  *************************************
  ************************************
   **********************************
    *******************************
  * 　*****************************
  **   *** *********************
  ***  ** *********************
  * **** **  *****************
  *  *  **     *************
  *     ***      *******
  *        ***      **
  *************
....................................................................
"""
print('Enter a message to display:')
message = input('> ')
if message == '':
    exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()