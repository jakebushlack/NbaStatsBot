class Player:
    stats = []

    def __init__(self, _attr, _val):
        setattr(self, _attr, _val)

    def adding_new_attr(self, _attr, _val):
        setattr(self, _attr, _val)
