import pyautogui
import time
import random
  
# pyautogui.hotkey("ctrlleft", "pagedown")
i=0
j=0


def func(ran,i):
    while(True):
        print("test",i)
        i=i+1
        if i>ran:
            pyautogui.hotkey("pagedown")
            i=0
            break
            time.sleep(3)
        pyautogui.hotkey("ctrlleft", "pagedown")
        time.sleep(1)

def func2(ran,j):
    while(True):
        print("test",j)
        j=j+1
        if j>random.randint(0,9):
            pyautogui.hotkey("pageup")
            j=0
            break
            time.sleep(3)
        pyautogui.hotkey("ctrlleft", "pageup")
        time.sleep(1)

def main():
    res = int(input('Enter Your Response (0/1): '))
    while(True):
        try:
            if(res>0):
                ran=random.randint(0,9)
                func(ran,i)
                time.sleep(random.randint(0,4))
                func2(ran,j)
            else:
                print('The End')
                break
        except KeyboardInterrupt:
            print('Restart For KeyboardInterrupt')
            res = int(input('Enter Your Response (0/1): '))
            continue
        except:
            print('Restart')
            continue

main()