import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.InitToken()

        self.url = 'http://127.0.0.1:3000/bolsas'

        self.sent_descricao = 'bolsa55'
        self.sent_fotoLink = 'https://i.pinimg.com/originals/51/fe/18/51fe180cc453fccbf05652ad051b4803.jpg'
        self.sent_estado = 'ativo'
        self.sent_dataPublicacao = '2021-06-22'
        self.sent_dataInicio = '2021-06-22'
        self.sent_idEmpresa = 1
        self.sent_idTipoEmprego = 2
        self.sent_idNroProfessor = 2000000
        self.dados = dict(
            descricao=self.sent_descricao,
            fotoLink=self.sent_fotoLink,
            estado=self.sent_estado,
            data_publicacao=self.sent_dataPublicacao,
            data_inicio=self.sent_dataInicio,
            id_empresa=self.sent_idEmpresa,
            id_tipoEmprego=self.sent_idTipoEmprego,
            id_nroProfessor=self.sent_idNroProfessor
        )

        self.d2 = '{"descricao": "Excelente oportunidade de emprego e de enriquecer o vosso CV. Para mais informações,' \
                  ' contactar a Blip.", ' \
                  '"fotoLink": "https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/15935' \
                  '95898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI",' \
                  ' "estado": "ativo",' \
                  ' "data_publicacao": "2021-06-22", "data_inicio": "2021-06-22", ' \
                  '"id_empresa": "1", "id_tipoEmprego": "2", "id_nroProfessor": "Admin", ' \
                  '"ofertaLink": "https://blip.pt/"}'

    def InitToken(self):
        # login data
        self.loginData = {
            'id_nroProfessor': 'Admin',
            'password': 'Esmad_2021'
        }

        # usar nos que não tem authentication header --> rotas publicas
        self.header = {"Content-Type": "application/json"}

        # fazer login
        response = requests.post('http://127.0.0.1:3000/auth/signin/professor',
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

    def test_postBolsas(self):
        response = requests.post(self.url, json=json.loads(self.d2), headers=self.authHeaders)

        json_response = json.loads(response.text)

        print(response.text)

        response_descricao = jsonpath.jsonpath(json_response, 'dados.descricao')
        response_fotoLink = jsonpath.jsonpath(json_response, 'dados.fotoLink')
        response_estado = jsonpath.jsonpath(json_response, 'dados.estado')
        response_dataPublicacao = jsonpath.jsonpath(json_response, 'dados.data_publicacao')
        response_dataInicio = jsonpath.jsonpath(json_response, 'dados.data_inicio')
        response_idEmpresa = jsonpath.jsonpath(json_response, 'dados.id_empresa')
        response_idEmprego = jsonpath.jsonpath(json_response, 'dados.id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(json_response, 'dados.id_nroProfessor')
        response_ofertaLink = jsonpath.jsonpath(json_response, 'dados.ofertaLink')

        print(response_descricao)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(
            "Excelente oportunidade de emprego e de enriquecer o vosso CV. Para mais informações, contactar a Blip.",
            response_descricao[0])
        self.assertEqual(
            "https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/1593595898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI",
            response_fotoLink[0])
        self.assertEqual("ativo", response_estado[0])
        self.assertEqual("2021-06-22", response_dataPublicacao[0])
        self.assertEqual("2021-06-22", response_dataInicio[0])
        self.assertEqual(1, int(response_idEmpresa[0]))
        self.assertEqual(2, int(response_idEmprego[0]))
        self.assertEqual("Admin", response_idNroProfessor[0])
        self.assertEqual("https://blip.pt/",
                         response_ofertaLink[0])

    def test_getBolsas(self):
        response = requests.get(self.url, headers=self.authHeaders)

        self.assertEqual(response.status_code, 200)

    def test_getBolsasById(self):
        response = requests.get(self.url + '/2', headers=self.authHeaders)

        json_response = json.loads(response.text)
        jsonArray = jsonpath.jsonpath(json_response, 'message')
        jsonArray = json.loads(jsonArray[0])
        jsonArray = jsonArray[0]

        response_id = jsonpath.jsonpath(jsonArray, 'id_bolsas')
        response_descricao = jsonpath.jsonpath(jsonArray, 'descricao')
        response_fotoLink = jsonpath.jsonpath(jsonArray, 'fotoLink')
        response_estado = jsonpath.jsonpath(jsonArray, 'estado')
        response_dataPublicacao = jsonpath.jsonpath(jsonArray, 'data_publicacao')
        response_dataInicio = jsonpath.jsonpath(jsonArray, 'data_inicio')
        response_idEmpresa = jsonpath.jsonpath(jsonArray, 'id_empresa')
        response_idEmprego = jsonpath.jsonpath(jsonArray, 'id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(jsonArray, 'id_nroProfessor')
        response_ofertaLink = jsonpath.jsonpath(jsonArray, 'ofertaLink')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, int(response_id[0]))
        self.assertEqual(
            "Excelente oportunidade de emprego e de enriquecer o vosso CV. Para mais informações, contactar a Blip.",
            response_descricao[0])
        self.assertEqual(
            "https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/1593595898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI",
            response_fotoLink[0])
        self.assertEqual("ativo", response_estado[0])
        self.assertEqual("2021-06-22", response_dataPublicacao[0])
        self.assertEqual("2021-06-22", response_dataInicio[0])
        self.assertEqual(1, int(response_idEmpresa[0]))
        self.assertEqual(2, int(response_idEmprego[0]))
        self.assertEqual("Admin", response_idNroProfessor[0])
        self.assertEqual("https://blip.pt/",
                         response_ofertaLink[0])




    def test_deleteBolsa(self):
        response = requests.delete('http://127.0.0.1:3000/bolsas' + '/10', headers=self.authHeaders)

        if not response:
            self.assertEqual(response.status_code, 500)
            print(response.text)

        else:
            self.assertEqual(response.status_code, 200)
            print(response.text)

    def test_put(self):
        response = requests.put(self.url + '/2', json=json.loads(self.d2), headers=self.authHeaders)

        print(response.text)

        json_response = json.loads(response.text)

        response_descricao = jsonpath.jsonpath(json_response, 'dados.descricao')
        response_fotoLink = jsonpath.jsonpath(json_response, 'dados.fotoLink')
        response_estado = jsonpath.jsonpath(json_response, 'dados.estado')
        response_dataPublicacao = jsonpath.jsonpath(json_response, 'dados.data_publicacao')
        response_dataInicio = jsonpath.jsonpath(json_response, 'dados.data_inicio')
        response_idEmpresa = jsonpath.jsonpath(json_response, 'dados.id_empresa')
        response_idEmprego = jsonpath.jsonpath(json_response, 'dados.id_tipoEmprego')
        response_idNroProfessor = jsonpath.jsonpath(json_response, 'dados.id_nroProfessor')
        response_ofertaLink = jsonpath.jsonpath(json_response, 'dados.ofertaLink')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            "Excelente oportunidade de emprego e de enriquecer o vosso CV. Para mais informações, contactar a Blip.",
            response_descricao[0])
        self.assertEqual(
            "https://media-exp1.licdn.com/dms/image/C4D0BAQENxzWcIgPK4g/company-logo_200_200/0/1593595898739?e=2159024400&v=beta&t=h3Hcd6RBtkOo560E_u2O9BZfbQYbLbfvVtRSGQEcFqI",
            response_fotoLink[0])
        self.assertEqual("ativo", response_estado[0])
        self.assertEqual("2021-06-22", response_dataPublicacao[0])
        self.assertEqual("2021-06-22", response_dataInicio[0])
        self.assertEqual(1, int(response_idEmpresa[0]))
        self.assertEqual(2, int(response_idEmprego[0]))
        self.assertEqual("Admin", response_idNroProfessor[0])
        self.assertEqual("https://blip.pt/",
                         response_ofertaLink[0])











if __name__ == '__main__':
    unittest.main()