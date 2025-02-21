class Person:
    def __init__(self, name, educational_institutions, colleagues=None):
        self.name = name
        self.educational_institutions = educational_institutions
        self.colleagues = colleagues if colleagues else []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)

    def __repr__(self):
        return f"Person(name={self.name}, educational_institutions={self.educational_institutions}, colleagues={[c.name for c in self.colleagues]})"
