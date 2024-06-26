import os, inspect, sys

KEY_LOCATION = '../key.txt'

def key_file_exists():
    return os.path.exists(KEY_LOCATION)

def confirm_key():
    if key_file_exists() == False:
        file = open(KEY_LOCATION, 'x')
        file.close()
        return False
    if os.stat(KEY_LOCATION).st_size == 0:
        return False
    return True

def get_key():
    global KEY_LOCATION
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    if(path[-11:] == 'weatherwise'):    # for Django server execution
        KEY_LOCATION = KEY_LOCATION[1:] 
    if confirm_key():
        with open(KEY_LOCATION,'r') as file:

            return file.readline().strip()
    return 'n/a'

if __name__ == '__main__':
    print(get_key())