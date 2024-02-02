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
                    return user.get_by_id()
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
                if user.id is not None:
                    user.add_cursor_and_connection(cursor, connection)
                    user.create_db()
                else:
                    print("User not found")

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
                    user.update()
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
