import json
import fastapi
import requests


def submit(data):
    data_dictionary = json.loads(data)
    submission_folder_name = create_base_folder(data_dictionary)
    upload_questionnaire_information(data_dictionary, submission_folder_name)

    # return fastapi.responses.PlainTextResponse(
    #     status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     content=data
    # )

    location = f'https://nextcloud.inrae.fr/s/sqmqMHzj83zPP6T?path=%2F{submission_folder_name}'
    return fastapi.responses.JSONResponse(
        headers={
            'Location': location,
        },
        status_code=fastapi.status.HTTP_201_CREATED,
        content={
            'uuid': submission_folder_name,
            'location': location,
            'length': len(data),
        }
    )


def create_base_folder(data_dictionary):
    submission_folder_name = f'{data_dictionary["questionnaireName"]}_{data_dictionary["questionnaireUuid"]}'

    url = f'https://nextcloud.inrae.fr/public.php/webdav/{submission_folder_name}'
    payload = {}
    headers = {
        'Authorization': 'Basic c2FtcU1Iemo4M3pQUDZUOnFDeERaTk02',
        'Cookie': 'SERVERID=nextcloud0-tls.stockage.inra.fr; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; oc_sessionPassphrase=1EueLH85g26B8HE5oKIvPQijT34RDkmQge7cOY%2FqGL%2B9v4wSxamAIcUor3UTApd1yQCNeKeRx2RyQNX0GTEMuOKCsyP4FsP7Ti9NvP27slo%2F%2BKWP2A4f%2F6gLzw5sjImn; ocr4hnlcfib7=3abac879e786a81464216bb57a101f05'
    }

    requests.request("MKCOL", url, headers=headers, data=payload)
    return submission_folder_name


def upload_questionnaire_information(data_dictionary, submission_folder_name):
    # Récupération du questionnaire context / migration information
    url = f'http://172.17.0.1:3000/questionnaires/{data_dictionary["questionnaireUuid"]}'
    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2ODUwOTUyOTgsInRva2VuVXVpZCI6Ijc1N2RkNGUwLTRiZWUtNGJmYy1hMjY3LTYyOGJmNWZmNDJlNyIsInVzZXJVdWlkIjoiZWM2ZjhlOTAtMmE5MS00OWVjLWFhM2YtOWVhYjIyNjdmYzY2IiwidmVyc2lvbiI6M30.DavH_BrbB61KIroQSg4E5p-csOixaoc0jcqPJf6WAjjPzwE2t25Hu23igenmvSX7O_f3vgTkclf7gINlq-qOWo6dDX1U-_rptB9cpvNcuYRxcJM_85o-MhN9-JGfoSbemgH36QvPs2mu35_hqCSbyXVHUG_YVZjBakbhwUHH2z9sqUAm-2lWlKPOs451q_ge1QhO3szPbyd6WX4fNP51XKdos0VsUWKqp5mR-Jj4aLhCs8XP-UkaK1Eq2lF5R3Dos8zKKiI9PH9IHI8jqsQsazi5yEQUg6rJ6eScBAcys7vxKaTA7PJzk3eQUN0vFo65bewO2q7drkKnmhiRt07e5NR2Tp15F0V_MEdx66NPYL1OQ0Ah2aEKJoVgvcnT8BvkSwcmlKz2RtI0F9ZY8U00J6F0XXaDRB9MGIGr8WGmwMD-laVxyqjcQkU3VHPkRBHw9Z186Re-E5hEhf-YbCooK1Pu-8NmzKWuqafWKfoBLmeeuqskwQL6cqlGCub_WEB09HlX9h9M61EqNhLUt5tAX43iPtWZVghouzDXoznT5-UPAsRt6ADh84NEWE9oIeLABetTUCI_FJ-QuKIzKnYzieIS0TIVxIO4PNevm0__Od5cCjIz_2udsB4w5bdG1mKtZwZYwPVSxXWNcvJP4LBI4BChykmQhFcS6Dj346JyFvo'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    payload = response.json()
    url = f'https://nextcloud.inrae.fr/public.php/webdav/{submission_folder_name}/questionnaire_information.json'
    headers = {
        'Content-Type': 'text/json',
        'Authorization': 'Basic c2FtcU1Iemo4M3pQUDZUOnFDeERaTk02',
        'Cookie': 'SERVERID=nextcloud0-tls.stockage.inra.fr; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; oc_sessionPassphrase=1EueLH85g26B8HE5oKIvPQijT34RDkmQge7cOY%2FqGL%2B9v4wSxamAIcUor3UTApd1yQCNeKeRx2RyQNX0GTEMuOKCsyP4FsP7Ti9NvP27slo%2F%2BKWP2A4f%2F6gLzw5sjImn; ocr4hnlcfib7=3abac879e786a81464216bb57a101f05'
    }
    requests.request("PUT", url, headers=headers, data=payload)
