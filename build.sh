#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Check if data exists, if not import it
python manage.py shell << EOF
from MaybellineGlam.models import Maybelline
if Maybelline.objects.count() == 0:
    from MaybellineGlam.views import importFromCSV
    from django.http import HttpRequest
    req = HttpRequest()
    importFromCSV(req)
    print("CSV data imported successfully!")
else:
    print("Data already exists, skipping import.")
EOF

