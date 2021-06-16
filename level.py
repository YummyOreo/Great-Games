import json

levelsCount = [100, 300, 600, 1000, 1500, 2100, 2850, 3850, 4000, 5900, 7500, 8050, 10000,
               15000, 30000, 55000, 70000, 95000, 100000, 110000, 122000, 145000, 159000, 200000, 250000, 400000, 800000, 1300000, 1750000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]


def api(levels):
    if levels >= levelsCount[0] and levels < levelsCount[1]:
        levelShow = 1
    elif levels >= levelsCount[1] and levels < levelsCount[2]:
        levelShow = 2
    elif levels >= levelsCount[2] and levels < levelsCount[3]:
        levelShow = 3
    elif levels >= levelsCount[3] and levels < levelsCount[4]:
        levelShow = 4
    elif levels >= levelsCount[4] and levels < levelsCount[5]:
        levelShow = 5
    elif levels >= levelsCount[5] and levels < levelsCount[6]:
        levelShow = 6
    elif levels >= levelsCount[6] and levels < levelsCount[7]:
        levelShow = 7
    elif levels >= levelsCount[7] and levels < levelsCount[8]:
        levelShow = 8
    elif levels >= levelsCount[8] and levels < levelsCount[9]:
        levelShow = 9
    elif levels >= levelsCount[9] and levels < levelsCount[10]:
        levelShow = 10
    elif levels >= levelsCount[10] and levels < levelsCount[11]:
        levelShow = 11
    elif levels >= levelsCount[11] and levels < levelsCount[12]:
        levelShow = 12
    elif levels >= levelsCount[12] and levels < levelsCount[13]:
        levelShow = 13
    elif levels >= levelsCount[13] and levels < levelsCount[14]:
        levelShow = 14
    elif levels >= levelsCount[14] and levels < levelsCount[15]:
        levelShow = 15
    elif levels >= levelsCount[15] and levels < levelsCount[16]:
        levelShow = 16
    elif levels >= levelsCount[16] and levels < levelsCount[17]:
        levelShow = 17
    elif levels >= levelsCount[17] and levels < levelsCount[18]:
        levelShow = 18
    elif levels >= levelsCount[18] and levels < levelsCount[19]:
        levelShow = 19
    elif levels >= levelsCount[19] and levels < levelsCount[20]:
        levelShow = 20
    elif levels >= levelsCount[20] and levels < levelsCount[21]:
        levelShow = 21
    elif levels >= levelsCount[21] and levels < levelsCount[22]:
        levelShow = 22
    elif levels >= levelsCount[21] and levels < levelsCount[23]:
        levelShow = 23
    elif levels >= levelsCount[23] and levels < levelsCount[24]:
        levelShow = 24
    elif levels >= levelsCount[24] and levels < levelsCount[25]:
        levelShow = 25
    elif levels < 99:
        levelShow = 0
    else:
        levelShow = 25
    return levelShow
