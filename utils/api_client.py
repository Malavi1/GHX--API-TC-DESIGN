class APIClient:
    def __init__(self, api_context):
        self.context = api_context  # store shared API session

    def get(self, endpoint):
        return self.context.get(endpoint)  # send GET request

    def post(self, endpoint, payload):
        return self.context.post(endpoint, data=payload)  # send POST with body

    def put(self, endpoint, payload):
        return self.context.put(endpoint, data=payload)  # send PUT (update)

    def delete(self, endpoint):
        return self.context.delete(endpoint)  # send DELETE request
    
    