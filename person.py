class Person:
    def __init__(self, name, job=None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return  self.name.split()[-1] # берем последнее троковое значение после раделения

    def give_raise(self,percent):
        self.pay = int(self.pay * (1+percent))

    def __str__(self): # для изменения работы вывода в print
        return '[Person: '+ self.name + ',' + str(self.pay) + ']'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name,'mngr',pay)

    def give_raise(self,percent, bonus=100):
        Person.give_raise(self, percent + bonus)

ivan = Person('Ivan Petrov')
viktor = Person('Viktor Sidorov','dev',100000)
tom = Manager('tom Johnes',55000)

print(ivan)
print(viktor)
print(ivan.last_name())
print(viktor.last_name())
viktor.give_raise(.10)
print(viktor)
print(tom)
tom.give_raise(.6)
print(tom)


