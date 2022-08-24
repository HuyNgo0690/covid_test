class BaseMode:
    def set_data(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
