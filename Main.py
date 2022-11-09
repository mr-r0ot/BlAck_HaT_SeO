try:
    import socket, requests
except:
    import os
    os.system("pip install requests")
    import socket, requests 

def black_seo():
    try:
        socket.gethostbyname("google.com")
        print('''

'########:::::'##:::::::::::::'###::::::::'######:::::'##:::'##:::::::
 ##.... ##:::: ##::::::::::::'## ##::::::'##... ##:::: ##::'##::::::::
 ##:::: ##:::: ##:::::::::::'##:. ##::::: ##:::..::::: ##:'##:::::::::
 ########::::: ##::::::::::'##:::. ##:::: ##:::::::::: #####::::::::::
 ##.... ##:::: ##:::::::::: #########:::: ##:::::::::: ##. ##:::::::::
 ##:::: ##:::: ##:::::::::: ##.... ##:::: ##::: ##:::: ##:. ##::::::::
 ########::::: ########:::: ##:::: ##::::. ######::::: ##::. ##:::::::
........::::::........:::::..:::::..::::::......::::::..::::..::::::::
:'######:::::'########:::::'#######:::::'########::::'########::
'##... ##:::: ##.....:::::'##.... ##:::: ##.....::::: ##.... ##:
 ##:::..::::: ##:::::::::: ##:::: ##:::: ##:::::::::: ##:::: ##:
. ######::::: ######:::::: ##:::: ##:::: ######:::::: ########::
:..... ##:::: ##...::::::: ##:::: ##:::: ##...::::::: ##.. ##:::
'##::: ##:::: ##:::::::::: ##:::: ##:::: ##:::::::::: ##::. ##::
. ######::::: ########::::. #######::::: ########:::: ##:::. ##:
:......::::::........::::::.......::::::........:::::..:::::..::

''')
        url = input("\n [ Enter Url ] $_ ")
        url_http = "http://" + url
        url_https = "https://" + url
        ipl = input("\n\n[ Enter Path IpList For Seo ] $_ ")
        print("\n                 B L A C K    S E O E R        \n\n\n")
        print(" Url Target Is: "+str(url)+"\n\n\n\n")
        ip_list = open(ipl, "r")
        for ip in ip_list:
            proxy = {"socks5": ip}
            try:
                request = requests.get(url_http, proxies=proxy)
                print("\n  New View http Ok:)   Of Your Url   with: " + str(ip))
            except:
                print("\n\n   New View https NotOk:(   Of Your Url")
            try:
                request = requests.get(url_https, proxies=proxy)
                print("\n  New View https Ok:)   Of Your Url   with: " + str(ip))
            except:
                print("\n\n   New View https NotOk:(   Of Your Url")
        ip_list.close()


    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        input("\n\n\n\n\t  Enter for close ")
# ========================================================================================

black_seo()
