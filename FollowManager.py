try:
    import requests
    from time import sleep
    import  random,os,user_agent
    from colorama import init,Fore
except:
    for lb in open('requirements.txt','r').read().splitlines():
        os.system(f'pip install {str(lb)}')
    import requests
    from time import sleep
    import  random,os,user_agent
    from colorama import init,Fore
init(autoreset=True)
cr=Fore.RED
cy=Fore.YELLOW
cg=Fore.GREEN

class mka():

    def getusers(self):
        try:

            listid=[]
            url='https://i.instagram.com/api/v1/friendships/pending/'
            headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9',
                'cookie': f'mid=YgEtDAALAAG5XG7m9rn-w4skBvu8; ig_did=514E1762-66AB-44CE-88A0-59CDE64E392C; ig_nrcb=1; csrftoken=bdPttBDgBwatsmpggGIa6tA6k5eCGkGW; ds_user_id=51724955394; sessionid={self.sessionid}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',
                'x-asbd-id': '198387',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3PLklyPgm7YHjEjKznNP4thi2G_zj_FjF8gZFpEGkeEbVz',
            }
            resjson = requests.get(url=url,headers=headers).json()
            lstusers= resjson['users']
            for itm in lstusers:
                userid=itm['pk']
                username=itm['username']
                if userid not in listid:
                    listid.append(userid)
                    if self.qui==1:self.accept(userid,username)
                    if self.qui==2:self.ignore(userid, username)
                    sleep(random.randint(0,5))
        except Exception as ex:
            print(ex)
    def accept(self,userid:str,username:str):
        try:
            url=f'https://www.instagram.com/web/friendships/{userid}/approve/'
            header={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'mid=YgEtDAALAAG5XG7m9rn-w4skBvu8; ig_did=514E1762-66AB-44CE-88A0-59CDE64E392C; ig_nrcb=1; csrftoken=bdPttBDgBwatsmpggGIa6tA6k5eCGkGW; ds_user_id=51724955394; sessionid={self.sessionid}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',
                'x-asbd-id': '198387',
                'x-csrftoken': 'bdPttBDgBwatsmpggGIa6tA6k5eCGkGW',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3PLklyPgm7YHjEjKznNP4thi2G_zj_FjF8gZFpEGkeEbVz',
                'x-instagram-ajax': '9a16d12cf843',
                'x-requested-with': 'XMLHttpRequest',
            }
            res=requests.post(url=url,headers=header).text
            if '{"status":"ok"}' in res:
                print(cg+f'Succes Accept Mr : {username}')
            else:
                print(cr+res)
        except Exception as ex:
            print(cr+f'Error While Clean \n {ex}')
 
    def ignore(self,userid:str,username:str):
        try:
            url=f'https://www.instagram.com/web/friendships/{userid}/ignore/'
            header={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'mid=YgEtDAALAAG5XG7m9rn-w4skBvu8; ig_did=514E1762-66AB-44CE-88A0-59CDE64E392C; ig_nrcb=1; csrftoken=bdPttBDgBwatsmpggGIa6tA6k5eCGkGW; ds_user_id=51724955394; sessionid={self.sessionid}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',
                'x-asbd-id': '198387',
                'x-csrftoken': 'bdPttBDgBwatsmpggGIa6tA6k5eCGkGW',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3PLklyPgm7YHjEjKznNP4thi2G_zj_FjF8gZFpEGkeEbVz',
                'x-instagram-ajax': '9a16d12cf843',
                'x-requested-with': 'XMLHttpRequest',
            }
            res=requests.post(url=url,headers=header).text
            if '{"status":"ok"}' in res:
                print(cg+f'Succes ignore Mr : {username}')
            else:
                print(cr+res)
        except Exception as ex:
            print(cr+f'Error While Clean \n {ex}')
        
    def checkssid(self,ssid):
        headers = {
                'X-IG-Connection-Type':'WIFI',  'X-IG-Capabilities':'3brTBw==', 
                'User-Agent':'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)', 
                'Accept-Language':'en-US', 
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                'Accept-Encoding':'gzip, deflate', 
                'Host':'i.instagram.com', 
                'Connection':'keep-alive', 
                'Accept':'*/*'}    
        cookies = {'sessionid': str(ssid)}		
        response = requests.request('GET','https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=headers, cookies=cookies)
        if str('message') in str(response.json()):
            print(cr+' \n</message>  Login  Account Error ');sleep(1)
            os.sys.exit()			
        else:
            self.sessionid=ssid
            print(cg+' \n</>  Login  Account Successful ');sleep(1)
        
    def login(self,user,pswrd):
        try:
            r1 = requests.get('https://www.instagram.com',headers={'user_agent': str(user_agent.generate_user_agent())}).cookies
            data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' +
            str(pswrd), 'username': str(user)}
            r2 = requests.post('https://www.instagram.com/accounts/login/ajax/', headers={'user_agent': str(user_agent.generate_user_agent()), 'x-csrftoken': str(r1['csrftoken'])}, data=data)          
            if 'userId' in r2.text:
                self.sessionid= str(r2.cookies['sessionid'])
                print(cg+' \n</>  Login  Account Successful ');sleep(1)
            elif 'checkpoint_required' in r2.text:
              	 print(cy+' \n</>  Login  Account checkpoint_required');sleep(1);os.sys.exit()
            else:
                print(cr+' \n</message>  Login  Account Error ');sleep(1)
                os.sys.exit()
        except Exception as ex:
            print(ex)
            print(cr+' \n</message>  Login  Account Error ');sleep(1)
            os.sys.exit()

    def __init__(self):
        os.system('cls')
        logo='''
                    █████               █████                          ██████████             
                  ███░░░███            ░░███                          ░░███░░░░███            
 █████████████   ███   ░░███ █████ ████ ░███ █████  ██████             ░███   ░░███  █████████
░░███░░███░░███ ░███    ░███░░███ ░███  ░███░░███  ░░░░░███            ░███    ░███ ░█░░░░███ 
 ░███ ░███ ░███ ░███    ░███ ░███ ░███  ░██████░    ███████            ░███    ░███ ░   ███░  
 ░███ ░███ ░███ ░░███   ███  ░███ ░███  ░███░░███  ███░░███            ░███    ███    ███░   █
 █████░███ █████ ░░░█████░   ░░████████ ████ █████░░████████ █████████ ██████████    █████████
░░░░░ ░░░ ░░░░░    ░░░░░░     ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░░░░░░░░ ░░░░░░░░░░    ░░░░░░░░░ 
                                                                                              
                                                                                              
                                                                                              
                                                     T.me/@lllll8  

        '''
        print(cg+logo)
        where=input(cg+"[1] Login User:Pass\n[2] Login Sessionid\n[+] What Your Choice ?: ")
        if where =='1':
            os.system('cls')
            print(cg+logo)
            username=input(cy+'[+] Enter UserName : ')
            password=input(cy+"[+] Enter PassWord : ")
            self.login(username, password)
            self.qui=input(cy+'\n\n[1] For Accept\n[2] For ignore\nWhat Your Choice ?: ')
            self.getusers()
        elif where=='2':
             os.system('cls')
             print(cg+logo)
             ssid=input(cy+'[+] Enter Sessionid : ')
             self.checkssid(ssid)
             qui=input(cy+'\n\n[1] For Accept\n[2] For ignore\nWhat Your Choice ?: ')
             if qui=='1':self.qui=1
             elif qui=='2':self.qui=2
             else:print(cr+'Wrong Number');exit()
             self.getusers()
mka()
