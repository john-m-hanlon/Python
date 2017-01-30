""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

dir1 = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Intermediate'\
       'Python 3 Tutorial [Sentdex]/'


def random_starting_url():
    '''
    Returns http + three random characters + .com is a starting url

    Parameters
    ==========

    Returns
    =======
    url : str
        Starting url
    '''

    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       for _ in range(3))
    url = ''.join(['https://', starting, '.com'])
    return url


url = random_starting_url()
print(url)


def handle_loal_links(url, link):
    '''
    Creates a final url page to crawl with the primary and secondary links

    Parameters
    ==========
    url : str
        The starting url link to crawl

    link : str
        The tertiary page to crawl

    Returns
    =======
    link : str
        Returns the finalized url link
    '''
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link


def get_links(url):
    '''
    Searched for all links and returns all others

    Parameters
    ==========
    url : str
        The url link to search

    Returns
    =======
    links : str
        All links on any given url
    '''

    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_loal_links(url, link) for link in links]
        links = [str(link.encode('ascii')) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate')
        return []

    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, return empty link')
        return []

    except AttributeError as e:
        print(e)
        print('We likely got None for links, so we are throwing this')
        return []

    except Exception as e:
        print(str(e))
        # log this error
        return []


def main():
    '''
    Searches how_many random urls and returns the primary and teriary links
    found to urls.txt

    Parameters
    ==========
    Takes no parameters

    Returns
    =======
    Returns nothing
    '''

    how_many = 50
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('{}urls.txt'.format(dir1), 'w') as f:
        f.write(str(data))
        f.close()


if __name__ == '__main__':
    main()
