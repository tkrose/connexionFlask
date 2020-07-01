from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Nook": {
        "fname": "Tom",
        "lname": "Nook",
        "timestamp": get_timestamp()
    },
    "Clark": {
        "fname": "Kent",
        "lname": "Clark",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]