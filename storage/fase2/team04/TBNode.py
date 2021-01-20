# Package:      Storage Manager
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Alexis Peralta

# Nodos utilizados en las listas TBList
class TBNode:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.pk = []
        self.fk = []
        self.iu = []
        self.indx = []
        self.compress = False
        self.safeMode = False
        self.hidden = False
        self.next = None