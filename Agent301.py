import os
import time
import requests
from colorama import Fore, Style, init

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m-------------[Agent301Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def load_authorizations(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(authorization):
    return {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": authorization,
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"111\", \"Not(A:Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }

def login(authorization):
    url = "https://api.agent301.org/getMe"
    headers = get_headers(authorization)
    body = {"referrer_id": 5496274031}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        try:
            data = response.json()
            result = data.get("result", {})
            balance = result.get("balance")
            ticket = result.get("tickets")
            enrollments = result.get("enrollments", {})
            qr_p = enrollments.get("qr_points")
            qr_u = enrollments.get("qr_users")

            print(f"{Fore.GREEN + Style.BRIGHT}Balance: {Fore.WHITE + Style.BRIGHT}{balance} | {Fore.YELLOW + Style.BRIGHT}Tickets: {Fore.WHITE + Style.BRIGHT}{ticket}")
            print(f"{Fore.CYAN + Style.BRIGHT}QR User: {Fore.WHITE + Style.BRIGHT}{qr_u} | {Fore.GREEN + Style.BRIGHT}QR Points: {Fore.WHITE + Style.BRIGHT}{qr_p}")
            
            return ticket

        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response.")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request failed: {e}")

def friends(authorization):
    url = "https://api.agent301.org/getFriends"
    headers = get_headers(authorization)
    body = {"offset": 0}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        try:
            data = response.json()
            friends = data.get("result").get("total")
            print(f"{Fore.BLUE + Style.BRIGHT}Total Friend's: {Fore.WHITE + Style.BRIGHT}{friends}")
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response.")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Server Problem Not Script")

def load(authorization):
    url = "https://api.agent301.org/wheel/load"
    headers = get_headers(authorization)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        try:
            data = response.json()
            ton_c = data.get("result").get("toncoin")
            not_c = data.get("result").get("notcoin")
            print(f"{Fore.GREEN + Style.BRIGHT}TonCoin: {Fore.WHITE + Style.BRIGHT}{ton_c} | {Fore.CYAN + Style.BRIGHT}NotCoin: {Fore.WHITE + Style.BRIGHT}{not_c}")
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response.")
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Server Problem Not Script")

def spin(authorization):
    url = "https://api.agent301.org/wheel/spin"
    headers = get_headers(authorization)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        
        try:
            data = response.json()
            result = data.get("result", {})
            updated_tickets = result.get("tickets")
            reward = result.get("reward")
            new_balance = result.get("balance")

            if updated_tickets is not None:
                print(f"{Fore.YELLOW + Style.BRIGHT}Ticket's: {Fore.WHITE + Style.BRIGHT}{updated_tickets}")
            else:
                print(f"{Fore.RED + Style.BRIGHT}No updated ticket count in response.")
            
            if reward is not None:
                print(f"{Fore.GREEN + Style.BRIGHT}Reward: {Fore.WHITE + Style.BRIGHT}{reward}")
                print(f"{Fore.MAGENTA + Style.BRIGHT}New Balance: {Fore.WHITE + Style.BRIGHT}{new_balance}")
            else:
                print(f"{Fore.RED + Style.BRIGHT}No reward in response.")
            
            return updated_tickets
        
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response.")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Server Problem Not Script")
        return None

def task_complete(authorization):
    url_list = "https://api.agent301.org/getTasks"
    url_complete = "https://api.agent301.org/completeTask"
    headers = get_headers(authorization)
    
    try:
        response_list = requests.post(url_list, headers=headers, json={}, allow_redirects=True)
        response_list.raise_for_status()
        
        try:
            data_list = response_list.json()
            task_types = [task['type'] for task in data_list.get('result', {}).get('data', [])]
            task_titles = [task['title'] for task in data_list.get('result', {}).get('data', [])]
        except ValueError:
            print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response from task list.")
            return

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED + Style.BRIGHT}Request to get tasks failed: {e}")
        return
        
    for task_type, task_title in zip(task_types, task_titles):
        body_complete = {"type": task_type}
        try:
            response_complete = requests.post(url_complete, headers=headers, json=body_complete, allow_redirects=True)
            response_complete.raise_for_status()

            try:
                data_complete = response_complete.json()
                is_completed = data_complete.get("result", {}).get("is_completed")
                if is_completed:
                    print(f"{Fore.GREEN + Style.BRIGHT}Task Complete Successfully: {Fore.WHITE + Style.BRIGHT}'{task_title}'")
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Task Complete Manually: {Fore.WHITE + Style.BRIGHT}'{task_title}'")
            except ValueError:
                print(f"{Fore.RED + Style.BRIGHT}Failed to decode JSON response for task {Fore.WHITE + Style.BRIGHT}'{task_title}'.")
        
        except requests.exceptions.RequestException as e:
            print(f"{Fore.YELLOW + Style.BRIGHT}Task Already Completed: {Fore.WHITE + Style.BRIGHT}'{task_title}'")

def main():
    clear_terminal()
    art()
    
    authorizations = load_authorizations('data.txt')
    for i, authorization in enumerate(authorizations, start=1):
        print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{i}------{Style.RESET_ALL}")
        initial_tickets = login(authorization)
        load(authorization)
        friends(authorization)

        if initial_tickets is not None and initial_tickets > 0:
            current_tickets = initial_tickets
            print(f"{Fore.YELLOW + Style.BRIGHT}Ticket's: {Fore.WHITE + Style.BRIGHT}{current_tickets}{Style.RESET_ALL}")
            while current_tickets > 0:
                current_tickets = spin(authorization)
             
                if current_tickets is None:
                    print(f"{Fore.RED + Style.BRIGHT}Exiting due to error or invalid response.{Style.RESET_ALL}")
                    break  

                print(f"{Fore.MAGENTA + Style.BRIGHT}Spinning....{Style.RESET_ALL}")
                time.sleep(6) 

        task_complete(authorization)
        
    countdown_timer(1*15*60) # 15 Minutes Countdown

if __name__ == "__main__":
    while True:
        main()
