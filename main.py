# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter.messagebox import *

window = tk.Tk()
window.title('防火墙配置文件初始化')
window.geometry("600x800")
canvas = tk.Canvas(master=window, width=600, height=800)
scroll = tk.Scrollbar(master=window)
scroll.pack(side='right', fill='y')
canvas.pack(side='right')
frame = tk.Frame(canvas)
frame.pack()
canvas.create_window((100, 100), window=frame, anchor='center')
help_img = tk.PhotoImage(file="help.png")

'''-- Rule engine initialization --'''
RULE_Boundary = tk.PanedWindow(frame, width=460, height=40)
RULELabel = tk.Label(text="*** 规则引擎初始化 ***")
RULE_Boundary.grid()
RULE_Boundary.add(RULELabel)


# SecEngine开启
def close_warning():
    sec_mx1 = showwarning(title="警告", message="确认关闭防火墙 ？")
def detection_warning():
    sec_mx2 = showwarning(title="警告", message="确认防火墙开启仅监控模式 ？\n此模式下不会阻断任何数据")

SecEngine = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecEngine, width=200, height=35)
rightPane = tk.PanedWindow(SecEngine, width=260, height=35)
SecEngineLabel = tk.Label(text="开启防火墙")
se_model = tk.IntVar()
SecEngineEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=se_model)
SecEngineEntry2 = tk.Radiobutton(frame, text='仅监控', value=2, variable=se_model, command=detection_warning)
SecEngineEntry3 = tk.Radiobutton(frame, text='关闭', value=3, variable=se_model, command=close_warning)
se_model.set(1)
SecEngine.grid()
SecEngine.add(leftPane)
SecEngine.add(rightPane)
leftPane.add(SecEngineLabel)
rightPane.add(SecEngineEntry1)
rightPane.add(SecEngineEntry2)
rightPane.add(SecEngineEntry3)



'''--------------------------- Request body handling ---------------------------'''
REQUEST_Boundary = tk.PanedWindow(frame, width=460, height=40)
REQUESTLabel = tk.Label(text="*** 请求体限制 ***")
REQUEST_Boundary.grid()
REQUEST_Boundary.add(REQUESTLabel)


# 请求体访问
# 关闭请求访问后，无法操作参数信息
def request_close():
    variable_SecRequestBodyLimit.set("--关闭--")
    SecRequestBodyLimitEntry['state'] = 'disable'

    variable_SecRequestBodyNoFilesLimit.set("--关闭--")
    SecRequestBodyNoFilesLimitEntry['state'] = 'disable'

    srbl_action.set(0)
    SecRequestBodyLimitActionEntry1['state'] = 'disable'
    SecRequestBodyLimitActionEntry2['state'] = 'disable'

    variable_SecRequestBodyJsonDepthLimit.set("--关闭--")
    SecRequestBodyJsonDepthLimitEntry['state'] = 'disable'

    variable_SecArgumentsLimit.set("--关闭--")
    SecArgumentsLimitEntry['state'] = 'disable'

    variable_SecPcreMatchLimit.set("--关闭--")
    SecPcreMatchLimitEntry['state'] = 'disable'

    variable_SecPcreMatchLimitRecursion.set("--关闭--")
    SecPcreMatchLimitRecursionEntry['state'] = 'disable'


def request_open():
    variable_SecRequestBodyLimit.set("13107200")
    SecRequestBodyLimitEntry['state'] = 'normal'

    variable_SecRequestBodyNoFilesLimit.set("131072")
    SecRequestBodyNoFilesLimitEntry['state'] = 'normal'

    srbl_action.set(1)
    SecRequestBodyLimitActionEntry1['state'] = 'normal'
    SecRequestBodyLimitActionEntry2['state'] = 'normal'

    variable_SecRequestBodyJsonDepthLimit.set("512")
    SecRequestBodyJsonDepthLimitEntry['state'] = 'normal'

    variable_SecArgumentsLimit.set("1000")
    SecArgumentsLimitEntry['state'] = 'normal'

    variable_SecPcreMatchLimit.set("1000")
    SecPcreMatchLimitEntry['state'] = 'normal'

    variable_SecPcreMatchLimitRecursion.set("1000")
    SecPcreMatchLimitRecursionEntry['state'] = 'normal'


SecRequestBodyAccess = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRequestBodyAccess, width=200, height=35)
rightPane = tk.PanedWindow(SecRequestBodyAccess, width=260, height=35)
SecRequestBodyAccessLabel = tk.Label(text="允许访问请求体")
sra_open = tk.IntVar()
SecRequestBodyAccessEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=sra_open, command=request_open)
SecRequestBodyAccessEntry2 = tk.Radiobutton(frame, text='关闭', value=2, variable=sra_open, command=request_close)
sra_open.set(1)
SecRequestBodyAccess.grid()
SecRequestBodyAccess.add(leftPane)
SecRequestBodyAccess.add(rightPane)
leftPane.add(SecRequestBodyAccessLabel)
rightPane.add(SecRequestBodyAccessEntry1)
rightPane.add(SecRequestBodyAccessEntry2)

# 请求体大小限制
SecRequestBodyLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRequestBodyLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecRequestBodyLimit, width=260, height=35)
SecRequestBodyLimitLabel = tk.Label(text="请求体大小限制(Byte)")
variable_SecRequestBodyLimit = tk.StringVar()
variable_SecRequestBodyLimit.set("13107200")
SecRequestBodyLimitEntry = tk.Entry(frame, text=variable_SecRequestBodyLimit)
SecRequestBodyLimit.grid()
SecRequestBodyLimit.add(leftPane)
SecRequestBodyLimit.add(rightPane)
leftPane.add(SecRequestBodyLimitLabel)
rightPane.add(SecRequestBodyLimitEntry, padx=20, pady=5)

# 无上传文件下的请求体大小限制
SecRequestBodyNoFilesLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRequestBodyNoFilesLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecRequestBodyNoFilesLimit, width=260, height=35)
SecRequestBodyNoFilesLimitLabel = tk.Label(text="无上传文件下请求体大小限制(Byte)")
variable_SecRequestBodyNoFilesLimit = tk.StringVar()
variable_SecRequestBodyNoFilesLimit.set("131072")
SecRequestBodyNoFilesLimitEntry = tk.Entry(frame, text=variable_SecRequestBodyNoFilesLimit)
SecRequestBodyNoFilesLimit.grid()
SecRequestBodyNoFilesLimit.add(leftPane)
SecRequestBodyNoFilesLimit.add(rightPane)
leftPane.add(SecRequestBodyNoFilesLimitLabel)
rightPane.add(SecRequestBodyNoFilesLimitEntry, padx=20, pady=5)

# 请求体大小超限操作
SecRequestBodyLimitAction = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRequestBodyLimitAction, width=200, height=35)
rightPane = tk.PanedWindow(SecRequestBodyLimitAction, width=260, height=35)
SecRequestBodyLimitActionLabel = tk.Label(text="请求体大小超限操作")
srbl_action = tk.IntVar()
SecRequestBodyLimitActionEntry1 = tk.Radiobutton(frame, text='拒绝', value=1, variable=srbl_action)
SecRequestBodyLimitActionEntry2 = tk.Radiobutton(frame, text='呈现请求第一部分', value=2, variable=srbl_action)
srbl_action.set(1)
SecRequestBodyLimitAction.grid()
SecRequestBodyLimitAction.add(leftPane)
SecRequestBodyLimitAction.add(rightPane)
leftPane.add(SecRequestBodyLimitActionLabel)
rightPane.add(SecRequestBodyLimitActionEntry1)
rightPane.add(SecRequestBodyLimitActionEntry2)

# JSON对象深度
SecRequestBodyJsonDepthLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRequestBodyJsonDepthLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecRequestBodyJsonDepthLimit, width=260, height=35)
SecRequestBodyJsonDepthLimitLabel = tk.Label(text="JSON对象深度")
variable_SecRequestBodyJsonDepthLimit = tk.StringVar()
variable_SecRequestBodyJsonDepthLimit.set("512")
SecRequestBodyJsonDepthLimitEntry = tk.Entry(frame, text=variable_SecRequestBodyJsonDepthLimit)
SecRequestBodyJsonDepthLimit.grid()
SecRequestBodyJsonDepthLimit.add(leftPane)
SecRequestBodyJsonDepthLimit.add(rightPane)
leftPane.add(SecRequestBodyJsonDepthLimitLabel)
rightPane.add(SecRequestBodyJsonDepthLimitEntry, padx=20, pady=5)

# 请求参数数量
SecArgumentsLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecArgumentsLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecArgumentsLimit, width=260, height=35)
SecArgumentsLimitLabel = tk.Label(text="请求参数数量")
variable_SecArgumentsLimit = tk.StringVar()
variable_SecArgumentsLimit.set("1000")
SecArgumentsLimitEntry = tk.Entry(frame, text=variable_SecArgumentsLimit)
SecArgumentsLimit.grid()
SecArgumentsLimit.add(leftPane)
SecArgumentsLimit.add(rightPane)
leftPane.add(SecArgumentsLimitLabel)
rightPane.add(SecArgumentsLimitEntry, padx=20, pady=5)

# PCRE库匹配限制
def help_pcre():
    pcre_mx = showinfo(title="PCRE库匹配限制说明", message="用于防止潜在的基于正则匹配的DOS攻击")
SecPcreMatchLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecPcreMatchLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecPcreMatchLimit, width=260, height=35)
btnHelpPCRE = tk.Button(frame, image=help_img, command=help_pcre)
SecPcreMatchLimitLabel = tk.Label(text="PCRE库匹配限制")
variable_SecPcreMatchLimit = tk.StringVar()
variable_SecPcreMatchLimit.set("1000")
SecPcreMatchLimitEntry = tk.Entry(frame, text=variable_SecPcreMatchLimit)
SecPcreMatchLimit.grid()
SecPcreMatchLimit.add(leftPane, padx=35, width=130, sticky='e')
SecPcreMatchLimit.add(rightPane)
leftPane.add(SecPcreMatchLimitLabel)
leftPane.add(btnHelpPCRE, width=23, height=23, sticky='w')
rightPane.add(SecPcreMatchLimitEntry, padx=20, pady=5)

# PCRE库匹配递归限制
SecPcreMatchLimitRecursion = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecPcreMatchLimitRecursion, width=200, height=35)
rightPane = tk.PanedWindow(SecPcreMatchLimitRecursion, width=260, height=35)
SecPcreMatchLimitRecursionLabel = tk.Label(text="PCRE库匹配递归限制")
variable_SecPcreMatchLimitRecursion = tk.StringVar()
variable_SecPcreMatchLimitRecursion.set("1000")
SecPcreMatchLimitRecursionEntry = tk.Entry(frame, text=variable_SecPcreMatchLimitRecursion)
SecPcreMatchLimitRecursion.grid()
SecPcreMatchLimitRecursion.add(leftPane)
SecPcreMatchLimitRecursion.add(rightPane)
leftPane.add(SecPcreMatchLimitRecursionLabel)
rightPane.add(SecPcreMatchLimitRecursionEntry, padx=20, pady=5)



'''-- Response body handling --'''
RESPONSE_Boundary = tk.PanedWindow(frame, width=460, height=40)
RESPONSELabel = tk.Label(text="*** 响应体限制 ***")
RESPONSE_Boundary.grid()
RESPONSE_Boundary.add(RESPONSELabel)


# 允许访问响应体
# 关闭请求访问后，无法操作参数信息
def response_close():
    SecResponseBodyMimeTypeEntry1['state'] = 'disable'
    SecResponseBodyMimeTypeEntry2['state'] = 'disable'
    SecResponseBodyMimeTypeEntry3['state'] = 'disable'

    variable_SecResponseBodyLimit.set('--关闭--')
    SecResponseBodyLimitEntry['state'] = 'disable'

    srpl_action.set(0)
    SecResponseBodyLimitActionEntry1['state'] = 'disable'
    SecResponseBodyLimitActionEntry2['state'] = 'disable'


def response_open():
    SecResponseBodyMimeTypeEntry1['state'] = 'normal'
    SecResponseBodyMimeTypeEntry2['state'] = 'normal'
    SecResponseBodyMimeTypeEntry3['state'] = 'normal'

    variable_SecResponseBodyLimit.set('524288')
    SecResponseBodyLimitEntry['state'] = 'normal'

    srpl_action.set(1)
    SecResponseBodyLimitActionEntry1['state'] = 'normal'
    SecResponseBodyLimitActionEntry2['state'] = 'normal'


SecResponseBodyAccess = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecResponseBodyAccess, width=200, height=35)
rightPane = tk.PanedWindow(SecResponseBodyAccess, width=260, height=35)
SecResponseBodyAccessLabel = tk.Label(text="允许访问请求体")
srp_open = tk.IntVar()
SecResponseBodyAccessEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=srp_open, command=response_open)
SecResponseBodyAccessEntry2 = tk.Radiobutton(frame, text='关闭', value=2, variable=srp_open, command=response_close)
srp_open.set(1)
SecResponseBodyAccess.grid()
SecResponseBodyAccess.add(leftPane)
SecResponseBodyAccess.add(rightPane)
leftPane.add(SecResponseBodyAccessLabel)
rightPane.add(SecResponseBodyAccessEntry1)
rightPane.add(SecResponseBodyAccessEntry2)

# 响应体的资源类型
SecResponseBodyMimeType = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecResponseBodyMimeType, width=200, height=35)
rightPane = tk.PanedWindow(SecResponseBodyMimeType, width=260, height=35)
SecResponseBodyMimeTypeLabel = tk.Label(text="响应体的资源类型")
cb_plain = tk.StringVar(value="text/plain")
cb_html = tk.StringVar(value="text/html")
cb_xml = tk.StringVar(value="text/xml")
SecResponseBodyMimeTypeEntry1 = tk.Checkbutton(frame, text='text/plain', variable=cb_plain, onvalue="text/plain")
SecResponseBodyMimeTypeEntry2 = tk.Checkbutton(frame, text='text/html', variable=cb_html, onvalue="text/html")
SecResponseBodyMimeTypeEntry3 = tk.Checkbutton(frame, text='text/xml', variable=cb_xml, onvalue="text/xml")
SecResponseBodyMimeType.grid()
SecResponseBodyMimeType.add(leftPane)
SecResponseBodyMimeType.add(rightPane)
leftPane.add(SecResponseBodyMimeTypeLabel)
rightPane.add(SecResponseBodyMimeTypeEntry1)
rightPane.add(SecResponseBodyMimeTypeEntry2)
rightPane.add(SecResponseBodyMimeTypeEntry3)

# 响应体大小限制
SecResponseBodyLimit = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecResponseBodyLimit, width=200, height=35)
rightPane = tk.PanedWindow(SecResponseBodyLimit, width=260, height=35)
SecResponseBodyLimitLabel = tk.Label(text="响应体大小限制(Byte)")
variable_SecResponseBodyLimit = tk.StringVar()
variable_SecResponseBodyLimit.set('524288')
SecResponseBodyLimitEntry = tk.Entry(frame, text=variable_SecResponseBodyLimit)
SecResponseBodyLimit.grid()
SecResponseBodyLimit.add(leftPane)
SecResponseBodyLimit.add(rightPane)
leftPane.add(SecResponseBodyLimitLabel)
rightPane.add(SecResponseBodyLimitEntry, padx=20, pady=5)

# 响应体大小超限操作
SecResponseBodyLimitAction = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecResponseBodyLimitAction, width=200, height=35)
rightPane = tk.PanedWindow(SecResponseBodyLimitAction, width=260, height=35)
SecResponseBodyLimitActionLabel = tk.Label(text="响应体大小超限操作")
srpl_action = tk.IntVar()
SecResponseBodyLimitActionEntry1 = tk.Radiobutton(frame, text='拒绝', value=1, variable=srpl_action)
SecResponseBodyLimitActionEntry2 = tk.Radiobutton(frame, text='呈现请求第一部分', value=2, variable=srpl_action)
srpl_action.set(1)
SecResponseBodyLimitAction.grid()
SecResponseBodyLimitAction.add(leftPane)
SecResponseBodyLimitAction.add(rightPane)
leftPane.add(SecResponseBodyLimitActionLabel)
rightPane.add(SecResponseBodyLimitActionEntry1)
rightPane.add(SecResponseBodyLimitActionEntry2)



'''-- Filesystem configuration --'''
FILESYSTEM_Boundary = tk.PanedWindow(frame, width=460, height=40)
FILESYSTEMLabel = tk.Label(text="*** 文件系统配置 ***")
FILESYSTEM_Boundary.grid()
FILESYSTEM_Boundary.add(FILESYSTEMLabel)

# 临时文件目录
def help_tmp():
    tmp_mx = showinfo(title="临时文件说明", message="用于存储数据处理过程中的临时文件，例如超出限制大小的上传文件。\n默认为/tmp，但更理想的选择是专门指定的private权限目录")
SecTmpDir = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecTmpDir, width=200, height=35)
rightPane = tk.PanedWindow(SecTmpDir, width=260, height=35)
btnHelpTmpDir = tk.Button(frame, image=help_img, command=help_tmp)
SecTmpDirLabel = tk.Label(text="临时文件目录")
SecTmpDirEntry = tk.Entry(frame)
SecTmpDirEntry.insert(0, "/tmp/")
SecTmpDir.grid()
SecTmpDir.add(leftPane, padx=35, width=130, sticky='e')
SecTmpDir.add(rightPane)
leftPane.add(SecTmpDirLabel)
leftPane.add(btnHelpTmpDir, width=23, height=23, sticky='w')
rightPane.add(SecTmpDirEntry, padx=20, pady=5)


# 持久性文件目录
def help_data():
    tmp_mx = showinfo(title="持久文件说明", message="ModSecurity存放持久化数据（如ip 地址数据，session 数据等）路径，initcol、setsid和setuid需要用到这个指令")
SecDataDir = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecDataDir, width=200, height=35)
rightPane = tk.PanedWindow(SecDataDir, width=260, height=35)
btnHelpTmpDir = tk.Button(frame, image=help_img, command=help_data)
SecDataDirLabel = tk.Label(text="持久文件目录")
SecDataDirEntry = tk.Entry(frame)
SecDataDirEntry.insert(0, "/tmp/")
SecDataDir.grid()
SecDataDir.add(leftPane, padx=35, width=130, sticky='e')
SecDataDir.add(rightPane)
leftPane.add(SecDataDirLabel)
leftPane.add(btnHelpTmpDir, width=23, height=23, sticky='w')
rightPane.add(SecDataDirEntry, padx=20, pady=5)



'''-- File uploads handling configuration --'''
FILEUPLOAD_Boundary = tk.PanedWindow(frame, width=600, height=40)
FILEUPLOADLabel = tk.Label(text="*** 文件上传配置 ***")
FILEUPLOAD_Boundary.grid()
FILEUPLOAD_Boundary.add(FILEUPLOADLabel)

# 是否进行上传文件配置
# 关闭上传文件配置后，无法操作参数信息
def upload_close():
    variable_SecUploadDir.set("--关闭--")
    SecUploadDirEntry['state'] = 'disable'

    sukf_model.set(0)
    SecUploadKeepFilesEntry1['state'] = 'disable'
    SecUploadKeepFilesEntry2['state'] = 'disable'
    SecUploadKeepFilesEntry3['state'] = 'disable'

    variable_SecUploadFileMode.set("--关闭--")
    SecUploadFileModeEntry['state'] = 'disable'

def upload_open():
    dbg_mx = showwarning(title="文件上传拦截说明",
                      message="文件上传配置可对用户上传文件进行拦截保存操作")
    variable_SecUploadDir.set("/opt/modsecurity/var/upload/")
    SecUploadDirEntry['state'] = 'normal'

    sukf_model.set(1)
    SecUploadKeepFilesEntry1['state'] = 'normal'
    SecUploadKeepFilesEntry2['state'] = 'normal'
    SecUploadKeepFilesEntry3['state'] = 'normal'

    variable_SecUploadFileMode.set("0600")
    SecUploadFileModeEntry['state'] = 'normal'


SecFileUploadAccess = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecFileUploadAccess, width=200, height=35)
rightPane = tk.PanedWindow(SecFileUploadAccess, width=260, height=35)
SecFileUploadAccessLabel = tk.Label(text="开启上传文件配置")
sfu_open = tk.IntVar()
SecFileUploadAccessEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=sfu_open, command=upload_open)
SecFileUploadAccessEntry2 = tk.Radiobutton(frame, text='关闭', value=2, variable=sfu_open, command=upload_close)
sfu_open.set(2)
SecFileUploadAccess.grid()
SecFileUploadAccess.add(leftPane)
SecFileUploadAccess.add(rightPane)
leftPane.add(SecFileUploadAccessLabel)
rightPane.add(SecFileUploadAccessEntry1)
rightPane.add(SecFileUploadAccessEntry2)

# 拦截文件存放目录
def help_uploadfile():
    upfi_mx = showwarning(title="权限说明", message="此存放目录必须为私有")
SecUploadDir = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecUploadDir, width=200, height=35)
rightPane = tk.PanedWindow(SecUploadDir, width=260, height=35)
btnHelpUploadFile = tk.Button(frame, image=help_img, command=help_uploadfile)
variable_SecUploadDir = tk.StringVar()
variable_SecUploadDir.set("/opt/modsecurity/var/upload/")
SecUploadDirLabel = tk.Label(text="拦截文件存放目录")
SecUploadDirEntry = tk.Entry(frame, text=variable_SecUploadDir)
SecUploadDir.grid()
SecUploadDir.add(leftPane, padx=35, width=130, sticky='e')
SecUploadDir.add(rightPane)
leftPane.add(SecUploadDirLabel)
leftPane.add(btnHelpUploadFile, width=23, height=23, sticky='w')
rightPane.add(SecUploadDirEntry, padx=20, pady=5)

# 选择保存文件类型
def warning_uploadclose():
    upcl_mx = showwarning(title="提示", message="此选择下将不会保存事务处理后的拦截文件，在事务处理完成后会自动删除")
def warning_upoloadon():
    upon_mx = showwarning(title="提示", message="此选择下将会保存所有用户上传文件，注意可能引起的磁盘占用问题")
def warning_upoloadrelevant():
    upre_mx = showwarning(title="提示", message="此选择下仅会保存可疑请求下的上传文件")
SecUploadKeepFiles = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecUploadKeepFiles, width=200, height=35)
rightPane = tk.PanedWindow(SecUploadKeepFiles, width=260, height=35)
SecUploadKeepFilesLabel = tk.Label(text="是否保存上传文件")
sukf_model = tk.IntVar()
SecUploadKeepFilesEntry1 = tk.Radiobutton(frame, text='仅相关', value=1, variable=sukf_model, command=warning_upoloadrelevant)
SecUploadKeepFilesEntry2 = tk.Radiobutton(frame, text='全部', value=2, variable=sukf_model, command=warning_upoloadon)
SecUploadKeepFilesEntry3 = tk.Radiobutton(frame, text='关闭', value=3, variable=sukf_model, command=warning_uploadclose)
sukf_model.set(1)
SecUploadKeepFiles.grid()
SecUploadKeepFiles.add(leftPane)
SecUploadKeepFiles.add(rightPane)
leftPane.add(SecUploadKeepFilesLabel)
rightPane.add(SecUploadKeepFilesEntry1)
rightPane.add(SecUploadKeepFilesEntry2)
rightPane.add(SecUploadKeepFilesEntry3)

# 配置上传文件权限模式
def help_auth():
    auth_mx = showinfo(title="权限说明", message="此处等同于Linux下权限表示方式：\n四位数，每一位分别表示gid/uid、owner、group、other的权限。\n"
                                             "每一位十进制数字转换为三位二进制数，分别表示r-w-x权限。\n"
                                             "如 0600 => 110 表示owner有读写权限，无执行权限，其余人无权限。\n"
                                             "上传文件默认不允许其他用户访问，但某些情况可能需要放开设置(例如需要ModSecurity接入外部程序如anti-virus)")
SecUploadFileMode = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecUploadFileMode, width=200, height=35)
rightPane = tk.PanedWindow(SecUploadFileMode, width=260, height=35)
btnHelpAuth = tk.Button(frame, image=help_img, command=help_auth)
SecUploadFileModeLabel = tk.Label(text="配置上传文件权限模式")
variable_SecUploadFileMode = tk.StringVar()
variable_SecUploadFileMode.set("0600")
SecUploadFileModeEntry = tk.Entry(frame, text=variable_SecUploadFileMode)
SecUploadFileMode.grid()
SecUploadFileMode.add(leftPane, padx=20, width=160, sticky='e')
SecUploadFileMode.add(rightPane)
leftPane.add(SecUploadFileModeLabel)
leftPane.add(btnHelpAuth, width=23, height=23, sticky='w')
rightPane.add(SecUploadFileModeEntry, padx=20, pady=5)

upload_close()



'''-- Debug log configuration --'''
DEBUGLOG_Boundary = tk.PanedWindow(frame, width=460, height=40)
DEBUGLOGLabel = tk.Label(text="*** 调试日志设置 ***")
DEBUGLOG_Boundary.grid()
DEBUGLOG_Boundary.add(DEBUGLOGLabel)

def debug_open():
    dbg_mx = showwarning(title="调试日志及说明",
                      message="开启调试日志会提供丰富的ModSecurity操作细节.\n注意由于其对性能存在消极影响，默认一般推荐为关闭状态")

    SecDebugLogEntry['state'] = 'normal'
    variable_SecDebugLog.set("/opt/modsecurity/var/log/debug.log")

    SecDebugLogLevelEntry0['state'] = 'normal'
    SecDebugLogLevelEntry1['state'] = 'normal'
    SecDebugLogLevelEntry2['state'] = 'normal'
    SecDebugLogLevelEntry3['state'] = 'normal'
    SecDebugLogLevelEntry4['state'] = 'normal'
    SecDebugLogLevelEntry5['state'] = 'normal'
    SecDebugLogLevelEntry9['state'] = 'normal'
    sdll_model.set('3')

def debug_close():
    SecDebugLogEntry['state'] = 'disable'
    variable_SecDebugLog.set("--关闭--")

    SecDebugLogLevelEntry0['state'] = 'disable'
    SecDebugLogLevelEntry1['state'] = 'disable'
    SecDebugLogLevelEntry2['state'] = 'disable'
    SecDebugLogLevelEntry3['state'] = 'disable'
    SecDebugLogLevelEntry4['state'] = 'disable'
    SecDebugLogLevelEntry5['state'] = 'disable'
    SecDebugLogLevelEntry9['state'] = 'disable'
    sdll_model.set('10')

# 开启调试日志
SecDebugLogAccess = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecDebugLogAccess, width=200, height=35)
rightPane = tk.PanedWindow(SecDebugLogAccess, width=260, height=35)
SecDebugLogAccessLabel = tk.Label(text="开启调试日志")
sdl_open = tk.IntVar()
SecDebugLogAccessEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=sdl_open, command=debug_open)
SecDebugLogAccessEntry2 = tk.Radiobutton(frame, text='关闭', value=2, variable=sdl_open, command=debug_close)
sdl_open.set(2)
SecDebugLogAccess.grid()
SecDebugLogAccess.add(leftPane)
SecDebugLogAccess.add(rightPane)
leftPane.add(SecDebugLogAccessLabel)
rightPane.add(SecDebugLogAccessEntry1)
rightPane.add(SecDebugLogAccessEntry2)

# 调试日志保存位置
SecDebugLog = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecDebugLog, width=200, height=35)
rightPane = tk.PanedWindow(SecDebugLog, width=260, height=35)
SecDebugLogLabel = tk.Label(text="调试日志保存位置")
variable_SecDebugLog = tk.StringVar()
variable_SecDebugLog.set("/opt/modsecurity/var/log/debug.log")
SecDebugLogEntry = tk.Entry(frame, text=variable_SecDebugLog)
SecDebugLog.grid()
SecDebugLog.add(leftPane)
SecDebugLog.add(rightPane)
leftPane.add(SecDebugLogLabel)
rightPane.add(SecDebugLogEntry, padx=20, pady=5)


# 日志记录等级
def helpDebugLogLevel():
    newWindow = tk.Toplevel(window)
    newWindow.geometry("500x300")
    newWindow.title("日志记录等级说明")
    helpText = tk.Text(newWindow, padx=20, pady=20)
    helpText.pack()
    helpText.insert(tk.INSERT, "\
0: no logging\n\n\
1: errors (intercepted requests) only\n\n\
2: warnings\n\n\
3: notices\n\n\
4: details of how transactions are handled\n\n\
5: as above, but including information about each piece of information handled\n\n\
9: log everything, including very detailed debugging information\n\n")
    helpText.config(state=tk.DISABLED)

def performance_warning():
    pf_mx = showwarning(title="警告",
                      message="实际产品中应谨慎使用过高等级的日志记录，该行为会对性能造成较大的影响")

SecDebugLogLevel = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecDebugLogLevel, width=120, height=35)
rightPane = tk.PanedWindow(SecDebugLogLevel, width=340, height=35)
SecDebugLogLevelLabel = tk.Label(text="日志记录等级")
btnHelpDebugLog = tk.Button(frame, image=help_img, command=helpDebugLogLevel)
sdll_model = tk.IntVar()
SecDebugLogLevelEntry0 = tk.Radiobutton(frame, text='0', value=0, variable=sdll_model)
SecDebugLogLevelEntry1 = tk.Radiobutton(frame, text='1', value=1, variable=sdll_model)
SecDebugLogLevelEntry2 = tk.Radiobutton(frame, text='2', value=2, variable=sdll_model)
SecDebugLogLevelEntry3 = tk.Radiobutton(frame, text='3', value=3, variable=sdll_model)
SecDebugLogLevelEntry4 = tk.Radiobutton(frame, text='4', value=4, variable=sdll_model, command=performance_warning)
SecDebugLogLevelEntry5 = tk.Radiobutton(frame, text='5', value=5, variable=sdll_model, command=performance_warning)
SecDebugLogLevelEntry9 = tk.Radiobutton(frame, text='9', value=9, variable=sdll_model, command=performance_warning)
sdll_model.set(3)
SecDebugLogLevel.grid()
SecDebugLogLevel.add(leftPane, padx=42, width=110, sticky='e')
SecDebugLogLevel.add(rightPane)
leftPane.add(SecDebugLogLevelLabel)
leftPane.add(btnHelpDebugLog, width=23, height=23, sticky='w')
rightPane.add(SecDebugLogLevelEntry0)
rightPane.add(SecDebugLogLevelEntry1)
rightPane.add(SecDebugLogLevelEntry2)
rightPane.add(SecDebugLogLevelEntry3)
rightPane.add(SecDebugLogLevelEntry4)
rightPane.add(SecDebugLogLevelEntry5)
rightPane.add(SecDebugLogLevelEntry9)

debug_close()



'''-- Audit log configuration --'''
AUDITLOG_Boundary = tk.PanedWindow(frame, width=460, height=40)
AUDITLOGLabel = tk.Label(text="*** 审计日志设置 ***")
AUDITLOG_Boundary.grid()
AUDITLOG_Boundary.add(AUDITLOGLabel)

def audit_close():
    showinfo(title="提示", message="此选项下会关闭审计日志")
    SecAuditLogRelevantStatusEntry['state'] = 'disable'
    variable_SecAuditLogRelevantStatus.set("--关闭--")

    SecAuditLogPartsEntry['state'] = 'disable'
    variable_SecAuditLogParts.set("--关闭--")

    SecAuditLogTypeEntry1['state'] = 'disable'
    SecAuditLogTypeEntry2['state'] = 'disable'
    salt_model.set(0)

    SecAuditLogEntry['state'] = 'disable'
    fileordir.set("--关闭--")

def audit_relevant():
    showinfo(title="提示", message="此选项下仅会记录触发告警或符合下方状态码的事务")
    SecAuditLogRelevantStatusEntry['state'] = 'normal'
    variable_SecAuditLogRelevantStatus.set("\"^(?:5|4(?!04))\"")

    SecAuditLogPartsEntry['state'] = 'normal'
    variable_SecAuditLogParts.set("ABIJDEFHZ")

    SecAuditLogTypeEntry1['state'] = 'normal'
    SecAuditLogTypeEntry2['state'] = 'normal'
    salt_model.set(1)

    SecAuditLogEntry['state'] = 'normal'
    fileordir.set("/var/log/modsec_audit.log")

def audit_open():
    showinfo(title="提示", message="此选项下会记录所有事务，适用于调试")
    SecAuditLogRelevantStatusEntry['state'] = 'normal'
    variable_SecAuditLogRelevantStatus.set("\"^(?:5|4(?!04))\"")

    SecAuditLogPartsEntry['state'] = 'normal'
    variable_SecAuditLogParts.set("ABIJDEFHZ")

    SecAuditLogTypeEntry1['state'] = 'normal'
    SecAuditLogTypeEntry2['state'] = 'normal'
    salt_model.set(1)

    SecAuditLogEntry['state'] = 'normal'
    fileordir.set("/var/log/modsec_audit.log")

# 日志记录类型
SecAuditEngine = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditEngine, width=200, height=35)
rightPane = tk.PanedWindow(SecAuditEngine, width=260, height=35)
SecAuditEngineLabel = tk.Label(text="日志记录类型")
sae_model = tk.IntVar()
SecAuditEngineEntry1 = tk.Radiobutton(frame, text='仅相关', value=1, variable=sae_model, command=audit_relevant)
SecAuditEngineEntry2 = tk.Radiobutton(frame, text='全部', value=2, variable=sae_model, command=audit_open)
SecAuditEngineEntry3 = tk.Radiobutton(frame, text='关闭', value=3, variable=sae_model, command=audit_close)
sae_model.set(1)
SecAuditEngine.grid()
SecAuditEngine.add(leftPane)
SecAuditEngine.add(rightPane)
leftPane.add(SecAuditEngineLabel)
rightPane.add(SecAuditEngineEntry1)
rightPane.add(SecAuditEngineEntry2)
rightPane.add(SecAuditEngineEntry3)

# 事务状态记录规则
SecAuditLogRelevantStatus = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogRelevantStatus, width=200, height=35)
rightPane = tk.PanedWindow(SecAuditLogRelevantStatus, width=260, height=35)
SecAuditLogRelevantStatusLabel = tk.Label(text="事务状态记录规则")
variable_SecAuditLogRelevantStatus = tk.StringVar()
variable_SecAuditLogRelevantStatus.set("\"^(?:5|4(?!04))\"")
SecAuditLogRelevantStatusEntry = tk.Entry(frame, text=variable_SecAuditLogRelevantStatus)
SecAuditLogRelevantStatus.grid()
SecAuditLogRelevantStatus.add(leftPane)
SecAuditLogRelevantStatus.add(rightPane)
leftPane.add(SecAuditLogRelevantStatusLabel)
rightPane.add(SecAuditLogRelevantStatusEntry, padx=20, pady=5)

# 日志记录内容
def helpAuditLogParts():
    newWindow = tk.Toplevel(window)
    newWindow.geometry("600x400")
    newWindow.title("日志记录内容说明")
    helpText = tk.Text(newWindow, width=600, height=300, undo=True, padx=20, pady=20, relief=tk.RIDGE)
    helpText.pack()
    helpText.insert(tk.INSERT, "A -- 审计日志标题(强制)\n\n\
B -- 请求头 \n\n\
C -- 请求体\n\n\
D -- 中间人响应头(暂未实现)\n\n\
E -- 中间人响应体(需开启响应体限制)\n\n\
F -- 最终响应头\n\n\
G -- 响应体(暂未实现)\n\n\
H -- 审计跟踪\n\n\
I -- C部分的替换,在使用multipart/form-data编码时会记录与C相同的数据。\n但application/x-www-form-urlencoded情况下仅记录参数和假的文件体而不包含文件。\n该选项用于处理不想保存(过大)上传文件于审计日志中的情况\n\n\
J -- 文件使用multipart/form-data编码上传的信息\n\n\
K -- 包含其匹配的触发规则列表\n\n\
Z -- 最终分界，意味条目的最后(强制)\n")
    helpText.config(state=tk.DISABLED)


SecAuditLogParts = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogParts, width=120, height=35)
rightPane = tk.PanedWindow(SecAuditLogParts, width=340, height=35)
SecAuditLogPartsLabel = tk.Label(text="日志记录内容")
variable_SecAuditLogParts = tk.StringVar()
variable_SecAuditLogParts.set("ABIJDEFHZ")
SecAuditLogPartsEntry = tk.Entry(frame, text=variable_SecAuditLogParts)
btnHelpAuditLog = tk.Button(frame, image=help_img, command=helpAuditLogParts)
SecAuditLogParts.grid()
SecAuditLogParts.add(leftPane, padx=42, width=110, sticky='e')
SecAuditLogParts.add(rightPane, padx=20, width=215, height=24, sticky='es')
leftPane.add(SecAuditLogPartsLabel)
leftPane.add(btnHelpAuditLog, width=23, height=23, sticky='w')
rightPane.add(SecAuditLogPartsEntry)

# 日志记录机制
# 针对不同机制修改保存位置为文件或目录
fileordir = tk.StringVar()


def changeStroageToFile():
    showinfo(title="Serial", message="此种情况下全部记录会存于一个文件中，便于简单使用，但会由于日志输入的争用导致降低服务器性能")
    SecAuditLogLabel['text'] = "日志保存文件位置"
    fileordir.set("/var/log/modsec_audit.log")



def changeStorageToDir():
    showinfo(title="Concurrent", message="为每件事务单独创建日志记录文件，依时间分类。面对大规模日志需求下能够具备更好的扩展性(多项事务可并行记录)，同时也是远程记录时的唯一选择")
    SecAuditLogLabel['text'] = "日志保存目录位置"
    fileordir.set("/opt/modsecurity/var/audit/")



SecAuditLogType = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogType, width=200, height=35)
rightPane = tk.PanedWindow(SecAuditLogType, width=260, height=35)
SecAuditLogTypeLabel = tk.Label(text="日志记录机制")
salt_model = tk.IntVar()
SecAuditLogTypeEntry1 = tk.Radiobutton(frame, text='全部存于主记录文件', value=1, variable=salt_model,
                                       command=changeStroageToFile)
SecAuditLogTypeEntry2 = tk.Radiobutton(frame, text='事务单独文件存储', value=2, variable=salt_model, command=changeStorageToDir)
salt_model.set(1)
SecAuditLogType.grid()
SecAuditLogType.add(leftPane)
SecAuditLogType.add(rightPane)
leftPane.add(SecAuditLogTypeLabel)
rightPane.add(SecAuditLogTypeEntry1)
rightPane.add(SecAuditLogTypeEntry2)

# 日志保存位置文件/目录
SecAuditLog = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLog, width=200, height=35)
rightPane = tk.PanedWindow(SecAuditLog, width=260, height=35)
SecAuditLogLabel = tk.Label(text="日志保存文件位置")
fileordir.set("/var/log/modsec_audit.log")
SecAuditLogEntry = tk.Entry(frame, textvariable=fileordir)
SecAuditLog.grid(row=33)
SecAuditLog.add(leftPane)
SecAuditLog.add(rightPane)
leftPane.add(SecAuditLogLabel)
rightPane.add(SecAuditLogEntry, padx=20, pady=5)

'''-- SecRule configuration --'''
SECRULE_Boundary = tk.PanedWindow(frame, width=460, height=40)
SECRULELabel = tk.Label(text="*** 自定义规则设置 ***")
SECRULE_Boundary.grid()
SECRULE_Boundary.add(SECRULELabel)

# 自定义规则
SecRule = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRule, width=200, height=35)
rightPane = tk.PanedWindow(SecRule, width=260, height=35)
SecRuleLabel = tk.Label(text="自定义规则")
SecRuleEntry = tk.Entry(frame)
SecRule.grid()
SecRule.add(leftPane)
SecRule.add(rightPane)
leftPane.add(SecRuleLabel)
rightPane.add(SecRuleEntry, padx=20, pady=5)



def getInput():
    with open("ModSecurity.conf", "w+") as f:

        '''SecEngine'''
        SecEngine = se_model.get()
        content = "SecRuleEngine "
        if SecEngine == 1:
            option = "On"
        elif SecEngine == 2:
            option = "DetectionOnly"
        elif SecEngine == 3:
            option = "Off"
        input = content + option + "\n\n"
        f.writelines(input)

        '''SecRequestBodyAccess'''
        SecRequestBodyAccess = sra_open.get()
        content = "SecRequestBodyAccess "
        if SecRequestBodyAccess == 1:
            option = "On"
        elif SecRequestBodyAccess == 2:
            option = "Off"
        input = content + option + "\n\n"
        f.writelines(input)

        if SecRequestBodyAccess == 1:
            '''SecRequestBodyLimit'''
            SecRequestBodyLimit = SecRequestBodyLimitEntry.get()
            content = "SecRequestBodyLimit "
            option = SecRequestBodyLimit
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecRequestBodyNoFilesLimit'''
            SecRequestBodyNoFilesLimit = SecRequestBodyNoFilesLimitEntry.get()
            content = "SecRequestBodyNoFilesLimit "
            option = SecRequestBodyNoFilesLimit
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecRequestBodyLimitAction '''
            SecRequestBodyLimitAction = srbl_action.get()
            content = "SecRequestBodyLimitAction "
            if SecRequestBodyLimitAction == 1:
                option = "Reject"
            elif SecRequestBodyLimitAction == 2:
                option = "ProcessPartial"
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecRequestBodyJsonDepthLimit'''
            SecRequestBodyJsonDepthLimit = SecRequestBodyJsonDepthLimitEntry.get()
            content = "SecRequestBodyJsonDepthLimit "
            option = SecRequestBodyJsonDepthLimit
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecPcreMatchLimit '''
            SecPcreMatchLimit = SecPcreMatchLimitEntry.get()
            content = "SecPcreMatchLimit "
            option = SecPcreMatchLimit
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecPcreMatchLimitRecursion'''
            SecPcreMatchLimitRecursion = SecPcreMatchLimitRecursionEntry.get()
            content = "SecPcreMatchLimitRecursion "
            option = SecPcreMatchLimitRecursion
            input = content + option + "\n\n"
            f.writelines(input)

        '''SecResponseBodyAccess'''
        SecResponseBodyAccess = srp_open.get()
        content = "SecResponseBodyAccess "
        if SecResponseBodyAccess == 1:
            option = "On"
        elif SecResponseBodyAccess == 2:
            option = "Off"
        input = content + option + "\n\n"
        f.writelines(input)

        if SecResponseBodyAccess == 1:
            '''SecResponseBodyMimeType'''
            content = "SecResponseBodyMimeType "
            option = ""
            plain = cb_plain.get()
            html = cb_html.get()
            xml = cb_xml.get()
            if plain != '0':
                option += plain
                option += ' '
            if html != '0':
                option += html
                option += ' '
            if xml != '0':
                option += xml
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecResponseBodyLimit'''
            SecResponseBodyLimit = SecResponseBodyLimitEntry.get()
            content = "SecResponseBodyLimit "
            option = SecResponseBodyLimit
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecRequestBodyLimitAction '''
            SecResponseBodyLimitAction = srpl_action.get()
            content = "SecResponseBodyLimitAction "
            if SecResponseBodyLimitAction == 1:
                option = "Reject"
            elif SecResponseBodyLimitAction == 2:
                option = "ProcessPartial"
            input = content + option + "\n\n"
            f.writelines(input)

        '''SecTmpDir'''
        SecTmpDir = SecTmpDirEntry.get()
        content = "SecTmpDir "
        option = SecTmpDir
        input = content + option + "\n\n"
        f.writelines(input)

        '''SecDataDir'''
        SecDataDir = SecDataDirEntry.get()
        content = "SecDataDir "
        option = SecDataDir
        input = content + option + "\n\n"
        f.writelines(input)

        '''SecUploadAccess'''
        if sfu_open.get() == 1:
            '''SecUploadDir'''
            SecUploadDir = SecUploadDirEntry.get()
            content = "SecUploadDir "
            option = SecUploadDir
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecUploadKeepFiles'''
            SecUploadKeepFiles = sukf_model.get()
            content = "SecUploadKeepFiles "
            if SecUploadKeepFiles == 1:
                option = "RelevantOnly"
            elif SecUploadKeepFiles == 2:
                option = "On"
            elif SecUploadKeepFiles == 3:
                option = "Off"
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecUploadFileMode'''
            SecUploadFileMode = SecUploadFileModeEntry.get()
            content = "SecUploadFileMode "
            option = SecUploadFileMode
            input = content + option + "\n\n"
            f.writelines(input)

        '''SecDebugLogAccess'''
        if sdl_open.get() == 1:
            '''SecDebugLog'''
            SecDebugLog = SecDebugLogEntry.get()
            content = "SecDebugLog "
            option = SecDebugLog
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecDebugLogLevel'''
            SecDebugLogLevel = sdll_model.get()
            content = "SecDebugLogLevel "
            option = str(SecDebugLogLevel)
            input = content + option + "\n\n"
            f.writelines(input)

        '''SecAuditEngine'''
        SecAuditEngine = sae_model.get()
        content = "SecAuditEngine "
        if SecAuditEngine == 1:
            option = "RelevantOnly"
        elif SecAuditEngine == 2:
            option = "On"
        elif SecAuditEngine == 3:
            option = "Off"
        input = content + option + "\n\n"
        f.writelines(input)

        if SecAuditEngine == 1 or SecAuditEngine == 2:
            '''SecAuditLogRelevantStatus'''
            SecAuditLogRelevantStatus = SecAuditLogRelevantStatusEntry.get()
            content = "SecAuditLogRelevantStatus "
            option = SecAuditLogRelevantStatus
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecAuditLogParts'''
            SecAuditLogParts = SecAuditLogPartsEntry.get()
            content = "SecAuditLogParts "
            option = SecAuditLogParts
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecAuditLogType'''
            SecAuditLogType = salt_model.get()
            content = "SecAuditLogType "
            if SecAuditLogType == 1:
                option = "Serial"
            elif SecAuditLogType == 2:
                option = "Concurrent"
            input = content + option + "\n\n"
            f.writelines(input)

            '''SecAuditLog or SecAuditLogStorageDir'''
            SecAuditLog = SecAuditLogEntry.get()
            option = SecAuditLog
            if SecAuditLogType == 1:
                content = "SecAuditLog "
            elif SecAuditLogType == 2:
                content = "SecAuditLogStorageDir "
            input = content + option + "\n\n"
            f.writelines(input)

        '''SecRule'''
        SecRule = SecRuleEntry.get()
        if SecRule != "":
            content = "SecRule "
            option = SecRule
            input = content + option + "\n\n"
            f.writelines(input)


btnOutput = tk.Button(frame, height=1, width=10, text="OUTPUT", command=getInput, font=("Times", 10, "bold"))
btnOutput.grid(pady=50)

frame.update()
canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox("all"))
scroll.config(command=canvas.yview)
canvas.yview_moveto(0)

window.mainloop()
