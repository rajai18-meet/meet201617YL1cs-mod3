class Student():
    """
    hi
    """
    def __init__(self, name, hometown, age, height, icecream):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.icecream=icecream
    def print_summary(self):
        print ('The name of the person is '+str(self.name)+", he/she lives in " +str(self.hometown)+', he/she is ' +str(self.age)+' years old, he/she has a height of ' +str(self.height)+ ", and the person's favorite icecream flavor is "+ str(self.icecream)+".")

    def get_giraffe_gap(self):
        return (str(500-int(self.height)))
                
    

