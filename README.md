# Dotspell.py - Damage Over Time Email Attack

-----------------------
Dotspell.py is a powerful email security testing tool that overloads free email accounts with thousands of non-rejectable newsletter confirmation denial or rejection emails at 80-100kb each.
-----------------------
For more information please visit: https://www.warlox.org

* Only need the target's email address
* Can run on any operating system.
* Gmail, Yahoo, Protonmail and more are all succeptible to overload.

### Quick Usage

It is recommended that you have a VPN with a killswitch engaged at all times.

```shell
# Install
git clone https://github.com/warloxactual/dotspell.git
sudo apt-get autoremove && sudo apt autoremove

# Run
$ for i in {1..5}; do python3 dotpsell.py; do

```

### Description

This is a Python script created by Warlox LLC (https://www.warlox.org) a blockchain and cybersecurity IP holding company in Silicon Valley.

When the script is run, the email account's free data is used up by newsletter confirmation emails
which themselves cannot always be blocked as they are the result of measures taken to prevent 
crawlers from actually signing people up for newsletters.

What we have done is ramped up the rate and volume of attempts to hundreds of thousands or
millions depending on how many times the script is run.

Eventually a good percentage of these either end up prompting confirmation requests or even
possibly signing the email up successfully. We have no metric for successful sign ups and even
0.01% successful signups would permanently render an email address unusable.

### Documentation

Documentation under development and will be fleshed out as more features are released.


### Disclaimer

Warlox LLC accepts no liability for the use of this tool and assumes that any and all use
is done with the full written permission of the owner of the email address being targetted.

We have no metric for how many of these attempts are successful but with the millions of
attempts being run, even 0.01% success would permanently render an email account useless.
Regardless, the point is not successful signups but confirmation emails en masse to "pop"
the maximum data usage on most free email accounts including Gmail.

Enter the target email address and just walk away... just walk away...

