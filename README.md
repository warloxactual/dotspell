# dotspell
DISCLAIMER: Warlox LLC accepts no liability for the use of this tool and assumes that any and all use
is done with the full written permission of the owner of the email address being targetted.

Dotspell.py -The official Warlox LLC Damage Over Time Email Attack

This is a Python script created by Warlox LLC a blockchain and cybersecurity IP holding company in Silicon Valley.

Dotspell.py performs millions of email newsletter signup and form fill requsts across tens
of thousands of legitimate websites with the goal of triggring confirmation/rejection emails
at 80-100kb each that are intended to stop crawlers just like this by requiring human email
confirmation.

What ends up happening is the email account's free data is used up by these rejection emails
which themselves cannot be blocked as they are the result of measures taken to prevent 
crawlers from actually signing people up for newsletters.

We have no metric for how many of these attempts are successful but with the millions of
attempts being run, even 0.01% success would permanently render an email account useless.

In the terminal run:

> for i in {1..10}; do python3 dotspell.py; done

Enter the target email address and just walk away... just walk away...

