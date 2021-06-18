class Config:
    SECRET_KEY = '001project'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:newpassword@localhost/001project'.format(user='root', password='newpassword', server='localhost', database='001project')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
