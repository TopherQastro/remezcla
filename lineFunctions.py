
import globalFunctions as gF

def veto(qAnteLine, proxExpress):  #  Resets values in a line to
    print(gF.lineno(), 'veto() | qAnteLine:', qAnteLine)
    runLine = ([],[])
    for each in qAnteLine[0]:  #  Re-create any qAnteLinegF.superPopList, qLine, gF.qLineIndexList, proxDicIndexList as a mutable variable
        runLine[0].append(each)
    for each in qAnteLine[1]:  #  Re-create any qAnteLinegF.superPopList, qLine, gF.qLineIndexList, proxDicIndexList as a mutable variable
        runLine[1].append(each)
    for mList in gF.superList:
        while len(mList) > 0:
            mList.pop()
    gF.printGlobalData(([],[]))
    return ([],[]), runLine, [], False
          #qLine, qAnteLine, pLEmps, killSwitch


def removeWordL(superPopList, qLine):  #  Remove the leftmost word from line
    # do something
    return data


def removeWordR(empLine, qLine, runLine):  #  Remove the rightmost word from line
    print(gF.lineno(), 'removeWordR-in', 'qLine:', qLine, 'runLine:', runLine)
    if len(qLine[0]) == 0 and len(runLine[0]) > 0:  #  Cut runLine
        print(gF.lineno(), "rMR - if0")
        minusWordX = runLine[0].pop(0)  #  Since the previous line didn't yield any following line
        minusWordY = runLine[1].pop(0)  #  minusWordX just holds whatever is getting popped
    if len(qLine[0]) > 0:
        print(gF.lineno(), "rMR - if1")
        minusWord0 = qLine[0].pop()  #  Remove word from first part of line
        minusWord1 = qLine[1].pop()  #  Until better method introduced, cut rLine here
        pWEmps = gF.pEmpsLine(empLine, [minusWord0])
        pLEmps = gF.pEmpsLine(empLine, qLine[0])
        pLEmps = pLEmps[:-len(pWEmps)]  #  Cut emps from main line)
        gF.superBlackList.pop()  #  If we leave blacklisted words further down the road, they may negate an otherwise compatible sentence
        print(gF.lineno(), 'minusWord0:', minusWord0)
        gF.superBlackList[-1].append(minusWord0)  #  Add to blackList at correct point
    else:
        pLEmps = []
    #if len(gF.superPopList) > (len(qLine[1]) + 1):  #  If we've gone further than checking the list of next words
    print('liF:', gF.lineno(), '| rMR - snipPopList')
    for mList in gF.superList:
        if len(mList) > 0:
            mList.pop()
        elif len(qLine[1]) > 0:
            print('liF:', gF.lineno(), '|', qLine)
            gF.printGlobalData(qLine)
    print(gF.lineno(), 'removeWordR-out', qLine)
    gF.printGlobalData(qLine)
    return pLEmps, qLine, runLine


def acceptWordL(qLine, nextWord):  #  Add the rightmost word to line

##  INVERT THESE VALUES

    print('acceptWord:', qLine, '|', nextWord)
    pLine.append(nextWord)
    if len(proxNumList) > 0:
        proxNum = proxNumList[-1] + 1
    else:
        proxNum = 0
    proxNumList.append(proxNum)
    proxLineNum = proxLineNumList[0] + 1
    proxLineNumList.insert(0, proxLineNum)
    return qLine


def acceptWordR(empLine, qLine, runLine, nextWord):  #  Add word to right side of line
    print('liF:', gF.lineno(), '| acceptWordR-in:', runLine, qLine, '|', nextWord)
    for each in nextWord[0]:
        qLine[0].append(each)
    for each in nextWord[1]:
        qLine[1].append(each)
    #gF.proxFunk.proxDataBuilder(gF.qLineIndexList, proxDicIndexList, qLine, len(qLine[1]))
    #if len(gF.superBlackList) == len(qLine[1]):  #  We don't have any blackListed words that far ahead
    gF.superBlackList.append([])
    gF.qLineIndexList.append([])
    gF.proxDicIndexList.append([])
    gF.proxFunk.proxDataBuilder((runLine[0]+qLine[0], runLine[1]+qLine[1]), len(runLine[1]+qLine[1]))
    qLine, runLine = gF.popFunk.superPopListMaker(empLine, [], qLine, runLine)
    print('liF:', gF.lineno(), '| acceptWordR-out:', qLine, '|', nextWord, gF.qLineIndexList, gF.proxDicIndexList)
    return qLine


def gov(empLine, rhymeThisLine, rhymeList, qAnteLine):
    print(gF.lineno(), 'lineGovernor start', rhymeThisLine)
    qLine, qAnteLine, pLEmps, killSwitch = veto(qAnteLine, [])  #  Start with empty variables declared. This function is also a reset button if lines are to be scrapped.
    proxExpress = []
    if rhymeThisLine == True:
        print(gF.lineno(), 'len(rhymeList):', len(rhymeList))
        if (len(rhymeList) > 0):  #  This dictates whether stanzaGovernor sent a rhyming line. An empty line indicates metered-only, or else it would've been a nonzero population
            proxExpress = []
            for rhymers in rhymeList:  #  Find words that come before rhymeWords, so you direct it towards that one
                try:
                    for words in gF.proxMinusLista[:len(empLine)]:  #  Only go as far as the empLine, as if all words are one-syllable long
                        thisProxList = words[rhymers]
                        for proxWord in thisProxList:
                            if proxWord not in proxExpress and proxWord not in quantumList:
                                proxExpress.append(proxWord)
                except KeyError:
                    continue
            print(gF.lineno(), 'len(proxExpress):', len(proxExpress))
            qLine, killSwitch = rhymeLiner(empLine, proxExpress, rhymeList, qAnteLine)
        else:
            print(gF.lineno(), 'no rhymes')
            return [], ([],[]), True  #  usedList, qLine, killSwitch
    elif gF.metSwitch == True:  #  If metSwitch is off, then we wouldn't have either rhyme or meter
        print(gF.lineno(), 'lineGov - gF.meterLineFunk.gov activate')
        qLine, killSwitch = gF.meterLineFunk.gov(empLine, [[], []], [], qAnteLine, proxExpress)
                                              #  empLine, qLine, pLEmps, runLine, proxExpress
    else:
        print(gF.lineno(), 'lineGov - plainLiner activate')
        qLine, killSwitch = plainLinerLtoR(empLine, qAnteLine)
    if killSwitch == True:
        print(gF.lineno(), 'lineGov - killSwitch')
        qLine, qAnteLine, pLEmps, killSwitch = veto(qAnteLine, [])
        return qLine, True
    else:
        print(gF.lineno(), 'lineGov - last else', qLine)
        return qLine, False  #  usedList, qLine, killSwitch