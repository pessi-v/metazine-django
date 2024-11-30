    
#!/bin/bash
cd /var/www/metazine
source environment/bin/activate
python3 manage.py migrate
nohup python3 manage.py runserver