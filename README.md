# MQTT Subscriber for screen management

This project has been created in order to manage screen via XML file and an external app. This app allows you to switch
between different profile of screen. The MQTT part is used to be integrated in Home Assistant, in order to be able to
switch presets remotely (like on the couch :p ).

## Libraries

- [paho-mqtt](https://pypi.org/project/paho-mqtt/)
- [pyinstaller](https://pypi.org/project/pyinstaller/)

## External Apps

This app has been used to create template and work with them. [MonitorSwitcher](https://sourceforge.net/projects/monitorswitcher/)

## Usage

Copy the .env file to .env.local and modify to your needs, and then run the creation of the executable.

```shell
venv\Scripts\pyinstaller -F subscriber.py
```

Once build complete, you can run the executable, or create a service with [NSSM](https://nssm.cc/download).
