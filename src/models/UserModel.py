from src.utils.Logger import Logger


class User:
    cursor = None
    connection = None

    def __init__(self, id, username, password, fullname) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    def add_cursor_and_connection(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    def create_db(self):
        try:
            query = (f"INSERT INTO `user` (`username`, `password`, `fullname`) "
                     f"VALUES ('{self.username}', '{self.password}', '{self.fullname}')")
            Logger.add_to_log("debug", query)
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            Logger.add_to_log("error", e)

    def update(self):
        query = (f"UPDATE `user` "
                 f"SET "
                 f"`username`='{self.username}', "
                 f"`password`='{self.password}', "
                 f"`fullname`='{self.fullname}' "
                 f"WHERE "
                 f"`id`={self.id}")
        self.cursor.execute(query)
        self.connection.commit()

    def get_by_id(self):
        query = "SELECT * FROM `user` WHERE `id` = %s;"
        self.cursor.execute(query, (self.id,))
        result = self.cursor.fetchone()
        print(result)
        return result

    def destroy(self):
        sql = f"DELETE FROM `user` WHERE `id`={self.id}"
        self.cursor.execute(sql)
        self.connection.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.username,
            'fullName': self.fullname
        }
