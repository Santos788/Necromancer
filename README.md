# Necromancer

Control a Linux computer remotely from an Android device running **Termux**, using **Python** and **SSH**.

![Python](https://img.shields.io/badge/Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![SSH](https://img.shields.io/badge/SSH-secure-informational?style=flat-square)
![Termux](https://img.shields.io/badge/Termux-000000?style=flat-square&logo=termux&logoColor=white)
![Version](https://img.shields.io/badge/version-v0.6_MVP-orange?style=flat-square)

---

## Overview

Necromancer lets a phone run actions on a computer over the network, such as checking system status, listing files and checking disk usage.

The architecture is simple and split into two sides:

| Component | Role | Runs on |
|---|---|---|
| `master/` | Sends the commands | Phone (Android + Termux) |
| `zombie/` | Runs the actions and returns the response | Target computer (Linux) |

```text
 ┌──────────────────────┐          SSH          ┌──────────────────────┐
 │  Android / Termux    │ ────────────────────► │    Linux (target)    │
 │     master.py        │ ◄──────────────────── │      zombie.py       │
 └──────────────────────┘       response        └──────────────────────┘
```

## Features

- View the remote computer's system status
- List files in the user's home directory
- Check disk usage
- Run remote commands simply over SSH

## How it works

1. `master/master.py` runs on the phone.
2. It connects to the remote computer over SSH.
3. The command is sent to `zombie/zombie.py`.
4. The computer performs the operation and returns the response.

## Project structure

```text
necromancer/
├── master/
│   └── master.py
├── zombie/
│   └── zombie.py
└── README.md
```

## Requirements

- **Phone:** Android with Termux and Python 3
- **Target computer:** Linux (tested on Linux Mint) with Python 3 and the SSH server enabled
- SSH access configured between the phone and the computer, on the same network

## Configuration

In `master/master.py`, set the following variables:

```python
IP = "YOUR_IP"
USER = "USERNAME"
```

| Variable | What to set |
|---|---|
| `IP` | IP address of the Linux computer on the network |
| `USER` | Username on the remote machine |

## Usage

### On Termux (phone)

```bash
python3 ~/projeto/necromancer/master/master.py
```

### On the target computer

`zombie.py` can also be called directly:

```bash
python3 ~/projeto/necromancer/zombie/zombie.py status
python3 ~/projeto/necromancer/zombie/zombie.py files
python3 ~/projeto/necromancer/zombie/zombie.py disk
```

| Command | Action |
|---|---|
| `status` | Shows the system status |
| `files` | Lists files in the home directory |
| `disk` | Shows disk usage |

## Security

This project is an MVP. Before any use beyond testing on a local network, consider:

- Using **SSH key authentication** instead of passwords
- Keeping a **fixed allowlist of permitted commands**, never running arbitrary input
- Validating and sanitizing any input received by `zombie.py`
- Using it only on machines **you own or are authorized to administer**

## Roadmap

- [ ] SSH key authentication
- [ ] Command allowlist on the `zombie` side
- [ ] New commands (memory, processes, network)
- [ ] Logging of executed actions

## Version

**v0.6 (MVP):** first working version of the project.

## Author

**Clayton Santos** · Backend Developer | Python | FastAPI | AppSec

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:claytondev43@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/claytonsantos-backend)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Santos788)
