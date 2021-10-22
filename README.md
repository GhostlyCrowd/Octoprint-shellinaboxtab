**Disclaimer:**
    Shell in a box or any exposure of SSH access publicly via port forwarding or any other means is highly discouraged. This plugin is designed to be used locally on a private network and thus the Default URL reflects this, as it should not resolve it accessed by port forwarding. External access to your Octoprint instance should never be via direct port forward and instead a VPN connection to the local network it resides on for remote access is regarded as the best option.

   **If you choose to use this plugin and allow it to be accessed publicly via port forwarding to your Octoprint instance or any other means it is YOUR responsibility to secure it properly and any undesired access to your system and any reprocussions because of it are solely on you the end user and your decision to use this plugin outside of its intended use.**


# OctoPrint-shellinaboxtab

   Quick and dirty plugin, based on the "Hello World!" Octoprint plugin example, that creates a Tab that points to a local Shell In A Box server for SSH. A settings option to configure the tab URL from the default "https://octoprint.local:4200" is available.

## Setup


Install manually using this URL:

   https://github.com/GhostlyCrowd/Octoprint-shellinaboxtab/releases/download/V0.0.1/Octoprint-shellinaboxtab.zip

   To use this plugin for Shell In A Box SSH, you must have it set up on your local Octoprint instance. Details on how to do a basic setup can be found here for most popular Linux distros. https://tecmint.com/shell-in-a-box-a-web-based-ssh-terminal-to-access-remote-linux-servers/

## Configuration

   You can change the default URL via the Settings under "Shell In A Box Tab"

![image](https://user-images.githubusercontent.com/1682110/138502946-2d10944e-7d65-45dc-8be3-7f87a804027e.png)
