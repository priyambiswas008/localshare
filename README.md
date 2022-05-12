# Localshare

A tiny CLI app to share files between your devices under the same local network. 

![Project Banner](banner.png)

## Description

Python flask is used in the backend of the app, and tailwind css for the frontend. And a little bit of Javascript to add functionalities like ***theming*** & ***previewing local file information***. No installation is needed to use the app. Find the download links from [release](#) section for your respective operating system and the app should work out of the box.

This app is made for two things, Upload and Download. It lists all the files shared by the host(basically *your pc*) and any guest device(*your phone* or *other pc*) can download those files. Alternatively any guest device can upload files to that server and immediately that file will be available to download by all other devices. 


## Installation

You will find pre-built binary from the [release](#) section for ***Windows*** and ***Linux***. Source code will be also their in case you are interested. 

```
No additional installation is required.
Download & Run 
```

## Usage

After downloading the zip file,unzip it navigate inside the *localshare* directory. 

You will find ***localshare***(linux) or ***localshare.exe***(windows).

Execute that file and a command prompt should appear. Copy the server link from there and paste it in any browser and you will be greeted by the GUI. You can access this server from any device as long as you are connected to the same wifi.

![](screenshots/Screenshot%20from%202022-05-04%2000-57-17.png)

Put all the files you want to share in the ***files*** directory. Uploaded files are also copied to that directory.


## Back Story

This project was made to solve a day to day life problem.😆😆😆

When i built this tool, it was not actually for sharing files but it was to copy my files to virtual machine !!😅😅😅 

My primary operating system is a laptop running Latest Ubuntu release but sometime i need windows to run my **Photoshop** and **Microsoft Office**. So i setup a KVM Virt Manager and installed Windows 10 in it. Everything was going smoothly, apps are running without any issues and there isn't any noticeable lag or delay. But i was unable to share files between my host and guest os. I searched all over the internet to find the solution but none of those solution actually works. Most of the solutions are for Linux guest and host os. 

At first i used google drive to share files but the experience was not easy and it was an issue for my productive workflow. Then i wrote localshare and the issue is gone entirely.Now I am able to share my files between my Phone + Laptop + VM. 


## Credits

[Icons8](https://icons8.com/) for the icons
