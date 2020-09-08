
class Student01(object):
    
    def __init__(self, math, chinese) -> None:
        self.math = math
        self.chinese = chinese
        
    def __repr__(self) -> str:
        return "Object {}, math {}, chinese {}.".format(Student01, self.math, self.chinese)
    
def main():
    
    evan = Student01(100, 10000)
    evan.__repr__()
    
if __name__ == "__main__":
    main()