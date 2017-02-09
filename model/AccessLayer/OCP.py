from Query import Query
from RequestHandler import RequestHandler

class OCP(RequestHandler):

    def parse(self, request):

        whois = self.request.remote_ip
        settings = {
            'feature': whois
        }
        return Query(**settings)