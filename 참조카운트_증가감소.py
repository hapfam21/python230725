class MyClass:
    #초기화메소드
    def __init__(self, value):
        self.Value = value 
        print("Insatance is created! Value = ", value)
    #소멸자메소드    
    def __del__(self):
        print("Instance is deleted!")
        

c = MyClass(10)
c_copy = c
del c 
del c_copy
