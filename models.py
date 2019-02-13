import sys,os

path = os.path.join(os.getcwd(),"gen-py")
sys.path.append(path)
import calendar_service.ttypes as tt 

from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


'creator', 'deadline', 'description', 'dt_created', 'id', 'owner', 'priority', 'read', 'status', 'thrift_spec', 'title', 'ttype', 'validate', 'write'

class Mixin(object):

    def to_dict(self):
        d = {}
        columns = list(filter(lambda x: x[0] != "_" ,self.__dict__))
        for c in columns:
            val = self.__getattribute__(c)
            # если тип поля DATETIME и не равен None преобразовать его в строку
            if self.__table__.columns[c].type.__str__() == "DATETIME" and val: val = str(val)
            # проверка, не является ли поле None
            if val != None: d[c] = val
        return d

    def update(self, data):
        for k in data:
            original_columns= self.getBDColumns()
            if k in original_columns:
                if data[k] == "": data[k] = None
                if self.__table__.columns[k].nullable:  self.__setattr__(k, data[k])
                if not self.__table__.columns[k].nullable and data[k]:  self.__setattr__(k, data[k])

    def getBDColumns(self):
        return [i for i in dir(self) if not callable(i) and not i.startswith('__')]


class Department(Mixin, Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    def __init__(self, entity):
        self.name = entity.name
        self.description = entity.description

    def __repr__(self):
        return '<Department %r %r>' % (self.name, self.description)

class UserRole(Mixin, Base):
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    def __init__(self, entity):
        self.name = entity.name
        self.description = entity.description

    def __repr__(self):
        return '<UserRole %r %r>' % (self.name, self.description)

class UserGroup(Mixin, Base):
    __tablename__ = 'user_group'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    def __init__(self, entity):
        self.name = entity.name
        self.description = entity.description

    def __repr__(self):
        return '<UserGroup %r %r>' % (self.name, self.description)

class User(Mixin, Base):
    __tablename__ = 'user'

    uid = Column(Integer, primary_key=True)
    dept = Column(Integer, ForeignKey("department.id"), nullable=False)
    role = Column(Integer, ForeignKey("user_role.id"), nullable=False)
    group = Column(Integer, ForeignKey("user_group.id"), nullable=True)
    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    birthday = Column(DateTime, nullable=False)
    phone = Column(String(8), nullable=False)
    phone_mobile = Column(String(11), nullable=False)
    work_start = Column(DateTime, nullable=False)
    rank = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=False, default=0)
    vacation_days = Column(Integer, nullable=False, default=30)

    def __init__(self, entity):
        self.uid = entity.uid
        self.dept = entity.dept
        self.role = entity.role
        self.group = entity.group
        self.firstname = entity.firstname
        self.middlename = entity.middlename
        self.lastname = entity.lastname
        self.phone = entity.phone
        self.phone_mobile = entity.phone_mobile
        self.work_start = entity.work_start
        self.rank = entity.rank
        self.birthday = entity.birthday
        
    def __repr__(self):
        return '<User %r>' % (self.lastname)

class Event(Mixin, Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.uid"), nullable=False)
    etype = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    dt_start = Column(DateTime, nullable=False)
    dt_end = Column(DateTime, nullable=True)
    hours = Column(String, nullable=True)
    comment = Column(String, nullable=True)

    def __init__(self, entity):
        self.user = entity.user
        self.etype = entity.etype
        self.status = entity.status
        self.dt_start = entity.dt_start
        self.dt_end = entity.dt_end
        self.hours = entity.hours
        self.comment = entity.comment

    def __repr__(self):
        return '<Event %r %r>' % (self.user, self.dt_start)

class Task(Mixin, Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    status = Column(Integer, default=tt.TaskStatus.NEW)
    priority = Column(Integer, nullable=True)
    ttype = Column(Integer, nullable=False)
    owner = Column(Integer, ForeignKey("user.uid"), nullable=False)
    creator = Column(Integer, ForeignKey("user.uid"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    dt_created = Column(DateTime, nullable=False)
    deadline = Column(DateTime, nullable=True)
    
    def __init__(self, entity):
        if entity.status: self.status = entity.status
        self.priority = entity.priority
        self.ttype = entity.ttype
        self.creator = entity.creator
        self.owner = entity.owner
        self.title = entity.title
        self.description = entity.description
        self.dt_created = entity.dt_created
        self.deadline = entity.deadline
    
    def __repr__(self):
        return '<Task %r>' % (self.title)

class ExtraWeekend(Mixin, Base):
    __tablename__ = 'extraweekend'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    weekend = Column(Boolean, nullable=False)

    def __init__(self, entity):
        self.date = entity.date
        self.weekend = entity.weekend

    def __repr__(self):
        return '<Weekend %r %r>' % (self.date, self.weekend)