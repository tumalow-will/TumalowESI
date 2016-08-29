import time

from bottle import Bottle, route, run
from battery_emulation import SimpleEmulator
from configs import configs, connection, users

def authenticate(user, facility, key):
    print 'authenticating'
    print user, facility, key
    try:
        user_d = users[user]
    except KeyError:
        return 'No user with that name'
    
    if user_d['key'] != key:
        #wrong key given
        return 'Incorrect key'

    if facility not in user_d['facilities']:
        #requesting information about a facility
        #that this user is not allowed to
        return 'Facility not in approved list for this user'
    
    return 'ok'


app = Bottle()

emulator = SimpleEmulator(initial_soc=configs['soc'], #state of charge
        initial_ts = time.time(),  #time
        efficiency = configs['efficiency'],  #electrical efficiency
        capacity = configs['capacity'])  #battery energy capacity

output = configs['output']

status_codes = {    'on': 'operational',
                    'off': 'offline'
                }
status = status_codes[configs['status']]

@app.route('/current/status/<user>/<facility>/<key>')
def hello(user, facility, key):
    auth = authenticate(user, facility, key)
    if auth == 'ok':
        ts = time.time()
        #simulate time passing for the battery system
        #it has been (dis)charging the whole time
        emulator.calc_new_soc(output=output, curr_ts=ts)
        return {"output": emulator.output,
            "soc": emulator.soc,
            "status": status}
    else:
        return auth


if __name__ == '__main__':
    run(app, 
        host=connection['host'], 
        port=connection['port'])
