import socket
import json
import sys


def get_args():
    if len(sys.argv) == 3:
        return [sys.argv[1], sys.argv[2]]
    else:
        print("Invalid count of arguments")
        return False


def print_weather(weather):
        print(weather['name'])
        if weather['weather'][0]:
            print(weather['weather'][0]['description'])
        print("temp: {} °C".format(weather['main']['temp']))
        print("humidity: {} %".format(weather['main']['humidity']))
        print("pressure: {} hPa".format(weather['main']['pressure']))
        print("wind-speed: {} m/s".format(weather['wind']['speed']))
        if 'deg' in weather['wind']:
            print("wind-deg: {}".format(weather['wind']['deg']))


def __main__():
    args = get_args()
    if args:
        key = args[0]
        city = args[1]
    else:
        sys.exit(-1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ('api.openweathermap.org', 80)

    try:
        client_socket.connect(server)
    except socket.error as exc:
        print("Caught exception socket.error: {}".format(exc))

    req = 'GET /data/2.5/weather?q={}&APPID={}&units=metric HTTP/1.0\r\n\r\n'.format(city, key).encode('UTF-8')

    try:
        client_socket.send(req)
    except socket.error as exc:
        print("Caught exception socket.error: {}".format(exc))

    response = ''
    while True:
        received = client_socket.recv(1024)
        if not received:
            break
        response += received.decode('UTF-8')

    try:
        client_socket.close()
    except socket.error as exc:
        print("Caught exception socket.error: {}".format(exc))

    response = json.loads(response.split("\r\n")[-1])

    if response["cod"] == 200:
        print_weather(response)
    else:
        print("Error {}: {}".format(response["cod"], response["message"]))


__main__()
