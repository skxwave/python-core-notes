class DatabaseHelper:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("No existing instance. Creating one...")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, db_url):
        if not self._initialized:
            self._db_url = db_url
            self.__class__._initialized = True

    def __call__(self, *args, **kwds):
        print("hello") # db() -> will call this

    @property
    def db_url(self):
        return self._db_url


db = DatabaseHelper("test")
db2 = DatabaseHelper("test2")

print(db is db2)
print(db.db_url)
print(db2.db_url)
