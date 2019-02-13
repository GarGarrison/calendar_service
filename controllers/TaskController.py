from models import Task,User
import calendar_service.ttypes as tt
import json

etypes = [ 
                tt.TaskType.TASK,
                tt.TaskType.REMINDER
            ]

priorities = [ 
                tt.TaskPriority.HIGH,
                tt.TaskPriority.MID,
                tt.TaskPriority.LOW
            ]

etypes = tt.TaskType._VALUES_TO_NAMES
priorities = tt.TaskPriority._VALUES_TO_NAMES

class TaskController:
    def add_task(self, entity):
        try:
            uids = [ uid for (uid,) in self.session.query(User.uid).all() ]
            if entity.owner not in uids:                               raise tt.InvalidValueException(1, "no such user exception (owner)") #raise Exception("error owner")
            if entity.creator not in uids:                             raise tt.InvalidValueException(2, "no such user exception (creator)") #raise Exception("error creator")
            if entity.ttype == None:                                   raise tt.InvalidValueException(3, "no ttype value exception") #raise Exception("error ttype")
            if entity.title == None:                                   raise tt.InvalidValueException(4, "no title value exception") #raise Exception("error title")
            if entity.priority == None:                                raise tt.InvalidValueException(6, "no priority value exception") #raise Exception("error priority")
            if entity.dt_created == None:                              raise tt.InvalidValueException(7, "no dt_created value exception") #raise Exception("error dt_created")
            if entity.ttype not in etypes:                             raise tt.InvalidValueException(8, 'wrong ttype id') #raise Exception("error ttype")
            if entity.priority and entity.priority not in priorities:  raise tt.InvalidValueException(9, 'wrong priority id') #raise Exception("error priority")
            entity = Task(entity)
            self.session.add(entity)
            self.session.commit()
            print("Processing task {0} {1}".format(entity.title, entity.description))
            return True
        except Exception as e:
            self.session.rollback()
            raise

    def get_task(self, eid):
        entity = self.session.query(Task).get(eid).to_dict()
        return json.dumps(entity)

    def get_user_tasks(self, uid):
        entitys = [t.to_dict() for t in self.session.query(Task).filter( (Task.owner == uid) | (Task.creator == uid) ).all()]
        return json.dumps(entitys)

    def edit_task(self, eid, json_data):
        try:
            entity = self.session.query(Task).get(eid)
            entity.update(json.loads(json_data))
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise
        return True