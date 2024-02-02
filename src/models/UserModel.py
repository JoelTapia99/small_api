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
            return self.get_last()
        except Exception as e:
            Logger.add_to_log("error", e)

    def update_db(self):
        try:
            query = (f"UPDATE `user` "
                     f"SET "
                     f"`username`='{self.username}', "
                     f"`password`='{self.password}', "
                     f"`fullname`='{self.fullname}' "
                     f"WHERE "
                     f"`id`={self.id}")
            self.cursor.execute(query)
            self.connection.commit()
            return self.get_by_id()
        except Exception as e:
            Logger.add_to_log("error", e)

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

    def get_last(self):
        query = "SELECT * FROM `user` order by id desc limit 1"
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.username,
            'fullName': self.fullname
        }

    @staticmethod
    def tuple_to_dict(tuple_res):
        return {
            'id': tuple_res[0],
            'name': tuple_res[1],
            'fullName': tuple_res[2]
        }
