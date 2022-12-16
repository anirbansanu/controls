import pyautogui
import time
import random
import requests

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

def fetch(key):
    response = requests.get("http://pytalk.c1.biz/api/js/read_all.php?key="+key)

    print(response.status_code)

    if response.status_code == 200:
        print(response.text)
    else:
        return None
    return response

def validate_fetch():
    res = fetch("redmi123")
    try:
        status = int(res.text.replace('"',''))
    except ValueError:
        print("value error")
        return res,None
    except:
        print("error occur")
        return res,None
    return res,status

def main():
    while True:
        try:
            res,status = validate_fetch()
            while(True):
                try:
                    if(status>1):
                        ran=random.randint(0,9)
                        func(ran,i)
                        time.sleep(random.randint(0,4))
                        func2(ran,j)
                    else:
                        print('The End')
                        break
                except:
                    print('Restart')
                    break
        except KeyboardInterrupt:
            break
        except:
            print('Restart')
            continue


main()