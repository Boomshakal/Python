import json
from json import JSONDecodeError

from socket import *
from database.database_connect import DatabasePool, Parameters

# import sentry_sdk
#
# # sentry报错收集服务器
# sentry_sdk.init("https://89f2e30912c64c1c8b4da5b739e706a8@sentry.io/1876964")

HOST = '0.0.0.0'
PORT = 9999
BUFSIZ = 1024
LIKK_SIZE = 10
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(LIKK_SIZE)

while True:
    clientsock, addr = server.accept()
    # print("addr=%s %s" % (addr, type(addr)))
    # host = gethostname()
    # print(host)
    print(f"客户端ip地址为：{addr[0]}")

    while True:
        try:
            msg = clientsock.recv(BUFSIZ)
        except ConnectionResetError as e:
            break
        if not msg:
            break
        msg_str = msg.decode('utf-8', "ignore")

        try:
            msg_dic = json.loads(msg_str)
        except JSONDecodeError as e:
            clientsock.send('请传入正确的JSON字符串'.encode('utf-8'))
            continue
        print('dict:', msg_dic.get('details', ''))

        rtnstr = ''
        barcode = msg_dic.get('barcode', '')
        result = msg_dic.get('result', '')
        taskorder = msg_dic.get('taskorder', '')
        workline = msg_dic.get('workline', '')
        workstation = msg_dic.get('workstation', '')
        workshift = msg_dic.get('workshift', '')
        sequence = msg_dic.get('sequence', '')
        workdevice = msg_dic.get('workdevice', '')
        worker = msg_dic.get('worker', '')
        workleader = msg_dic.get('workleader', '')
        department = msg_dic.get('department', '')
        usercode = msg_dic.get('usercode', '')
        details = msg_dic.get('details', '')

        if details:
            details = details.replace("'", '"')
        else:
            rtnstr = '没有测试明细'

        # TODO: p_fm_work_check_barcode_and
        sql = '''
            EXEC p_fm_work_check_barcode_and @taskorder,@sequence,'',@barcode,'MAIN'
            '''

        p = Parameters().add('taskorder', taskorder).add('sequence', sequence).add('barcode', barcode)

        connect = DatabasePool('X1_CORE_PROD')
        lists = connect.ExecuteQuery(sql, p)

        rtnstr = lists[0].get('rtnstr', '')
        if rtnstr == 'OK':

            # TODO: p_fm_work_create_for_test
            sql = '''
            EXEC p_fm_work_create_for_test @taskorder,@workline,@workstation,@workshift,@workdevice,@department,
            @sequence,@worker,@workleader,@barcode,@result,'',@details,NULL,0,@usercode,0
            '''

            p = Parameters().add('taskorder', taskorder).add('workline', workline).add('workstation', workstation)
            p.add('workshift', workshift).add('workdevice', workdevice).add('department', department)
            p.add('sequence', sequence).add('worker', worker).add('workleader', workleader).add('barcode', barcode)
            p.add('result', result).add('details', details).add('usercode', usercode)

            connect = DatabasePool('X1_CORE_DATA')
            res = connect.ExecuteQuery(sql, p)

            if isinstance(res, Exception):
                rtnstr = res.args[1].decode('utf-8')
                print(rtnstr)
            else:
                rtnstr = 'OK'

        clientsock.send(rtnstr.encode('utf-8'))
