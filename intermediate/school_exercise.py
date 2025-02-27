sch_levels = ['primary', 'middle', 'high']

class School:  
  def __init__(self, name, level, numberOfStudents):
    self.__name = name
    self.__level = level
    self.__numberOfStudents = numberOfStudents 
  
  @property
  def name(self):
    return self.__name
  @property
  def level(self):
    return self.__level
  @property
  def numberOfStudents(self):
    return self.__numberOfStudents
  
  @name.setter
  def name(self, name_str):
    self.__name = name_str
  @level.setter
  def level(self, level):
    self.__level = level if level in sch_levels else None
  @numberOfStudents.setter
  def numberOfStudents(self, number_of_students):
    if isinstance(number_of_students, int):
      self.__numberOfStudents = number_of_students
    else:
      raise TypeError

  def __repr__(self):
    print(f"A {self.__level} school named {self.__name} with {str(self.__numberOfStudents)} students")

  def __str__(self):
    return f"A {self.__level} school named {self.__name} has {str(self.__numberOfStudents)} students"

class PrimarySchool(School):
  def __init__(self, name, number_of_students, pick_up_policy):
    super().__init__(name, "primary", number_of_students)
    self.__pickupPolicy = pick_up_policy
  
  @property
  def pickupPolicy(self):
    return self.__pickupPolicy

  @pickupPolicy.setter
  def pickupPolicy(self, policy):
    self.__pickupPolicy = policy
  
  def __repr__(self):
    super().__repr__()
    print(f"The pick-up policy for {self.name} primary school is {self.__pickupPolicy}")
  
  def __str__(self):
    super().__repr__()
    return f"The pick-up policy for {self.name} primary school is {self.__pickupPolicy}"


class MiddleSchool(School):
  def __init__(self, name, number_of_students):
    super().__init__(name, 'middle', number_of_students)

class HighSchool(School):
  def __init__(self, name, number_of_students, sports_teams):
    super().__init__(name, "high", number_of_students)
    self.__sportsTeams = sports_teams
  
  @property
  def sportsTeams(self):
    return self.__sportsTeams

  @sportsTeams.setter
  def sportsTeams(self, sports_teams):
    self.__sportsTeams = sports_teams

  def __repr__(self):
    print(f"The {self.level} school named {self.name} has the following {self.__sportsTeams} teams")

  def __str__(self):
    return f"The {self.level} school named {self.name} has the following {', '.join(self.__sportsTeams)} teams"


my_school = PrimarySchool("Mugwanya", 256, "Pick up after 3pm")
print(my_school)
print("\n")

school_teams = ['Rugby', 'Football', 'Swimming', 'Hockey', 'Basketball']
secondary = HighSchool("SMACK", 1000, school_teams)
print(secondary)
print("\n")

middle_sch = MiddleSchool("Seeta Boarding", 128)
print(middle_sch)