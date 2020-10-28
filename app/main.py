import re

from flask import Blueprint, render_template, request

from control.search_dns import Whois

app = Blueprint('app', __name__, url_prefix='/whois/')

# You can add more searches.
allowed_search = ('e-mail profissional')


@app.route('/')
def home():
    return render_template('nslookup/index.html')


@app.route('/result/', methods=['POST'])
def result_whois():
    whois = Whois()
    if request.method == 'POST':

        domain = request.form.get('domain')
        zone = request.form.get('zone')

        if domain and zone:

            conditions = [zone.lower() in allowed_search]
            # Remove www, http and https in the domain
            domain_regex = re.sub(r"^(?:https?:\/\/)?(?:www\.)?", '', domain)
            verification_ns = whois.consult_ns(domain_regex)

            if any(conditions) and verification_ns:
                result = whois.email_profissional(domain_regex, zone)
                return render_template('nslookup/results.html', domain=result)

            return render_template(
                'nslookup/results.html', error=f'Not Found {domain_regex}'
            )

    return render_template('nslookup/index.html')
