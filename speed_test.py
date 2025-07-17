from speedtest import Speedtest
from speedtest import ConfigRetrievalError
import time
import sys
import pyfiglet
from tqdm import tqdm

NAME = "Speed  test"


def speed_test():
    try:
        name = pyfiglet.figlet_format(NAME)
        print(f"{name}\n\n")
        time.sleep(3)

        with tqdm(total=100, desc="Starting speed test", unit="%",colour="green") as pbar:
            time.sleep(1)
            pbar.update(10)

            inet = Speedtest()

            pbar.update(20)
            time.sleep(1)
            pbar.set_description("Testing download speed")
            download_speed = inet.download()
            download = float(str(download_speed)[0:2] + "." + str(round(download_speed, 2))[1]) * 0.125
            pbar.update(30)

            pbar.set_description("Testing upload speed")
            time.sleep(1)
            upload_speed = inet.upload()
            upload = float(str(upload_speed)[0:2] + "." + str(round(upload_speed, 2))[1]) * 0.125
            pbar.update(30)
            time.sleep(1)
            pbar.update(10)
            pbar.close()

            print(f"\nIncoming speed: {download:.2f} Mbps")
            print(f"Outgoing speed: {upload:.2f} Mbps\n")


            choice = input("\nDo you want to scan again? (y/n) >>>>").lower()

            if choice == "n":
                sys.exit(0)

            elif choice == "y":
                print("\n\n")
                return speed_test()

            else:
                print("This option is not available!")
                sys.exit(1)

    except ConfigRetrievalError:
        print("\nYou are not connected to the Internet!")
        return False

    except Exception as e:
        print(f"\nError: {e}")
        return False


if __name__ == "__main__":
    try:
        speed_test()

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
