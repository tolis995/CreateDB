import json
import requests

with open('red2.json', 'r', encoding='utf-8') as testfile:
    query = json.load(testfile)
print(query)

# print(query['query_result'])


for label, value in query['query_result'].items():
    print(label, value)
    if label == 'data':
        # for x1 in value['columns']:
        #     print(x1)
        print('*' * 40)
        print("{:<18} {:<8}".format('Store', 'Order Value'))
        yogimsg = "{:<12} {:<5} {:<7}\n".format(' Store', 'Ordrs', 'Values')
        for x2 in value['rows']:
            yogimsg = yogimsg + "  {0:<11} {1:<4} {2:<7} \n".format(x2['case'], x2['count'], x2['sum'])
            # yogimsg = yogimsg + "{0}  {1}   {2}\n".format(x2['case'], x2['count'], x2['sum'])
            case = x2['case']
            sum_value = float(x2['sum'])
            print("{:<18} {:>10.2f}".format(case, sum_value), x2['count'])

            # print(f"Store: {case}, Orders Value: {sum_value}")
            # print(x2['case'],x2['sum'])
print('*' * 40)

# print(query['retrieved_at'].split('T'))
print(yogimsg)

url = 'https://hooks.slack.com/services/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'
# myobj = {"text": "Today's stats {0}".format(yogimsg), "icon_emoji": ":ghost:"}
myobj = {"text": yogimsg}
x = requests.post(url, json=myobj)
print("-" * 40)
print(x.text)

msg="https://redash.rabbitapp.co/api/queries/180/results.csv?api_key=sn0IUT1nkjrT0NQQ4XciOrrPpGEbI3QA4OvxtuMt"
x = requests.get(msg )
print(x.text)
