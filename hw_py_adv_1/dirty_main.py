from datetime import *
from psycopg2 import *
from application.salary import *
from application.db.people import *

print(datetime.now())
calculate_salary()
get_employees()