from flask import Flask
import json
app = Flask(__name__)

#open text file in read mode
secrets_file   = open("secrets.json", "r")
secrets_json   = secrets_file.read()
secrets_file.close()
secrets = json.loads(secrets_json)

flag3 = open("flag3/flag3.txt","w+")
flag3.write(secrets['flag3'])
flag3.close()

config_file = open ("config/show_flag4.conf", "r")
config_json = config_file.read()
config_file.close()
config = json.loads(config_json)

if (config['enabled']):
    flag4 = open("config/flag4.txt","w+")
    flag4.write(secrets['flag4'])
    flag4.close()

@app.route('/')
def hello():
    data = "flag1: %s </br></br> hint: look at Image ports" % (secrets['flag1'])
    return data

if __name__ == "__main__":
    app.run(debug=True, port=8080)