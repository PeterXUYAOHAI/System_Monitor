# System_Monitor
Web-based system monitor

###
System_Monitor provides a web-based graphic interface of the system staus.  
![System-Info](https://cloud.githubusercontent.com/assets/11495951/26002339/eaee156c-3761-11e7-9d65-7c6d535e9ba1.jpeg)
system-info lists some basic information about the machine.  
![System-Monitor](https://cloud.githubusercontent.com/assets/11495951/26001744/fed6678e-375f-11e7-9fb1-ff37f3400939.png)
system-monitor show the cpu and memory status in real-time.  

## Requirement  
* Django >= 1.11.1  
find install guide [here](https://docs.djangoproject.com/en/1.11/topics/install/).  


* psutil >= 5.52   
` pip install psutil `


## To Use
1. clone the repository to local  
2. In the repo directory do  
` python manage.py runserver `  
3. visit ` http://127.0.0.1:8000/ ` by browser 


## To Do
* Add Network Monitor  
* Add Process Monitor
* Add more System Info
* Add wechat auto-notification function
