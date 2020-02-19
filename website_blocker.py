import time
from datetime import datetime as dt

# hosts_path = "hosts.txt"
hosts_path = r"/private/etc/hosts.txt"
redirect = "127.0.0.1"
website_list = ["www.netflix.com", "www.youtube.com"]

while True:
    if (8 < dt.now().hour < 19):
        print ("working hours")
        with open(hosts_path, 'w+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'w+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

