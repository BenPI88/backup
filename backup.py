import platform
temp = open("version.ini")
version = temp.read()
temp.close()
print(f"BenPI88 File Backup Tool {version}")
if str(platform.system()) == "Windows":
  os = "Windows"
elif str(platform.system()) == "Darwin":
  os = "MacOS"
else:
  os = "Linux"
print(f"Detected OS: {os}\n")

#shitty code to check if the option is invalid or not
option = "0"
while not str(option) == "1" or str(option) == "2" or str(option) == "3":
print("Please select an option.\n1) Backup\n2) Restore\n3) Exit")
option = input()
