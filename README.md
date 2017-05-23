# Thermon

A monitoring tool designed to poll data from system sensors for logging and
plotting.

# Setup

Thermon requires Python 2.7 along with a few python libraries such as Paramiko
and Matplotlib

```
pip install -r requirements.txt
```

# Usage

Thermon operates with a configuration file that tells it which sensors to poll
and can also be used to specify the target to connect to and the credentials to
use.

The configuration files are in an .ini format. Sections of the configuration
that start with `probes:` will define a category of probes, within each section
you can define a probe as `name`=`/polling/path`. See `barreleye_temps.ini` as
an example.

If you want to provide the target host address and credentials, these will go
in a section called `target`, any values provided here will skip the
interactive prompts.

```
[target]
host=mysystem.example.com
username=myuser
password=luvK1ttyC@t$
```
