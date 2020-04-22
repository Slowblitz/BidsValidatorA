class DataError(Exception):
    def __init__(self, arg):
        names=arg
        self.strerror = "\nError 1 type [Data folder error ] at : " + names[0]+"\n \nThe general folder structure does not resemble a BIDS dataset. Have you chosen the right folder (data) ? Or does not respect the naming convention for a subject directory, which is (data). Check for structural/naming issues."

class SubError(Exception):
    def __init__(self, arg):
        names=arg
        self.strerror = "\nError 2 type [Subject folder error] at : "+names[2]+"\n \ndoes not respect the naming convention for a subject directory, which is (sub-GUID) Check for structural/naming issues"

class DateError(Exception):
    def __init__(self, arg):
        names=arg
        self.strerror ="\nError 3 type [Date folder error] at : "+names[3]+"\n \nIt does not respect the naming convention for a session directory, which is  [yymmdd] _ numéro de session (expérience) _ espèce [m, o, r, s] _ UFID animal(User friendly ID) _ commentaire libre [anesth/awake, nom de manip, méthode d’imagerie etc.] Check for structural/naming issues."   

class SourceError(Exception):
    def __init__(self, arg):
        names=arg
        self.strerror ="\nError 4 type [Source folder error] at : "+names[4]+"\n \ndoes not respect the naming convention for a subject directory, which is (source) Check for structural/naming issues"
   