# script_mailer
#### send pieces of text one bit at a time to your friend's numbers. Uses Twilio

To use this, import your text block (each new line is an individual text)
put your friends' numbers into numbers.txt (each new line is a new number. # ex: +11234567890)
run the script, put it on a bash timer, you choose! Then it will send your text blobs one at a time to friends.

#### NOTE:
you will need to create a env.txt file with this format:
auth
sid (AC...)
twilio_phone_number (+1...)
