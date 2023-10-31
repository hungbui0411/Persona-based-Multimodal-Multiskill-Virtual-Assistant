class PersonaSpecs:
    def __init__(self,
                 name=None, # use
                 greeting=None,
                 short_description=None,
                 long_description=None, # use
                 character_categories=None,
                 persona_definition=None, # use
                 user_name=None):
        self.name = name
        self.greeting = greeting
        self.short_description = short_description,
        self.long_description = long_description,
        self.character_categories = character_categories,
        self.persona_definition = persona_definition
        self.user_name = user_name

        if type(self.name) == tuple:
            self.name = self.name[0]
        if type(self.greeting) == tuple:
            self.greeting = self.greeting[0]
        if type(self.short_description) == tuple:
            self.short_description = self.short_description[0]
        if type(self.long_description) == tuple:
            self.long_description = self.long_description[0]
        if type(self.persona_definition) == tuple:
            self.persona_definition = self.persona_definition[0]
        if type(self.user_name) == tuple:
            self.user_name = self.user_name[0]

    def print(self):
        print(self.name)
        print(self.greeting)
        print(self.short_description)
        print(self.long_description)
        print(self.persona_definition)
        print(self.user_name)
        print(type(self.name))
        print(type(self.greeting))
        print(type(self.short_description))
        print(type(self.long_description))
        print(type(self.persona_definition))
        print(type(self.user_name))

