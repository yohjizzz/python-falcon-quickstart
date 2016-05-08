

class ExtensionComponent(object):
    """
    Falcon’s middleware
    基本は Falcon で管理されるすべてのリソース (というかリクエスト) に対して一律で適用されます
    """
    def process_request(self, req, resp):
        """
        リクエスト受信直後にコールされます
        URI に対するリソースが見つからなくても、このメソッドはコールされます
        """
        print("middleware: process before routing")

    def process_resource(self, req, resp, resource, param):
        """
        URL に対するリソースの直前にコールされます
        URI に対するリソースが見つからなければ、このメソッドはコールされません (v0.3.0 ではコールされてた)
        引数 param は v1.0.0 で追加された (v0.3.0 では存在しない)
        """
        print("middleware: process before resource", resource)

    def process_response(self, req, resp, resource):
        """
        レスポンス送信直前にコールされます
        URL に対するリソースが見つからなくても、このメソッドはコールされます
        """
        print("middleware: process before response", resource)


def before_resource(req, resp, resource, params):
    """
    Falcon's hook function for before resources
    @falcon.before(..) や @falcon.after(..) を使ってファンクションまたはリソースクラス単位で指定します
    """
    print("hook: process before resource", resource)


def after_resource(req, resp, resource):
    """
    Falcon's hook function for after resources
    @falcon.before(..) や @falcon.after(..) を使ってファンクションまたはリソースクラス単位で指定します
    """
    print("hook: process after resource", resource)
