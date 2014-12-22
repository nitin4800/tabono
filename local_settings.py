
DEBUG = True

# Make these unique, and don't share it with anybody.
#SECRET_KEY = "b4273110-358d-4722-b787-01bb1b2ef9be3e8eefdf-28e0-413a-8551-2f44fb7cef7220e98b26-c744-4c0f-a111-63072805ef8f"
SECRET_KEY = "c5384221-358d-4722-b787-01bb1b2ef9be3e8eefdf-28e0-413a-8551-2f44fb7cef7220e98b26-c744-4c0f-a111-63072805ef8f"
#NEVERCACHE_KEY = "35c16766-c18d-4f8e-af8d-8efd58146bfc4fd4f603-ea5c-4b41-a176-1e6469b3222dc433dcb2-b163-4018-acf1-27834be7d9d4"
NEVERCACHE_KEY = "46d27977-c18d-4f8e-af8d-8efd58146bfc4fd4f603-ea5c-4b41-a176-1e6469b3222dc433dcb2-b163-4018-acf1-27834be7d9d4"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
