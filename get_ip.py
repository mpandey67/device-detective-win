import subprocess
import re
def get_ip_addr():
    i=0
    ipconfig_value=subprocess.check_output(["ipconfig"])
    lhost=re.search(r"\d\d\d.\d\d\d.\d[0-9]*.", str(ipconfig_value))
    if not lhost:
        print("\ncheck your internet connection. CONNECT TO A NETWORK")
        print("EXITING...")
        exit()
    lhost=lhost.group(0)
    lhost=lhost+"1/24"
    print("\nLOCAL HOST RANGE FOUND AT "+lhost+" press enter to set this or provide a valid LHOST range on this device")
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    user_lhost = input(">>")
    user_lhost = user_lhost.strip(' ')
    if not user_lhost:
        print("setting your ip to " + lhost)
        user_lhost = lhost
        return user_lhost
    if re.search(regex, user_lhost):
        user_lhost = user_lhost.split('.')
        user_lhost1 = ""
        while i < 3:
            user_lhost1 = user_lhost1 + user_lhost[i] + '.'
            i = i + 1

        user_lhost1 = user_lhost1+"1/24"
        print("setting you ip range to " + user_lhost1)
        return user_lhost1
    else:
        print("ERROR: Network range must be 0.0.0.0 I WILL AUTOMATICALLY USE IT IN ENTIRE SUBNET")
        print("Run the tool again ")
        print("EXITING...")
        exit()
