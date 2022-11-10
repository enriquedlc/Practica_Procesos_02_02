import os
import platform


def pingCommand(host):
    if platform.system() == "Windows":
        output = os.popen("ping -n 2 " + host).read()
    else:
        output = os.popen("ping -c 2 " + host).read()
    return output


if __name__ == "__main__":
    host = input("Enter the host to ping: ")
    print(pingCommand(host))
