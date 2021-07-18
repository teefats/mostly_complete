CLIENTS_EXAMPLE = [
    {
        "first-name": "Elsa",
        "last-name": "Frost",
        "title": "Princess",
        "address": "33 Castle Street, London",
        "loyalty-program": "Gold",
    },
    {
        "first-name": "Anna",
        "last-name": "Frost",
        "title": "Princess",
        
        "address": "34 Castle Street, London",
        "loyalty-program": "Platinum",
    },
    {
        "first-name": "Harry",
        "middle-name": "Harold",
        "last-name": "Hare",
        "title": "Mr",
        "email-address": "harry.harold@hare.name",
        "loyalty-program": "Silver",
    },
    {
        "first-name": "Leonnie",
        "last-name": "Lion",
        "title": "Mrs",
        "loyalty-program": "Silver"
        
    },
]


def process_clients(segment):
    """
    This function processes a list of data about clients to prepare for a marketing
    campaign.

    Each client is represented by a dictionary with various fields (see CLIENTS_EXAMPLE
    above). Note that sometimes, some of the fields can be missing, you will need to
    take extra care to handle them.

    This function should return a new list of clients with the following format:

    For each client that have a registered address, we need a tuple that contains
    the following details:
        - full name with title (e.g., "Mr John Smith") omitting any parts that
          are not provided,
        - full name includes title, first name, middle name and last name in
          that order if defined,
        - the mailing address (not the email-address).
    If a client has no registered addresses, they should not be included in the
    returned list.

    E.g., preprocess_client_segment(CLIENTS_EXAMPLE) includes 'Princess Elsa Frost'
    but it should not include 'Mrs Leonnie Lion' because there are no associated addresses in the data.

    So, for preprocess_client_segment(CLIENTS_EXAMPLE) one of the tuples included in the list
    is ('Princess Elsa Frost', '33 Castle Street, London')

    :param segment: list of client records. See sample above.
    :return: preprocessed list of tuples consisting of full name and mailing address.
    :rtype: list of tuples
    """

    #Obtain list of clients
    client_profiles = []
    for client_details in CLIENTS_EXAMPLE:
        if "address" in client_details.keys():
            address = client_details["address"]
            first_name = client_details["first-name"] 
            last_name = client_details["last-name"]
            if "title" in client_details.keys():
            
                title = client_details['title']
                name = title + ' '+ first_name + ' ' + last_name
                
                client_profile = (name, address)
                client_profiles.append(client_profile)
            else:
                # title = client_details['title']
                name = title + ' '+ first_name + ' ' + last_name
                client_profile = (name, address)
                client_profiles.append(client_profile)
    print(client_profiles)
    return client_profiles

            

    #Check if this dictionary for entries that have a valid address.

    #Turn The items that have a valid address to a list

    #Turn that list to a tuple
process_clients(CLIENTS_EXAMPLE)
