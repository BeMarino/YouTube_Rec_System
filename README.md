# YouTube_Rec_System

This repo contains a tool to collect the information of the videos suggested by YouTube recommender system. <br>
The purpose of the tool is to collect the metadata (title, description, producer, channel and category) 
of the suggested videos and keep track of various videos viewed by the user, in order to perform an analysis on the bias of the suggested content. <br>
A database is used as support to store the collected informations.
<br>
<br>

## Collection pipeline
<img src=https://raw.githubusercontent.com/BeMarinoGit/YouTube_Rec_System/master/pipeline.png> 
<br><br>

## Pre-requisites
 * [Python](https://www.python.org/downloads/) 
 * A webServer to store the database ([Xampp](https://www.apachefriends.org/it/index.html) or [Wampp](https://www.wampserver.com/en/))
 * A youtube data apyKey (https://developers.google.com/youtube/v3/getting-started?hl=it)
 
 
## Usage

### Preparatory steps

Follow the steps listed below to set up the tool:
  * Clone the repository. In terminal run  ``` git clone https://github.com/BeMarinoGit/YouTube_Rec_System.git  ```
  * Move into the downloaded folder ``` cd YouTube_Rec_System ```
  * Install required python libraries ``` pip install -r requirements.txt ```
  * Import database into the choosen webServer
  * Setting up the ```config.py``` file.

<br>
Now you are ready to use the tool!

### Using the tool

First of all you need to create at least a session_setup, that is a setup that will be use to navigate youtube. <br>
To do this run ```python newSetup.py``` in terminal.
<br> After you create a session setup you can run ``` python main.py``` in terminal and the process will start. <br> The script check every minute if there are 
some session to be execute.

## Final thoughts

A united-states google account is recommended to use this tool.
