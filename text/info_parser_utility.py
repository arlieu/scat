def parseInfo(message):
    message = message.lower()
    firstName = lastName = city = country = relationship = None
    if 'first name' in message:
        firstName = message.split('first name:')[1]
        firstName = firstName.split(',')[0]
        firstName = firstName.split('\n')[0].rstrip()
    if 'last name' in message:
        lastName = message.split('last name:')[1]
        lastName = lastName.split(',')[0]
        lastName = lastName.split('\n')[0].rstrip()
    if 'city' in message:
        city = message.split('city:')[1]
        city = city.split(',')[0]
        city = city.split('\n')[0].rstrip()
    if 'country' in message:
        country = message.split('country:')[1]
        country = country.split(',')[0]
        country = country.split('\n')[0].rstrip()
    if 'relationship' in message:
        relationship = message.split('relationship:')[1]
        relationship = relationship.split(',')[0]
        relationship = relationship.split('\n')[0].rstrip()

    return (firstName, lastName, city, country, relationship)


if __name__ == '__main__':
    message = 'first name: Jerry,\n' \
              'last name: Bob,\n' \
              'city: Chicago,\n' \
              'country: USA,' \
              'relationship: friend'
    print(message)
    print(parseInfo(message))