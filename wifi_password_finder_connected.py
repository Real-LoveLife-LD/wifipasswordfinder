# This only finds the wifi passwords of the wifi connections you have connected before.
# If the wifi password or SSID has been updated, you will need to re-connect then run this file to get the updated SSID and password.
# You cannot find the SSID or the passwords of wifi connections you haven't connected to before.
# This ofcourse isn't considered "hacking" because it only shows the passwords of the wifi connections have connected to before and you have to reconnect to the wifi if the SSID or password is updated.
# This is just a small little project to impress your **crush**/friends/relatives. 
# There is a much more simpler way by using command prompt. Just do some research and you'll find it!
# Remove all these comments (every line that starts with a #) so that it's more effective in impressing your crush.
# DO NOT EDIT ANYTHING BELOW THIS COMMENT IF YOU DON'T KNOW WHAT YOU ARE DOING. ⚠⚠⚠
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")
