import sys,os

path = os.path.join(os.getcwd(),"gen-py")
sys.path.append(path)

from calendar_service import CalendarManager
import calendar_service.ttypes as tt

from thrift.transport import THttpClient
from thrift.protocol import TJSONProtocol

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol

from thrift.transport import TTransport


# transport = THttpClient.THttpClient("http://localhost:8080")
# protocol = TJSONProtocol.TJSONProtocol(transport)

transport = TSocket.TSocket('localhost', 8080)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
# protocol = TJSONProtocol.TJSONProtocol(transport)

client = CalendarManager.Client(protocol)
transport.open()

testUsers = [
    { "uid": 111111,
      "dept": 1,
      "role": 1,
      "rank": tt.RankType.NUB, 
      "firstname": "her", 
      "middlename": "ivanovich", 
      "lastname": "petrovich", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 222222, 
      "dept": 1,
      "role": 2,
      "group": 1,
      "rank": tt.RankType.BOSS, 
      "firstname": "nikita", 
      "middlename": "ivanovich", 
      "lastname": "ggurda", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 333333,
      "dept": 1,
      "role": 2,
      "group": 1,   
      "rank": tt.RankType.NUB, 
      "firstname": "efim", 
      "middlename": "ivanovich", 
      "lastname": "herov", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 444444, 
      "dept": 1,
      "role": 2,
      "group": 2,
      "rank": tt.RankType.OBERNUB, 
      "firstname": "ivan", 
      "middlename": "ivanovich", 
      "lastname": "shedrin", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 555555, 
      "dept": 1,
      "role": 2,
      "group": 2,
      "rank": tt.RankType.OBERNUB, 
      "firstname": "rulon", 
      "middlename": "ivanovich", 
      "lastname": "oboev", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 666666, 
      "dept": 1,
      "role": 2,
      "group": 3,
      "rank": tt.RankType.OBERNUB, 
      "firstname": "ushat", 
      "middlename": "ivanovich", 
      "lastname": "pomoev", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 777777, 
      "dept": 1,
      "role": 2,
      "group": 3,
      "rank": tt.RankType.NUB, 
      "firstname": "hren", 
      "middlename": "ivanovich", 
      "lastname": "ivanovich", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    },
    { "uid": 888888, 
      "dept": 1,
      "role": 2,
      "group": 3,
      "rank": tt.RankType.NUB, 
      "firstname": "adolf", 
      "middlename": "ivanovich", 
      "lastname": "zigulin", 
      "phone": "11-22-33", 
      "phone_mobile": "79998887766", 
      "work_start": "2011-05-01 00:00:00", 
      "birthday": "1987-03-04 00:00:00"
    }
]

testExtraWeekends = [
    { "date": "2019-01-04 00:00:00", "weekend": True},
    { "date": "2019-01-06 00:00:00", "weekend": False},
]

# drop table event; drop table task; drop table extraweekend; drop table "user"; drop table department; drop table user_role; drop table user_group; 

dept = tt.Department(name="otdel1", description="test_otdel")
role1 = tt.UserRole(name="boss")
role2 = tt.UserRole(name="regular")
group1 = tt.UserGroup(name="network")
group2 = tt.UserGroup(name="admin")
group3 = tt.UserGroup(name="proger")
client.add_department(dept)
client.add_user_role(role1)
client.add_user_role(role2)
client.add_user_group(group1)
client.add_user_group(group2)
client.add_user_group(group3)

for u in testUsers:
    user = tt.User()
    for k in u:
        user.__setattr__(k, u[k])
    client.add_user(user)

for ew in testExtraWeekends:
    extra = tt.ExtraWeekend()
    for k in ew:
        extra.__setattr__(k, ew[k])
    client.add_weekend(extra)
    

transport.close()