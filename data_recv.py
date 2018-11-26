import socket
import time

class Clock:
    def __main__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

class Date:
    def __main__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

def tick():
    time.sleep(1000)

ip = raw_input('IP: ')
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

clock = Clock()
date = Date()
commands = ['set', 'time', 'date']
maxlenTime = 8
maxlenDate = 10
expect = 0
expectNum = 0
flagDate = 0
flagClock = 0

while True:

    data, addr = sock.recvfrom(1024)
    data = data.decode('UTF-8')
    string = data

    if string == 'stop':
        print('Finish')
        break
    elif string == 'database':
        print('\n------------------+')
        print('Data:             |')
        print('------------------|')
        result1 = clock.h + ':' + clock.m + ':' + clock.s
        print('time: ' + result1 + '    |')
        result2 = date.d + '.' + date.m + '.' + date.y
        print('date: ' + result2 + '  |')
        print('------------------+\n')
    elif string == commands[0]:
        #print('1st')
        expect = 1
    elif string == commands[1]:
        #print('2nd')
        if expect == 1:
            expectNum = 1
        expect = 0
    elif string == commands[2]:
        #print('3rd')
        if expect == 1:
            expectNum = 1
        expect = 0
    else:
        if expectNum == 1:
            #print('length: ' + str(maxlenTime))
            #print('length: ' + str(maxlenDate))
            if len(string) == maxlenDate:
                #print(string)
                if string[2] == '.' and string[5] == '.':
                    #print('4th')
                    print('set date')
                    for count in range(0, len(string)):
                        if string[count] >= '0' and string[count] <= ':':
                            date.d = string[0] + string[1]
                            date.m = string[3] + string[4]
                            date.y = string[6] + string[7] + string[8] + string[9]
                    flagDate = 1
                else:
                    print('ERROR: Wrong input!')
                    #break
            elif len(string) == maxlenTime:
                if string[2] == ':' and string[5] == ':':
                    #print('5th')
                    print('set clock')
                    for count in range(0, len(string)):
                        if string[count] >= '.' and string[count] <= '9':
                            clock.h = string[0] + string[1]
                            clock.m = string[3] + string[4]
                            clock.s = string[6] + string[7]
                    flagClock = 1
                else:
                    print('ERROR: Wrong input!')
                    #break
            else:
                print('ERROR: Not a command!')
                #break
        else:
            print('ERROR: Not a command!')
            #break
            
            expectNum = 0
        

    #print(string)
    #print('flagDate: ' + str(flagDate))
    #print('flagClock : ' + str(flagClock))

    if flagClock == 1:
        result1 = clock.h + ':' + clock.m + ':' + clock.s
        print('time: ' + result1)
        flagClock = 0
    elif flagDate == 1:
        result2 = date.d + '.' + date.m + '.' + date.y
        print('date: ' + result2)
        flagDate = 0

    

