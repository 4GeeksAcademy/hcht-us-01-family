"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []  # Example list of members

    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        new_members = [row for row in self._members if row['id'] != id]
        self._members = new_members

    def get_member(self, id):
        member = [row for row in self._members if row['id'] == id]
        print(member)
        if not member:
            return False
        return member[0]
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
