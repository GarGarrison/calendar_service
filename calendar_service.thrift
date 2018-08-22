namespace py calendar

enum RankType {
    NUB = 1,
    OBERNUB = 2,
    BOSS = 3

}

enum Status {
    CREATED = 1,
    OPENED = 2,
    CLOSED = 3
}

struct User {
    1: i32 uid,
    2: string firstname,
    3: string middlename,
    4: string lastname,
    5: string phone,
    6: RankType rank
}

struct Task {
    1: i32 id,
    2: Status status,
    3: i32 uid,
    4: string title,
    5: string description,
    6: string date_start,
    7: string date_end
}

exception InvalidValueException {
    1: i32 error_code,
    2: string error_msg
}

service UserManager {
    i32 add_user(1:User u) throws (1: InvalidValueException e),
    User get_user(1: i32 uid) throws (1: InvalidValueException e)
}