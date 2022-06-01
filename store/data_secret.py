SECRET_KEY = 'django-insecure-$(+qs^qem)@2(b0+epc&7@=w^xc0q1kvdcw2!5d05#*w#hqhk8'
PGPASS = '127.0.0.1:5432:schedule:ilya:asdwow'


def read_pgpass():
    words = PGPASS.split(':')

    return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST' : words[0],
            'PORT' : words[1],
            'NAME': words[2],
            'USER': words[3],
            'PASSWORD': words[4],
            }