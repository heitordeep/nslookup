from flask import Blueprint, render_template, request

from app.process import Process

app = Blueprint('app', __name__, url_prefix='/whois/')


@app.route('/')
def home():
    return render_template('nslookup/index.html')


@app.route('/result/', methods=['POST'])
def result_whois():
    if request.method == 'POST':

        domain = request.form.get('domain')
        service = request.form.get('service')

        if domain and service:

            process = Process()
            service_whois = process.get_service(input_service=service)

            if not service_whois:
                return render_template(
                    'nslookup/results.html', error=f'Serviço {service} não existe'
                )
            
            domain_ns = process.run_job(service_whois, domain)

            if not domain_ns:
                return render_template(
                    'nslookup/results.html', error=f'Domínio {domain} não existe'
                )

            return render_template('nslookup/results.html', domain=domain_ns)

    return render_template('nslookup/index.html')
