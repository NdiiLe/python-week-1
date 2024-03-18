class Group:
  def __init__(self, group, week, topic):
    self.group = group
    self.week = week
    self.topic = topic
print(".........................................")
group = input("Enter your group name :")
week = int(input("Enter python learning week :"))
topic = input("What topic are you focusing on :")
print(".........................................")
p1 = Group(group, week, topic)

print("Welcome " + p1.group + " you are in week " + str(p1.week) + " and learning " + topic +".")
print("Keep up the good work " + group +".")