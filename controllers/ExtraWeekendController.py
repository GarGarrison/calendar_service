from models import ExtraWeekend
import calendar_service.ttypes as tt
import json
class ExtraController:
    def add_weekend(self, ew):
        extra = ExtraWeekend(ew)
        self.session.add(extra)
        self.session.commit()
        print("Processing extra weekend {0} {1}".format(ew.date, ew.weekend))
        return True

    def get_weekends(self, f, t):
        answer = {}
        weekends = self.session.query(ExtraWeekend).filter(ExtraWeekend.date >= f,  ExtraWeekend.date <= t).all()
        for ew in weekends: answer[str(ew.date)] = ew.weekend
        return json.dumps(answer)