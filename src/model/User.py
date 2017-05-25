class User():
    '''
    Class used to store the users and process their info
    '''

    def __init__(self):
        self.distinguishedname = ""
        self.sid = ""
        self.samaccountname = ""
        self.samaccounttype = ""
        self.deleted = False
        self.enabled = True
        self.lastlogon = ""
        self.displayname = ""
        self.givenname = ""
        self.surname = ""
        self.nthash = ""
        self.lmhash = ""
        self.nthistory = []  # Defined as property. It is set without append.
        self.lmhistory = []  # Defined as property. It is set without append.
        self.cleartext = ""
        self.wdigest = []  # Defined as property. It is set without append.

    @property
    def distinguishedname(self):
        return self.distinguishedname

    @distinguishedname.setter
    def distinguishedname(self, value):
        self.distinguishedname = value

    @property
    def sid(self):
        return self.sid

    @sid.setter
    def sid(self, value):
        self.sid = value

    @property
    def samaccountname(self):
        return self.samaccountname

    @samaccountname.setter
    def samaccountname(self, value):
        self.samaccountname = value

    @property
    def samaccounttype(self):
        return self.samaccounttype

    @samaccounttype.setter
    def samaccounttype(self, value):
        self.samaccounttype = value

    @property
    def deleted(self):
        return self.sid

    @deleted.setter
    def deleted(self, value):
        self.deleted = value

    @property
    def enabled(self):
        return self.enabled

    @enabled.setter
    def enabled(self, value):
        self.enabled = value

    @property
    def lastlogon(self):
        return self.lastlogon

    @lastlogon.setter
    def lastlogon(self, value):
        self.lastlogon = value

    @property
    def displayname(self):
        return self.displayname

    @displayname.setter
    def displayname(self, value):
        self.displayname = value

    @property
    def givenname(self):
        return self.givenname

    @givenname.setter
    def givenname(self, value):
        self.givenname = value

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, value):
        self.surname = value

    @property
    def nthash(self):
        return self.nthash

    @nthash.setter
    def nthash(self, value):
        self.nthash = value

    @property
    def lmhash(self):
        return self.lmhash

    @lmhash.setter
    def lmhash(self, value):
        self.lmhash = value

    @property
    def cleartext(self):
        return self.cleartext

    @cleartext.setter
    def cleartext(self, value):
        self.cleartext = value

    @property
    def nthistory(self):
        return self.nthistory

    @nthistory.setter
    def nthistory(self, value):
        self.nthistory = value

    @property
    def lmhistory(self):
        return self.lmhistory

    @lmhistory.setter
    def lmhistory(self, value):
        self.lmhistory = value

    @property
    def wdigest(self):
        return self.wdigest

    @wdigest.setter
    def wdigest(self, value):
        self.wdigest = value