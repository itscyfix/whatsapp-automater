import pywhatkit
import time


print("welcome to whatsapp automater by cyfix(kanav) \n before you hop on consider some of these steps \n 1. for eg if the group link is this https://chat.whatsapp.com/XYZ then the grp id will be XYZ \n 2. if you want to send it to a phone mentioning the country code is a must unless the app would give errors \n 3. make sure whatsapp web is logged in your browser \n here you go! ")
time.sleep(3)



p_g = input("msg to phno or a grp (p/g): ")
phno_g = input("enter the phno/group id : ")
msg = input("enter the message that is to be conveyed : ")
hr = int(input("enter the hour (acc to 24 hour clock) : "))
min = int(input("enter the min (acc to 24 hour clock) : "))
preopen = int(input("how many seconds before shall we open the browser : "))
close_browser = input("shall we close the browser after the work is done (y/n): ")
closing_time = int(input("how much time before we close the browsser (in secs) : "))


#as the arg must be in boolean
if close_browser == "y" or close_browser =="Y":
    close_browser = True
else:
    close_browser =  False
    print("ok wont /n ")



if p_g == 'p' or p_g =="P":
    pywhatkit.sendwhatmsg(phno_g , msg , hr , min , preopen , close_browser ,closing_time )
else:
    pywhatkit.sendwhatmsg_to_group(phno_g , msg , hr , min , preopen , close_browser ,closing_time)

print("sent")
time.sleep(10)

