from abc import ABC, abstractmethod

class Absclass(ABC):
    
    def print(self,x):
        print("Passed value is: ", x)
    
    @abstractmethod
    def task(self):
        pass

class test_class(Absclass):
    
    def task(self):
        print("Task method implemented in test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)