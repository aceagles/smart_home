# smart_home
A hub for wifi plugs and switches

# Motivations and Scope

I have a number of smart switches around the house but find their reliance on cloud based hubs cumbersome and worrying from a security perspective.
Tasmota is a nice third party firmware that these switches can be flashed with which will allow me to control them by simple http requests.
This hub will be hosted locally on a raspberry pi and interface with these switches.

Iniitial Scope:
- DRF backend to store information on all the switches in the system. Admin page will be used to add new switches
- React app which displays the current status of switches on the system and allows the user to toggle them
- Add, View, Delete switch schedules from the frontend
- Use Celery to schedule these commands in the backend

Expanded Scope:
- I have been making an embedded thermostat based on ESP8266, The backend will poll temperatures and operation modes from this
and imlement ITTT style operations based on commands, times, and temperatues
