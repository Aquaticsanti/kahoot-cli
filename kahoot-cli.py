from selenium import webdriver
from selenium.webdriver.common.by import By
from termcolor import colored
import time

print(colored("""
██╗░░██╗░█████╗░██╗░░██╗░█████╗░░█████╗░████████╗░░░░░░░█████╗░██╗░░░░░██╗
██║░██╔╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝░░░░░░██╔══██╗██║░░░░░██║
█████═╝░███████║███████║██║░░██║██║░░██║░░░██║░░░█████╗██║░░╚═╝██║░░░░░██║
██╔═██╗░██╔══██║██╔══██║██║░░██║██║░░██║░░░██║░░░╚════╝██║░░██╗██║░░░░░██║
██║░╚██╗██║░░██║██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░░░░░░░╚█████╔╝███████╗██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░░░░░░░░╚════╝░╚══════╝╚═╝""", (100, 53, 173)))

print("Welcome to Kahoot-CLI! Made by @Aquaticsanti\n")

while True:
    try:
        pin = int(input("Input the game pin (no spaces): "))
    except ValueError:
        pin = int(input("That doesn't look like a number... Please input the game pin (no spaces): "))
    else:
        break

driver = webdriver.Chrome()
driver.get("https://www.kahoot.it")
driver.implicitly_wait(0.5)


pin_box = driver.find_element(by=By.NAME, value="gameId")
pin_submit = driver.find_element(By.CSS_SELECTOR, ("button[type='submit']"))

pin_box.send_keys(pin)
pin_submit.click()

time.sleep(3)

while True:
    if driver.current_url == "https://kahoot.it/join":
        break
    else:
        while True:
            try:
                pin = int(input("Uh oh, the pin is invalid. Input the game pin (no spaces): "))
            except ValueError:
                pin = int(input("That doesn't look like a number... Please input the game pin (no spaces): "))
            else:
                break
        pin_box.send_keys(pin)
        pin_submit.click()

name_box = driver.find_element(by=By.NAME, value="nickname")
name_submit = driver.find_element(By.CSS_SELECTOR, ("button[type='submit']"))

nickname = input("What's your name? (Don't use your real name): ")

name_box.send_keys(nickname)
name_submit.click()

time.sleep(3)

if driver.current_url == "https://kahoot.it/instructions":
    print("You're in! See your name on the screen?")
    print(colored("Note: Reactions and avatars are not supported yet.", "dark_grey"))
