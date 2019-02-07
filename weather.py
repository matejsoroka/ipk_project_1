import json
import socket
import sys


def get_args():
    if len(sys.argv) == 3:
        return [sys.argv[1], sys.argv[2]]
    else:
        print("Invalid count of arguments")
        return False


def print_weather(weather):
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print("temp: {0:.1f}°C".format(float(weather['main']['temp']) - 273.15))
    print("humidity: {}%".format(weather['main']['humidity']))
    print("pressure: {}hPa".format(weather['main']['pressure']))
    print("wind-speed: {}km/h".format(weather['wind']['speed']))
    print("wind-deg: {}".format(weather['wind']['deg']))


def __main__():
    "Blablabalbla"
    args = get_args()
    if args:
        key = args[0]
        city = args[1]
    else:
        sys.exit(-1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ('api.openweathermap.org', 80)

    client_socket.connect(server)

    req = 'GET /data/2.5/weather?q={}&APPID={} HTTP/1.0\r\n\r\n'.format(city, key).encode('UTF-8')

    client_socket.send(req)

    response = ''
    while True:
        received = client_socket.recv(1024)
        if not received:
            break
        response += received.decode('UTF-8')

    client_socket.close()

    print_weather(json.loads(response.split("\r\n\r\n")[-1]))


__main__()