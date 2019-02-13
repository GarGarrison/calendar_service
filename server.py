#!/usr/bin/env python3
import sys,os

path = os.path.join(os.getcwd(),"gen-py")
sys.path.append(path)

from calendar_service import CalendarManager

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
# from thrift.protocol import TJSONProtocol
# from thrift.server import THttpServer

import sqlalchemy

from models import Base
from controllers.UserController import UserController
from controllers.EventController import EventController
from controllers.TaskController import TaskController
from controllers.ExtraWeekendController import ExtraController
# from controllers.DutyController import DutyController

class CalendarManagerHandler(
                                UserController,
                                EventController,
                                TaskController,
                                ExtraController
                            ):
    db_location = "postgres://testuser:12345@localhost:5432/calendar"

    def __init__(self):
        self.base = Base
        self.engine = sqlalchemy.create_engine(self.db_location)
        Session = sqlalchemy.orm.sessionmaker(self.engine)
        self.session = Session()
        self.base.metadata.create_all(self.engine, checkfirst=True)

    def ping(self):
        print("pong")

handler = CalendarManagerHandler()
processor = CalendarManager.Processor(handler)
transport = TSocket.TServerSocket(port=8080)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

# pfactory = TJSONProtocol.TJSONProtocolFactory()

# processor = CalendarManager.Processor(CalendarManagerHandler())
# protoFactory = TJSONProtocol.TJSONProtocolFactory()
# server = THttpServer.THttpServer(processor, ("127.0.0.1", 8080), protoFactory)
# You could do one of these for a multithreaded server

# server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print('Starting the server...')
server.serve()
print('done.')
