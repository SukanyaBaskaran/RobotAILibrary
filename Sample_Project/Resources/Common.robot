*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String
Library    Collections

*** Keywords ***
Create Screenshot Folder
    [Documentation]    Creates folder for Screenshots
    BuiltIn.run keywords    remove directory    ${EXECDIR}/AutomationResults/${TEST_NAME}    recursive=True
    ...    AND    create directory    ${EXECDIR}/AutomationResults/${TEST_NAME}
    ...    AND    set global variable    ${Screenshot_Folder}    ${EXECDIR}/AutomationResults/${TEST_NAME}
    ...    AND    set screenshot directory    ${Screenshot_Folder}

Click Dynamic Element
    [Arguments]    ${Obj}   ${Replace_Value}
    ${dynobj}=    replace string    ${Obj}    <<<>>>    ${Replace_Value}
    click element    ${dynobj}

Input Dynamic Text
    [Arguments]    ${Obj}   ${Replace_Value}  ${Value}
    ${dynobj}=    replace string    ${Obj}    <<<>>>    ${Replace_Value}
    input text    ${dynobj}  ${Value}

page should contain dynamic element
    [Arguments]    ${Obj}   ${Replace_Value}
    ${dynobj}=    replace string    ${Obj}    <<<>>>    ${Replace_Value}
    ${exist}=    run keyword and return status    page should contain element   ${dynobj}
    IF  '${exist}'=='True'
        Highlight Element      ${dynobj}
        page should contain element    ${dynobj}
    ELSE
        ${Elements}=    SeleniumLibrary.find elements    //input
        FOR    ${i}    IN    ${Elements}:
             ${exist}=    run keyword and return status    page should contain element   ${dynobj}
             IF  '${exist}'=='True'
                 Highlight Element      ${i}
                 page should contain element    ${i}
             ELSE
                continue for loop
             END
        END
    END


#    ${healed_element}=    Evaluate    Helenium.Heal Locator    ${dynobj}    # Helium healing step


Highlight Element
    [Arguments]    ${dynobj}
    BuiltIn.run keywords    execute javascript   var element = document.evaluate("${dynobj}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) { element.style.background='yellow'; element.style.border='3px solid red'; }
    ...    AND    capture page screenshot
    ...    AND    Add Subtitle    ${dynobj}
    ...    AND    execute javascript    var element = document.evaluate("${dynobj}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) { element.style.border=''; }

Add Subtitle
    [Arguments]    ${dynobj}
    ${Count}=    count files in directory    ${Screenshot_Folder}    0-selenium-screenshot-*.png

Test Teardown Activities for dry run
    run keyword if test passed    Add Details
    run keyword if test failed    Add screenshot to report
#    Get Browser Console Log Entries
#    close browser

Add Details
    set test message    This Execution is completed Successfully

Add screenshot to report
    run keyword    Capture Page Screenshot Util

Capture Page Screenshot Util
    ${index}=    count files in directory    ${Screenshot_Folder}
    ${temp}    evaluate    ${index} + 1
    capture page screenshot    selenium-screenshot-${temp}.png

Get Browser Console Log Entries
    ${selenium}=    get library instance    SeleniumLibrary
    ${webdriver}=    set variable   ${selenium._drivers.active_drivers}[0]
    ${log entries}=  evaluate    $webdriver.get_log('browser')
    @{listvalue}=    convert to list    ${log entries}
    FOR    ${index}    IN    @{listvalue}
        log    ${index}
    END
