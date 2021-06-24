# Summer '21 locators
outboundfunds_lex_locators = {
    "app_launcher": {
        "view_all_button": "//button[text()='View All']",
        "app_link": "//p[contains(@title,'{}')]",
        "app_link_search_result": "//mark[contains(text(),'{}')]",
        "search_input": "//input[contains(@placeholder,'Search apps or items...')]",
    },
    "new_record": {
        "label": "//label[text()='{}']",
        "title": "//h2[contains(@class, 'inlineTitle') and text()='{}']",
        "field_label": "//div[./*/*[text()='{}']]",
        "edit_title": "//h2[contains(@class, 'title') and text()='{}']",
        "list": "//div[contains(@class,'forcePageBlockSectionRow')]/div[contains(@class,'forcePageBlockItem')]/div[contains(@class,'slds-hint-parent')]/div[@class='slds-form-element__control']/div[.//span[text()='{}']][//div[contains(@class,'uiMenu')]//a[@class='select']]",
        "text_field": "//div[contains(@class, 'uiInput')][.//label[contains(@class, 'uiLabel')][.//span[text()='{}']]]//*[self::input or self::textarea]",
        "flexipage-list": '//lightning-combobox[./label[text()="{}"]]//input[contains(@class,"combobox__input")]',
        "dd_selection": "//lightning-base-combobox-item[@data-value='{}']",
        "button": "//button[contains(@class, 'slds-button')  and text()='{}']",
        "lookup_field": "//div[contains(@class, 'autocompleteWrapper')]//input[@title='{}']",
        "lightning_lookup": "//label[text()='{}']/following-sibling::div//input",
        "lookup_value": "//div[contains(@class, 'listContent')]//div[contains(@class, 'slds-truncate') and @title='{}']",
        "checkbox": "//div[contains(@class,'uiInputCheckbox')]/label/span[text()='{}']/../following-sibling::input[@type='checkbox']",
        "field_input": '//label[text()="{}"]/following-sibling::div//*[self::input or self::textarea]',
        "open_date_picker": "//div[@class='slds-form-element__control']/div[.//span[text()='{}']]//div//a[contains(@class,'datePicker-openIcon display')]",
        "datepicker_popup": "//table[@class='calGrid' and @role='grid']",
        "select_date": "//div[contains(@class,'uiDatePickerGrid')]/table[@class='calGrid']//*[text()='{}']",
        "text-field": "//label/span[text()='{}']/../following-sibling::input",
        "footer_button": "//lightning-button//button[text()='{}']",
        "dropdown_field": "//lightning-combobox[./label[text()='{}']]/div//input[contains(@class,'combobox__input')]",
        "dropdown_popup": "//div[contains(@class, 'slds-dropdown-trigger')]/div[contains(@class, 'slds-listbox')]",
        "dropdown_value": "//div[contains(@class,'slds-listbox')]//lightning-base-combobox-item//span[text()='{}']",
        "modal_footer_button": "//*[@id='wrapper-body']/footer/button/span[text()='{}']",
        "modal_footer": "//footer[@class='slds-modal__footer']",
        "amount_field": "//label[text()='{}']/..//*[self::input or self::textarea]",
        "date_field": "//div[contains(@class,'slds-dropdown-trigger')][./label[text()='{}']]/div/input",
    },
    "confirm": {
        "check_value": "//div[contains(@class, 'forcePageBlockItem') or contains(@class, 'slds-form-element_stacked')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]//*[text()='{}']",
        "check_status": "//div[contains(@class, 'field-label-container')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span//lightning-formatted-text[text()='{}']",
        "check_numbers": "//div[contains(@class, 'field-label-container')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span//lightning-formatted-number[text()='{}']",
    },
    "tab": {
        "tab_header": "//a[@class='slds-tabs_default__link' and text()='{}']",
        "record_detail_tab": "//a[contains(@data-label,'{}')]",
        "verify_header": "//div[contains(@class, 'entityNameTitle')]",
        "verify_details": "//div[contains(@class, 'slds-form-element')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span",
    },
    "related": {
        "title": '//div[contains(@class, "slds-card")]/header[.//span[@title="{}"]]',
        "button": "//div[contains(@class, 'forceRelatedListSingleContainer')][.//img][.//span[@title='{}']]//a[@title='{}']",
        "count": "//tbody/tr/td[1]",
        "flexi_button": "//div[@lst-listviewmanagerheader_listviewmanagerheader][.//span[@title='{}']]//lightning-button//button[text()='{}']",
        "flexi_link": "//a//span[text()='{}']",
    },
    "details": {
        "button": "//button[contains(@class, 'slds-button') and text() = '{}']",
        "header": "//h1//div[contains(@class, 'entityNameTitle') and contains(text(),'{}')]",
    },
    "funding_req_role": {
        "select_value": "//li/a[text()='{}']",
        "select_dropdown": "//div[contains(@class, 'uiInput')][.//span[contains(@class, 'inputLabel')]]//span[text()='{}']/../following-sibling::div//a[@class='select']",
        "save_button": "//footer/button/span[text()='Save']",
        "fr_link": "//div//a//span[contains(text(),'FR-')]",
        "save_button_old": "//div[contains(@class, 'modal-footer')]//button/span[text()='Save']",
    },
    "sharing": {
        "sharing_link": "//a//span[contains(text(), 'Sharing')]",
        "sharing_button": "//div[contains(@class, 'highlights slds-clearfix slds-page-header slds-page-header_record-home fixed-position')]//lightning-button-menu[contains(@class,'slds-dropdown-trigger')]/button[contains(@class, 'slds-button_icon-border-filled')]",
        "search_user": "//label//span[text()='Search']/../../div//input",
        "save_share": "//div[contains(@class, 'modal-footer')]//button[text()='Save']",
    },
    "link": "//a[contains(text(),'{}')]",
    "flexipage-popup": "//div[contains(@class, 'slds-is-open')][contains(@class, 'slds-combobox')]",
    "header_title": "//h2[(contains(@class, 'inlineTitle') or contains(@class, 'slds-text-heading') or contains(@class, 'listTitle') or contains(@class, 'slds-hyphenate')) and contains(text(),'{}')]",
    "object_button": "//div[contains(@class, 'slds-page-header')]//*[self::a[@title='Edit'] or self::button[@name='Edit']]",
    "toast_message": "//div[contains(@class,'toastContent')]/child::div/span[contains(text(),\"{}\")]",
    "toast_close": "//span[contains(@class, 'toastMessage') and text()=\"{}\"]/ancestor::div//button[@title='Close']",
}
