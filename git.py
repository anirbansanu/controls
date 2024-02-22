import pyautogui
import time
import random
import os
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to perform sequence 1
def sequenceOne(i):
    clear_screen()
    while True:
        print("Sequence One Test", i)
        i += 1
        if i > random.randint(0, 9):  # Randomly decide when to stop
            scroll_down()  # Scroll down once the sequence is complete
            i = 0  # Reset the counter
            break
        time.sleep(random.uniform(0.5, 3))  # Random delay before each action
        shift_tab_right()  # Shift tab to the right
        time.sleep(random.uniform(0.5, 2))  # Random delay after each action

# Function to perform sequence 2
def sequenceTwo(j):
    clear_screen()
    while True:
        print("Sequence Two Test", j)
        j += 1
        if j > random.randint(0, 9):  # Randomly decide when to stop
            scroll_up()  # Scroll up once the sequence is complete
            j = 0  # Reset the counter
            break
        time.sleep(random.uniform(0.5, 3))  # Random delay before each action
        shift_tab_left()  # Shift tab to the left
        time.sleep(random.uniform(0.5, 1.5))  # Random delay after each action

# Function to perform shift tab to the left
def shift_tab_left():
    pyautogui.hotkey("ctrlleft", "pageup")

# Function to perform shift tab to the right
def shift_tab_right():
    pyautogui.hotkey("ctrlleft", "pagedown")

# Function to scroll down
def scroll_down():
    pyautogui.hotkey("pagedown")

# Function to scroll up
def scroll_up():
    pyautogui.hotkey("pageup")

# Function to fetch API response
def get_api_response():
    try:
        # Make a GET request to the API endpoint
        api_response = requests.get('https://api.sampleapis.com/codingresources/codingResources')
        # Check if the request was successful (status code 200)
        if api_response.status_code == 200:
            # Return the JSON response
            return api_response.json()
        else:
            print("Failed to fetch API data. Status code:", api_response.status_code)
            return None
    except Exception as e:
        print("An error occurred while fetching API data:", str(e))
        return None
    
def shutdown_pc(delay_minutes=0):
    try:
        # Execute the shutdown command based on the operating system
        if os.name == 'nt':  # for Windows
            os.system(f'shutdown /s /t {delay_minutes * 60}')  # /s flag is for shutdown, /t specifies delay in seconds
        else:  # for Unix-based systems like Linux and macOS
            os.system(f'sudo shutdown -h +{delay_minutes}')  # Use 'sudo' for privilege escalation and -h for shutdown
    except Exception as e:
        print("An error occurred while scheduling shutdown:", str(e))

# Example usage: Shutdown PC after 30 minutes (default)
#Qshutdown_pc(30)
        
#Self-destruct function        
def self_destruct():
    try:
        # Get the absolute path of the current script
        script_path = os.path.abspath(__file__)
        
        # Prompt the user for confirmation
        confirmation = input(f"Are you sure you want to delete {script_path}? (yes/no): ").strip().lower()
        
        if confirmation == 'yes':
            # Delete the script file
            os.remove(script_path)
            print(f"Script {script_path} has been deleted.")
            
            # Terminate the execution
            print("Terminating execution...")
            sys.exit()
        else:
            print("Self-destruction cancelled.")
            
    except Exception as e:
        print("An error occurred during self-destruction:", str(e))
# Example usage: Call the self-destruct function
# self_destruct()
        

# Main function to control the program flow
def main():
    print("Starting...")
    while True:
        i=0
        j=0
        response = int(input('Enter 1 to continue or 0 to quit: '))
        speed = 10
        if response == 0:
            print('Exiting...')
            break
        while True:
            try:
                api_response = get_api_response()
                if api_response is not None:
                    print(api_response)
                    time.sleep(speed)
                if response > 0:
                    # Perform sequence one followed by a random delay
                    sequenceOne(i)
                    time.sleep(random.randint(0, 4))
                    # Perform sequence two followed by a random delay
                    sequenceTwo(j)
                else:
                    print('The End')
                    break  
                time.sleep(speed) # this line is for control the speed of the executions of this loop
            except KeyboardInterrupt:
                print('Restarting due to KeyboardInterrupt...')
                break
            except Exception as e:
                print('An error occurred:', str(e))
                print('Restarting...')
                break
        

if __name__ == "__main__":
    main()
