import os
import os.path
from archive import PygeArchive, GenericEntry


class FileSystem(PygeArchive):
    name = "directory"
    desc = "plain directory"

    def detect(self):
        return os.path.isdir(self.file.name)

    def _read(self):
        self.list = {}
        #for n in os.listdir(self.filename):
        #    self.list[n] = fpath, 0, os.stat(n).st_size
        for root, dirs, files in os.walk(self.file.name):
            for n in files:
                fpath = os.path.normpath(os.path.join(root, n))
                if os.path.isfile(fpath):
                    self.list[fpath] = {
                        "name": fpath,
                        "start": 0,
                        "length": os.stat(fpath).st_size
                    }
        return True

    def create(self, filelist):
        if os.path.isdir(self.file.name) is False:
            os.mkdir(self.file.name)

    def extract(self, filename):
        ifile = open(self.file.name + "/" + filename, 'rb')
        ofile = open(filename, 'wb')
        ofile.write(ifile.read(os.stat(filename).st_size))
        ofile.close()
        ifile.close()

    def append(self, filename):
        ifile = open(filename, 'rb')
        ofile = open(self.file.name + "/" + filename, 'wb')
        ofile.write(ifile.read(os.stat(filename).st_size))
        ofile.close()
        ifile.close()
