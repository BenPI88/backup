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
print(f"Detected OS: {os} ({platform.version()})")
