# GuardGrid

## Description

GuardGrid is a Python-based program designed to strengthen network defenses on Windows systems. It provides advanced security configurations and monitoring features to bolster the security posture of a network. The program focuses on enabling the Windows Firewall, disabling unnecessary services, and monitoring network activity.

## Features

- **Enable Firewall**: Automatically enables the Windows Firewall on all profiles to protect against unauthorized access.
- **Disable Unnecessary Services**: Identifies and disables non-essential Windows services to minimize potential attack vectors.
- **Network Activity Monitoring**: Utilizes `netstat` to monitor and log network activity, providing a report for further analysis.

## Requirements

- Python 3.x
- Windows Operating System
- Administrative privileges

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/guardgrid.git
```

Navigate to the directory:

```bash
cd guardgrid
```

## Usage

Run the program with administrative privileges to ensure all features function properly:

```bash
python guardgrid.py
```

The program will generate logs for its operations in `guardgrid.log` and network activity in `network_activity.log`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## Acknowledgments

- Inspiration for advanced security configurations and monitoring techniques.
- Thanks to the open-source community for their invaluable resources and tools.