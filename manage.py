import os
import sys

if __name__ == "__main":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project,settings")
    try:
        from django.core.management import execute_from_command_line
        except ImportError: