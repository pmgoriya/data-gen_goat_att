import psycopg2
import random
import string
import datetime
from dateutil.relativedelta import relativedelta

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your-aws-postgresql-endpoint",
    database="your-database-name",
    user="your-username",
    password="your-password"
)
cur = conn.cursor()

# Function to generate random data for goats_vital table
def generate_goats_vital_data():
    created_at = f"{int(datetime.datetime.now().timestamp() * 1000000000)}"
    ambient_temperature = random.randint(20, 40)
    battery = random.randint(70, 100)
    temperature = round(random.uniform(20, 40), 2)
    humidity = round(random.uniform(30, 60), 2)
    rssi = random.randint(-100, -50)
    hub_id = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    tag_id = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    return (created_at, ambient_temperature, battery, temperature, humidity, rssi, hub_id, tag_id)

# Function to generate random data for tag_details table
def generate_tag_details_data(tag_id):
    status = random.choice([True, False])
    vendor_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return (tag_id, status, vendor_id)

# Function to generate random data for hub_details table
def generate_hub_details_data(hub_id):
    status = random.choice([True, False])
    vendor_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return (hub_id, vendor_id, status)

# Function to generate random data for goat_details table
def generate_goat_details_data(tag_id):
    goat_image_url = f"https://example.com/goat-image-{random.randint(1, 100)}.jpg"
    goat_birth_date = datetime.date.today() - relativedelta(years=random.randint(1, 5))
    goat_registration_date = datetime.date.today() - relativedelta(months=random.randint(1, 12))
    status = random.choice([True, False])
    return (tag_id, goat_image_url, goat_birth_date, goat_registration_date, status)

# Function to generate random data for hub_goat_tag_junction table
def generate_hub_goat_tag_junction_data(hub_id, tag_id):
    farmer_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    goat_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return (farmer_id, hub_id, tag_id, goat_id)

# Insert data into goats_vital table
for _ in range(10):
    data = generate_goats_vital_data()
    query = """
        INSERT INTO goats_vital (created_at, ambient_temperature, battery, temperature, humidity, rssi, hub_id, tag_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(query, data)

# Insert data into tag_details table
tag_ids = set()
for _ in range(5):
    tag_id = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    tag_ids.add(tag_id)
    data = generate_tag_details_data(tag_id)
    query = "INSERT INTO tag_details (tag_id, status, vendor_id) VALUES (%s, %s, %s)"
    cur.execute(query, data)

# Insert data into hub_details table
hub_ids = set()
for _ in range(3):
    hub_id = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
    hub_ids.add(hub_id)
    data = generate_hub_details_data(hub_id)
    query = "INSERT INTO hub_details (hub_id, vendor_id, status) VALUES (%s, %s, %s)"
    cur.execute(query, data)

# Insert data into goat_details table
for tag_id in tag_ids:
    data = generate_goat_details_data(tag_id)
    query = """
        INSERT INTO goat_details (tag_id, goat_image_url, goat_birth_date, goat_registration_date, status)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(query, data)

# Insert data into hub_goat_tag_junction table
for hub_id in hub_ids:
    for tag_id in tag_ids:
        data = generate_hub_goat_tag_junction_data(hub_id, tag_id)
        query = "INSERT INTO hub_goat_tag_junction (farmer_id, hub_id, tag_id, goat_id) VALUES (%s, %s, %s, %s)"
        cur.execute(query, data)

conn.commit()
cur.close()
conn.close()
