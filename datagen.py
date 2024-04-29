import psycopg2
import random
import string
import datetime
import time
from dateutil.relativedelta import relativedelta

# Function to generate random data for goats_vital table
def generate_goats_vital_data(tag_hub_mapping):
    created_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    ambient_temperature = random.randint(20, 40)
    battery = random.randint(70, 100)
    temperature = round(random.uniform(20, 40), 2)
    humidity = round(random.uniform(30, 60), 2)
    rssi = random.randint(-100, -50)
    tag_id, hub_id = random.choice(list(tag_hub_mapping.items()))
    return (created_at, ambient_temperature, battery, temperature, humidity, rssi, hub_id, tag_id)

# Function to generate random data for tag_details table
def generate_tag_details_data():
    tag_id = ':'.join(random.choices(string.hexdigits, k=6))
    status = random.choice([True, False])
    vendor_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return (tag_id, status, vendor_id)

# Function to generate random data for hub_details table
def generate_hub_details_data():
    hub_id = ':'.join(random.choices(string.hexdigits, k=6))
    status = random.choice([True, False])
    vendor_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return (hub_id, vendor_id, status)

# Function to generate random data for goat_details table
def generate_goat_details_data(tag_id):
    goat_image_url = f"https://example.com/goat-image-{random.randint(1, 100)}.jpg"
    goat_birth_date = (datetime.date.today() - relativedelta(years=random.randint(1, 5))).strftime("%Y%m%d")
    goat_registration_date = (datetime.date.today() - relativedelta(months=random.randint(1, 12))).strftime("%Y%m%d")
    status = random.choice([True, False])
    return (tag_id, goat_image_url, goat_birth_date, goat_registration_date, status)

# Function to generate random data for hub_goat_tag_junction table
def generate_hub_goat_tag_junction_data(hub_ids, tag_ids):
    tag_hub_mapping = {}
    for hub_id in hub_ids:
        for tag_id in tag_ids:
            if tag_id not in tag_hub_mapping:
                farmer_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                goat_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                tag_hub_mapping[tag_id] = hub_id
                data = (farmer_id, hub_id, tag_id, goat_id)
                print(f"Hub goat tag junction data: {data}")
                # query = "INSERT INTO hub_goat_tag_junction (farmer_id, hub_id, tag_id, goat_id) VALUES (%s, %s, %s, %s)"
                # cur.execute(query, data)
    return tag_hub_mapping

# Generate data for tag_details table
tag_ids = set()
for _ in range(5):
    tag_id, status, vendor_id = generate_tag_details_data()
    tag_ids.add(tag_id)
    data = (tag_id, status, vendor_id)
    print(f"Tag details data: {data}")
    # query = "INSERT INTO tag_details (tag_id, status, vendor_id) VALUES (%s, %s, %s)"
    # cur.execute(query, data)

# Generate data for hub_details table
hub_ids = set()
for _ in range(3):
    hub_id, vendor_id, status = generate_hub_details_data()
    hub_ids.add(hub_id)
    data = (hub_id, vendor_id, status)
    print(f"Hub details data: {data}")
    # query = "INSERT INTO hub_details (hub_id, vendor_id, status) VALUES (%s, %s, %s)"
    # cur.execute(query, data)

# Generate data for goat_details table
for tag_id in tag_ids:
    data = generate_goat_details_data(tag_id)
    print(f"Goat details data: {data}")
    # query = """
    #     INSERT INTO goat_details (tag_id, goat_image_url, goat_birth_date, goat_registration_date, status)
    #     VALUES (%s, %s, %s, %s, %s)
    # """
    # cur.execute(query, data)

# Generate data for hub_goat_tag_junction table
tag_hub_mapping = generate_hub_goat_tag_junction_data(hub_ids, tag_ids)

# Generate data for goats_vital table every minute
while True:
    try:
        for _ in range(10):
            data = generate_goats_vital_data(tag_hub_mapping)
            print(f"Goats vital data: {data}")
            # query = """
            #     INSERT INTO goats_vital (created_at, ambient_temperature, battery, temperature, humidity, rssi, hub_id, tag_id)
            #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            # """
            # cur.execute(query, data)

        # Commit the transaction (you can comment this out if you don't want to connect to the database)
        # conn.commit()

        # Wait for a minute before the next iteration
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {e}")
        # conn.rollback()
        time.sleep(60)