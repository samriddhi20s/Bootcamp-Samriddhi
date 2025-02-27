# Tools Setup Notes

## Understanding the Problem
The task is to set up a cloud-based Linux server and configure a web server that serves a page displaying my name. Additionally, a DNS name should resolve to the cloud server. The environment setup also involves installing necessary tools like Pyenv, Pyenv Virtualenv, and VSCode.

## Approach

### Server Setup
1. Created a VM instance for a Linux server.
2. Used SSH to open the console.
3. Created an HTML file to be served.
4. Allowed port 8000 in firewall settings.
5. Ran the web server using:
   ```sh
   python3 -m http.server 8000 --bind 0.0.0.0
   ```
6. Tested the setup by visiting:
   ```
   http://your-server-external-ip:8000
   ```
7. Created a subdomain resolving to the Linux server using services like DuckDNS or FreeDNS.
8. Verified domain resolution with:
   ```sh
   ping yourdomain.com
   ```
   or
   ```sh
   nslookup yourdomain
   ```
9. Tested the setup by visiting:
   ```
   http://yourdomainname:8000
   ```

### Client Setup
- Installed **Pyenv** and **Pyenv Virtualenv**.
- Configured VSCode and performed necessary drills.

## Problems Faced

### WSL Issue
After installing WSL, I encountered the error:

> Windows Subsystem for Linux has no installed distributions.

**Solution:**
- Ran:
  ```sh
  wsl.exe --list --online
  ```
  to list available distributions.
- Installed Ubuntu with:
  ```sh
  wsl.exe --install Ubuntu
  ```

### Web Server Issue
The web server URL was not accessible initially. Resolved by allowing HTTP traffic in the VM instance firewall settings.

## LLMs Used
For assistance in setting up the environment, I consulted the following LLMs:
- ChatGPT - Provided guidance on setting up Linux servers and troubleshooting.
- [ChatGPT Share Link 1](https://chatgpt.com/share/67baf31a-2e7c-8004-b732-88e297b863ac)
- [ChatGPT Share Link 2](https://chatgpt.com/share/67baf2b0-4954-8004-b99c-3ab363ade379)
