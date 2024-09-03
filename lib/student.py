#!/usr/bin/env python


from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Initialize first_name and last_name from the User class
        super().__init__(first_name, last_name)
        # Initialize self.knowledge as an empty list
        self.knowledge = []

    def learn(self, new_knowledge):
        # Add the new string to the student's knowledge list
        self.knowledge.append(new_knowledge)
