# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

import pyperclip

window = tk.Tk()
window.title('创建新规则')
window.geometry("520x860+500+50")


'''--------- 全局变量 ---------'''
VARIABLES = ""
OPERATORS = ""
ID = ""
T = "t:none,\\"
T_LIST = []
MSG = ""
OTHER_ACTION = ""
SEVERITY = ""
SETVAR_OR_CHAIN = ""


'''--------- SecRule文本更新函数 ---------'''
def rule_text_update():
    _new_rule = f"""\
SecRule {VARIABLES} {OPERATORS}
    "{ID}
    {OTHER_ACTION}
    {MSG}
    {T}
    {SEVERITY}
    {SETVAR_OR_CHAIN}"
"""
    ruleText.delete("1.0", "end")
    ruleText.insert(tk.INSERT, _new_rule)


'''--------- SecRule文本显示面板 ---------'''
RulePane = tk.PanedWindow(window, width=520, height=300, borderwidth=20)
ruleText = tk.Text(RulePane, width=300, height=100, padx=10, pady=10, undo=True)
rule_text_update()
RulePane.add(ruleText)
RulePane.grid()

'''--------- 规则说明 ---------'''
# id
def add_id(*args):
    global ID
    _id = IdEntry.get()
    ID = "id:" + _id + ",\\"
    rule_text_update()
# 规则说明
def add_msg(*args):
    global MSG
    _msg = MsgEntry.get()
    MSG = "msg:\'" + _msg + "\',\\"
    rule_text_update()

MsgPane = tk.PanedWindow(window, width=520, orient='horizontal')

variable_id = tk.StringVar()
variable_id.trace('w', add_id)
IdLabel = tk.Label(MsgPane, text="ID:")
IdEntry = tk.Entry(MsgPane, width=10, textvariable=variable_id)

variable_msg = tk.StringVar()
variable_msg.trace('w', add_msg)
MsgLabel = tk.Label(MsgPane, text="说明:")
MsgEntry = tk.Entry(MsgPane, width=37, textvariable=variable_msg)

BlankLabel = tk.Label(MsgPane)

MsgPane.grid()
IdLabel.grid(row=0, column=0, sticky="w", padx=5)
IdEntry.grid(row=0, column=1, sticky="w")
BlankLabel.grid(row=0, column=2, padx=30)
MsgLabel.grid(row=0, column=3, sticky="e", padx=5)
MsgEntry.grid(row=0, column=4, sticky="e")






'''--------- 匹配对象 ---------'''
def add_variables():
    global VARIABLES
    _variables = ""
    _have_one = 0
    _request_headers = cb_request_headers.get()
    _args = cb_args.get()
    _remote_addr = cb_remote_addr.get()
    _cookies = cb_cookies.get()
    _file = cb_file.get()
    _xml = cb_xml.get()
    _request_line = cb_request_line.get()
    _request_body = cb_request_body.get()

    if _request_headers != "":
        # 判断当前是否有至少一个变量对象
        if _have_one == 0:
            _variables += "REQUEST_HEADERS"
            _have_one = 1
        # 若当前已有变量，则添加 “|” 作为分隔符
        else:
            _variables += "|"
            _variables += "REQUEST_HEADERS"
    if _request_line != "":
        if _have_one == 0:
            _variables += "REQUEST_LINE"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "REQUEST_LINE"
    if _request_body != "":
        if _have_one == 0:
            _variables += "REQUEST_BODY"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "REQUEST_BODY"
    if _args != "":
        if _have_one == 0:
            _variables += "ARGS_NAMES|ARGS"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "ARGS_NAMES|ARGS"
    if _remote_addr != "":
        if _have_one == 0:
            _variables += "REMOTE_ADDR"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "REMOTE_ADDR"
    if _cookies != "":
        if _have_one == 0:
            _variables += "REQUEST_COOKIES|!REQUEST_COOKIES:/__utm/|REQUEST_COOKIES_NAMES"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "REQUEST_COOKIES|!REQUEST_COOKIES:/__utm/|REQUEST_COOKIES_NAMES"
    if _file != "":
        if _have_one == 0:
            _variables += "FILES|REQUEST_HEADERS:X-Filename|REQUEST_HEADERS:X_Filename|REQUEST_HEADERS:X.Filename|REQUEST_HEADERS:X-File-Name"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "FILES|REQUEST_HEADERS:X-Filename|REQUEST_HEADERS:X_Filename|REQUEST_HEADERS:X.Filename|REQUEST_HEADERS:X-File-Name"
    if _xml != "":
        if _have_one == 0:
            _variables += "XML:/*"
            _have_one = 1
        else:
            _variables += "|"
            _variables += "XML:/*"

    VARIABLES = _variables
    rule_text_update()


MATCH_boundary = tk.PanedWindow(window, width=520, height=40)
MATCH_Label = tk.Label(MATCH_boundary, text="--- 检测对象 ---")
MATCH_boundary.grid()
MATCH_boundary.add(MATCH_Label)

MatchPane = tk.PanedWindow(window, width=520)

cb_request_headers = tk.StringVar()
cb_args = tk.StringVar()
cb_remote_addr = tk.StringVar()
cb_cookies = tk.StringVar()
cb_file = tk.StringVar()
cb_xml = tk.StringVar()
cb_request_line = tk.StringVar()
cb_request_body = tk.StringVar()
MatchPaneCheckButton1 = tk.Checkbutton(MatchPane, text='REQUEST_HEADERS', variable=cb_request_headers,
                                       onvalue="REQUEST_HEADERS", offvalue="", command=add_variables)
MatchPaneCheckButton2 = tk.Checkbutton(MatchPane, text='REQUEST_LINE', variable=cb_request_line, onvalue="REQUEST_LINE",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton3 = tk.Checkbutton(MatchPane, text='REQUEST_BODY', variable=cb_request_body, onvalue="REQUEST_BODY",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton4 = tk.Checkbutton(MatchPane, text='ARGS', variable=cb_args, onvalue="ARGS", offvalue="",
                                       command=add_variables)
MatchPaneCheckButton5 = tk.Checkbutton(MatchPane, text='COOKIES', variable=cb_cookies, onvalue="COOKIES",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton6 = tk.Checkbutton(MatchPane, text='FILE_UPLOAD', variable=cb_file, onvalue="FILE",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton7 = tk.Checkbutton(MatchPane, text='XML', variable=cb_xml, onvalue="XML",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton8 = tk.Checkbutton(MatchPane, text='REMOTE_ADDR', variable=cb_remote_addr,
                                       onvalue="REMOTE_ADDR",
                                       offvalue="", command=add_variables)

MatchPane.grid()
MatchPaneCheckButton1.grid(row=0, column=0, sticky='w', padx=20)
MatchPaneCheckButton2.grid(row=1, column=0, sticky='w', padx=20)
MatchPaneCheckButton3.grid(row=2, column=0, sticky='w', padx=20)
MatchPaneCheckButton4.grid(row=0, column=1, sticky='w', padx=20)
MatchPaneCheckButton5.grid(row=1, column=1, sticky='w', padx=20)
MatchPaneCheckButton6.grid(row=2, column=1, sticky='w', padx=20)
MatchPaneCheckButton7.grid(row=0, column=2, sticky='w', padx=20)
MatchPaneCheckButton8.grid(row=1, column=2, sticky='w', padx=20)

'''--------- 运算符 ---------'''


# 鼠标聚焦后清空文本框
focus = 1
def on_focus(*args):
    global focus
    if focus == 1:
        variable_operator.set("")
        focus = 0


# 根据ComboBox选择更改提示内容
def operator_combox_select(*args):
    global focus
    _select = OperatorPaneComboBox.get()
    if _select == "@rx":
        variable_operator.set("<请在此输入正则表达式>")
        focus = 1
    elif _select == "@contains":
        variable_operator.set("<请在此输入包含的内容>")
        focus = 1
    elif _select == "@beginsWith":
        variable_operator.set("<请在此输入起始字符串>")
        focus = 1
    elif _select == "@ipMatch":
        variable_operator.set("<请在此输入目标IP地址>")
        focus = 1
    elif _select == "@pmFromFile":
        variable_operator.set("<请在此输入匹配文件名>")
        focus = 1


# 确认添加内容
def add_operators(*args):
    global OPERATORS
    _operators = "\"" + OperatorPaneComboBox.get() + " " + variable_operator.get() + "\"" + "\\"
    OPERATORS = _operators
    rule_text_update()


OPERATOR_boundary = tk.PanedWindow(window, width=520, height=30)
OPERATOR_Label = tk.Label(OPERATOR_boundary, text="--- 匹配内容 ---")
OPERATOR_boundary.grid()
OPERATOR_boundary.add(OPERATOR_Label)

OperatorPane = tk.PanedWindow(window, width=520, orient='horizontal')

com_operator = tk.StringVar()
com_operator.set("请选择运算符")
OperatorPaneComboBox = ttk.Combobox(OperatorPane, width=15, textvariable=com_operator, state='readonly')
OperatorPaneComboBox["values"] = ("@rx", "@contains", "@beginsWith", "@ipMatch", "@pmFromFile")
OperatorPaneComboBox.bind("<<ComboboxSelected>>", operator_combox_select)

variable_operator = tk.StringVar()
OperatorPaneEntry = tk.Entry(OperatorPane, width=35, textvariable=variable_operator)
OperatorPaneEntry.bind("<FocusIn>", on_focus)
variable_operator.trace('w', add_operators)

OperatorPane.grid()
OperatorPaneComboBox.grid(row=0, column=0, sticky='w', padx=20)
OperatorPaneEntry.grid(row=0, column=1)



'''--------- ACTIONS ---------'''

ACTIONS_boundary = tk.PanedWindow(window, width=520, height=30)
ACTIONS_Label = tk.Label(ACTIONS_boundary, text="--- 数据处理 ---")
ACTIONS_boundary.grid()
ACTIONS_boundary.add(ACTIONS_Label)

# t
TPane = tk.PanedWindow(window, width=520, orient='horizontal')
def add_t(_value):
    global T, T_LIST
    _t = "t:none,"
    _t_list = [cb_t_htmlentitydecode.get(), cb_t_lowercase.get(), cb_t_removenulls.get(), cb_t_urldecodeuni.get(), cb_t_normalisepath.get(), cb_t_cmdline.get(), cb_t_base64decodeext.get(), cb_t_removewhitespace.get()]
    if _value not in T_LIST:
        T_LIST.append(_value)
    for t in T_LIST:
        if t in _t_list:
            _t += "t:" + t + ","
    T = _t + "\\"
    rule_text_update()

cb_t_htmlentitydecode = tk.StringVar()
cb_t_lowercase = tk.StringVar()
cb_t_removenulls = tk.StringVar()
cb_t_urldecodeuni = tk.StringVar()
cb_t_normalisepath = tk.StringVar()
cb_t_cmdline = tk.StringVar()
cb_t_base64decodeext = tk.StringVar()
cb_t_removewhitespace = tk.StringVar()
TCheckButton1 = tk.Checkbutton(TPane, text='htmlEntityDecode', variable=cb_t_htmlentitydecode,
                                       onvalue="htmlEntityDecode", offvalue="", command=lambda: add_t("htmlEntityDecode"))
TCheckButton2 = tk.Checkbutton(TPane, text='lowercase', variable=cb_t_lowercase,
                                       onvalue="lowercase", offvalue="", command=lambda: add_t("lowercase"))
TCheckButton3 = tk.Checkbutton(TPane, text='removeNulls', variable=cb_t_removenulls,
                                       onvalue="removeNulls", offvalue="", command=lambda: add_t("removeNulls"))
TCheckButton4 = tk.Checkbutton(TPane, text='urlDecodeUni', variable=cb_t_urldecodeuni,
                                       onvalue="urlDecodeUni", offvalue="", command=lambda: add_t("urlDecodeUni"))
TCheckButton5 = tk.Checkbutton(TPane, text='normalizePath', variable=cb_t_normalisepath,
                                       onvalue="normalizePath", offvalue="", command=lambda: add_t("normalizePath"))
TCheckButton6 = tk.Checkbutton(TPane, text='cmdLine', variable=cb_t_cmdline,
                                       onvalue="cmdLine", offvalue="", command=lambda: add_t("cmdLine"))
TCheckButton7 = tk.Checkbutton(TPane, text='base64DecodeExt', variable=cb_t_base64decodeext,
                               onvalue="base64DecodeExt", offvalue="", command=lambda: add_t("base64DecodeExt"))
TCheckButton8 = tk.Checkbutton(TPane, text='removeWhitespace', variable=cb_t_removewhitespace,
                               onvalue="removeWhitespace", offvalue="", command=lambda: add_t("removeWhitespace"))
TPane.grid()
TCheckButton1.grid(row=0, column=0, sticky='w')
TCheckButton2.grid(row=0, column=1, sticky='w')
TCheckButton3.grid(row=0, column=2, sticky='w')
TCheckButton4.grid(row=1, column=0, sticky='w')
TCheckButton5.grid(row=1, column=1, sticky='w')
TCheckButton6.grid(row=1, column=2, sticky='w')
TCheckButton7.grid(row=0, column=3, sticky='w')
TCheckButton8.grid(row=1, column=3, sticky='w')


'''--------- Severity ---------'''

SEVERITY_boundary = tk.PanedWindow(window, width=520, height=30)
SEVERITY_Label = tk.Label(SEVERITY_boundary, text="--- 严重性等级 ---")
SEVERITY_boundary.grid()
SEVERITY_boundary.add(SEVERITY_Label)

def severity_combox_select(*args):
    global SEVERITY
    _select = SeverityPaneComboBox.get()
    SEVERITY = "severity:'" + _select + "',\\"
    # 同时更新设置分值
    check_setvar_or_chain()
    rule_text_update()

SeverityPane = tk.PanedWindow(window, width=520)
SeverityPaneComboBox = ttk.Combobox(SeverityPane, width=15, state='readonly')
SeverityPaneComboBox["values"] = ("EMERGENCY", "ALERT", "CRITICAL", "ERROR", "WARNING", "NOTICE", "INFO", "DEBUG")
SeverityPaneComboBox.bind("<<ComboboxSelected>>", severity_combox_select)

SeverityPane.grid()
SeverityPane.add(SeverityPaneComboBox, padx=130)

# 用于文本缩进对齐
TAB_COUNT = 0
def new_rule_chain(master):
    global TAB_COUNT
    TAB_COUNT += 1
    _tabs = TAB_COUNT*'    '
    new_window = tk.Toplevel(master)
    new_window.title("新的规则链")
    new_window.geometry("500x650")

    # 绑定关闭事件
    def mydestory():
        global TAB_COUNT
        TAB_COUNT -= 1
        new_window.destroy()

    new_window.protocol('WM_DELETE_WINDOW', mydestory)
    '''--------- 新规则变量 ---------'''
    NEW_VARIABLES = ""
    NEW_OPERATORS = ""
    NEW_T = "t:none,\\"
    NEW_T_LIST = []
    NEW_SETVAR_OR_CHAIN = ""

    '''--------- SecRule文本更新函数 ---------'''
    def chain_rule_text_update():
        _new_rule = f"""\
{_tabs}SecRule {NEW_VARIABLES} {NEW_OPERATORS}
{_tabs}    "{NEW_T}
{_tabs}    {NEW_SETVAR_OR_CHAIN}\
"""
        ruleText.delete("1.0", "end")
        ruleText.insert(tk.INSERT, _new_rule)

    '''--------- SecRule文本显示面板 ---------'''
    RulePane = tk.PanedWindow(new_window, width=500, height=150, borderwidth=20)
    ruleText = tk.Text(RulePane, padx=10, pady=10, undo=True)
    chain_rule_text_update()
    RulePane.add(ruleText)
    RulePane.grid()

    '''--------- 匹配对象 ---------'''

    def add_variables():
        nonlocal NEW_VARIABLES
        _variables = ""
        _have_one = 0
        _request_headers = cb_request_headers.get()
        _args = cb_args.get()
        _remote_addr = cb_remote_addr.get()
        _cookies = cb_cookies.get()
        _file = cb_file.get()
        _xml = cb_xml.get()
        _request_line = cb_request_line.get()
        _request_body = cb_request_body.get()
        _matched = cb_matched.get()

        if _matched != "":
            # 判断当前是否有至少一个变量对象
            if _have_one == 0:
                _variables += "MATCHED_VARS"
                _have_one = 1
            # 若当前已有变量，则添加 “|” 作为分隔符
            else:
                _variables += "|"
                _variables += "MATCHED_VARS"
        if _request_headers != "":
            # 判断当前是否有至少一个变量对象
            if _have_one == 0:
                _variables += "REQUEST_HEADERS"
                _have_one = 1
            # 若当前已有变量，则添加 “|” 作为分隔符
            else:
                _variables += "|"
                _variables += "REQUEST_HEADERS"
        if _request_line != "":
            if _have_one == 0:
                _variables += "REQUEST_LINE"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "REQUEST_LINE"
        if _request_body != "":
            if _have_one == 0:
                _variables += "REQUEST_BODY"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "REQUEST_BODY"
        if _args != "":
            if _have_one == 0:
                _variables += "ARGS_NAMES|ARGS"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "ARGS_NAMES|ARGS"
        if _remote_addr != "":
            if _have_one == 0:
                _variables += "REMOTE_ADDR"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "REMOTE_ADDR"
        if _cookies != "":
            if _have_one == 0:
                _variables += "REQUEST_COOKIES|!REQUEST_COOKIES:/__utm/|REQUEST_COOKIES_NAMES"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "REQUEST_COOKIES|!REQUEST_COOKIES:/__utm/|REQUEST_COOKIES_NAMES"
        if _file != "":
            if _have_one == 0:
                _variables += "FILES|REQUEST_HEADERS:X-Filename|REQUEST_HEADERS:X_Filename|REQUEST_HEADERS:X.Filename|REQUEST_HEADERS:X-File-Name"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "FILES|REQUEST_HEADERS:X-Filename|REQUEST_HEADERS:X_Filename|REQUEST_HEADERS:X.Filename|REQUEST_HEADERS:X-File-Name"
        if _xml != "":
            if _have_one == 0:
                _variables += "XML:/*"
                _have_one = 1
            else:
                _variables += "|"
                _variables += "XML:/*"

        NEW_VARIABLES = _variables
        chain_rule_text_update()

    MATCH_boundary = tk.PanedWindow(new_window, width=500, height=30)
    MATCH_Label = tk.Label(MATCH_boundary, text="--- 检测对象 ---")
    MATCH_boundary.grid()
    MATCH_boundary.add(MATCH_Label)

    MatchPane = tk.PanedWindow(new_window, width=500)
    cb_request_headers = tk.StringVar()
    cb_args = tk.StringVar()
    cb_remote_addr = tk.StringVar()
    cb_cookies = tk.StringVar()
    cb_file = tk.StringVar()
    cb_xml = tk.StringVar()
    cb_matched = tk.StringVar()
    cb_request_line = tk.StringVar()
    cb_request_body = tk.StringVar()
    MatchPaneCheckButton0 = tk.Checkbutton(MatchPane, text='MATCHED_VARS', variable=cb_matched, onvalue="MATCHED_VARS",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton1 = tk.Checkbutton(MatchPane, text='REQUEST_HEADERS', variable=cb_request_headers,
                                           onvalue="REQUEST_HEADERS", offvalue="", command=add_variables)
    MatchPaneCheckButton2 = tk.Checkbutton(MatchPane, text='REQUEST_LINE', variable=cb_request_line, onvalue="REQUEST_LINE",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton3 = tk.Checkbutton(MatchPane, text='REQUEST_BODY', variable=cb_request_body, onvalue="REQUEST_BODY",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton4 = tk.Checkbutton(MatchPane, text='ARGS', variable=cb_args, onvalue="ARGS", offvalue="",
                                           command=add_variables)
    MatchPaneCheckButton5 = tk.Checkbutton(MatchPane, text='COOKIES', variable=cb_cookies, onvalue="COOKIES",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton6 = tk.Checkbutton(MatchPane, text='FILE_UPLOAD', variable=cb_file, onvalue="FILE",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton7 = tk.Checkbutton(MatchPane, text='XML', variable=cb_xml, onvalue="XML",
                                           offvalue="", command=add_variables)
    MatchPaneCheckButton8 = tk.Checkbutton(MatchPane, text='REMOTE_ADDR', variable=cb_remote_addr,
                                           onvalue="REMOTE_ADDR",
                                           offvalue="", command=add_variables)
    MatchPane.grid()
    MatchPaneCheckButton0.grid(row=0, column=0, sticky='w', padx=20)
    MatchPaneCheckButton1.grid(row=1, column=0, sticky='w', padx=20)
    MatchPaneCheckButton2.grid(row=2, column=0, sticky='w', padx=20)
    MatchPaneCheckButton3.grid(row=0, column=1, sticky='w', padx=20)
    MatchPaneCheckButton4.grid(row=1, column=1, sticky='w', padx=20)
    MatchPaneCheckButton5.grid(row=2, column=1, sticky='w', padx=20)
    MatchPaneCheckButton6.grid(row=0, column=2, sticky='w', padx=20)
    MatchPaneCheckButton7.grid(row=1, column=2, sticky='w', padx=20)
    MatchPaneCheckButton8.grid(row=2, column=2, sticky='w', padx=20)

    '''--------- 运算符 ---------'''

    # 鼠标聚焦后清空文本框
    # 鼠标聚焦后清空文本框
    focus_new = 1

    def on_focus(*args):
        nonlocal focus_new
        if focus_new == 1:
            variable_operator.set("")
            focus_new = 0

    # 根据ComboBox选择更改提示内容
    def operator_combox_select(*args):
        nonlocal focus_new
        _select = OperatorPaneComboBox.get()
        if _select == "@rx":
            variable_operator.set("<请在此输入正则表达式>")
            focus_new = 1
        elif _select == "@contains":
            variable_operator.set("<请在此输入包含的内容>")
            focus_new = 1
        elif _select == "@beginsWith":
            variable_operator.set("<请在此输入起始字符串>")
            focus_new = 1
        elif _select == "@ipMatch":
            variable_operator.set("<请在此输入目标IP地址>")
            focus_new = 1

    # 确认添加内容
    def add_operators(*args):
        nonlocal NEW_OPERATORS
        _operators = "\"" + OperatorPaneComboBox.get() + " " + variable_operator.get() + "\"" + "\\"
        NEW_OPERATORS = _operators
        chain_rule_text_update()

    OPERATOR_boundary = tk.PanedWindow(new_window, width=500, height=30)
    OPERATOR_Label = tk.Label(OPERATOR_boundary, text="--- 匹配内容 ---")
    OPERATOR_boundary.grid()
    OPERATOR_boundary.add(OPERATOR_Label)

    OperatorPane = tk.PanedWindow(new_window, width=500, orient='horizontal')

    com_operator = tk.StringVar()
    com_operator.set("请选择运算符")
    OperatorPaneComboBox = ttk.Combobox(OperatorPane, width=15, textvariable=com_operator, state='readonly')
    OperatorPaneComboBox["values"] = ("@rx", "@contains", "@beginsWith", "@ipMatch")
    OperatorPaneComboBox.bind("<<ComboboxSelected>>", operator_combox_select)
    variable_operator = tk.StringVar()
    OperatorPaneEntry = tk.Entry(OperatorPane, width=35, textvariable=variable_operator)
    OperatorPaneEntry.bind("<FocusIn>", on_focus)
    variable_operator.trace('w', add_operators)
    OperatorPane.grid()
    OperatorPaneComboBox.grid(row=0, column=0, sticky='w', padx=20)
    OperatorPaneEntry.grid(row=0, column=1)

    '''--------- ACTIONS ---------'''

    ACTIONS_boundary = tk.PanedWindow(new_window, width=500, height=30)
    ACTIONS_Label = tk.Label(ACTIONS_boundary, text="--- 数据处理 ---")
    ACTIONS_boundary.grid()
    ACTIONS_boundary.add(ACTIONS_Label)

    def add_t(_value):
        nonlocal NEW_T, NEW_T_LIST
        _t = "t:none,"
        _t_list = [cb_t_htmlentitydecode.get(), cb_t_lowercase.get(), cb_t_removenulls.get(), cb_t_urldecodeuni.get(),
                   cb_t_normalisepath.get(), cb_t_cmdline.get(), cb_t_base64decodeext.get(), cb_t_removewhitespace.get()]
        if _value not in NEW_T_LIST:
            NEW_T_LIST.append(_value)
        for t in NEW_T_LIST:
            if t in _t_list:
                _t += "t:" + t + ","
        NEW_T = _t + "\\"
        chain_rule_text_update()
    TPane = tk.PanedWindow(new_window, width=500)
    cb_t_htmlentitydecode = tk.StringVar()
    cb_t_lowercase = tk.StringVar()
    cb_t_removenulls = tk.StringVar()
    cb_t_urldecodeuni = tk.StringVar()
    cb_t_normalisepath = tk.StringVar()
    cb_t_cmdline = tk.StringVar()
    cb_t_base64decodeext = tk.StringVar()
    cb_t_removewhitespace = tk.StringVar()
    TCheckButton1 = tk.Checkbutton(TPane, text='htmlEntityDecode', variable=cb_t_htmlentitydecode,
                                   onvalue="htmlEntityDecode", offvalue="", command=lambda: add_t("htmlEntityDecode"))
    TCheckButton2 = tk.Checkbutton(TPane, text='lowercase', variable=cb_t_lowercase,
                                   onvalue="lowercase", offvalue="", command=lambda: add_t("lowercase"))
    TCheckButton3 = tk.Checkbutton(TPane, text='removeNulls', variable=cb_t_removenulls,
                                   onvalue="removeNulls", offvalue="", command=lambda: add_t("removeNulls"))
    TCheckButton4 = tk.Checkbutton(TPane, text='urlDecodeUni', variable=cb_t_urldecodeuni,
                                   onvalue="urlDecodeUni", offvalue="", command=lambda: add_t("urlDecodeUni"))
    TCheckButton5 = tk.Checkbutton(TPane, text='normalisePath', variable=cb_t_normalisepath,
                                   onvalue="normalisePath", offvalue="", command=lambda: add_t("normalisePath"))
    TCheckButton6 = tk.Checkbutton(TPane, text='cmdLine', variable=cb_t_cmdline,
                                   onvalue="cmdLine", offvalue="", command=lambda: add_t("cmdLine"))
    TCheckButton7 = tk.Checkbutton(TPane, text='base64DecodeExt', variable=cb_t_base64decodeext,
                                   onvalue="base64DecodeExt", offvalue="", command=lambda: add_t("base64DecodeExt"))
    TCheckButton8 = tk.Checkbutton(TPane, text='removeWhitespace', variable=cb_t_removewhitespace,
                                   onvalue="removeWhitespace", offvalue="", command=lambda: add_t("removeWhitespace"))
    TPane.grid()
    TCheckButton1.grid(row=0, column=0, sticky='w')
    TCheckButton2.grid(row=0, column=1, sticky='w')
    TCheckButton3.grid(row=0, column=2, sticky='w')
    TCheckButton4.grid(row=1, column=0, sticky='w')
    TCheckButton5.grid(row=1, column=1, sticky='w')
    TCheckButton6.grid(row=1, column=2, sticky='w')
    TCheckButton7.grid(row=0, column=3, sticky='w')
    TCheckButton8.grid(row=1, column=3, sticky='w')

    '''--------- SetVar or Chain ---------'''

    CHAIN_boundary = tk.PanedWindow(new_window, width=500, height=30)
    CHAIN_Label = tk.Label(CHAIN_boundary, text="--- 处置措施 ---")
    CHAIN_boundary.grid()
    CHAIN_boundary.add(CHAIN_Label)

    def check_setvar_or_chain(*args):
        _text_content = ""
        _choose = ChainPaneComboBox.get()
        if _choose == "设置分值":
            _select = SeverityPaneComboBox.get()
            if _select == "CRITICAL":
                _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.critical_anomaly_score}'"
            elif _select == "ERROR":
                _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.error_anomaly_score}'"
            elif _select == "WARNING":
                _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.warning_anomaly_score}'"
            elif _select == "NOTICE":
                _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.notice_anomaly_score}'"
            else:
                _text_content = ""
                MSB_SetVar = showwarning(title="SetVar提示", message=f"""当前{_select}等级下不会增加分值""")

            ChainPaneText.delete("1.0", "end")
            ChainPaneText.insert(tk.INSERT, _text_content)

        if _choose == "添加规则链":
            _text_content = ""
            new_rule_chain(ChainPaneText)


    def add_setvar_or_chain():
        nonlocal NEW_SETVAR_OR_CHAIN
        _choose = ChainPaneComboBox.get()
        NEW_SETVAR_OR_CHAIN = ChainPaneText.get("1.0", "end-1c")
        if _choose == "设置分值":
            chain_rule_text_update()
        if _choose == "添加规则链":
            NEW_SETVAR_OR_CHAIN = "chain\"\n" + NEW_SETVAR_OR_CHAIN
            chain_rule_text_update()


    ChainPane = tk.PanedWindow(new_window, width=500)
    ChainPaneComboBox = ttk.Combobox(ChainPane, width=15, state='readonly')
    ChainPaneComboBox["values"] = ("设置分值", "添加规则链")
    ChainPaneComboBox.bind("<<ComboboxSelected>>", check_setvar_or_chain)
    ChainPaneButton = tk.Button(ChainPane, text="确定添加", command=add_setvar_or_chain)
    ChainPaneText = tk.Text(ChainPane, width=55, height=5, undo=True)
    ChainPane.grid()
    ChainPaneComboBox.grid(row=0, column=0, sticky='w', padx=10)
    ChainPaneButton.grid(row=0, column=1, sticky='e', padx=10)
    ChainPaneText.grid(row=2, columnspan=2, padx=10, pady=10)

    def add_new_rule():
        _rule_chain = ruleText.get("1.0", "end-1c")
        master.delete("1.0", "end")
        master.insert(tk.INSERT, _rule_chain)
        mydestory()

    OKPane = tk.PanedWindow(new_window, width=400, height=80)
    OKButton = tk.Button(OKPane, text="添加规则链", command=add_new_rule)
    OKPane.grid()
    OKPane.add(OKButton, padx=80, pady=15)


'''--------- SetVar or Chain ---------'''

CHAIN_boundary = tk.PanedWindow(window, width=520, height=30)
CHAIN_Label = tk.Label(CHAIN_boundary, text="--- 处置措施 ---")
CHAIN_boundary.grid()
CHAIN_boundary.add(CHAIN_Label)

def check_setvar_or_chain(*args):
    _text_content = ""
    _choose = ChainPaneComboBox.get()
    if _choose == "设置分值":
        _select = SeverityPaneComboBox.get()
        if _select == "CRITICAL":
            _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.critical_anomaly_score}'"
        elif _select == "ERROR":
            _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.error_anomaly_score}'"
        elif _select == "WARNING":
            _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.warning_anomaly_score}'"
        elif _select == "NOTICE":
            _text_content = "setvar:'tx.inbound_anomaly_score_pl1=+%{tx.notice_anomaly_score}'"
        else:
            _text_content = ""
            MSB_SetVar = showwarning(title="SetVar提示", message=f"""当前{_select}等级下不会增加分值""")
            ChainPaneComboBox.set('')
            ChainPaneText.delete('1.0', 'end-1c')

        ChainPaneText.delete("1.0", "end")
        ChainPaneText.insert(tk.INSERT, _text_content)

    if _choose == "添加规则链":
        _text_content = ""
        new_rule_chain(ChainPaneText)

def add_setvar_or_chain():
    global SETVAR_OR_CHAIN
    _choose = ChainPaneComboBox.get()
    SETVAR_OR_CHAIN = ChainPaneText.get("1.0", "end-1c")
    if _choose == "设置分值":
        rule_text_update()
    if _choose == "添加规则链":
        SETVAR_OR_CHAIN = "chain\"\n" + SETVAR_OR_CHAIN
        rule_text_update()


ChainPane = tk.PanedWindow(window, width=520)
ChainPaneComboBox = ttk.Combobox(ChainPane, width=15, state='readonly')
ChainPaneComboBox["values"] = ("设置分值", "添加规则链")
ChainPaneComboBox.bind("<<ComboboxSelected>>", check_setvar_or_chain)
ChainPaneButton = tk.Button(ChainPane, text="确定添加", command=add_setvar_or_chain)
ChainPaneText = tk.Text(ChainPane, width=55, height=5, undo=True)
ChainPane.grid()
ChainPaneComboBox.grid(row=0, column=0, sticky='w', padx=10)
ChainPaneButton.grid(row=0, column=1, sticky='e', padx=10)
ChainPaneText.grid(row=2, columnspan=2, padx=10, pady=10)

'''--------- 补全默认配置 ---------'''
def add_other_config():
    global OTHER_ACTION
    _default = cb_default.get()
    if _default == 0:
        OTHER_ACTION = ""
    elif _default == 1:
        OTHER_ACTION = """\
phase:2,\\
    block,\\
    capture,\\"""
    rule_text_update()

def copy_rule():
    _rule_text = ruleText.get('1.0', 'end-1c')
    pyperclip.copy(_rule_text)

def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list

def clean_rule():
    # 清空当前选择
    variable_id.set('')
    variable_msg.set('')
    cb_request_headers.set('')
    cb_args.set('')
    cb_remote_addr.set('')
    cb_cookies.set('')
    cb_file.set('')
    cb_xml.set('')
    cb_request_line.set('')
    cb_request_body.set('')
    com_operator.set("请选择运算符")
    variable_operator.set('')
    cb_t_htmlentitydecode.set('')
    cb_t_lowercase.set('')
    cb_t_removenulls.set('')
    cb_t_urldecodeuni.set('')
    cb_t_normalisepath.set('')
    cb_t_cmdline.set('')
    cb_t_base64decodeext.set('')
    cb_t_removewhitespace.set('')
    SeverityPaneComboBox.set('')
    ChainPaneComboBox.set('')
    ChainPaneText.delete('1.0', 'end-1c')
    cb_default.set(0)

    # 清空数据
    global VARIABLES, OPERATORS, ID, T, T_LIST, MSG, OTHER_ACTION, SEVERITY, SETVAR_OR_CHAIN
    VARIABLES = ""
    OPERATORS = ""
    ID = ""
    T = "t:none,\\"
    T_LIST = []
    MSG = ""
    OTHER_ACTION = ""
    SEVERITY = ""
    SETVAR_OR_CHAIN = ""
    rule_text_update()


CopyPane = tk.PanedWindow(window, width=520, height=60)
cb_default = tk.IntVar()
CopyPaneCheckButton = tk.Checkbutton(CopyPane, text='补全默认配置', variable=cb_default, onvalue=1, offvalue=0, command=add_other_config, width=10, height=1)
CopyPaneButton = tk.Button(CopyPane, text='复制到剪贴板', command=copy_rule, width=10, height=1)
CopyPaneCleanButton = tk.Button(CopyPane, text='清空', command=clean_rule, width=10, height=1)
CopyPane.grid()
CopyPaneCheckButton.place(x=300, y=11)
CopyPaneButton.place(x=410, y=10)
CopyPaneCleanButton.place(x=20, y=10)


window.mainloop()
