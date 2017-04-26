__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import re
import requests
import operator

def espnNBA():
    headersiPad = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Referer': 'http://www.espn.com/nba/schedule',
    }
    headersMac = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
        'Referer': 'http://www.espn.com/nba/schedule',
    }
    headersiPhone = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Referer': 'http://www.espn.com/nba/schedule',
    }
    # Create session
    sessionNBA = requests.Session()
    # Update header
    sessionNBA.headers.update(headersMac)
    html = sessionNBA.get('http://www.espn.com/nba/schedule')
    soup = BeautifulSoup(html.text, "html.parser")
    tag = str(soup.find_all('td'))
    tag = tag.replace('</a>', ',')
    tag_home = str(soup.find_all('a'))
    home = re.findall(r'(?<=&amp;lpos=nba:schedule:team"><span>)[A-Za-z ]+(?=</span> <abbr)', str(tag_home))
    match_game = re.findall(r'(?<=nba:schedule:score">)[A-Za-z0-9 ,]+(?=</td>)', tag)
    match_player_score = re.findall(r'(?<=player">)[A-Za-z0-9 ,]+(?=</td>)', tag)
    n = 0
    m = 1
    for i in match_game:
        match_team = re.findall(r'\w+ \d+', str(i))
        print('%s : %s\nHome Team: %s\nWinner High: %s\nLoser High: %s\n' % (
        str(match_team[0]), str(match_team[1]), str(home[m]), str(match_player_score[n]),
        str(match_player_score[n + 1])))
        n += 2
        m += 2

if __name__ == '__main__':
    espnNBA()
