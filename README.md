Remote Windows Volume Control API

A Python-based solution to control and monitor the volume on remote Windows machines using Flask APIs. This project allows users to control the volume remotely via simple HTTP API requests using tools like curl, PowerShell, or Postman.
Features

    Control Volume Remotely: Adjust the volume of remote Windows machines using HTTP API.
    View Current Volume Levels: Fetch the current volume level of a remote client.
    Built with Python: Uses Flask and pycaw libraries to manage volume control.

Requirements

    Python 3.7+
    Flask
    pycaw
    comtypes

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/Remote-Windows-Volume-Control-API.git
cd Remote-Windows-Volume-Control-API

Install the required packages:

bash

pip install Flask pycaw comtypes

Run the Client:

On each client machine, run the following command to start the Flask API server:

bash

    python main.py

    Ensure that the port is set correctly and that the client machine is accessible via the network.

Usage
Using curl Commands

You can use curl commands to interact with the API to control and monitor the volume.

    Set Volume:

    To set the volume to a specific level (e.g., 30%):

    bash

curl -X POST http://192.168.1.100:5000/set_volume -H "Content-Type: application/json" -d "{\"level\": 30}"

Get Current Volume:

To get the current volume level:

bash

    curl http://192.168.1.100:5000/get_volume

Using PowerShell Commands

For Windows users, PowerShell can be used to send HTTP requests:

    Set Volume:

    powershell

Invoke-RestMethod -Uri "http://192.168.1.100:5000/set_volume" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"level": 30}'

Get Current Volume:

powershell

    Invoke-RestMethod -Uri "http://192.168.1.100:5000/get_volume" -Method Get

Using Postman

    Set Volume:
        Method: POST
        URL: http://192.168.1.100:5000/set_volume
        Body: Raw JSON
        Content-Type: application/json
        Data: {"level": 30}

    Get Current Volume:
        Method: GET
        URL: http://192.168.1.100:5000/get_volume

Project Structure

graphql

remote-windows-volume-control/
├── main.py            # Client-side Flask API for volume control
├── README.md            # Project documentation
└── requirements.txt     # List of required Python packages

Notes

    Ensure that the pycaw library has the appropriate permissions to access and modify system volume settings.
    Make sure that the client machine is accessible via the network.

Contributing

Contributions are welcome! Please fork this repository and open a pull request to add improvements or bug fixes.
License

This project is licensed under the MIT License - see the LICENSE file for details.
by meen
