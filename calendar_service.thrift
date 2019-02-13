namespace py calendar_service

typedef string DateTime
typedef string JSONObjects

enum RankType {
    NUB = 1,
    OBERNUB = 2,
    BOSS = 3
}

enum TaskType {
    TASK = 1,
    REMINDER = 2
}

enum TaskStatus {
    NEW = 1,
    OPENED = 2,
    CLOSED = 3
}

enum TaskPriority {
    HIGH = 1,
    MID = 2,
    LOW = 3
}

enum EventType {
    DUTY = 0,
    PLANNED_VACATION = 1,
    VACATION = 2,
    ADD_HOLIDAY = 3,
    HOLIDAY = 4,
    ADD_HOURS = 5,
    HOURS = 6,
    ILL = 7,
    BUSINESS = 8,
    STUDY = 9,
}

enum EventStatus {
    NEW = 1,
    PLANNED = 2,
    ACCEPT = 3,
    CANCEL = 4,
}

enum UserStatTypes {
    REWARD = 1,
    CLASSIFICATION = 2,
    QUALIFICATION = 3,
    CONTRACT = 4,
}

// подразделение
struct Department {
    1: i64 id,
    2: string name,
    3: optional string description
}

// начальник/подчиненный
struct UserRole {
    1: i64 id,
    2: string name,
    3: optional string description
}

// группа внутри подразделения
struct UserGroup {
    1: i64 id,
    2: string name,
    3: optional string description
}

struct User {
    1: i64 uid,
    2: i64 dept,
    3: i64 role,
    4: i64 group,
    5: string firstname,
    6: string middlename,
    7: string lastname,
    8: DateTime birthday,
    9: string phone,
    10: string phone_mobile,
    11: DateTime work_start,
    12: RankType rank,
    13: i64 hours
}

struct Event {
    1: i64 id,
    2: i64 user,
    3: EventType etype,
    4: DateTime dt_start,
    5: optional DateTime dt_end,
    6: EventStatus status,
    7: optional i64 hours,
    8: optional string comment
}

struct Task {
    1: i64 id,
    2: TaskStatus status,
    3: TaskType ttype,
    4: TaskPriority priority,
    5: i64 owner,
    6: i64 creator,
    7: string title,
    8: string description,
    9: DateTime dt_created,
    10: optional DateTime deadline
}

struct ExtraWeekend {
    1: i64 id,
    2: DateTime date,
    3: bool weekend
}

struct UserStat {
    1: i64 id,
    2: i64 user,
    3: UserStatTypes stype,
    4: DateTime dt_start,
    5: optional DateTime dt_end
}

exception InvalidValueException {
    1: i64 error_code,
    2: string error_msg
}

service CalendarManager {
    bool            add_department              (1: Department d)                throws (1: InvalidValueException e)
    bool            edit_department(
                        1: i64 id,
                        2: JSONObjects data 
                    )

    bool            add_user_role               (1: UserRole ur)                 throws (1: InvalidValueException e)
    bool            edit_user_role(
                        1: i64 id,
                        2: JSONObjects data 
                    )

    bool            add_user_group              (1: UserGroup ug)                throws (1: InvalidValueException e)
    bool            edit_user_group(
                        1: i64 id,
                        2: JSONObjects data 
                    )

    bool            add_user                    (1: User u)                      throws (1: InvalidValueException e)
    JSONObjects     get_user                    (1: i64 id)
    JSONObjects     get_users                   ()

    bool            add_event                   (1: Event a)                     throws (1: InvalidValueException e)
    JSONObjects     get_new_events              ()
    JSONObjects     get_user_events             (1: i64 id)
    JSONObjects     get_users_events_stat       ()
    JSONObjects     get_events(
                        1: DateTime f, // from
                        2: DateTime t  // till
                    )
    bool            edit_event(
                        1: i64 eid,
                        2: JSONObjects data 
                    )
    bool            set_event_status(
                        1: i64 eid,
                        2: i64 status
                    )
    bool            add_task                    (1: Task t)                      throws (1: InvalidValueException e)
    JSONObjects     get_task                    (1: i64 id)
    JSONObjects     get_tasks()
    JSONObjects     get_user_tasks              (1: i64 id)
    bool            edit_task(
                        1: i64 tid,
                        2: JSONObjects data 
                    )

    bool            add_weekend                  (1: ExtraWeekend w)             throws (1: InvalidValueException e)

    JSONObjects     get_weekends(
                        1: DateTime first,
                        2: DateTime last
                    )

    JSONObjects     get_today_birthday          ()
    JSONObjects     get_today_vacation          ()
    JSONObjects     get_today_holiday           ()
    JSONObjects     get_today_duty              ()

    bool            users_stat                  ()
}