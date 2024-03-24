import const

DATA ={
    "player": {
        "center" : (160, 520),
        "speed_fwd" : 7.0,
        "speed_down" : 4.0,
        "speed_lt" : 5.0,
        "speed_rt" : 5.0,
    },
    "enemy": {
        "speed_fwd" : 7.0,
        "speed_down" : 4.0,
        "speed_lt" : 5.0,
        "speed_rt" : 5.0,
    }
}

def assertValueTypeforKeys(in_dict:dict, setType, *args):
    try:
        dict_keys = in_dict.keys()
    except:
        dict_keys = None

    if dict_keys:
        for key in dict_keys:
            assertValueTypeforKeys(in_dict[key], setType, *args)

        for key in dict_keys:
            if key in args:
                assert(type(in_dict[key]) == setType)
    return
        
assertValueTypeforKeys(DATA, type(0.1), *["speed_fwd", "speed_down", "speed_lt", "speed_rt"])