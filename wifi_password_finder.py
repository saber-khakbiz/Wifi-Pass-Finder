import subprocess

def get_wifi_profiles():
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in profiles_data if "All User Profile" in i]
    return profiles

def get_wifi_password(profile):
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    password_line = [b for b in profile_info if "Key Content" in b]
    if password_line:
        password = password_line[0].split(":")[1][1:-1]
    else:
        password = None
    return password

if __name__ == "__main__":
    profiles = get_wifi_profiles()
    if profiles:
        print("List of Wi-Fi profiles:")
        for profile in profiles:
            print(f"- {profile}")
        
        profile_name = input("\nEnter the name of the Wi-Fi profile you want to see the password for: ")
        if profile_name in profiles:
            password = get_wifi_password(profile_name)
            if password:
                print(f"\nThe password for {profile_name} is: {password}")
            else:
                print(f"\nNo password found for {profile_name}")
        else:
            print("\nThe entered profile name does not exist.")
    else:
        print("No Wi-Fi profiles found.")
