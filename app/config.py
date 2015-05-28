ENV = 'Dev'
def get_settings():
    return eval(ENV)

class Dev():
    ''' Development Settings '''

    #tdbm API key
    tmdb_key = "27591dafb389ecb4d7c7bb206fbfe833"

