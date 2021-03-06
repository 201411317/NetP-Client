class SettingFrameHandler:
    client = None

    # Constructor for Login setting Handler instance
    def __init__(self, client):
        self.client = client

    # Send Change Password Request to Server
    def changePW(self, id, curPW, newPW, newPW2):
        if newPW != newPW2:
            msg = 'Check PW and PW2'
        else:
            changeDict = {'MSG': '/CHPW', 'NEWPW': newPW, 'CURPW': curPW}
            self.client.sendMsg(changeDict)
            self.client.sem.acquire()
            if self.client.rcvThread.msg == 'ACK':
                self.client.rcvThread.msg == ''
                msg = '''Change PW Pass'''
                return True, msg
            else:
                msg = '''Change PW Failed'''
        return False, msg

    # Send Charge Money Request to Server
    def chargeMoney(self, money):
        chargeDict = {'MSG': '/CHMN', 'MONEY': money}
        self.client.sendMsg(chargeDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            self.client.rcvThread.msg == ''
            msg = '''Charge Money Complete'''
            return True, msg
        else:
            msg = '''Change Money Failed'''
        return False, msg

    # Send Auction List Request to Server
    def aucList(self):
        aucDict = {'MSG': '/ACLT'}
        self.client.sendMsg(aucDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            msg = '''Get List Complete'''
            return True, msg
        else:
            msg = '''No Auction List'''
        return False, msg

    # Send Purchased List Request to Server
    def purchaseList(self):
        purDict = {'MSG': '/PCLT'}
        self.client.sendMsg(purDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            msg = '''Get List Complete'''
            return True, msg
        else:
            msg = '''No Purchased List'''
        return False, msg

    def watchList(self):
        watchDict = {'MSG': '/WCLT'}
        self.client.sendMsg(watchDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            msg = '''Get List Complete'''
            return True, msg
        else:
            msg = '''No Watch List'''
        return False, msg