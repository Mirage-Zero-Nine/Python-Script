__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import re
import requests
import json
import operator

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
    'Referer': 'https://www.v2ex.com/signin',
    'Origin': 'https://www.www.v2ex.com'
}


def nba():
    # Create session
    sessionNBA = requests.Session()
    # Update header
    sessionNBA.headers.update(headers)
    # Obtain toady's game schedule
    nbaRespond = sessionNBA.get('http://sports1.sina.cn/nba/schedule?vt=4&pos=113')
    # Obtain teams name
    findTeam = re.findall(r"(?<=nba&match_id=\d{10}\'>)[\u4e00-\u9fa5]+(?=<\/a>)", nbaRespond.text)
    # Obtain team's score
    findScore = re.findall(r'\d+(?=<\/span><\/p>)', nbaRespond.text)
    # Count team sum
    teamNum = 0
    # Count score sum
    scoreNum = 0
    # Set a dictionary to stash player's score
    scoreDic = {}
    # Obtain player statistics
    statisticsUrl = re.findall(r'http://sports1\.sina\.cn/nba/boxscore\?matchid=\d+', nbaRespond.text)
    # Control the index of statistics
    statisticsNum = 0
    if findScore == []:
        # Exception
        print('Today\'s matches do not start yet!')
    else:
        while scoreNum < len(findScore):
            teamNum1 = teamNum + 1
            findScore1 = scoreNum + 1
            print(findTeam[teamNum], findScore[scoreNum], ':', findScore[findScore1], findTeam[teamNum1])
            teamNum += 2
            scoreNum += 2
            statistics = sessionNBA.get(str(statisticsUrl[statisticsNum]))
            score = re.findall(r'(?<=<li><p>得分).+(?=<\/p><\/li>)', statistics.text)
            scoreTeam1 = re.findall(r'\d+', str(score[0]))
            scoreTeam2 = re.findall(r'\d+', str(score[1]))
            mainName = re.findall(r'(?<=class="cur">).+(?=</a></p>)', statistics.text)
            subName = re.findall(r'(?<=vt=4" class="">).+(?=</a><\/p>)', statistics.text)
            while len(scoreTeam2) - 5 > 0:
                name = subName.pop()
                score = scoreTeam2.pop()
                scoreDic[name] = int(score)
            while len(scoreTeam1) - 5 > 0:
                name = subName.pop()
                score = scoreTeam1.pop()
                scoreDic[name] = int(score)
            scoreTeam = scoreTeam1 + scoreTeam2
            while len(scoreTeam) > 0:
                name = mainName.pop()
                score = scoreTeam.pop()
                scoreDic[name] = int(score)
            # sortResult Type: List
            sortResult = sorted(scoreDic.items(), key=operator.itemgetter(1), reverse=True)
            result, playerScore = re.findall(r'[\u4e00-\u9fa5]+', str(sortResult[0])), re.findall(r'\d+', str(sortResult[0]))
            print('Highest Score Player: %s: %s pts. \n' % (str(result[0]), str(playerScore[0])))
            scoreDic = {}
            statisticsNum += 1
            
            
if __name__ == '__main__':
	nba()