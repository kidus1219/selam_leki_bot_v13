class Me():
    def __init__(self, uid, username, name):
        self.uid = uid
        self.username = username
        self.name = name
        self.nick_name = None
        self.phone = None
        self.lang = "English"
        self.star = 0
        self.accepted = 0
        self.declined = 0
        self.is_registered = False

    def dict_form(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'name': self.name,
            'nick_name': self.nick_name,
            'phone': self.phone
        }

