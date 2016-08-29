#Tumalow ESI
##A very simple prototype of the Tumalow Energy Storage Interface (ESI).

This is a very simple prototype showing the future behavior of the Tumalow ESI.
It was created to give BEMOSS developers something quick and easy to develop against.

###Installation

This was tested on python 2.7 and requires bottle.  To get bottle you can
```
pip install bottle
```

###Usage
You can use it out of the box by simply starting the script esi_server.py

```
python esi_server.py
```
and then navigating your web browser to [this site on your localhost]
(http://localhost:8080/current/status/VaTech/1021Prince/b7a362e4-01b8-49af-8dcd-54e9473eeb06)

By default this will start a battery energy storage emulator that will
discharge at a constant rate.  You'll be able to get JSON-formatted output.

Note that the precision that the emulator reports the state of charge is
far higher than the real device.  Expect 1 decimal place at best from the 
actual hardware.

Feel free to tweak the configs.py file.  I hope that the items are straightforward
so please ask if there is some confusion.

###A Note About Security
I understand that the current authentication of a plain-text key against a 
user-name is not secure.  This will be fixed in future versions.  Because the
purpose of this was to get something quick and easy to develop against, this 
was the most lightweight way to do this at first.


