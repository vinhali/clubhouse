import requests
import json

def searchTasks(id):

    url = 'https://api.clubhouse.io/api/v2/stories/{}?token=code-here'.format(id)
    res = requests.get(url)

    if res.status_code == 200:

        return res.json()

    else:

        print('[FAILED] Response returned status: {}'.format(res.status_code))

def main():

    url = 'https://api.clubhouse.io/api/v2/projects/2/stories?token=code-here'
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        try:

            for line in data:

                nameStorie = line['name']
                startStorie = line['started_at']
                statusStorie = line['completed']
                endStorie = line['completed_at']
                category = line['labels'][0]['name']
                    
                twentyFive = searchTasks(line['id'])['tasks'][0]['description']
                statusTwentyFive = searchTasks(line['id'])['tasks'][0]['complete']

                fifty = searchTasks(line['id'])['tasks'][1]['description']
                statusFifty = searchTasks(line['id'])['tasks'][1]['complete']

                seventyFive = searchTasks(line['id'])['tasks'][2]['description']
                statusSeventyFive = searchTasks(line['id'])['tasks'][2]['complete']

                oneHundred = searchTasks(line['id'])['tasks'][3]['description']
                statusOneHundred = searchTasks(line['id'])['tasks'][3]['complete']

                print("'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(nameStorie,startStorie,statusStorie,endStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category))

        except IndexError:

            pass

    else:

        print('[FAILED] Response returned status: {}'.format(res.status_code))

if __name__ == "__main__":
    main()
