from flaskapi_basic2 import app
import unittest 
import json

class Flask_api(unittest.TestCase): 

    '''
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 
    '''
	
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.post('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 201) 

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 
        data = json.loads(result.data)
        # assert the response data
        self.assertEqual(data['about'], "Hello World!\n")

    def test_multi_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/multi/10')
        data = json.loads(result.data)
        # assert the response data
        self.assertEqual(data['result'], 10*10)
    
    def test_multi_data1(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/multi/5')
        data = json.loads(result.data)
        # assert the response data
        self.assertEqual(data['result'], 5*10)

