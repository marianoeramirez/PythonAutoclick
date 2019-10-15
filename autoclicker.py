import time, pyautogui, keyboard

cs = int(input("Cliques por segundo: "))

time.sleep(4)

while True:
    if not keyboard.is_pressed("alt"):
        try:
            pyautogui.click()
            time.sleep(int(1/cs))
        except KeyboardInterrupt:
            print("Encerrando...")
            time.sleep(1)
    else:
        break
        print("Encerrando...")
        time.sleep(1)
        exit()