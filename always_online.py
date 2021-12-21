import os
import time
from BitSrunLogin.LoginManager import LoginManager
import user_login
import argparse
 

def get_args():
    parser = argparse.ArgumentParser(description="always_online.py script description")      # description参数可以用于插入描述脚本用途的信息，可以为空。
    parser.add_argument("--test_ip", "-ip", type=str, default="114.114.114.114", help="ip address to test connection")
    parser.add_argument("--invl", "-invl", type=int, default=5*60, help="interval to checking online, unit is second")
    args = parser.parse_args()
    return args
def is_connect_internet(testip):
    status = os.system(u"ping {} -c 8".format(testip))
    return status == 0

def always_login(username, password, testip, checkinterval):
    lm = LoginManager()
    login = lambda : lm.login(username=username, password=password)
    timestamp = lambda : print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        time.sleep(checkinterval) 
        if not is_connect_internet(testip):
            timestamp()
            try:
                login()
            except Exception:
                pass
        
if __name__ == "__main__":
    # username = "Your srun account name"
    # password = "Your password"
    #parse argumentation
    args = get_args()
    testip = "114.114.114.114" # IP to test whether the Internet is connected
    checkinterval = 5 * 60
    if args.test_ip:
        test_ip = args.test_ip
    if args.invl:
        checkinterval = args.invl
    print("your test_ip = {}".format(test_ip))
    print("your check_interval = {}".format(checkinterval))

    username = user_login.input_username()
    password = user_login.input_password()
    
    # checkinterval = 5

    always_login(username, password, testip, checkinterval)
