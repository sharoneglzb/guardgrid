import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='guardgrid.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enable_firewall():
    """Enables the Windows Firewall."""
    try:
        subprocess.check_call('netsh advfirewall set allprofiles state on', shell=True)
        logging.info("Windows Firewall enabled.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to enable Windows Firewall: {e}")

def disable_unnecessary_services():
    """Disables unnecessary Windows services to strengthen security."""
    services = ['Spooler', 'WSearch', 'RemoteRegistry']
    for service in services:
        try:
            subprocess.check_call(f'net stop {service} && sc config {service} start= disabled', shell=True)
            logging.info(f"Service {service} stopped and disabled.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to stop and disable service {service}: {e}")

def monitor_network_activity():
    """Monitors network activity using netstat."""
    try:
        result = subprocess.check_output('netstat -ano', shell=True)
        logging.info("Network activity monitored. Report generated.")
        with open('network_activity.log', 'w') as file:
            file.write(result.decode())
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to monitor network activity: {e}")

def main():
    logging.info("GuardGrid Security Program Started.")
    enable_firewall()
    disable_unnecessary_services()
    monitor_network_activity()
    logging.info("GuardGrid Security Program Finished.")

if __name__ == "__main__":
    main()