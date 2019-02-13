from models import Event, User
import calendar_service.ttypes as tt
import json
from sqlalchemy import func, extract
import datetime as dt
etypes = tt.EventType._VALUES_TO_NAMES

class EventController:
    def add_event(self, entity):
        try:
            uids = [ uid for (uid,) in self.session.query(User.uid).all() ]
            if entity.user == None:        raise tt.InvalidValueException(1, "no user value exception")
            if entity.user not in uids:    raise tt.InvalidValueException(2, "no such user exception")
            if entity.etype == None:       raise tt.InvalidValueException(3, "no etype value exception")
            if entity.status == None:      raise tt.InvalidValueException(4, "no status value exception")
            if entity.dt_start == None:    raise tt.InvalidValueException(5, "no dt_start value exception")
            if entity.etype not in etypes: raise tt.InvalidValueException(6, "wrong etype id: " + str(entity.etype))
            entity = Event(entity)
            self.session.add(entity)
            self.session.commit()
            print("Processing event {0} {1} {2}".format(entity.user, entity.etype, entity.dt_start))
            return True
        except Exception as e:
            self.session.rollback()
            raise

    def edit_event(self, eid, json_data):
        try:
            entity = self.session.query(Event).get(eid)
            entity.update(json.loads(json_data))
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise
        return True

    def get_events(self, f, t):
        entitys = [entity.to_dict() for entity in self.session.query(Event).filter( (Event.status == tt.EventStatus.ACCEPT ) & (((Event.dt_start <= t) & (Event.dt_end >= f)) | ((Event.dt_start <= t) & (Event.dt_start >= f))) ).all()]
        return json.dumps(entitys)

    def get_event(self, eid):
        entity = self.session.query(Event).get(eid).to_dict()
        return json.dumps(entity)

    def get_new_events(self):
        entitys = [entity.to_dict() for entity in self.session.query(Event).filter( (Event.status == tt.EventStatus.NEW) & (Event.etype != tt.EventType.DUTY) ).all()]
        return json.dumps(entitys)

    def get_user_events(self, uid):
        entitys = [entity.to_dict() for entity in self.session.query(Event).filter( Event.status == tt.EventStatus.NEW ).all()]
        return json.dumps(entitys)

    def get_users_events_stat(self):
        rez = {}
        # return tuple (uid, etype, count)
        entitys = self.session.query(Event.user, Event.etype, func.sum(self.subtract_dates(Event.dt_end, Event.dt_start)/(3600*24) + 1)).filter( Event.status == tt.EventStatus.ACCEPT ).group_by(Event.user, Event.etype).all()
        for e in entitys:
            if e[0] in rez: rez[e[0]][e[1]] = e[2]
            else: rez[e[0]] = {e[1]: e[2]}
        #rez - {uid1: {etype1:count, etype2:count ...} ... uidN:{...}}
        return json.dumps(rez)

    def set_event_status(self, eid, status):
        try:
            entity = self.session.query(Event).get(eid)
            user = self.session.query(User).get(entity.user)
            entity.status = status
            if entity.hours and status == tt.EventStatus.ACCEPT and entity.etype == tt.EventType.ADD_HOURS: user.hours += int(entity.hours)
            if entity.hours and status == tt.EventStatus.ACCEPT and entity.etype == tt.EventType.HOURS: user.hours -= int(entity.hours)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise(e)
        return True

    def get_today_duty(self):
        today = dt.datetime.today().strftime("%Y-%m-%d 00:00:00")
        user = self.session.query(Event).filter( (Event.dt_start == today) & (Event.etype == tt.EventType.DUTY) ).first()
        if user: user = user.to_dict()
        return json.dumps(user)

    def get_today_vacation(self):
        today = dt.datetime.today().strftime("%Y-%m-%d 00:00:00")
        users = [u.to_dict() for u in self.session.query(Event).filter( (Event.dt_start <= today) & (Event.dt_end >= today) & (Event.etype == tt.EventType.VACATION) ).all()]
        return json.dumps(users)

    def get_today_holiday(self):
        today = dt.datetime.today().strftime("%Y-%m-%d 00:00:00")
        users = [u.to_dict() for u in self.session.query(Event).filter( (Event.dt_start == today) & (Event.etype == tt.EventType.HOLIDAY) ).all()]
        return json.dumps(users)

    def subtract_dates(self, d1,d2):
        return extract('epoch', d1) - extract('epoch', d2)

    def users_stat(self):
        stat = self.session.query( Event.user, self.subtract_dates(Event.dt_end, Event.dt_start)/(3600*24) + 1 ).all()
        for s in stat: print(s)
        return True