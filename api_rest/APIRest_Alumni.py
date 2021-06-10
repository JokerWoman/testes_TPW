import unittest
import requests
import json
import jsonpath

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:3000/auth/signup/alumni'
        self.url2 = 'http://127.0.0.1:3000/alumni'
        self.InitToken()

        self.sent_id_nroEstudante = "13105126"
        self.sent_nome = "Joana Correia"
        self.sent_dataNascimento = "2000-07-24"
        self.sent_morada = "Rua das Flores n36"
        self.sent_email = "joanaC@gmail.com"
        self.sent_descricao = "Bem-vindo ao meu perfil!"
        self.sent_telemovel = 917733556
        self.sent_password = "123456789"
        self.sent_id_role = 1
        self.sent_id_genero = 2

        self.dados = dict(
            id_nroEstudante=self.sent_id_nroEstudante,
            nome=self.sent_nome,
            dataNascimento=self.sent_dataNascimento,
            morada=self.sent_morada,
            email=self.sent_email,
            descricao=self.sent_descricao,
            telemovel=self.sent_telemovel,
            password=self.sent_password,
            id_role=self.sent_id_role,
            id_genero=self.sent_id_genero
        )

        self.d2 = '{"id_nroEstudante":"13105126",' \
                  '"nome": "Joana Correia",' \
                  '"dataNascimento": "2000-07-24",' \
                  '"morada": "Rua das Flores n36",' \
                  '"email": "joanaC@gmail.com",' \
                  '"descricao": "Bem-vindo ao meu perfil!",' \
                  '"telemovel": "917733556",' \
                  '"password": "123456789",' \
                  '"id_role": "1",' \
                  '"id_genero": "2"}'

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
                                 data=json.dumps(self.loginData),
                                 headers=self.header)
        # parse dos dados json
        data = response.json()
        data = json.loads(data)

        token = jsonpath.jsonpath(data, 'accessToken')
        userType = jsonpath.jsonpath(data, 'userType')

        self.authHeaders = {
            "Content-Type": "application/json",
            'x-access-token': token[0],
            'user-type': userType[0]
        }

    def test_post(self):
        response = requests.post(self.url, json=json.loads(self.d2))

        print(response.text)

        json_response = json.loads(response.text)

        response_nome = jsonpath.jsonpath(json_response, 'message.nome')
        response_datanascimento = jsonpath.jsonpath(json_response, 'message.dataNascimento')
        response_morada = jsonpath.jsonpath(json_response, 'message.morada')
        response_email = jsonpath.jsonpath(json_response, 'message.email')
        response_descricao = jsonpath.jsonpath(json_response, 'message.descricao')
        response_telemovel = jsonpath.jsonpath(json_response, 'message.telemovel')
        response_id_role = jsonpath.jsonpath(json_response, 'message.id_role')
        response_id_genero = jsonpath.jsonpath(json_response, 'message.id_genero')

        print(response_nome,self.sent_id_nroEstudante)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.sent_nome, response_nome[0])
        self.assertEqual(self.sent_dataNascimento, response_datanascimento[0])
        self.assertEqual(self.sent_morada, response_morada[0])
        self.assertEqual(self.sent_email, response_email[0])
        self.assertEqual(self.sent_descricao, response_descricao[0])
        self.assertEqual(self.sent_telemovel, int(response_telemovel[0]))
        self.assertEqual(self.sent_id_role, int(response_id_role[0]))
        self.assertEqual(self.sent_id_genero, int(response_id_genero[0]))

    def test_put(self):
        response = requests.put(self.url2 + '/13105126', json=json.loads(self.d2),headers = self.authHeaders)

        print(response.text)

        json_response = json.loads(response.text)


        response_morada = jsonpath.jsonpath(json_response, 'message.morada')
        response_telemovel = jsonpath.jsonpath(json_response, 'message.telemovel')
        response_descricao = jsonpath.jsonpath(json_response, 'message.descricao')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.sent_morada, response_morada[0])
        self.assertEqual(self.sent_descricao, response_descricao[0])
        self.assertEqual(self.sent_telemovel, int(response_telemovel[0]))


    def test_404(self):
        response = requests.get(self.url2 + '/13105125', json=json.loads(self.d2), headers=self.authHeaders)

        print(response.text)

        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()