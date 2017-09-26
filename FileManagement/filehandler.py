from FileManagement.interface_filehandler import *
# Brendan
import pickle
import os
import sys
# kate



# Kris Little design
class FileHandler(IFileHandler):
    def __init__(self):
        self.valid = True

    def to_object(self, contents):
        id = contents[0]
        sex = contents[1]
        age = contents[2]
        sales = contents[3]
        bmi = contents[4]
        salary = contents[5]
        dob = contents[6]
        person = {
            "id": id,
            "sex": sex,
            "age": age,
            "sales": sales,
            "bmi": bmi,
            "salary": salary,
            "dob": dob
        }
        return person

    # Kris
    def load_file(self, file):
        # put error handling here
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError:
            print("file does not exist.")
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(self.to_object(line))
            the_file.close()
            
            return contents

    def data_to_saveable_string(self, data):
        string = ""
        for person in data:
            string += str(person['id']) + ","
            string += str(person['sex'])  + ","
            string += str(person['age'])  + ","
            string += str(person['sales'])  + ","
            string += str(person['bmi'])  + ","
            string += str(person['salary'])  + ","
            string += str(person['dob'])  + ","
            string += "\n"

        print(string)
        return string

    # Kris
    def write_file(self, file, data):
        the_file = open(file, 'w')
        string = self.data_to_saveable_string(data)
        the_file.write(string)
        the_file.close()

    # Brendan Holt
    # Used to pickle the loaded graphs to default pickle file
    def pack_pickle(self, graphs):
        # Raises exception if the default file does not exits and creates it should this exception be raised
        try:
            realfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if not os.path.exists(realfilepath):
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfilepath))
            pass
        # The pickle process
        pickleout = open(realfilepath, "wb")
        pickle.dump(graphs, pickleout)
        pickleout.close()

    # Brendan Holt
    # Used to unpickle graphs in the pickle file and return them to the interpreters graph list
    def unpack_pickle(self, filepath):
        # Raises exception if for some reason the default file has been deleted
        try:
            if os.path.exists(filepath) is False:
                raise IOError
        except IOError:
            print('File does not exits')
            return
        # The unpickle process
        picklein = open(filepath, "rb")
        graphs = pickle.load(picklein)
        picklein.close()
        # Return the graphs to the interpreter
        return graphs

    # Brendan Holt
    # Used to pickle the entire database to default pickle file
    def pickle_all(self, data):
        # Raises exception if for some reason the default file has been deleted
        try:
            realfiledirectory = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\"
            if os.path.exists(realfiledirectory) is False:
                raise IOError
        except IOError:
            os.makedirs(os.path.dirname(realfiledirectory))
            return
        # The pickle process
        pickleout = open(realfiledirectory + "\\db_backup.dat", "wb")
        pickle.dump(data, pickleout)
        pickleout.close()
