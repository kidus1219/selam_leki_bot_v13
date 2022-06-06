class Me():
    def __init__(self, uid, username, name):
        self.uid = uid
        self.username = username
        self.name = name
        self.nick_name = None
        self.phone = None
        self.lang = "English"
        self.star = 0
        self.my_mezmurs = 0
        self.is_registered = False

    def dict_form(self):
        return {
            'uid': self.uid,
            'username': self.username,
            'name': self.name,
            'nick_name': self.nick_name,
            'phone': self.phone,
            'lang': self.phone,
            'star': self.star,
            'my_mezmurs': self.my_mezmurs,
            'is_registered': self.is_registered,
        }

    def update_me(self, **kwargs):
        self.star = kwargs.get('star', self.star)
        self.my_mezmurs = kwargs.get('my_mezmurs', self.my_mezmurs)
        return self
