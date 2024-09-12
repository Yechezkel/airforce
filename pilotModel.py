class Pilot:

    def __init__(self, name,skill_level):
        self.name = name
        self.skill_level = skill_level

    def get_string(self):
        return f"name: {self.name},   skill level: {self.skill_level}."