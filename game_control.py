import pyautogui
from subprocess import run
PackageFamilyName = "FINGERSOFT.HILLCLIMBRACING_r6rtpscs7gwyg"
Id="App"
print(run('explorer.exe shell:appsFolder\\'+ PackageFamilyName +'!'+Id))
# pyautogui.sleep(10)

print(pyautogui.size())
im1 = pyautogui.screenshot()
im1.save("screenshot.png")
loc = pyautogui.locateAllOnScreen('paddle.png', confidence = 0.8, grayscale=True)
print(loc)
def game_started():
    while True:
        if (pyautogui.locateOnScreen('paddle.png', confidence = 0.9, grayscale=True) != None):
            print("boom")
            pyautogui.keyDown('right')
            break
        # pyautogui.sleep(5)

    # pyautogui.sleep(10)
    # pyautogui.keyUp('right')
    # pyautogui.keyDown('left')
    # pyautogui.sleep(5)
    # pyautogui.keyUp('left')
    # pyautogui.keyDown('right')
    # pyautogui.sleep(5)
    # pyautogui.keyUp('right')

    while True:
        if (pyautogui.locateOnScreen('game_end.png', confidence = 0.8, grayscale=True) != None):
            print("boom")
            pyautogui.keyUp('right')
            pyautogui.press('enter')
            break
        pyautogui.sleep(8)
    

while True:
    if pyautogui.locateOnScreen('paddle.png',confidence=0.9, grayscale=True) != None :
        game_started()
        
    pyautogui.sleep(0.5)
