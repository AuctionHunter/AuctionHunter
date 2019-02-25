# noinspection PyMethodMayBeStatic,PyProtectedMember
class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'scrapy_app':
            return 'mongo'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'scapy_app':
            return 'mongo'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'auth':
            return db == 'auth_db'
        return True
