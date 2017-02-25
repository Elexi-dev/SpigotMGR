import subprocess
import cfscrape
import sys
try:
    dlLink = sys.argv[1]
    spigotmcLogin = sys.argv[2]
    spigotmcPass = sys.argv[3]
except IndexError:
    print('Something went wrong with link parsing or SpigotMC login details. Please check your configuration in spigotmgr.')
    sys.exit(1)
cookie_arg, user_agent = cfscrape.get_cookie_string(dlLink)
result = subprocess.check_output(["curl", "--cookie", cookie_arg, "-A", user_agent, "--data", "login=" + spigotmcLogin + "&password=" + spigotmcPass, "-O", "-J", "-L", dlLink])