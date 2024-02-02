import traceback

# Database
from src.database.db_mysql import get_connection
# Models
# Logger
from src.utils.Logger import Logger


class UserService:

    @classmethod
    def find(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                if user.id is not None:
                    user.add_cursor_and_connection(cursor, connection)
                    result = user.get_by_id()
                    return user.tuple_to_dict(result)
                else:
                    print("User not found")

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def save(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                if user.id is None:
                    user.add_cursor_and_connection(cursor, connection)
                    result = user.create_db()
                    return user.tuple_to_dict(result)
                else:
                    print("A new User not wold contain id")

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def update(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                user.add_cursor_and_connection(cursor, connection)

                if user.get_by_id() is not None:
                    result = user.update_db()
                    return user.tuple_to_dict(result)
                else:
                    print("User not found")

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def destroy(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                user.add_cursor_and_connection(cursor, connection)

                if user.get_by_id() is not None:
                    user.destroy()
                else:
                    print("Cant' destroy user")

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
