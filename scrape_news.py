import requests, os, sys, time, random
from bs4 import BeautifulSoup
from selenium import webdriver


'''Quick, dirty, somewhat ugly and unnecessarily repetitive script which scrapes 5 newspapers: 1) Ottawa Citizen, 2) Toronto Star, 3) National Post, 4) Montreal Gazette, 5) The Province
   and 2 TV networks: 5) CTV News and 6) Global News or Google News for Canadian cyber crime related headlines'''


def main():


    os.system('clear')


    print('\n========================================== MENU ===============================================\n')
    print('[1] SCRAPE INDIVIDUAL SITES  ')
    print('    (Ottawa Citizen, Toronto Star, National Post, Montreal Gazette, The Province, CTV, Global)\n')
    print('[2] QUERY GOOGLE NEWS SEARCH\n')
    print('===============================================================================================')


    init_choice = int(input('\nENTER CHOICE: '))


    # BRANCH 1

    if init_choice == 1:

        # OTTAWA CITIZEN
        def ottcitz():

            html_ottcitz = requests.get('https://ottawacitizen.com/')
            html = html_ottcitz.text

            headlines = BeautifulSoup(html, 'html.parser')

            with open('citz_headlines.txt', 'w') as file:
                file.write(str(html))

            def ottcitz_menu():

                print('\n|OTTAWA CITIZEN| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')

                choice = int(input('ENTER CHOICE: '))
                print('\n')

                if choice == 1:
                    os.system("""cat citz_headlines.txt | grep '"title":' | cut -c 23-150""") 
                elif choice == 2:
                    os.system("""cat citz_headlines.txt | grep '"title":' | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                            |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|compu'} | cut -c 23-140""")
                elif choice == 3:
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    ottcitz_menu()

            ottcitz_menu()

            os.system('rm citz_headlines.txt')
            
        ottcitz()


        # TORONTO STAR
        def torstar():

            html_torstar = requests.get('https://www.torontostar.com')
            html = html_torstar.text 

            headlines = BeautifulSoup(html, 'html.parser')

            headlines = headlines.find_all('span')

            with open('star_headlines.txt', 'w') as file:
                for title in headlines:
                    file.write(str(title))
                    file.write('\n')   

            def torstar_menu():

                print('\n|TORONTO STAR| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')
                choice = int(input('ENTER CHOICE: '))

                if choice == 1:
                    os.system('cat star_headlines.txt | grep "mediacard-headline" | cut -c 41- | more')
                elif choice == 2:
                    os.system("""cat star_headlines.txt | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                            |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|compu'}  | cut -c 41-""")
                elif choice == 3:
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    torstar_menu()

            torstar_menu()

            os.system('rm star_headlines.txt')

        torstar()


        # NATIONAL POST
        def natpost():

            html_natpost = requests.get('https://nationalpost.com/')
            html = html_natpost.text 

            with open('post_headlines.txt', 'w') as file:
                file.write(str(html))  

            def natpost_menu():

                print('\n|NATIONAL POST| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')
                choice = int(input('ENTER CHOICE: '))
                print('\n')

                if choice == 1:
                    os.system("""cat post_headlines.txt | grep '"title":' | cut -c 23-140 | more""") 
                elif choice == 2:
                    os.system("""cat post_headlines.txt | grep '"title":' | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                            |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|compu'}  | cut -c 23-140""")
                elif choice == 3:
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    natpost_menu()

            natpost_menu()

            os.system('rm post_headlines.txt')

        natpost()


        # CTV NEWS
        def ctvnews():

            html_ctv = requests.get('https://www.ctvnews.ca/')

            headlines = BeautifulSoup(html_ctv.content, 'html.parser')

            headlines = headlines.find_all('h2', class_="teaserTitle")

            with open('ctv_headlines.txt', 'w') as file:
                for line in headlines:
                    file.write(str(line.get_text()))

            def ctv_menu():

                print('\n|CTV NEWS| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')
                choice = int(input('ENTER CHOICE: '))
                print('\n')

                if choice == 1:
                    os.system("cat ctv_headlines.txt | more") 
                elif choice == 2:
                    os.system("""cat ctv_headlines.txt | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                            |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|comput'}""")

                elif choice == 3:
                    
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    ctv_menu()

            ctv_menu()

            os.system('rm ctv_headlines.txt')

        ctvnews()


        # GLOBAL NEWS    
        def globnews():

            html_glob = requests.get('https://globalnews.ca/canada/')

            headlines = BeautifulSoup(html_glob.content, 'html.parser')

            headlines = headlines.find_all('span', class_="c-posts__headlineText")

            with open('glob_headlines.txt', 'w') as file:
                for title in headlines:
                    file.write(str(title.get_text()))
                    file.write('\n')

            def glob_menu():

                print('\n|GLOBAL NEWS| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')
                choice = int(input('ENTER CHOICE: '))
                print('\n')

                if choice == 1:
                    os.system("cat glob_headlines.txt | more") 
                elif choice == 2:
                    os.system("""cat glob_headlines.txt | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                            |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|comput'}  """)
                elif choice == 3:
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    glob_menu()

            glob_menu()

            os.system('rm glob_headlines.txt')

        globnews()


        # MONTREAL GAZETTE
        def mongazet():

            html_mongazet = requests.get('https://montrealgazette.com/')
            html = html_mongazet.text

            headlines = BeautifulSoup(html, 'html.parser')

            with open('gazet_headlines.txt', 'w') as file:
                file.write(str(html))

            def mongazet_menu():

                print('\n|MONTREAL GAZETTE| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')

                choice = int(input('ENTER CHOICE: '))
                print('\n')

                if choice == 1:
                    os.system("""cat gazet_headlines.txt | grep '"title":' | cut -c 23-120 | more""") 
                elif choice == 2:
                    os.system("""cat gazet_headlines.txt | grep '"title":' | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                        |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|comput'} | cut -c 23-100 """)
                elif choice == 3:
                    sys.exit(0)

                print('\n')
                print('+------------------------------------------------------+')
                print('|Enter y to make selection again or <enter> to continue|')
                print('+------------------------------------------------------+')

                choice2 = input('')

                if choice2 == 'y':
                    os.system('clear')
                    mongazet_menu()

            mongazet_menu()

            os.system('rm gazet_headlines.txt')
            
        mongazet()


        # THE PROVINCE
        def vanprov():

            html_prov = requests.get('https://theprovince.com/category/news/')

            headlines = BeautifulSoup(html_prov.content, 'html.parser')

            headlines = headlines.find_all('article', class_="article-card article-card--two-column article-card--no-meta-top article-card--no-excerpt--sm-down")

            with open('prov_headlines.txt', 'w') as file:
                for title in headlines:
                    file.write(title.get_text())
                    file.write('\n\n')

            def prov_menu():

                    print('\n|THE PROVINCE| - [1] All headlines [2] Hacking specific headlines [3] Exit program\n')
                    choice = int(input('ENTER CHOICE: '))
                    print('\n')

                    if choice == 1:
                        os.system("cat prov_headlines.txt | more") 
                    elif choice == 2:
                        os.system("""cat prov_headlines.txt | grep -Ei {'hack|phish|vish|ddos|ware|cybe|breac|ranso|extor|botn|abus|isinfo|web|onlin|seiz|harra|sting|schem
                                                                    |scam|dox|spam|swatt|cloni|skimm|frau|porn|unautho|stalk|piracy|syndicate|launder|espion|sabot|spy
                                                                    |interne|dark|bitco|leak|denia|threat|illeg|btc|ethere|thef|creden|defac|vanda|misus|comput'}  """)
                    elif choice == 3:
                        sys.exit(0)

                    print('\n')
                    print('+------------------------------------------------------+')
                    print('|Enter y to make selection again or <enter> to continue|')
                    print('+------------------------------------------------------+')

                    choice2 = input('')

                    if choice2 == 'y':
                        os.system('clear')
                        prov_menu()

            prov_menu()

            os.system('rm prov_headlines.txt')

        vanprov()


    # BRANCH 2 (GOOGLE NEWS)

    elif init_choice == 2:

        delay = random.randint(2,6)

        wd = webdriver.Firefox()

        queries = ['hack','phishing','vishing','ddos','malware','cyber','breach','ransom','dark web','botnet','deep web',
                'scams','dox','spam','swatting','cloning','skimming','fraud','stalking','piracy','syndicate','laundering',
                'bitcoin','leak','threat','illegal','credentials','deface','vandalized','dark web']

        random.shuffle(queries)

        for term in queries: 
            control_string = "window.open('{0}')".format(f'https://news.google.com/search?q={term}&hl=en-CA&gl=CA&ceid=CA%3Aen')
            browser = wd.execute_script(control_string)
            time.sleep(delay)

main()










