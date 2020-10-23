class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    """Cambiar admin por tu usuario y password por tu contraseña"""
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:password@localhost:5432/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'development': DevelopmentConfig
}