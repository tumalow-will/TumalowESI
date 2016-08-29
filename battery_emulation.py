def apply_efficiency(discharged_energy, efficiency):
    # POS -> discharging    
    if discharged_energy < 0 :  # We are charging...
        discharged_energy = discharged_energy * efficiency
    return discharged_energy

def constrain_soc(soc, upper_limit=None, lower_limit=0):
    #constrain the soc
    if not (upper_limit is None):
        soc = min(soc, upper_limit)
    soc = max(soc, lower_limit)
    return soc

def calc_new_soc(old_soc, discharged_energy, efficiency=1.0,
                    upper_limit=None, lower_limit=0):
    discharged_energy = apply_efficiency(discharged_energy, efficiency)
    soc = old_soc - discharged_energy
    soc = constrain_soc(soc, upper_limit, lower_limit)
    return soc


class SimpleEmulator(object):
    def __init__(self, initial_soc=6, initial_ts=None, efficiency=1.0, capacity=None):
        #set the time that the simulation started
        self.previous_ts = initial_ts
        self.output = 0
        self.soc = initial_soc
        self.efficiency = efficiency
        self.capacity = capacity

    def set_ts(self, ts):
        self.previous_ts = ts
    def calc_new_soc(self, output, curr_ts):
        self.output = output
        old_soc = self.soc
        if not (self.previous_ts is None):
            elapsed_time = curr_ts - self.previous_ts
            discharged_energy = output * elapsed_time/3600.
            soc = calc_new_soc(old_soc=old_soc,
                        discharged_energy=discharged_energy,
                        efficiency=self.efficiency,
                        upper_limit=self.capacity,
                        lower_limit=0)
            self.soc = soc            
        self.set_ts(curr_ts)
    
        return soc
