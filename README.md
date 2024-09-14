# Keylogger - Documentation

## What is a Keylogger?
A keylogger is a program designed to record every keystroke made on a keyboard. This type of software is often used for monitoring, diagnostic purposes, or security testing. However, it is important to note that the use of a keylogger must always comply with laws and respect users' privacy. Using a keylogger for malicious purposes or without explicit consent is illegal and unethical.

## Prerequisites
Make sure to install the following Python libraries before using this program:

- `DateTime`: 5.5
- `psutil`: 6.0.0
- `pynput`: 1.7.7

You can install these dependencies using `pip`:
```bash
pip install DateTime==5.5 psutil==6.0.0 pynput==1.7.7
```

## Usage

### 1. Start the Program
To start the keylogger, run the following batch file:
```bash
keyloggerOn.bat
```
The program will record all keystrokes in text files located in the `keyloggerLog/` folder.

### 2. Stop the Program
To stop the keylogger, run the following batch file:
```bash
keyloggerOff.bat
```
This script will terminate the currently running keylogger process, ensuring a clean and secure shutdown.

### 3. Clear the Logs
If you want to delete the log files, run the following batch file:
```bash
cleanKeyloggerLog.bat
```
This will remove all the files stored in the `keyloggerLog/` folder.

## Notes
- **Logging Location**: All recorded keystrokes are saved in text files within the `keyloggerLog/` directory.
- **Shutdown Process**: It is recommended to use `keyloggerOff.bat` to stop the program correctly, ensuring that all associated processes are terminated.
