import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:3000/alumni/19180041'

        self.InitToken()

    def InitToken(self):
        # login data
        self.loginData = {
            'id_nroEstudante': '19180048',
            'password': 'Esmad_2021'
        }

        # usar nos que não tem authentication header --> rotas publicas
        self.header = {"Content-Type": "application/json"}

        # fazer login
        response = requests.post('http://127.0.0.1:3000/auth/signin/alumni',
                                       data = json.dumps(self.loginData),
                                       headers = self.header)
        #parse dos dados json
        data = response.json()
        data = json.loads(data)

        token = jsonpath.jsonpath(data, 'accessToken')
        userType = jsonpath.jsonpath(data, 'userType')

        self.authHeaders = {
                            "Content-Type": "application/json",
                            'x-access-token': token[0],
                            'user-type': userType[0]
                            }

    def test_getAlumniByNumeroEstudante(self):
        # testar route get alumni by numero de estudante
        response = requests.get(self.url, headers = self.authHeaders)

        # analisar e processar os dados
        json_response = json.loads(response.text)
        json_response = jsonpath.jsonpath(json_response, 'message')
        data = json.loads(json_response[0])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(19180041, data['id_nroEstudante'])
        self.assertEqual('Andrea Isabel Freita', data['nome'])
        self.assertEqual('03/06/2021', data['dataNascimento'])
        self.assertEqual('Rua das Loucas', data['morada'])
        self.assertEqual('andreaisabelfreitas@gmail.com', data['email'])
        self.assertEqual('917574444', data['telemovel'])
        self.assertEqual('Sou uma developer.',data['descricao'])
        self.assertEqual(3, data['id_role'])
        self.assertEqual(2, data['id_genero'])

if __name__ == '__main__':
    unittest.main()
