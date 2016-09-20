class ZipResolverFactory:
    country_to_zip_resolver = {

    }

    def __init__(self, country):
        self._country = country

    def create(self):
        return self.country_to_zip_resolver.get(self._country)
