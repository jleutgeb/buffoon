from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        participation_fee=5,
        name='buffoon',
        display_name="Buffoon",
        num_demo_participants=3,
        app_sequence=['consent_ger',
                      'buffoon',
                      'buffoon_computerized',
                      'feedback',
                      'feedback_computerized',
                      'survey',
                      'payment_info',
                      ],
    ),
    dict(
        participation_fee=5,
        name='buffoon_test',
        display_name="Buffoon 24 Participants (Test)",
        num_demo_participants=24,
        app_sequence=['consent_ger',
                      'buffoon',
                      'buffoon_computerized',
                      'feedback',
                      'feedback_computerized',
                      'survey',
                      'payment_info',
                      ],
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    {
        'name': 'TU_LAB',
        'display_name': 'TU lab',
        'participant_label_file': '_rooms/tulab.txt',
    },
    {
        'name': 'TU_LAB_noIDs',
        'display_name': 'TU lab no IDs',
    }
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'j39hacqveq=k%r%cri%5j+uj$la04n4a(usd@x!i1^a#@y=2$n'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
