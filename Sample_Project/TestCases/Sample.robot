*** Settings ***
Library    SeleniumLibrary
Library    String
Library    Collections
Library    OperatingSystem
Resource   ../Resources/Common.robot
Library    Playwright


Test Setup    Create Screenshot Folder
Test Teardown    Test Teardown Activities for dry run
Suite Teardown    Close all browsers

*** Variables ***
title = '//h1[text()="<<<>>>"]'
text_xpath = '//td[text()="<<<>>>"]'
submit_xpath = '//input[@value="<<<>>>"]'

*** Test Cases ***
TC01_Sample TC01
    [Documentation]    This is for the first TC01
    [Tags]    Sample
    open browser    https://demoqa.com/automation-practice-form      Chrome
    maximize browser window
    set browser implicit wait      5
    CAPTURE PAGE SCREENSHOT
    execute javascript    window.scrollTo(0,150)
    page should contain dynamic element     ${title}     Practice Form


TC02_Sample TC02
    [Documentation]    This is for the first TC01
    [Tags]    Helium
    open browser    https://demo.guru99.com/      Chrome
    maximize browser window
    set browser implicit wait      5
    CAPTURE PAGE SCREENSHOT
    find element    //input
    page should contain dynamic element     ${text_xpath}     Email ID
    sleep    5
    page should contain dynamic element    ${submit_xpath}    Submits
    Input Dynamic Text    ${text_xpath}     Email ID    aaa@gmail.com
    Click Dynamic Element    ${submit_xpath}    Submits

*** Keywords ***
First Action
    page should contain element