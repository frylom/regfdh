class Whole_Apple:
    def about(self):
        print('I am whole Apple')
    def about_myself(self):
        print('I am whole Apple')
class Half_A_Whole_Apple(Whole_Apple):
    def about_myself(self):
        print('I am half a whole Apple')
class Half_A_Half_Of_A_Whole_Apple(Half_A_Whole_Apple):
    height = 8
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

class Half_A_Half_Of_A_Whole_Apple(Half_A_Whole_Apple):
    def __init__(self):
        super().about()
        super().about_myself()

nick = Half_A_Half_Of_A_Whole_Apple()