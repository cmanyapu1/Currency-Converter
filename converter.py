import requests

class Converter():

    def __init__(self, old, new, amount):

        self.old = old
        self.new = new
        self.amount = amount

    def convert(self):

        url = 'https://api.exchangerate.host/convert?from={}&to={}&amount={}'.format(self.old, self.new, self.amount)
        response = requests.get(url)
        data = response.json()

        return data.get("result")
    
    # def symbol(self):


    
        

    
