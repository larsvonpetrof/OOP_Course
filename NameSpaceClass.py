#Name space of Class

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2
    
    def info(self):
        #these names are not available here
        #except they are globally determined
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, 
              DepartmentIT.REACT_DEV)
        
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_satic():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV,
              DepartmentIT.REACT_DEV)

    def hiring_pyt_dev(self):
        self.PYTHON_DEV += 1 #DepartmentIT.PYTHON_DEV is not re-determined 
        DepartmentIT.PYTHON_DEV += 1 #not is re-determined


it1 = DepartmentIT()
it1.info_prop #as a property

