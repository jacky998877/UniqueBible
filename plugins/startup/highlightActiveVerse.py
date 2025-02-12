import config, re

terminalTextStart = "「Back.{0}」「Fore.{1}」".format(config.terminalVerseSelectionBackground, config.terminalVerseSelectionForeground) if config.runMode == "terminal" else ""
terminalTextEnd = "「Style.RESET_ALL」" if config.runMode == "terminal" else ""

def highlightActiveVerseMain(text):
    colour = config.darkThemeActiveVerseColor if config.theme in ("dark", "night") else config.lightThemeActiveVerseColor
    searchReplace = (
        # underline
        #('(<vid id="v{0}\.{1}\.{2}".*?</vid>)(.*?)</verse>'.format(config.mainB, config.mainC, config.mainV), r"\1<u>\2</u></verse>"),
        # color
        ("(<span id='s{0}\.{1}\.{2}'.*?>)(.*?)</span>".format(config.mainB, config.mainC, config.mainV), r"\1<span style='color: {0};'>{1}\2{2}</span></span>".format(colour, terminalTextStart, terminalTextEnd)),
        ('(<vid id="v{0}\.{1}\.{2}".*?</vid>)(.*?)</verse>'.format(config.mainB, config.mainC, config.mainV), r"\1<span style='color: {0};'>{1}\2{2}</span></verse>".format(colour, terminalTextStart, terminalTextEnd)),
        (r"""(document\.title="_menu:::)([^<>]+?)(\.{0}\.{1}\.{2}"'>\2</ref>\)</sup></td><td><bibletext class='\2'>)(.*?)</bibletext>""".format(config.mainB, config.mainC, config.mainV), r"\1\2\3<span style='color: {0};'>{1}\4{2}</span></bibletext>".format(colour, terminalTextStart, terminalTextEnd)),
    )
    for search, replace in searchReplace:
        text = re.sub(search, replace, text)
    return text

def highlightActiveVerseStudy(text):
    colour = config.darkThemeActiveVerseColor if config.theme in ("dark", "night") else config.lightThemeActiveVerseColor
    searchReplace = (
        # underline
        #('(<vid id="v{0}\.{1}\.{2}".*?</vid>)(.*?)</verse>'.format(config.studyB, config.studyC, config.studyV), r"\1<u>\2</u></verse>"),
        # color
        ("(<span id='s{0}\.{1}\.{2}'.*?>)(.*?)</span>".format(config.studyB, config.studyC, config.studyV), r"\1<span style='color: {0};'>{1}\2{2}</span></span>".format(colour, terminalTextStart, terminalTextEnd)),
        ('(<vid id="v{0}\.{1}\.{2}".*?</vid>)(.*?)</verse>'.format(config.studyB, config.studyC, config.studyV), r"\1<span style='color: {0};'>{1}\2{2}</span></verse>".format(colour, terminalTextStart, terminalTextEnd)),
    )
    for search, replace in searchReplace:
        text = re.sub(search, replace, text)
    return text

config.bibleWindowContentTransformers.append(highlightActiveVerseMain)
config.studyWindowContentTransformers.append(highlightActiveVerseStudy)
