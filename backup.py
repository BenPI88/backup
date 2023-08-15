import platform, os
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
  print("\n")
if str(option) == "3":
  exit
if str(option) == "1":
  option = "0"
  backupoption = option
  option = input("Where do you want the backup to go?\n")
  print("\n\nBacking up... (This may take a while)\nStep 1: Copying files...")
  if os == "Linux" or os == "MacOS":
    os.system(f"cp /* {option}")
  if os == "Windows":
    os.system(f"copy C:/* {option}")
  print("Step 2: Compressing...")
  if os == "Windows":
    os.system("tar.exe -a -c -f out.zip {option}")
  if os == "MacOS":
    os.system("")
  
