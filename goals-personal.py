import requests
import json
import psycopg2

def connect():
    
    try:

        conn = psycopg2.connect("host='127.0.0.1' dbname='checkpoint' user='postgres' password='postgres'")
        conn.autocommit = True
        cur = conn.cursor()

        return conn, cur

    except Exception as e:

        print('[FAILED] Response returned status: {}'.format(e))


def searchTasks(id):

    url = 'https://api.clubhouse.io/api/v2/stories/{}?token=code-here'.format(id)
    res = requests.get(url)

    if res.status_code == 200:

        return res.json()

    else:

        print('[FAILED] Response returned status: {}'.format(res.status_code))

def main():

    print("[INFO] Start script ***************************************************")
    conn, cur = connect()
    url = 'https://api.clubhouse.io/api/v2/projects/2/stories?token=code-here'
    res = requests.get(url)
    cur.execute('TRUNCATE goals;')

    if res.status_code == 200:
        data = res.json()

        for line in data:

            try:

                idStorie = line['id']
                nameStorie = line['name']
                startStorie = line['created_at']
                statusStorie = line['completed']
                endStorie = line['completed_at']

                if line['labels'][0]['name'] == 'failed':

                    status = line['labels'][0]['name']
                    category = line['labels'][1]['name']

                else:

                    status = 'sucess'
                    category = line['labels'][0]['name']

                twentyFive = searchTasks(line['id'])['tasks'][0]['description']
                statusTwentyFive = searchTasks(line['id'])['tasks'][0]['complete']

                fifty = searchTasks(line['id'])['tasks'][1]['description']
                statusFifty = searchTasks(line['id'])['tasks'][1]['complete']

                seventyFive = searchTasks(line['id'])['tasks'][2]['description']
                statusSeventyFive = searchTasks(line['id'])['tasks'][2]['complete']

                oneHundred = searchTasks(line['id'])['tasks'][3]['description']
                statusOneHundred = searchTasks(line['id'])['tasks'][3]['complete']

                if endStorie is None:

                    cur.execute('''INSERT INTO goals (id,nameStorie,startStorie,statusStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(
                    idStorie,nameStorie,startStorie,statusStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status))

                    cur.execute('''INSERT INTO goals_history (id,nameStorie,startStorie,statusStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(
                    idStorie,nameStorie,startStorie,statusStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status))
                
                else:

                    cur.execute('''INSERT INTO goals (id,nameStorie,startStorie,statusStorie,endStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(
                    idStorie,nameStorie,startStorie,statusStorie,endStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status))

                    cur.execute('''INSERT INTO goals_history (id,nameStorie,startStorie,statusStorie,endStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(
                    idStorie,nameStorie,startStorie,statusStorie,endStorie,twentyFive,statusTwentyFive,fifty,statusFifty,seventyFive,statusSeventyFive,oneHundred,statusOneHundred,category,status))

            except IndexError:
                print("[FAILED] Storie {}".format(nameStorie))
                pass

    else:

        print('[FAILED] Response returned status: {}'.format(res.status_code))

    cur.execute('''UPDATE goals SET status = 'justified' FROM exception WHERE goals.id = exception.id AND justified = true''')
    conn.close()
    print("[OK] End script *******************************************************")

if __name__ == "__main__":
    main()
