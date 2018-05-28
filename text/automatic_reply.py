from .new_contact_info import NewContactInfo
from .existing_contact_info import ExistingContactInfo


unknownContactInquiry = {
    NewContactInfo.allUnknown: 'Hi! Sorry I don\'t have this number in my contacts. Would you mind responding with the'
                               ' following information:'
                               '\nfirst name: <YOUR FIRST NAME>,'
                               '\nlast name: <YOUR LAST NAME>,'
                               '\ncity: <YOUR CITY>,'
                               '\ncountry: <YOUR COUNTRY>,'
                               '\nrelationship: <YOUR RELATIONSHIP TO ME> '
                               '\nPlease follow the above format. Include each label (\'first name\', \'last name\', '
                               '\'city\', \'country\', \'relationship\') and separate each label by a new line.',
    NewContactInfo.cityKnown: 'Hi! Sorry I don\'t have this number in my contacts. Would you mind responding with the'
                              ' following information:'
                              '\nfirst name: <YOUR FIRST NAME>,'
                              '\nlast name: <YOUR LAST NAME>,'
                              '\ncountry: <YOUR COUNTRY>,'
                              '\nrelationship: <YOUR RELATIONSHIP TO ME> '
                              '\nPlease follow the above format. Include each label (\'first name\', \'last name\', '
                              '\'country\', \'relationship\') and separate each label by a new line.',
    NewContactInfo.countryKnown: 'Hi! Sorry I don\'t have this number in my contacts. Would you mind responding with '
                                 'the following information:'
                                 '\nfirst name: <YOUR FIRST NAME>,'
                                 '\nlast name: <YOUR LAST NAME>,'
                                 '\ncity: <YOUR CITY>,'
                                 '\nrelationship: <YOUR RELATONSHIP TO ME> '
                                 '\nPlease follow the above format. Include each label (\'first name\', \'last name\', '
                                 '\'city\', \'relationship\') and separate each label by a new line.',
    NewContactInfo.cityAndCountryKnown: 'Hi! Sorry I don\'t have this number in my contacts. Would you mind responding '
                                        'with the following information:'
                                        '\nfirst name: <YOUR FIRST NAME>,'
                                        '\nlast name: <YOUR LAST NAME>,'
                                        '\nrelationship: <YOUR RELATONSHIP TO ME> '
                                        '\nPlease follow the above format. Include each label (\'first name\', '
                                        '\'last name\',\'relationship\') and separate each label by a new line.',
}

existingContactInquiry = {
    ExistingContactInfo.firstNameAndRelationshipUnknown: 'Hi! I see that we\'ve talked before, but I don\'t have your '
                                                         'contact info saved. Please text me your first and last name '
                                                         'and your relationship to me in the following format: '
                                                         '\nname: <first name> <last name>, '
                                                         'relationship: <relationship to me> '
                                                         '(acquaintance, friend, family, client, or work)'
                                                         '\nThanks! I\'ll get back to you soon.',
    ExistingContactInfo.firstNameUnknown: 'Hi! I see that we\'ve talked before, but I don\'t have your '
                                          'contact info saved. Please text me your first and last name '
                                          'in the following format: '
                                          '\nname: <first name> <last name>'
                                          '\nThanks! I\'ll get back to you soon.',
    ExistingContactInfo.relationshipUnknown: 'Hi {0}! Please text me your relationship to me in the following format: '
                                             '\nrelationship: <relationship to me> '
                                             '(acquaintance, friend, family, client, or work)'
                                             '\nThis helps me to helps my smart assistant better organize my texts, and '
                                             'it helps me respond to you faster. Thanks! I\'ll get back to you soon.',
    ExistingContactInfo.recognized: 'Hi {0}! I got your text and will get back to you shortly!'
}