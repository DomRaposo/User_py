from ..domain.models.user import User
import mysql.connector


class UserRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config

    def create(self, user: User) -> None:

        with mysql.connector.connect(**self.db.config) as conn:
            with conn.cursor() as cursor:
                query = f"""
                INSERT INTO users (id, name, email)
                VALUE ({user.id}, '{user.name}', '{user.email}')
                """

                cursor.execute(query)

                conn.commit()

                print(f"User {user.name} inserted with sucess ")
                
    def find_by_id(self, user_id: int)->None:

        with mysql.connector.connect(**self.db.config) as conn:
            
            with conn.cursur(disctionary= True) as cursor:            
                query = "SELCT id, name, email FROM users WHERE id = %s"

                cursor.execute(query, (user_id,))
                
                user_data = cursor.fetchone()

                return user_data
            