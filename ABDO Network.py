import subprocess
from colorama import Fore, Style, init
import pyfiglet
import time
def print_header():
    # طباعة اسم الأداة بشكل كبير
    ascii_art = pyfiglet.figlet_format("ABDO Network Tool", font="slant")
    print(Fore.RED + Style.BRIGHT + ascii_art)
    print(Fore.RED + "=" * 50)
    print(Fore.GREEN + "💀👻👺👽 Welcome to the ABDO Tool! 👻💀👽\n")
    
def get_wifi_password(ssid):
    # تنفيذ الأمر للحصول على معلومات الشبكة
    command = f"netsh wlan show profiles {ssid} key=clear"
    
    try:
        # تنفيذ الأمر باستخدام subprocess
        output = subprocess.check_output(command, shell=True, text=True)
        
        # البحث عن كلمة المرور في المخرجات
        for line in output.splitlines():
            if "Key Content" in line:
                password = line.split(":")[1].strip()  # استخراج كلمة المرور
                return password
    except subprocess.CalledProcessError:
        print("Unable to find the specified SSID or other error.")
    return None

def main():
    print_header()
    ssid = input("Enter the Wi-Fi network name (SSID): ")
    password = get_wifi_password(ssid)
    
    if password:
        print(f"The password for '{ssid}' is: {password}")
    else:
        print(f"No password found for '{ssid}' or the SSID does not exist.")

if __name__ == "__main__":
    main()
    time.sleep(10000000)  # The Time To Stop Tool

