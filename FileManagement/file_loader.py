class FileLoader:
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