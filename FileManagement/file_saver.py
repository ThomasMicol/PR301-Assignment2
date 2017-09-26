class FileSaver:
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