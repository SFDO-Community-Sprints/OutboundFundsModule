*** Settings ***
Documentation   Create a new Contact via API and UI.
Resource        robot/OutboundFunds/resources/OutboundFunds.robot
Library         cumulusci.robotframework.PageObjects
...             robot/OutboundFunds/resources/ContactPageObject.py
Suite Setup     Open Test Browser
Suite Teardown  Delete Records and Close Browser

*** Test Cases ***

Via API
    ${first_name} =       Generate Random String
    ${last_name} =        Generate Random String
    ${contact_id} =       Salesforce Insert  Contact
    ...                     FirstName=${first_name}
    ...                     LastName=${last_name}

    &{contact} =          Salesforce Get  Contact  ${contact_id}
    Validate Contact      ${contact_id}  ${first_name}  ${last_name}

Via UI
    ${first_name} =       Generate Random String
    ${last_name} =        Generate Random String

    Go To Page            Home  Contact
    Click Object Button   New
    Wait For Modal        New  Contact

    Populate Form
    ...                   First Name=${first_name}
    ...                   Last Name=${last_name}
    Click Modal Button    Save

    Wait Until Modal Is Closed

    ${contact_id} =       Get Current Record Id
    Store Session Record  Contact  ${contact_id}
    Validate Contact      ${contact_id}  ${first_name}  ${last_name}


*** Keywords ***

Validate Contact
    [Arguments]          ${contact_id}  ${first_name}  ${last_name}
    [Documentation]
    ...  Given a contact id, validate that the contact has the
    ...  expected first and last name both through the detail page in
    ...  the UI and via the API.

    # Validate via UI
    Go To Page            Detail   Contact  ${contact_id}
    Page Should Contain    ${first_name} ${last_name}

    # Validate via API
    &{contact} =     Salesforce Get  Contact  ${contact_id}
    Should Be Equal  ${first_name}  ${contact}[FirstName]
    Should Be Equal  ${last_name}  ${contact}[LastName]
    Should Be Equal  ${first_name}  ${contact}[FirstName]
    Should Be Equal  ${last_name}  ${contact}[LastName]
