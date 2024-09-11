# The Kali Intellisense Project (KIP) ⚡
Current Build v0.2

![Untitled video (1)](https://github.com/user-attachments/assets/2386400c-1cc7-4c97-addb-804b3e282f5e)

## Overview

The **Kali Intellisense Project** is designed to enhance the user experience for penetration testers using Kali Linux by providing in-terminal IntelliSense-like functionality. This project builds on top of the popular [zsh-autocomplete](https://github.com/marlonrichert/zsh-autocomplete) package, extending its capabilities to offer additional compatibility and features tailored specifically for Kali Linux users.

### Why Kali Intellisense?

As a penetration tester, it’s challenging to keep up with the constant flow of new tools being developed. On top of that, each tool comes billions and billions and billions... of flags and options, making it even harder to manage everything. The **Kali Intellisense Project** aims to solve this by providing a streamlined autocomplete experience directly within the terminal. It helps users by auto-suggesting tools and flags as they type, significantly reducing the time spent looking up documentation.

## Features

- **Extended Zsh Compatibility**: Builds upon zsh-autocomplete, offering additional support for Kali-specific tools and commands.

![image](https://github.com/user-attachments/assets/04b5007b-cd9b-405a-b562-289d8d0b7764)

- **Realtime Autocomplete for Penetration Testing Tools**: Includes autocomplete for a wide range of commonly used penetration testing tools along with their flags, options and examples.

![image](https://github.com/user-attachments/assets/9bd111d4-a847-44c5-8538-9e38ce71cf50)

- **Easy Setup**: A simple, automated setup script ensures users can quickly integrate this functionality into their existing environments.


## How to Install

To install the **Kali Intellisense Project**, follow these steps:

1. Download the setup script directly from the [release page](https://github.com/Gman3214/Kali-Intellisense-Project/releases/download/Release/setup.sh).
2. Run the setup script to configure your environment.

### Install with Curl

Run the following command in your terminal:

```bash
curl -L https://raw.githubusercontent.com/Gman3214/Kali-Intellisense-Project/main/setup.sh | bash
```

This will automatically download and run the setup script, ensuring all dependencies are installed and the environment is configured for optimal use.

### Currently Supported Tools 🦾

List is being updated on a daily basis!!

| Tool         | InteliSense For All Flags                           | Example Commands |
|--------------|---------------------------------------------|---------------------|
| aircrack-ng   | ✅ | ❌ |
| crackmapexec   | ✅ | ❌ |
| evil-winrm   | ✅ | ❌ |
| ffuf         | ✅ | ✅ |
| gobuster     | ✅ | ❌ |
| httpx        | ✅                         | ❌                 |
| hydra        | ✅ | ❌             |
| john         | ✅       | ❌                 |
| kerbrute     | ✅ | ❌               |
| naabu        | ✅                   | ❌                 |
| nc           | ✅                             | ❌                 |
| nmap         | ✅                  | ❌                 |
| nuclei       | ✅              | ❌                 |
| remove-host  | ✅                   | ❌                 |
| responder    | ✅                         | ❌                 |
| sqlmap       | ✅        | ❌                 |
| wpscan       | ✅           | ❌                 |



### Synthetic sugar for penetration testers 🍭
| Command      | Example                              | Description                                                             |
|--------------|--------------------------------------|-------------------------------------------------------------------------|
| add-host     | `add-host example.com 192.168.1.1` | Adds a hostname and IP to the `/etc/hosts` file. If the IP already exists, it appends the hostname to the same line. If the IP doesn't exist, it creates a new entry. |
| remove-host  | `remove-host example.com` or `sudo remove-host 192.168.1.1` | Removes a hostname or IP from the `/etc/hosts` file. If an IP is provided, it deletes the entire line. If a hostname is provided, only the hostname is removed from the line. |


### Dont See the tools you use ?
Contact me ;)


### Disclaimer

This content, including scripts and examples, is provided solely for educational purposes and to aid in legal penetration testing, vulnerability assessment, and security research. The material is intended for use by professionals in controlled environments or those authorized to conduct such activities.

I (the creator) am not responsible for any illegal or unethical use of the content provided here. Unauthorized access to systems, networks, or data without explicit permission from the owner is a violation of law. By using any of the information or tools provided here, you agree that it will only be used in compliance with applicable laws and regulations.

It is your responsibility to ensure that your actions are ethical and lawful. The creator disclaims any liability for how the information is used or for any consequences that arise from its application.
