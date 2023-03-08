from datetime import datetime
from psycopg2 import sql
from application.salary import calculate_salary
from application.db.people import get_employees

print(datetime.now())
calculate_salary()
get_employees()