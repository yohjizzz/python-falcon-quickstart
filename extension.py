

class ExtensionComponent(object):
    """
    Falcon’s middleware
    """
    def process_request(self, req, resp):
        print("middleware: process before routing")

    def process_resource(self, req, resp, resource):
        print("middleware: process before resource", resource)

    def process_response(self, req, resp, resource):
        print("middleware: process before response", resource)


def before_resource(req, resp, resource, params):
    """
    Falcon's hook function for before resources
    :param req: Request
    :param resp: Response
    :param resource:
    :param params:
    """
    print("hook: process before resource", resource)


def after_resource(req, resp, resource):
    """
    Falcon's hook function for after resources
    :param req:
    :param resp:
    :param resource:
    """
    print("hook: process after resource", resource)
