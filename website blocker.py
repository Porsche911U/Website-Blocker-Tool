#!/usr/bin/env python
# coding: utf-8

# In[ ]:


site_block=["www.wscubetech.com","www.facebook.com"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect_no="127.0.0.1"

with open(host_path,"r+") as file:
    content=file.read()
    for i in site_block:
        file.write(redirect_no+" "+i+"\n")
        print("blocking start")


# In[ ]:


site_block = ["www.wscubetech.com", "www.facebook.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_no = "127.0.0.1"

with open(host_path, "r+") as file:
    content = file.read()
    for i in site_block:
        if i not in content:
            file.write(redirect_no + " " + i + "\n")
            print("Blocking", i)
    print("Blocking complete")


# In[ ]:


import os

site_block = ["www.wscubetech.com", "www.facebook.com"]
host_path = "C:/Users/bhush/Music/hosts"
redirect_no = "127.0.0.1"

try:
    with open(host_path, "r+") as file:
        content = file.read()
        for i in site_block:
            if i not in content:
                file.write(redirect_no + " " + i + "\n")
                print("Blocking", i)
        print("Blocking complete")

except PermissionError:
    print("PermissionError: Please run the script with administrator privileges.")
    # Uncomment the following line if you want to automatically request administrator privileges.
    # os.system('runas /user:Administrator "python script_name.py"')


# In[ ]:




