from datetime import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import os
import psutil
import platform
from requests import get
import csv
from subprocess import Popen


def my_machine(request):
    mach_info = dict()
    mach_info["p_count_l"] = psutil.cpu_count()
    mach_info["p_count"] = psutil.cpu_count(logical=False)
    mach_info["m_size"] = "%.2f" % (psutil.virtual_memory().total/(1024.0**3))
    mach_info["disk_free"] = "%.2f" %(psutil.disk_usage('/').free/(1024.0**3))
    mach_info["os"] = platform.linux_distribution()[0] + " " + platform.linux_distribution()[1]
    mach_info["p_type"] = platform.processor()
    mach_info["ex_ip"] = get('https://ipapi.co/ip/').text
#    sys.getfilesystemencoding()


    return render(request, 'System_Monitor/dashboard/home/my_machine.html', mach_info)


def run_model(request):

    cpu_num = psutil.cpu_count()

    cpu_html = ""
    for c in range(1,cpu_num+1):
        cpu_html = cpu_html+'<div class="widget_summary"><div class="w_left w_25"><span>CPU '+str(c)+'</span></div>' \
        '<div class="w_center w_55"><div class="progress"><div class="progress-bar bg-green" role="progressbar" ' \
        'id = "cpu_'+str(c)+'" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 80%;"><span class="sr-only"></span>' \
        '</div></div></div><div class="w_right w_20"><span id = "cpu_'+str(c)+'_p"></span></div><div class="clearfix"></div></div>'

    return render(request, 'System_Monitor/dashboard/run_the_engine/run_model.html', {'cpu_html':cpu_html})


def ram_status(request):
    response = psutil.virtual_memory().percent
    return HttpResponse(response)


def cpu_status(request):
    percent = psutil.cpu_percent(percpu=True)
    response = ""
    response = response + str(psutil.cpu_count()) + " "
    for p in percent:
        response = response +str(p) +" "
    return HttpResponse(response)


