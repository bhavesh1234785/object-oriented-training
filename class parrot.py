#create class
class parrot:
    #class attribute
    species="bird"
    #instance attribute
    def __int__(self,name,age):
        self.name=name
        self.name=age
#instantiate the parrot class
blu=parrot("Blu",10)
woo=parrot("woo",15)
#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))
#access the instance attributes
print("{}is{}years old".format(blu.name,blu.age))
print("{}is{}years old".format(woo.name,woo.age))