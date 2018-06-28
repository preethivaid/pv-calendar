import os
import psycopg2
this_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(this_dir, '..', '.env')
from dotenv import load_dotenv
load_dotenv(dotenv_path=env_path)

google_cal_auth = os.getenv('GOOGLE_CAL_AUTH')


class AddToDb:

    def __init__(self):
        self.conn = psycopg2.connect("dbname={} user={} host={} password={}".format(os.getenv('dbname'),
                                                                                    os.getenv('user'),
                                                                                    os.getenv('host'),
                                                                                    os.getenv('password')))
        self.cursor = self.conn.cursor()

    def create_secrets_table(self):
        schema_file = os.path.join(this_dir, "schema.sql")
        self.cursor.execute(open(schema_file, "r").read())
        self.conn.commit()

    def drop_secrets_table(self):
        query = "DROP TABLE secrets;"
        self.cursor.execute(query)
        self.conn.commit()

    def add_secret(self, secret_key, secret_value):
        query = "INSERT INTO secrets (secret_key, secret_value) VALUES (%s, %s);"
        data = (secret_key, secret_value,)
        self.cursor.execute(query, data)
        self.conn.commit()

    def read_secret(self, secret_key):
        query = "SELECT secret_value FROM secrets WHERE secret_key = %s;"
        data = (secret_key,)
        self.cursor.execute(query, data)
        secret_value = self.cursor.fetchall()[0][0]
        return secret_value



if __name__=="__main__":
    # AddToDb().drop_secrets_table()
    # AddToDb().create_secrets_table()
    AddToDb().add_secret('test1', 'test2')
    # AddToDb().read_secret('test1')
    # AddToDb().add_to_table('test_key', 'test_val')
