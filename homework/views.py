from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import subprocess
import re

def print_linux_uptime(request):
    template = loader.get_template("home.html")
    # Execute the commands and capture the output
    uptime_output = subprocess.check_output(['uptime']).decode('utf-8')
    data = subprocess.run(['bash', '/opt/sample.sh'], check=True, capture_output=True, text=True)
    server = request.POST.get("input_text")
    # Prepare the output for rendering in the template
    output = uptime_output + server + '<br>' + '<br>'.join(data.stdout.splitlines())

    # Render the template with the output
    context = {'output': output}
    return HttpResponse(template.render(context, request))
#    template = loaded.get_template("home.html")
#    uptime_output = subprocess.check_output(['uptime']).decode('utf-8')
#    data = subprocess.run(['bash', '/opt/sample.sh'], check=True, capture_output=True, text=True)
#    output = uptime_output + '<br>' + '<br>'.join(re.split(r'\r?\n', data.stdout))
#    return HttpResponse(template.render(request)
# Create your views here.
