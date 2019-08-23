import os.path
import filecmp
import shutil
import sqlite3
from sqlite3 import Error


class ConDat:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.sqlite")

    def __init__(self, create_connection):
        self._create_connection = create_connection

    def create_connection(default=db_path):
        """
        Create connection.
        :param default: database path.
        :return: connection object
        """
        global globconn
        globconn = sqlite3.connect(default)
        try:

            cur = globconn.cursor()
            print("connection established") # debuging purpose
            cur.execute("CREATE TABLE IF NOT EXISTS directories("
                        "pk INTEGER PRIMARY KEY,"
                        " fromdir TEXT,"
                        " todir TEXT,"
                        " active INTEGER)")
            globconn.commit()
            print("table has been created if didnt exist") # deb purpose
            return globconn
        except Error as e:
            print(e)
            return None


def create_database_entry(dir1, dir2, conn=globconn()):
    """
    Create database entry.
    :param dir1: directory from which files are going to be copied
    :param dir2: directory to which files are going to be copied
    :param conn: connection object
    :return: dir1 and dir2
    """

    cur = conn.cursor()
    try:
        cur.execute("UPDATE directories SET fromdir=?, todir=? WHERE pk=1",
                    (dir1, dir2))
        conn.commit()
        print("records updated successfully")
        conn.commit()
        conn.close()
        return dir1, dir2
    except sqlite3.IntegrityError:
        print("ERROR:")
#    def new_directories(dir1=create_database_entry())


def select_all_entries(conn=globconn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM directories")

    rows = cur.fetchall()


def delete_directory(dir1, dir2, conn=globconn):
    """
    Delete selected query
    :param conn:
    :return:
    """
    cur=conn.cursor()
    cur.execute("")


def compare_copy(dir1, dir2):
    """
    :param dir1:
    :param dir2:
    :return:
    """

    comp_ari = filecmp.dircmp(dir1, dir2).left_only
    if comp_ari:
        for f in comp_ari:
            shutil.copy2(dir1+r"\{}".format(f), dir2)
#            copylist.append(os.listdir(dir1+r"\n" + f))
            print(comp_ari)
    else:
        print("nothing to copy my frieeeeend.")
       # print(type(compare_copy)

