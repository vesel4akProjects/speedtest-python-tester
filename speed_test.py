from speedtest import Speedtest
import time
import sys

def speed_test():
    try:
        inet = Speedtest()
        timer = time.time()
        download = float(str(inet.download())[0:2] + "." + str(round(inet.download(),2))[1]) * 0.125
        upload = float(str(inet.upload())[0:2] + "." + str(round(inet.upload(),2))[1]) * 0.125
        print(f"Incoming speed of {download} megabits")
        print(f"Outgoing speed is {upload} megabits\n\n")
        scantime = time.time() - timer
        print(f"Internet connection speed scan completed successfully in {scantime} seconds")
        return True

    except Exception as e:
        print(f"error : {e}")
        return False

if __name__ == "__main__":
    speed_test()

    choice = input("Do you want to scan again? (y/n) >>>>").lower()

    if choice == "y":
        speed_test()

    elif choice == "n":
        sys.exit(0)

    else:
        print("This option is not available!")