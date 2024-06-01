from flask import Blueprint, render_template, request

from adapters import DigDNS
from app.service_application import ServiceApplication

app = Blueprint('app', __name__, url_prefix='/whois/')

@app.route('/')
def home():
    return render_template('nslookup/index.html')

@app.route('/result/', methods=['POST'])
def result_whois():

    domain = request.form.get('domain')
    service_application = ServiceApplication(whois=DigDNS())
    domain_info = service_application.get_dns(domain)
    
    if isinstance(domain_info, str):
        return render_template(
            'nslookup/error.html', error=domain_info
        ), 404
    
    return render_template('nslookup/results.html', domain=domain_info)
