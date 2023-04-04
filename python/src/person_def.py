import datetime

class Person:
    def __init__(self, last_name, first_name, school, date_of_birth, username, affiliation):
        self.last_name = last_name
        self.first_name = first_name
        self.school = school
        self.date_of_birth = date_of_birth
        self.username = username
        self.affiliation = affiliation

    @property
    def email(self):
        return self.username + '@' + self.school.domain 