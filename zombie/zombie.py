import subprocess
import sys

cmd = sys.argv[1] if len(sys.argv) > 1 else "status"

if cmd == "status":
    print("🧟 ZOMBIE ONLINE")
    print(subprocess.getoutput("uptime -p"))
    print(subprocess.getoutput("free -h | grep Mem"))

elif cmd == "files":
    print(subprocess.getoutput("ls ~"))

elif cmd == "disk":
    print(subprocess.getoutput("df -h /"))

else:
    print("Comando desconhecido.")


