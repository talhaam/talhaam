from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def check_abuse_ip(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': '1f1205e7d949ec9b05c3f874a5210cab1ba85ad0ba9fccba13be99a36d970b5b15aa3b9d6d76229f'
    }
    response = requests.get(url, headers=headers, params=querystring, verify=False)
    decoded_response = json.loads(response.text)
    return decoded_response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        result = check_abuse_ip(ip_address)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
