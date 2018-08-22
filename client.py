import sys,os

path = os.path.join(os.getcwd(),"gen-py")
sys.path.append(path)

from calendar_service import UserManager
from calendar_service.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = UserManager.Client(protocol)
transport.open()

# user = User()
# user.uid = 123456
# user.firstname = "ivan"
# user.middlename = "petrovich"
# user.lastname = "herov"
# user.phone = "11-22-33"
# user.rank = RankType.NUB

# client.add_user(user)

user = client.get_user(123456)
print user.firstname