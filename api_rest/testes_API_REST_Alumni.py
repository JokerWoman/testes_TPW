import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
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

    def test_getAlumniByNumeroEstudanteAuthOk(self):
        # testar route get alumni by numero de estudante
        response = requests.get('http://127.0.0.1:3000/alumni/19180047', headers = self.authHeaders)

        # analisar e processar os dados
        json_response = json.loads(response.text)
        json_response = jsonpath.jsonpath(json_response, 'message')
        data = json.loads(json_response[0])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(19180047, data['id_nroEstudante'])
        self.assertEqual('Antonio Hernandes', data['nome'])
        self.assertEqual('18/04/2000', data['dataNascimento'])
        self.assertEqual('Rua das Batatas', data['morada'])
        self.assertEqual('antonio@gmail.com', data['email'])
        self.assertEqual('914564845', data['telemovel'])
        self.assertEqual('Sou o Antonio',data['descricao'])
        self.assertEqual(3, data['id_role'])
        self.assertEqual(1, data['id_genero'])

    def test_getAllAlumniAuthOk(self):
        # testar route get alumni by numero de estudante
        response = requests.get('http://127.0.0.1:3000/alumni/', headers = self.authHeaders)
        self.assertEqual(response.status_code, 200)

    def test_getAllAlumniAuthNok(self):
        # testar route get alumni by numero de estudante
        response = requests.get('http://127.0.0.1:3000/alumni/')
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
