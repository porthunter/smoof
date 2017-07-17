import requests
import requests

elkuser = "user"
elkpass = "pass"

wrong_art = """
                                                                              ffffffffffffffff
                                                                             f::::::::::::::::f
                                                                            f::::::::::::::::::f
                                                                            f::::::fffffff:::::f
    ssssssssss      mmmmmmm    mmmmmmm      ooooooooooo      ooooooooooo    f:::::f       ffffff
  ss::::::::::s   mm:::::::m  m:::::::mm  oo:::::::::::oo  oo:::::::::::oo  f:::::f
ss:::::::::::::s m::::::::::mm::::::::::mo:::::::::::::::oo:::::::::::::::of:::::::ffffff
s::::::ssss:::::sm::::::::::::::::::::::mo:::::ooooo:::::oo:::::ooooo:::::of::::::::::::f
 s:::::s  ssssss m:::::mmm::::::mmm:::::mo::::o     o::::oo::::o     o::::of::::::::::::f
   s::::::s      m::::m   m::::m   m::::mo::::o     o::::oo::::o     o::::of:::::::ffffff
      s::::::s   m::::m   m::::m   m::::mo::::o     o::::oo::::o     o::::o f:::::f
ssssss   s:::::s m::::m   m::::m   m::::mo::::o     o::::oo::::o     o::::o f:::::f
s:::::ssss::::::sm::::m   m::::m   m::::mo:::::ooooo:::::oo:::::ooooo:::::of:::::::f
s::::::::::::::s m::::m   m::::m   m::::mo:::::::::::::::oo:::::::::::::::of:::::::f
 s:::::::::::ss  m::::m   m::::m   m::::m oo:::::::::::oo  oo:::::::::::oo f:::::::f
  sssssssssss    mmmmmm   mmmmmm   mmmmmm   ooooooooooo      ooooooooooo   fffffffff


  OH SHIT, IT'S SMISHING TIME!
  SMS SPOOFER BY @PORTHUNTER

"""
print wrong_art


print "To:",
recipient = raw_input()
print "From:",
sender = raw_input()
print "Message:",
messagetext = raw_input()

url = "https://api.46elks.com/a1/SMS"
r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(elkuser, elkpass))
print r.json()
