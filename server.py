#!/usr/bin/env python2
import sys,os

path = os.path.join(os.getcwd(),"gen-py")
sys.path.append(path)

from calendar_service import UserManager
from calendar_service.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

users = {}

class UserManagerHandler:
    def __init__(self):
        pass

    def ping(self):
        print("pong")

    def add_user(self, user):
        if user.uid == None:
            raise InvalidValueException(1, "no uid value exception")
        if user.firstname == None:
            raise InvalidValueException(2, "no firstname value exception")
        if user.middlename == None:
            raise InvalidValueException(3, "no middlename value exception")
        if user.lastname == None:
            raise InvalidValueException(4, "no lastname value exception")
        if user.phone == None:
            raise InvalidValueException(5, "no phone value exception")
        if user.rank == None:
            raise InvalidValueException(6, "no rank value exception")
        if user.uid <= 0:
            raise InvalidValueException(7, 'wrong user id')
        if user.rank not in [RankType.NUB, RankType.OBERNUB, RankType.BOSS]:
            raise InvalidValueException(4, 'wrong rank id')
        print("Processing user {0} {1} {2}".format(user.firstname, user.middlename, user.lastname))
        users[user.uid] = user
        print(users)
        return True

    def get_user(self, uid):
        if uid < 0:
            raise InvalidValueException(5, 'wrong id')
        if uid not in users:
            raise InvalidValueException(5, 'no user')
        return users[uid]

handler = UserManagerHandler()
processor = UserManager.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print('Starting the server...')
server.serve()
print('done.')