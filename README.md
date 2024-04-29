# Readme.md

## Project Overview

This project demonstrates how to generate random data and insert it into a PostgreSQL database at specified intervals. The code provided serves as a starting point for creating your own custom data generator.

## Database Structure

The code assumes a specific database structure, which consists of the following tables:

1. `tag_details`: Stores information about tags.
2. `hub_details`: Stores information about hubs.
3. `goat_details`: Stores information about goats associated with tags.
4. `hub_goat_tag_junction`: Stores information about the relationships between hubs, goats, and tags.
5. `goats_vital`: Stores vital information about goats, collected at specified intervals.

## Customizing the Code

To create your own custom data generator, follow these steps:

1. **Modify the database connection details**: Update the `host`, `database`, `user`, and `password` parameters in the `psycopg2.connect()` function to match your PostgreSQL database configuration.
2. **Adjust the data generation functions**: Modify the functions `generate_goats_vital_data()`, `generate_tag_details_data()`, `generate_hub_details_data()`, `generate_goat_details_data()`, and `generate_hub_goat_tag_junction_data()` to generate data according to your specific requirements. You can change the range of random values, the format of generated strings, and any other aspects of the generated data.
3. **Customize the initial data insertion**: Adjust the number of records inserted into the `tag_details`, `hub_details`, `goat_details`, and `hub_goat_tag_junction` tables by modifying the range of the `for` loops. You can also change the data generation logic inside these loops if needed.
4. **Configure the goats_vital data insertion interval**: Change the value passed to the `time.sleep()` function inside the `while` loop to control the interval at which data is inserted into the `goats_vital` table. The current value is set to 60 seconds (1 minute).
5. **Adjust the number of goats_vital records inserted per interval**: Modify the range of the `for` loop inside the `while` loop to control how many records are inserted into the `goats_vital` table during each interval.
6. **Add error handling and logging**: Implement additional error handling and logging mechanisms as needed to ensure proper functioning and monitoring of your data generator.

By following these steps, you can customize the provided code to generate data tailored to your specific use case and database structure.
