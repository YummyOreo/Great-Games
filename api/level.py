import json

levelsCount = [100, 300, 600, 1000, 1500, 2100, 2850, 3850, 4000, 5900, 7500, 8050, 10000,
               15000, 30000, 55000, 70000, 95000, 100000, 110000, 122000, 145000, 159000, 200000, 250000]


def level(ctx):
    levels = json.load(open('./json/Levels.josn'))
    if levels[str(ctx.author.id)] >= levelsCount[0] and levels[str(ctx.author.id)] < levelsCount[1]:
        levelShow = 1
    elif levels[str(ctx.author.id)] >= levelsCount[1] and levels[str(ctx.author.id)] < levelsCount[2]:
        levelShow = 2
    elif levels[str(ctx.author.id)] >= levelsCount[2] and levels[str(ctx.author.id)] < levelsCount[3]:
        levelShow = 3
    elif levels[str(ctx.author.id)] >= levelsCount[3] and levels[str(ctx.author.id)] < levelsCount[4]:
        levelShow = 4
    elif levels[str(ctx.author.id)] >= levelsCount[4] and levels[str(ctx.author.id)] < levelsCount[5]:
        levelShow = 5
    elif levels[str(ctx.author.id)] >= levelsCount[5] and levels[str(ctx.author.id)] < levelsCount[6]:
        levelShow = 6
    elif levels[str(ctx.author.id)] >= levelsCount[6] and levels[str(ctx.author.id)] < levelsCount[7]:
        levelShow = 7
    elif levels[str(ctx.author.id)] >= levelsCount[7] and levels[str(ctx.author.id)] < levelsCount[8]:
        levelShow = 8
    elif levels[str(ctx.author.id)] >= levelsCount[8] and levels[str(ctx.author.id)] < levelsCount[9]:
        levelShow = 9
    elif levels[str(ctx.author.id)] >= levelsCount[9] and levels[str(ctx.author.id)] < levelsCount[10]:
        levelShow = 10
    elif levels[str(ctx.author.id)] >= levelsCount[10] and levels[str(ctx.author.id)] < levelsCount[11]:
        levelShow = 11
    elif levels[str(ctx.author.id)] >= levelsCount[11] and levels[str(ctx.author.id)] < levelsCount[12]:
        levelShow = 12
    elif levels[str(ctx.author.id)] >= levelsCount[12] and levels[str(ctx.author.id)] < levelsCount[13]:
        levelShow = 13
    elif levels[str(ctx.author.id)] >= levelsCount[13] and levels[str(ctx.author.id)] < levelsCount[14]:
        levelShow = 14
    elif levels[str(ctx.author.id)] >= levelsCount[14] and levels[str(ctx.author.id)] < levelsCount[15]:
        levelShow = 15
    elif levels[str(ctx.author.id)] >= levelsCount[15] and levels[str(ctx.author.id)] < levelsCount[16]:
        levelShow = 16
    elif levels[str(ctx.author.id)] >= levelsCount[16] and levels[str(ctx.author.id)] < levelsCount[17]:
        levelShow = 17
    elif levels[str(ctx.author.id)] >= levelsCount[17] and levels[str(ctx.author.id)] < levelsCount[18]:
        levelShow = 18
    elif levels[str(ctx.author.id)] >= levelsCount[18] and levels[str(ctx.author.id)] < levelsCount[19]:
        levelShow = 19
    elif levels[str(ctx.author.id)] >= levelsCount[19] and levels[str(ctx.author.id)] < levelsCount[10]:
        levelShow = 20
    elif levels[str(ctx.author.id)] >= levelsCount[10] and levels[str(ctx.author.id)] < levelsCount[20]:
        levelShow = 21
    elif levels[str(ctx.author.id)] < 99:
        levelShow = 0
    else:
        levelShow = 21

    return levelShow


def first(ctx, firstLevels):
    levels = json.load(open('./json/Levels.josn'))
    if levels[firstLevels] >= levelsCount[0] and levels[firstLevels] < levelsCount[1]:
        levelShow = 1
    elif levels[firstLevels] >= levelsCount[1] and levels[firstLevels] < levelsCount[2]:
        levelShow = 2
    elif levels[firstLevels] >= levelsCount[2] and levels[firstLevels] < levelsCount[3]:
        levelShow = 3
    elif levels[firstLevels] >= levelsCount[3] and levels[firstLevels] < levelsCount[4]:
        levelShow = 4
    elif levels[firstLevels] >= levelsCount[4] and levels[firstLevels] < levelsCount[5]:
        levelShow = 5
    elif levels[firstLevels] >= levelsCount[5] and levels[firstLevels] < levelsCount[6]:
        levelShow = 6
    elif levels[firstLevels] >= levelsCount[6] and levels[firstLevels] < levelsCount[7]:
        levelShow = 7
    elif levels[firstLevels] >= levelsCount[7] and levels[firstLevels] < levelsCount[8]:
        levelShow = 8
    elif levels[firstLevels] >= levelsCount[8] and levels[firstLevels] < levelsCount[9]:
        levelShow = 9
    elif levels[firstLevels] >= levelsCount[9] and levels[firstLevels] < levelsCount[10]:
        levelShow = 10
    elif levels[firstLevels] >= levelsCount[10] and levels[firstLevels] < levelsCount[11]:
        levelShow = 11
    elif levels[firstLevels] >= levelsCount[11] and levels[firstLevels] < levelsCount[12]:
        levelShow = 12
    elif levels[firstLevels] >= levelsCount[12] and levels[firstLevels] < levelsCount[13]:
        levelShow = 13
    elif levels[firstLevels] >= levelsCount[13] and levels[firstLevels] < levelsCount[14]:
        levelShow = 14
    elif levels[firstLevels] >= levelsCount[14] and levels[firstLevels] < levelsCount[15]:
        levelShow = 15
    elif levels[firstLevels] >= levelsCount[15] and levels[firstLevels] < levelsCount[16]:
        levelShow = 16
    elif levels[firstLevels] >= levelsCount[16] and levels[firstLevels] < levelsCount[17]:
        levelShow = 17
    elif levels[firstLevels] >= levelsCount[17] and levels[firstLevels] < levelsCount[18]:
        levelShow = 18
    elif levels[firstLevels] >= levelsCount[18] and levels[firstLevels] < levelsCount[19]:
        levelShow = 19
    elif levels[firstLevels] >= levelsCount[19] and levels[firstLevels] < levelsCount[10]:
        levelShow = 20
    elif levels[firstLevels] >= levelsCount[10] and levels[firstLevels] < levelsCount[20]:
        levelShow = 21
    elif levels[firstLevels] < 99:
        levelShow = 0
    else:
        levelShow = 21
    return levelShow


def api(levels, firstLevels):
    if levels[firstLevels] >= levelsCount[0] and levels[firstLevels] < levelsCount[1]:
        levelShow = 1
    elif levels[firstLevels] >= levelsCount[1] and levels[firstLevels] < levelsCount[2]:
        levelShow = 2
    elif levels[firstLevels] >= levelsCount[2] and levels[firstLevels] < levelsCount[3]:
        levelShow = 3
    elif levels[firstLevels] >= levelsCount[3] and levels[firstLevels] < levelsCount[4]:
        levelShow = 4
    elif levels[firstLevels] >= levelsCount[4] and levels[firstLevels] < levelsCount[5]:
        levelShow = 5
    elif levels[firstLevels] >= levelsCount[5] and levels[firstLevels] < levelsCount[6]:
        levelShow = 6
    elif levels[firstLevels] >= levelsCount[6] and levels[firstLevels] < levelsCount[7]:
        levelShow = 7
    elif levels[firstLevels] >= levelsCount[7] and levels[firstLevels] < levelsCount[8]:
        levelShow = 8
    elif levels[firstLevels] >= levelsCount[8] and levels[firstLevels] < levelsCount[9]:
        levelShow = 9
    elif levels[firstLevels] >= levelsCount[9] and levels[firstLevels] < levelsCount[10]:
        levelShow = 10
    elif levels[firstLevels] >= levelsCount[10] and levels[firstLevels] < levelsCount[11]:
        levelShow = 11
    elif levels[firstLevels] >= levelsCount[11] and levels[firstLevels] < levelsCount[12]:
        levelShow = 12
    elif levels[firstLevels] >= levelsCount[12] and levels[firstLevels] < levelsCount[13]:
        levelShow = 13
    elif levels[firstLevels] >= levelsCount[13] and levels[firstLevels] < levelsCount[14]:
        levelShow = 14
    elif levels[firstLevels] >= levelsCount[14] and levels[firstLevels] < levelsCount[15]:
        levelShow = 15
    elif levels[firstLevels] >= levelsCount[15] and levels[firstLevels] < levelsCount[16]:
        levelShow = 16
    elif levels[firstLevels] >= levelsCount[16] and levels[firstLevels] < levelsCount[17]:
        levelShow = 17
    elif levels[firstLevels] >= levelsCount[17] and levels[firstLevels] < levelsCount[18]:
        levelShow = 18
    elif levels[firstLevels] >= levelsCount[18] and levels[firstLevels] < levelsCount[19]:
        levelShow = 19
    elif levels[firstLevels] >= levelsCount[19] and levels[firstLevels] < levelsCount[10]:
        levelShow = 20
    elif levels[firstLevels] >= levelsCount[10] and levels[firstLevels] < levelsCount[20]:
        levelShow = 21
    elif levels[firstLevels] < 99:
        levelShow = 0
    else:
        levelShow = 21
    return levelShow
