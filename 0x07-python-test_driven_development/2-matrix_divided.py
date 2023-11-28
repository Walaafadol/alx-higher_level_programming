{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x07-python-test_driven_development":{"items":[{"name":"tests","path":"0x07-python-test_driven_development/tests","contentType":"directory"},{"name":"0-add_integer.py","path":"0x07-python-test_driven_development/0-add_integer.py","contentType":"file"},{"name":"100-matrix_mul.py","path":"0x07-python-test_driven_development/100-matrix_mul.py","contentType":"file"},{"name":"101-lazy_matrix_mul.py","path":"0x07-python-test_driven_development/101-lazy_matrix_mul.py","contentType":"file"},{"name":"102-python.c","path":"0x07-python-test_driven_development/102-python.c","contentType":"file"},{"name":"2-matrix_divided.py","path":"0x07-python-test_driven_development/2-matrix_divided.py","contentType":"file"},{"name":"3-say_my_name.py","path":"0x07-python-test_driven_development/3-say_my_name.py","contentType":"file"},{"name":"4-print_square.py","path":"0x07-python-test_driven_development/4-print_square.py","contentType":"file"},{"name":"5-text_indentation.py","path":"0x07-python-test_driven_development/5-text_indentation.py","contentType":"file"}],"totalCount":9},"":{"items":[{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x17 C - Doubly linked lists","path":"0x17 C - Doubly linked lists","contentType":"directory"},{"name":"0x18 C - Dynamic libraries","path":"0x18 C - Dynamic libraries","contentType":"directory"},{"name":"100-realloc.c","path":"100-realloc.c","contentType":"file"},{"name":"101-mul.c","path":"101-mul.c","contentType":"file"},{"name":"101-password","path":"101-password","contentType":"file"},{"name":"2-calloc.c","path":"2-calloc.c","contentType":"file"},{"name":"3-array_range.c","path":"3-array_range.c","contentType":"file"},{"name":"_putchar.c","path":"_putchar.c","contentType":"file"},{"name":"main.h","path":"main.h","contentType":"file"}],"totalCount":12}},"fileTreeProcessingTime":7.389501,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":627534744,"defaultBranch":"main","name":"alx","ownerLogin":"sadatmisr","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-04-13T17:04:55.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/130691074?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1695082556.0","canEdit":false,"refType":"branch","currentOid":"907071687d98b6e848fd75176358115c4081617f"},"path":"0x07-python-test_driven_development/2-matrix_divided.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"Module for matrix_divided method.\"\"\"","","","def matrix_divided(matrix, div):","    \"\"\"Divides all elements of matrix by div.","    Args:","        matrix: List of lists containing int or float","        div: number to divide matrix by","    Returns:","        list: List of lists representing divided matrix.","    Raises:","        TypeError: If matrix is not list of lists containing int or float.","        TypeError: If sublists are not all same size.","        TypeError: If div is not int or float.","        ZeroDivisionError: If div is zero.","    \"\"\"","    if not isinstance(div, (int, float)):","        raise TypeError(\"div must be a number\")","    if not isinstance(matrix, list) or len(matrix) == 0:","        raise TypeError(\"matrix must be a matrix (list of lists) \" +","                        \"of integers/floats\")","    for row in matrix:","        if not isinstance(row, list) or len(row) == 0:","            raise TypeError(\"matrix must be a matrix (list of lists) \" +","                            \"of integers/floats\")","        if len(row) != len(matrix[0]):","            raise TypeError(\"Each row of the matrix must have the same size\")","        for x in row:","            if not isinstance(x, (int, float)):","                raise TypeError(\"matrix must be a matrix (list of lists) \" +","                                \"of integers/floats\")","    return [[round(x / div, 2) for x in row] for row in matrix]","","if __name__ == \"__main__\":","    import doctest","    doctest.testfile(\"tests/2-matrix_divided.txt\")"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":39,"cssClass":"pl-s"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":18,"cssClass":"pl-en"},{"start":19,"end":25,"cssClass":"pl-s1"},{"start":27,"end":30,"cssClass":"pl-s1"}],[{"start":4,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":9,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":39,"cssClass":"pl-s"}],[{"start":0,"end":12,"cssClass":"pl-s"}],[{"start":0,"end":56,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":74,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":46,"cssClass":"pl-s"}],[{"start":0,"end":42,"cssClass":"pl-s"}],[{"start":0,"end":7,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-c1"},{"start":11,"end":21,"cssClass":"pl-en"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":28,"end":31,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-k"},{"start":14,"end":23,"cssClass":"pl-v"},{"start":24,"end":46,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-c1"},{"start":11,"end":21,"cssClass":"pl-en"},{"start":22,"end":28,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":42,"cssClass":"pl-en"},{"start":43,"end":49,"cssClass":"pl-s1"},{"start":51,"end":53,"cssClass":"pl-c1"},{"start":54,"end":55,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-k"},{"start":14,"end":23,"cssClass":"pl-v"},{"start":24,"end":66,"cssClass":"pl-s"},{"start":67,"end":68,"cssClass":"pl-c1"}],[{"start":24,"end":44,"cssClass":"pl-s"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":37,"end":39,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-en"},{"start":44,"end":47,"cssClass":"pl-s1"},{"start":49,"end":51,"cssClass":"pl-c1"},{"start":52,"end":53,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":70,"cssClass":"pl-s"},{"start":71,"end":72,"cssClass":"pl-c1"}],[{"start":28,"end":48,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-en"},{"start":15,"end":18,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":26,"cssClass":"pl-en"},{"start":27,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":76,"cssClass":"pl-s"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":18,"cssClass":"pl-c1"},{"start":19,"end":29,"cssClass":"pl-en"},{"start":30,"end":31,"cssClass":"pl-s1"},{"start":34,"end":37,"cssClass":"pl-s1"},{"start":39,"end":44,"cssClass":"pl-s1"}],[{"start":16,"end":21,"cssClass":"pl-k"},{"start":22,"end":31,"cssClass":"pl-v"},{"start":32,"end":74,"cssClass":"pl-s"},{"start":75,"end":76,"cssClass":"pl-c1"}],[{"start":32,"end":52,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":31,"end":34,"cssClass":"pl-k"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":37,"end":39,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-s1"},{"start":45,"end":48,"cssClass":"pl-k"},{"start":49,"end":52,"cssClass":"pl-s1"},{"start":53,"end":55,"cssClass":"pl-c1"},{"start":56,"end":62,"cssClass":"pl-s1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":18,"cssClass":"pl-s1"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":20,"cssClass":"pl-en"},{"start":21,"end":49,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/sadatmisr/alx/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/sadatmisr/alx/security/dependabot","repoSecurityAndAnalysisPath":"/sadatmisr/alx/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"2-matrix_divided.py","displayUrl":"https://github.com/sadatmisr/alx/blob/main/0x07-python-test_driven_development/2-matrix_divided.py?raw=true","headerInfo":{"blobSize":"1.46 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"43ac34e","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsadatmisr%2Falx%2Fblob%2Fmain%2F0x07-python-test_driven_development%2F2-matrix_divided.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"37","truncatedSloc":"34"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/sadatmisr/alx/discussions/new","newIssuePath":"/sadatmisr/alx/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/sadatmisr/alx/blob/main/0x07-python-test_driven_development/2-matrix_divided.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/sadatmisr/alx/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/sadatmisr/alx/raw/main/0x07-python-test_driven_development/2-matrix_divided.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"sadatmisr","repoName":"alx","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"matrix_divided","kind":"function","identStart":65,"identEnd":79,"extentStart":61,"extentEnd":1397,"fullyQualifiedName":"matrix_divided","identUtf16":{"start":{"lineNumber":4,"utf16Col":4},"end":{"lineNumber":4,"utf16Col":18}},"extentUtf16":{"start":{"lineNumber":4,"utf16Col":0},"end":{"lineNumber":32,"utf16Col":63}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/sadatmisr/alx/branches":{"post":"wcGo44H0Vd2v3uW5R2ueOze69BY28ezlCGw0yWYgq-OFFDXzfEOoGiHDC5rDNmTP79wBKjGhJ4bssxLbAmAEbg"},"/repos/preferences":{"post":"ZaWl7EgX0k2Ceqri-zjDMcHpfnCgSGIjc29s_ICJRg4dF0MeSDl8hDveIDTP1_4cBufcaek8D75DTFTpq2gXDw"}}},"title":"alx/0x07-python-test_driven_development/2-matrix_divided.py at main · sadatmisr/alx"}