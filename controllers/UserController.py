from models import User, Department, UserRole, UserGroup
import calendar_service.ttypes as tt
import json
import datetime as dt
from sqlalchemy import func

uranks = tt.RankType._VALUES_TO_NAMES
class UserController:
    def add_user(self, entity):
        if entity.uid == None:        raise tt.InvalidValueException(1, "no uid value exception")
        if entity.firstname == None:  raise tt.InvalidValueException(2, "no firstname value exception")
        if entity.middlename == None: raise tt.InvalidValueException(3, "no middlename value exception")
        if entity.lastname == None:   raise tt.InvalidValueException(4, "no lastname value exception")
        if entity.phone == None:      raise tt.InvalidValueException(5, "no phone value exception")
        if entity.rank == None:       raise tt.InvalidValueException(6, "no rank value exception")
        if entity.rank not in uranks: raise tt.InvalidValueException(4, 'wrong rank id')
        entity = User(entity)
        self.session.add(entity)
        self.session.commit()
        print("Processing user {0} {1} {2}".format(entity.firstname, entity.middlename, entity.lastname))
        return True

    def get_user(self, uid):
        db_user = self.session.query(User).get(uid)
        return json.dumps(db_user.to_dict())

    def get_users(self):
        users = [u.to_dict() for u in self.session.query(User).order_by(User.lastname).all()]
        return json.dumps(users)

    def get_users_hours(self):
        rez = {}
        # return tuple (uid, etype, count)
        entitys = self.session.query(User.id, func.sum(User.hours)).group_by(User.id).all()
        for e in entitys:
            if e[0] in rez: rez[e[0]][e[1]] = e[2]
            else: rez[e[0]] = {e[1]: e[2]}
        #rez - {uid1: {etype1:count, etype2:count ...} ... uidN:{...}}
        return json.dumps(rez)

    def add_department(self, entity):
        if entity.name == None:
            raise tt.InvalidValueException(2, "no department name value exception")
        entity = Department(entity)
        self.session.add(entity)
        self.session.commit()
        print("Processing department {0}".format(entity.name))
        return True

    def edit_department(self, eid, data):
        try:
            entity = self.session.query(Department).get(eid)
            entity.update(json.loads(json_data))
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise(e)
        return True

    def add_user_role(self, entity):
        if entity.name == None:
            raise tt.InvalidValueException(2, "no role name value exception")
        entity = UserRole(entity)
        self.session.add(entity)
        self.session.commit()
        print("Processing user role {0}".format(entity.name))
        return True

    def edit_user_role(self, eid, data):
        try:
            entity = self.session.query(UserRole).get(eid)
            entity.update(json.loads(json_data))
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise(e)
        return True

    def add_user_group(self, entity):
        if entity.name == None:
            raise tt.InvalidValueException(2, "no groupe name value exception")
        entity = UserGroup(entity)
        self.session.add(entity)
        self.session.commit()
        print("Processing user group {0}".format(entity.name))
        return True

    def edit_user_group(self, eid, data):
        try:
            entity = self.session.query(UserGroup).get(eid)
            entity.update(json.loads(json_data))
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise(e)
        return True

    def get_today_birthday(self):
        today = dt.datetime.today()
        users = [u.to_dict() for u in self.session.query(User).filter( (func.date_part("month", User.birthday) == today.month) & (func.date_part("day", User.birthday) == today.day) ).all()]
        return json.dumps(users)