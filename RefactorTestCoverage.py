from interpreter import Interpreter
from Database.interface_database import IDatabase
import unittest

class CodeCoverage(unittest.TestCase):
    def setUp(self):
        self.db_interface = IDatabase()
        self.interpreter = Interpreter("dbName")

    def test_interpreter_dodisplaydata(self):
        self.interpreter.do_display_data("-o")

    def test_interpreter_doloadfromfile_txtfile(self):
        self.interpreter.do_load_from_file("file.txt")
        print(self.interpreter.database.backup_database())

    def test_interpreter_doloadfromfile_txtfile_d(self):
        self.interpreter.do_load_from_file("-d file.txt")
        print(self.interpreter.database.backup_database())
    
    def test_interpreter_doloadfromfile_txtfile_g(self):
        self.interpreter.do_load_from_file("-g file.txt")
        print(self.interpreter.database.backup_database())

    def test_interpreter_doloadfromfile_txtfile_invalid(self):
        self.interpreter.do_load_from_file("-invalid file.txt")
        print(self.interpreter.database.backup_database())

    def test_interpreter_do_backup_database_o(self):
        self.interpreter.do_backup_database("-o file.txt")

    def test_interpreter_do_backup_database_invalid(self):
        self.interpreter.do_backup_database("-invalid")

    def test_interperter_do_get_data(self):
        self.interpreter.do_get_data("select * from employees")

    def test_interpreter_do_display_graph(self):
        self.interpreter.do_display_graph("")

    def test_interpreter_do_list_graphs(self):
        self.interpreter.do_list_graphs("")

    @unittest.expectedFailure
    def test_databaseinterface_execute_sql(self):
        self.db_interface.execute_sql("string")

    @unittest.expectedFailure
    def test_databaseinterface_closeconnection(self):
        self.db_interface.close_connection()

    @unittest.expectedFailure
    def test_databaseinterface_commit(self):
        self.db_interface.commit()

    @unittest.expectedFailure
    def test_databaseinterface_setup(self):
        self.db_interface.setup()

    @unittest.expectedFailure
    def test_databaseinterface_reset(self):
        self.db_interface.reset()

    @unittest.expectedFailure
    def test_databaseinterface_displaydata(self):
        self.db_interface.display_data()

    @unittest.expectedFailure
    def test_databaseinterface_writetodatabase(self):
        self.db_interface.write_to_database("string")

    @unittest.expectedFailure
    def test_databaseinterface_backupdatabase(self):
        self.db_interface.backup_database()

    


if __name__ == "__main__":
    unittest.main()