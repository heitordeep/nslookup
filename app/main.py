from flask import Blueprint, render_template, request

from app.process import Process

app = Blueprint('app', __name__, url_prefix='/whois/')


@app.route('/')
def home():
    return render_template('nslookup/index.html')


@app.route('/result/', methods=['POST'])
def result_whois():

    domain = request.form.get('domain')
    service = request.form.get('service')

    if not domain or not service:
        return render_template('nslookup/index.html')
    
    process = Process()
    result = process.process_request(service=service, domain=domain)
    
    if isinstance(result, str):
        return render_template(
            'nslookup/results.html', error=result
        )
    return render_template('nslookup/results.html', domain=result)
