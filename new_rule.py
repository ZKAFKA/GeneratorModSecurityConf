# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from threading import Thread
from time import sleep, ctime
from tkinter.messagebox import *
import webbrowser
from tkinter.ttk import Separator

window = tk.Tk()
window.title('创建新规则')
window.geometry("520x800")


'''--------- 全局变量 ---------'''
VARIABLES = ""
OPERATORS = ""
ID = ""
T = ""
T_LIST = []
MSG = ""
OTHER_ACTION = ""
SEVERITY = ""
SETVAR = ""
CHAIN = ""


'''--------- SecRule文本更新函数 ---------'''
def rule_text_update():
    _new_rule = f"""\
SecRule {VARIABLES} {OPERATORS}\\
    {ID},\\
    {T},\\
    {MSG},\\
    {OTHER_ACTION},\\
    "
"""
    currentRule.set(_new_rule)
    ruleText.delete("1.0", "end")
    ruleText.insert(tk.INSERT, currentRule.get())


'''--------- SecRule文本显示面板 ---------'''
RulePane = tk.PanedWindow(window, width=520, height=300, borderwidth=20)
currentRule = tk.StringVar()
ruleText = tk.Text(RulePane, width=300, height=100, padx=10, pady=10, undo=True)
rule_text_update()
RulePane.add(ruleText)
RulePane.grid()

'''--------- 规则说明 ---------'''
# id
def add_id(*args):
    global ID
    _id = IdEntry.get()
    ID = "id:" + _id
    rule_text_update()
# 规则说明
def add_msg(*args):
    global MSG
    _msg = IdEntry.get()
    MSG = "msg:" + _msg
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
    _request_all = cb_cookies.get()
    _file = cb_file.get()
    _xml = cb_xml.get()

    if _request_headers != "":
        # 判断当前是否有至少一个变量对象
        if _have_one == 0:
            _variables += "REQUEST_HEADERS"
            _have_one = 1
        # 若当前已有变量，则添加 “|” 作为分隔符
        else:
            _variables += "|"
            _variables += "REQUEST_HEADERS"
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
    if _request_all != "":
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
MATCH_Label = tk.Label(text="--- 检测对象 ---")
MATCH_boundary.grid()
MATCH_boundary.add(MATCH_Label)

MatchPane = tk.PanedWindow(window, width=520)

cb_request_headers = tk.StringVar()
cb_args = tk.StringVar()
cb_remote_addr = tk.StringVar()
cb_cookies = tk.StringVar()
cb_file = tk.StringVar()
cb_xml = tk.StringVar()
MatchPaneCheckButton1 = tk.Checkbutton(MatchPane, text='REQUEST_HEADERS', variable=cb_request_headers,
                                       onvalue="REQUEST_HEADERS", offvalue="", command=add_variables)
MatchPaneCheckButton2 = tk.Checkbutton(MatchPane, text='ARGS', variable=cb_args, onvalue="ARGS", offvalue="",
                                       command=add_variables)
MatchPaneCheckButton3 = tk.Checkbutton(MatchPane, text='REMOTE_ADDR', variable=cb_remote_addr, onvalue="REMOTE_ADDR",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton4 = tk.Checkbutton(MatchPane, text='COOKIES', variable=cb_cookies, onvalue="COOKIES",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton5 = tk.Checkbutton(MatchPane, text='FILE_UPLOAD', variable=cb_file, onvalue="FILE",
                                       offvalue="", command=add_variables)
MatchPaneCheckButton6 = tk.Checkbutton(MatchPane, text='XML', variable=cb_xml, onvalue="XML",
                                       offvalue="", command=add_variables)

MatchPane.grid()
MatchPaneCheckButton1.grid(row=0, column=0, sticky='w', padx=20)
MatchPaneCheckButton2.grid(row=1, column=0, sticky='w', padx=20)
MatchPaneCheckButton3.grid(row=2, column=0, sticky='w', padx=20)
MatchPaneCheckButton4.grid(row=0, column=1, sticky='w', padx=20)
MatchPaneCheckButton5.grid(row=1, column=1, sticky='w', padx=20)
MatchPaneCheckButton6.grid(row=2, column=1, sticky='w', padx=20)


'''--------- 运算符 ---------'''


# 鼠标聚焦后清空文本框
def on_focus(*args):
    variable_operator.set("")


# 根据ComboBox选择更改提示内容
def combox_select(*args):
    _select = OperatorPaneComboBox.get()
    if _select == "@rx":
        variable_operator.set("<请在此输入正则表达式>")
    elif _select == "@contains":
        variable_operator.set("<请在此输入包含的内容>")
    elif _select == "@beginsWith":
        variable_operator.set("<请在此输入起始字符串>")
    elif _select == "@ipMatch":
        variable_operator.set("<请在此输入目标IP地址>")


# 确认添加内容
def add_operators(*args):
    global OPERATORS
    _operators = "\"" + OperatorPaneComboBox.get() + " " + variable_operator.get() + "\""
    OPERATORS = _operators
    rule_text_update()



OPERATOR_boundary = tk.PanedWindow(window, width=520, height=30)
sep=Separator(OPERATOR_boundary, orient=tk.HORIZONTAL) #HORIZONTAL建立水平分隔线，VERTICAL建立垂直分隔线
OPERATOR_Label = tk.Label(OPERATOR_boundary, text="--- 匹配内容 ---")
OPERATOR_boundary.grid()
OPERATOR_boundary.add(OPERATOR_Label)

OperatorPane = tk.PanedWindow(window, width=520, orient='horizontal')

com_operator = tk.StringVar()
com_operator.set("请选择运算符")
OperatorPaneComboBox = ttk.Combobox(OperatorPane, width=15, textvariable=com_operator, state='readonly')
OperatorPaneComboBox["values"] = ("@rx", "@contains", "@beginsWith", "@ipMatch")
OperatorPaneComboBox.bind("<<ComboboxSelected>>", combox_select)

variable_operator = tk.StringVar()
OperatorPaneEntry = tk.Entry(OperatorPane, width=35, textvariable=variable_operator)
OperatorPaneEntry.bind("<FocusIn>", on_focus)
variable_operator.trace('w', add_operators)

OperatorPane.grid()
OperatorPaneComboBox.grid(row=0, column=0, sticky='w', padx=20)
OperatorPaneEntry.grid(row=0, column=1)



'''--------- ACTIONS ---------'''

ACTIONS_boundary = tk.PanedWindow(window, width=520, height=30)
ACTIONS_Label = tk.Label(text="--- 数据处理 ---")
ACTIONS_boundary.grid()
ACTIONS_boundary.add(ACTIONS_Label)

# t
TPane = tk.PanedWindow(window, width=520, orient='horizontal')
def add_t(_value):
    global T, T_LIST
    _t = "t:none,"
    _t_list = [cb_t_htmlentitydecode.get(), cb_t_lowercase.get(), cb_t_removenulls.get(), cb_t_urldecodeuni.get(), cb_t_normalisepath.get(), cb_t_cmdline.get()]
    if _value not in T_LIST:
        T_LIST.append(_value)
    for t in T_LIST:
        if t in _t_list:
            _t += "t:" + t + ","
    T = _t
    rule_text_update()

cb_t_htmlentitydecode = tk.StringVar()
cb_t_lowercase = tk.StringVar()
cb_t_removenulls = tk.StringVar()
cb_t_urldecodeuni = tk.StringVar()
cb_t_normalisepath = tk.StringVar()
cb_t_cmdline = tk.StringVar()
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
TPane.grid()
TCheckButton1.grid(row=0, column=0, sticky='w')
TCheckButton2.grid(row=0, column=1, sticky='w')
TCheckButton3.grid(row=0, column=2, sticky='w')
TCheckButton4.grid(row=1, column=0, sticky='w')
TCheckButton5.grid(row=1, column=1, sticky='w')
TCheckButton6.grid(row=1, column=2, sticky='w')




# msg

# tag

# severity

# setvar

ActionsPaneButton = tk.Button(OperatorPane, text="生成默认动作")





'''--------- Chain ---------'''

CHAIN_boundary = tk.PanedWindow(window, width=520, height=30)
CHAIN_Label = tk.Label(text="--- 规则链 ---")
CHAIN_boundary.grid()
CHAIN_boundary.add(CHAIN_Label)

window.mainloop()
