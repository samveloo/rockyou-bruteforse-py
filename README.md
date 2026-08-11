# RockYou Brute-Force Simulator

A simple Python script that demonstrates the speed of dictionary-based brute-force attacks using the famous `rockyou.txt` wordlist. This project is published strictly for educational and informational purposes.

## How to Run Locally

1. Clone this repository or download the script.
2. Download the `rockyou.txt` dictionary.
3. Place the `rockyou.txt` file 2 levels above the script (according to the default path) or manually change the path inside `bruteforse.py`:
   ```python
   DICTIONARY_FILE = "path_to_your_file/rockyou.txt"
   ```
4. Run the script via terminal:
   ```bash
   python bruteforse.py
   ```
5. Enter a test password (e.g., `password` or `monkey`) to see how fast the script finds it.

## Disclaimer
This tool is created for educational purposes only. Do not use it for unauthorized benchmarking or malicious activity. The code is compiled from open-source examples.