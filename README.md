# Kali Intellisense Project

## Overview

The **Kali Intellisense Project** is designed to enhance the user experience for penetration testers using Kali Linux by providing in-terminal IntelliSense-like functionality. This project builds on top of the popular [zsh-autocomplete](https://github.com/marlonrichert/zsh-autocomplete) package, extending its capabilities to offer additional compatibility and features tailored specifically for Kali Linux users.

### Why Kali Intellisense?

As a penetration tester, it’s challenging to keep up with the constant flow of new tools being developed. On top of that, each tool comes with its own extensive list of flags and options, making it even harder to manage everything. The **Kali Intellisense Project** aims to solve this by providing a streamlined autocomplete experience directly within the terminal. It helps users by auto-suggesting tools and flags as they type, significantly reducing the time spent looking up documentation.

## Features

- **Extended Zsh Compatibility**: Builds upon zsh-autocomplete, offering additional support for Kali-specific tools and commands.
- **Autocomplete for Penetration Testing Tools**: Includes autocomplete for a wide range of commonly used penetration testing tools along with their flags and options.
- **Easy Setup**: A simple, automated setup script ensures users can quickly integrate this functionality into their existing environments.

## How to Install

To install the **Kali Intellisense Project**, follow these steps:

1. Download the setup script directly from the [release page](https://github.com/Gman3214/Kali-Intellisense-Project/releases/download/Release/setup.sh).
2. Run the setup script to configure your environment.

### Install with Curl

Run the following command in your terminal:

```bash
curl -L https://github.com/Gman3214/Kali-Intellisense-Project/releases/download/Release/setup.sh | bash
```

This will automatically download and run the setup script, ensuring all dependencies are installed and the environment is configured for optimal use.

Once installed, restart your terminal or source your Zsh configuration file to start using the Kali Intellisense features!
