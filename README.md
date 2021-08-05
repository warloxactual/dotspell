# Dotspell.py - Damage Over Time Email Attack

-----------------------
Dotspell.py is a powerful email security testing tool made by Warlox LLC that overloads free email accounts with thousands of non-rejectable newsletter confirmation denial or rejection emails at 80-100kb each.
-----------------------

* Only need the target's email address
* Can run on any operating system.
* Gmail, Yahoo, Protonmail and more are all succeptible to overload.

### Quick Usage

It is recommended that you have a VPN with a killswitch engaged at all times.

Download the appropriate Chrome WebDriver for your system and place the extracted chromedriver and add it to your PATH variable.

https://chromedriver.chromium.org/downloads

```shell
# Install
sudo apt-get autoremove && sudo apt autoremove git clone https://github.com/warloxactual/dotspell.py.git

# Run
$ for i in {1..5}; do python3 dotpsell.py; do

```
Enter the target email address and just walk away... just walk away...

### Description

This is a Python script created by Warlox LLC (https://www.warlox.org) a blockchain and cybersecurity IP holding company in Silicon Valley.

When the script is run, the email account's free data is used up by newsletter confirmation emails
which themselves cannot always be blocked as they are the result of measures taken to prevent 
crawlers from actually signing people up for newsletters.

What we have done is ramped up the rate and volume of attempts to hundreds of thousands or
millions depending on how many times the script is run.

Eventually a good percentage of these either end up prompting confirmation requests or even
possibly signing the email up successfully. We have no metric for successful sign ups and even
0.01% successful signups would permanently render an email address unusable. However, the point
is to trigger the confirmation emails from legitimate sources and use up all of their free email
data not necessarily to successfully sign the email address up for newsletters.

### Screenshots

![alt text] (https://imgur.com/a/FKo3Vfr)

### Documentation

Documentation under development and will be fleshed out as more features are released.


### Disclaimer

Warlox LLC accepts no liability for the use of this tool and assumes that any and all use
is done with the full written permission of the owner of the email address being targetted.

