from os.path import exists


class UTIDService:
    def __init__(self):
        self.utid = 1
        if not exists("../Service/utid.txt"):
            self.create_id_to_file()
        else:
            self.utid = self.read_id_from_file()
            self.append_to_file(int(self.utid))

    def create_id_to_file(self):
        f = open("../Service/utid.txt", "w")
        f.write(str(self.utid))
        f.close()

    @staticmethod
    def read_id_from_file():
        read_file = open("../Service/utid.txt", "r")
        return int(read_file.read()) + 1

    @staticmethod
    def append_to_file(current_utid):
        f = open("../Service/utid.txt", "w")
        f.write(str(current_utid))
        f.close()
