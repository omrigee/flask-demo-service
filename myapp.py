from flask import Flask,jsonify,request
app = Flask(__name__)


# Initialize resources(users) DB:

#users map:
resources = {}

#users availability map (False means not available):
available = {}

for x in range(1,20):
    ip = '127.0.5.{}'.format(x)
    resources[ip] = {'ip' : ip, 'username': 'omri{}'.format(x), 'password': 'omri{}'.format(x)}
    available[ip] = True


@app.route('/users/<string:ip>', methods=['GET'])
def getResource(ip):
     if available[ip]:
        available[ip] = False
        return jsonify(resources[ip])
     else:
         return "Resource is locked", 423


@app.route('/users', methods=['POST'])
def releaseResource():
    content = request.get_json()
    ip = content['Ip']
    if available[ip]:
        return ip + ' is available', 200
    available[ip] = True
    return ip + ' resource is now available.', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7800)



