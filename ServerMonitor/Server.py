#!/usr/bin/env python

from socketserver import (ThreadingTCPServer as TCP, StreamRequestHandler as SRH)
import json
import time

HOST = ''
PORT = 35601
ADDR = (HOST, PORT)
BUFSIZ = 1024
getpwd = 'C:\\ServerMonitor\\web\\json\\'
dic = []

class MyRequestHandler(SRH):
    def handle(self):
        self.wfile.write(bytes("Authentication required", encoding='utf-8'))
        Name = str(self.rfile.readline())
        if len(Name) > 0:
            print(Name)
            self.wfile.write(bytes("Authentication successfulIPv4", encoding='utf-8'))
        print('...connected from:', self.client_address)
        self.wfile.write(bytes('IPv4', encoding='utf-8'))
        while True:
            data_bin = self.rfile.readline()
            data_bin = str(data_bin)
            data_bin1 = json.loads(eval(data_bin))
            data_bin1['name'] = Name
            data_bin1['type'] = 'vmWare'
            data_bin1['host'] = 'Host'
            data_bin1['location'] = 'ChongQing'
            addRecord(Name, data_bin1)
            if not data_bin:
                break
        self.close()

def addRecord(Name, record):
    flag = True
    for index in range(len(dic)):
        print()
        if Name == dic[index]['name']:
            flag = False
            break
    if flag:
        dic.append(record)
    else:
        dic[index] = record

    all = {"servers": dic, "updated": str(int(time.time()))}
    updateFile(all)

def updateFile(update):
    try:
        with open(getpwd+'stats.json', 'w+') as f:
            update = json.dumps(update)
            f.write(update)
            f.close()
    except json.decoder.JSONDecodeError as e:
        print(e)


if __name__ == "__main__":
    tcpSer = TCP(ADDR, MyRequestHandler)
    print('waiting for connection...')
    tcpSer.serve_forever()



