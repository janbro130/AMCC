import requests, time, re, winsound, os

def RiverChecker(x):
    locale = 'de_DE'
    return 'http://store.digitalriver.com/store?Action=buy&Env=BASE&Locale=' + locale + '&ProductID=' + x + '&SiteID=defaults'

def AMDProductPage(x):
    locale = 'de'
    return 'https://www.amd.com/' + locale + '/direct-buy/' + x + '/' + locale

def alarm():
    duration = 5
    Timer = time.monotonic() + duration
    while Timer > time.monotonic():
        winsound.Beep(400,500)
        time.sleep(0.25)

Products = {
    1:['6800xt','GPU','5458374100'],
    2:['6800xt black', 'GPU', '5496921500'],
    3:['6900xt', 'GPU',  '5458374200'],
    4:['5800x', 'CPU', '5450881600'],
    5:['5900x', 'CPU', '5450881500'],
    6:['5950x', 'CPU', '5450881400']
}

UserProducts = input('Enter a sequence of the following numbers to search for your products:\n1: 6800xt\n2: 6800xt black\n3: 6900xt\n4: 5800x\n5: 5900x\n6: 5950x\n')
def UserProductCleanUp(x):
    a = re.sub(r'(\D)*', r'', x)
    # remove non-digit characters
    b = re.sub(r'([7-9])', r'', a)
    # remove product numbers above 6
    c = ''.join(sorted(b))
    # sort numbers by ascending order
    d = re.sub(r'(\d)\1+', r'\1', c)
    # remove duplicate numbers
    return d

def BoolChecker():
    UserProductCleansed = UserProductCleanUp(UserProducts)
    print('Program is starting')
    os.system('cls')
    while True:
        StopFlag = False
        ProductsToBeStocked = list()
        for number in UserProductCleansed:
            x = Products[int(number)]
            print('Checking product ' + x[0])
            y = x[2]
            z = RiverChecker(y)
            RiverProduct = requests.get(url=z)
            check = bool(re.search('CAT_000016', RiverProduct.text))
            print(x[0] +' CAT16 value is : ' + str(check) + '\n')

            if check == True:
                StopFlag = True
                ProductsToBeStocked.append(y)

            if StopFlag==True and number==UserProductCleansed[-1]:
                for product in ProductsToBeStocked:
                    webbrowser.open(AMDProductPage(product))
                alarm()
                input('Press Enter to continue')
            
            if number==UserProductCleansed[-1]:
                time.sleep(5)
                os.system('cls')
                
            else:
                time.sleep(5)
                continue

if __name__ == "__main__":
    BoolChecker()
