import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

print TEMPLATE_PATH