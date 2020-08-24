*** Settings  ***
Library    keywords.keyword.Kw     #类名与库的名称一致，python中的module,即模块与库 表示的是同一类
Library    keywords.keyword.Kw.ClsWithDifName     #类名与库的名称一致，python中的module,即模块与库 表示的是同一类

*** Test Cases ***
测试用例1
    [Tags]     模板
    [Documentation]    模块中使用同名的类

    ${resp} =    Create github repo    zmy
    Log to Console    ${resp}
    ${result} =    Get github repo
    Log to Console    ${result}
测试用例2
    [tags]    模板
    [Documentation]    模块名和类型不一致
    ${rsp} =     delete github repo    zmy
    Log to Console    ${rsp}
