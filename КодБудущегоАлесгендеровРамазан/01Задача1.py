class School:
  def __init__(self, id, age ,population):
    self.id = id
    self.age = age
    self.population = population

firstSchool = School(13, 25, 1500)

print(firstSchool.id, firstSchool.age, firstSchool.population)

firstSchool.age= 27 
firstSchool.population=1650

print(firstSchool.id, firstSchool.age, firstSchool.population)