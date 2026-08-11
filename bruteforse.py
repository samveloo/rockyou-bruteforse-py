import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_FILE = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "rockyou.txt"))

if not os.path.exists(DICTIONARY_FILE):
    print(f"[ERROR] Dictionary file not found at: {DICTIONARY_FILE}")
    print("[INFO] Please place 'rockyou.txt' in the correct folder or update DICTIONARY_FILE path in the code.")
    exit(1)

target_password = input("Enter a password for brute-force simulation: ")

print("\nLoading dictionary and starting the attack...\n")
start_time = time.time()

found = False
count = 0

with open(DICTIONARY_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        count += 1
        guess = line.strip()
        
        if count % 50000 == 0:
            print(f"\rPasswords checked: {count}... Current: {guess}", end="", flush=True)
            
        if guess == target_password:
            end_time = time.time()
            print("\n" + "="*40)
            print(f"Password cracked: {guess}")
            print(f"Dictionary position: #{count}")
            print(f"Time elapsed: {round(end_time - start_time, 2)} seconds")
            print("="*40)
            found = True
            break

if not found:
    end_time = time.time()
    print(f"\nPassword not found in the dictionary. Total lines checked: {count}")
    print(f"Search time: {round(end_time - start_time, 2)} seconds")