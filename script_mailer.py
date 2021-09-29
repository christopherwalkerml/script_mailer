import json, os
from twilio.rest import Client


def get_auth():
    auth = {}
    with open('env.txt') as f:
        auth['auth'] = f.readline().strip()
        auth['sid'] = f.readline().strip()
        return auth


def get_loc(number):
    with open('loc_data.txt') as f:
        data = f.read()
        
        if not data:
            return 0
        
        js = json.loads(data)

        if number in js:
            return js[number]
        else:
            return 0


def set_loc(number, val):
    with open('loc_data.txt') as f:
        data = f.read()

        js = {}
        if data:
            js = json.loads(data)

        js[number] = val

    with open('loc_data.txt', 'w+') as f:
        f.write(json.dumps((js)))


def load_script():
    script = []
    with open('script.txt') as f:
        return f.readlines()


def load_numbers():
    numbers = []
    with open('numbers.txt') as f:
        return f.readlines()


def send_message(message, number):
    client.messages.create(
        to=number,
        from_="+17054827843",
        body=message
        )

if __name__ == "__main__":
    script = load_script()
    numbers = load_numbers()
    auth = get_auth()

    client = Client(auth['sid'], auth['auth'])

    for n in numbers:
        num = n.strip()
        number_location = get_loc(num)

        send_message(script[number_location], num)

        set_loc(num, number_location + 1)
