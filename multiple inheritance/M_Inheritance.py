class Loggable:
    def __init__(self):
        self.title = ''

    def log(self):
        print('Log message from ' + self.title)


class Connection:
    def __init__(self) -> None:
        self.server = ''

    def connect(self):
        print('Connecting to database on ' + self.server)


def framework(item):
    if isinstance(item, Connection):
        item.connect()

    if isinstance(item, Loggable):
        item.log()


class SqlDatabase(Connection, Loggable):
    def __init__(self) -> None:
        super().__init__()
        self.title = "SQL Database Connection"
        self.server = "Some Server"


if __name__ == "__main__":
    sql_connection = SqlDatabase()
    framework(sql_connection)
