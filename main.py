# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter.messagebox import *
import webbrowser

window = tk.Tk()
window.title('防火墙配置文件初始化')
window.geometry("520x800")
canvas = tk.Canvas(master=window, width=520, height=800)
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
    srbl_action.set(2)
    srpl_action.set(2)

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
SecResponseBodyMimeTypeLabel = tk.Label(text="何种资源类型的响应体")
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


'''-- File uploads handling configuration --'''
FILEUPLOAD_Boundary = tk.PanedWindow(frame, width=460, height=40)
FILEUPLOADLabel = tk.Label(text="*** 文件上传配置 ***")
FILEUPLOAD_Boundary.grid()
FILEUPLOAD_Boundary.add(FILEUPLOADLabel)

# 是否进行上传文件配置
# 关闭上传文件配置后，无法操作参数信息
def upload_close():
    variable_SecUploadDir.set("--关闭--")
    SecUploadDirEntry['state'] = 'disable'

    variable_SecUploadFileMode.set("--关闭--")
    SecUploadFileModeEntry['state'] = 'disable'

def upload_open():
    variable_SecUploadDir.set("/opt/modsecurity/var/upload/")
    SecUploadDirEntry['state'] = 'normal'

    variable_SecUploadFileMode.set("0600")
    SecUploadFileModeEntry['state'] = 'normal'


# 是否保存上传文件
SecUploadKeepFiles = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecUploadKeepFiles, width=200, height=35)
rightPane = tk.PanedWindow(SecUploadKeepFiles, width=260, height=35)
SecUploadKeepFilesLabel = tk.Label(text="是否保存上传文件")
sukf_model = tk.IntVar()
SecUploadKeepFilesEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=sukf_model, command=upload_open)
SecUploadKeepFilesEntry2 = tk.Radiobutton(frame, text='关闭', value=2, variable=sukf_model, command=upload_close)
sukf_model.set(2)
SecUploadKeepFiles.grid()
SecUploadKeepFiles.add(leftPane)
SecUploadKeepFiles.add(rightPane)
leftPane.add(SecUploadKeepFilesLabel)
rightPane.add(SecUploadKeepFilesEntry1)
rightPane.add(SecUploadKeepFilesEntry2)

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
variable_SecDebugLog.set("/var/log/modsec_debug.log")
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
    variable_SecAuditLogParts.set("ABCJEFHZ")

    SecAuditLogTypeEntry1['state'] = 'normal'
    SecAuditLogTypeEntry2['state'] = 'normal'
    salt_model.set(1)

    SecAuditLogEntry['state'] = 'normal'
    fileordir.set("/var/log/modsec_audit.log")

def audit_open():
    showinfo(title="提示", message="此选项下会记录所有事务，占用磁盘空间较大，一般仅适用于调试")
    SecAuditLogRelevantStatusEntry['state'] = 'disable'
    variable_SecAuditLogRelevantStatus.set("--关闭--")

    SecAuditLogPartsEntry['state'] = 'normal'
    variable_SecAuditLogParts.set("ABCJEFHZ")

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
def helpAuditLogStatus():
    showinfo(title="事务状态记录规则说明", message="使用正则表达式规则编写，符合该规则的事务状态会纳入到审计记录中。\n如\"^(?:5|4(?!04))\"的正则表达式表示除404之外5xx和4xx的事务。")
SecAuditLogRelevantStatus = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogRelevantStatus, width=120, height=35)
rightPane = tk.PanedWindow(SecAuditLogRelevantStatus, width=340, height=35)
SecAuditLogRelevantStatusLabel = tk.Label(text="事务状态记录规则")
variable_SecAuditLogRelevantStatus = tk.StringVar()
variable_SecAuditLogRelevantStatus.set("\"^(?:5|4(?!04))\"")
btnHelpAuditLogStatus = tk.Button(frame, image=help_img, command=helpAuditLogStatus)
SecAuditLogRelevantStatusEntry = tk.Entry(frame, text=variable_SecAuditLogRelevantStatus)
SecAuditLogRelevantStatus.grid()
SecAuditLogRelevantStatus.add(leftPane, padx=30, width=139, sticky='e')
SecAuditLogRelevantStatus.add(rightPane, padx=1, width=300, height=35, sticky='es')
leftPane.add(SecAuditLogRelevantStatusLabel)
leftPane.add(btnHelpAuditLogStatus, width=23, height=23, sticky='w')
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
I -- C部分的替换,在使用multipart/form-data编码时会记录与C相同的数据。\n但application/x-www-form-urlencoded情况下仅记录参数和假的文件体而不包含文件。\n该选项用于处理不想保存(过大)上传文件于审计日志中的情况(暂未实现)\n\n\
J -- 文件使用multipart/form-data编码上传的信息\n\n\
K -- 包含其匹配的触发规则列表(暂未实现)\n\n\
Z -- 最终分界，意味条目的最后(强制)\n")
    helpText.config(state=tk.DISABLED)


SecAuditLogParts = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogParts, width=120, height=35)
rightPane = tk.PanedWindow(SecAuditLogParts, width=340, height=35)
SecAuditLogPartsLabel = tk.Label(text="日志记录内容")
variable_SecAuditLogParts = tk.StringVar()
variable_SecAuditLogParts.set("ABCJEFHZ")
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
SecAuditLog.grid()
SecAuditLog.add(leftPane)
SecAuditLog.add(rightPane)
leftPane.add(SecAuditLogLabel)
rightPane.add(SecAuditLogEntry, padx=20, pady=5)

# 日志记录格式
def json_tips():
    showwarning(title="JSON格式注意事项", message="该选项仅适用于在编译阶段通过包含YAJL库以支持JSON数据格式的ModSecurity")
SecAuditLogFormat = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecAuditLogFormat, width=200, height=35)
rightPane = tk.PanedWindow(SecAuditLogFormat, width=260, height=35)
SecAuditLogFormatLabel = tk.Label(text="日志记录格式")
salf_model = tk.IntVar()
SecAuditLogFormatEntry1 = tk.Radiobutton(frame, text='Native', value=1, variable=salf_model)
SecAuditLogFormatEntry2 = tk.Radiobutton(frame, text='JSON', value=2, variable=salf_model, command=json_tips)
salf_model.set(1)
SecAuditLogFormat.grid()
SecAuditLogFormat.add(leftPane)
SecAuditLogFormat.add(rightPane)
leftPane.add(SecAuditLogFormatLabel)
rightPane.add(SecAuditLogFormatEntry1)
rightPane.add(SecAuditLogFormatEntry2)

'''-- SecRule configuration --'''
SECRULE_Boundary = tk.PanedWindow(frame, width=460, height=40)
SECRULELabel = tk.Label(text="*** 自定义规则设置 ***")
SECRULE_Boundary.grid()
SECRULE_Boundary.add(SECRULELabel)

# 自定义规则开启
def sre_open():
    SecRuleEntry['state'] = "normal"
    SecRuleEntry.delete("1.0", "end")
    DefaultSecRulesEntry['state'] = 'normal'
def sre_close():
    SecRuleEntry.insert(tk.INSERT, "--关闭--")
    SecRuleEntry['state'] = "disable"
    DefaultSecRulesEntry['state'] = 'disable'
def sre_detection():
    SecRuleEntry['state'] = "normal"
    SecRuleEntry.delete("1.0", "end")
    DefaultSecRulesEntry['state'] = 'normal'
    showinfo(title="自定义规则仅监控模式", message="该选项下不会执行任何规则中的阻断操作(如 block,deny,drop,allow,proxy,redirect)")
SecRuleEngine = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecRuleEngine, width=200, height=35)
rightPane = tk.PanedWindow(SecRuleEngine, width=260, height=35)
SecRuleEngineLabel = tk.Label(text="开启自定义规则")
sre_model = tk.IntVar()
SecRuleEngineEntry1 = tk.Radiobutton(frame, text='开启', value=1, variable=sre_model, command=sre_open)
SecRuleEngineEntry2 = tk.Radiobutton(frame, text='仅监控', value=2, variable=sre_model, command=sre_detection)
SecRuleEngineEntry3 = tk.Radiobutton(frame, text='关闭', value=3, variable=sre_model, command=sre_close)
sre_model.set(3)
SecRuleEngine.grid()
SecRuleEngine.add(leftPane)
SecRuleEngine.add(rightPane)
leftPane.add(SecRuleEngineLabel)
rightPane.add(SecRuleEngineEntry1)
rightPane.add(SecRuleEngineEntry2)
rightPane.add(SecRuleEngineEntry3)

# 默认推荐SecRules规则配置
def defaultRules():
    newWindow = tk.Toplevel(window)
    newWindow.geometry("600x400")
    newWindow.title("默认推荐规则内容")
    helpText = tk.Text(newWindow, width=600, height=300, undo=True, padx=20, pady=20, relief=tk.FLAT)
    helpText.pack()
    helpText.insert(tk.INSERT, "默认推荐规则包含以下条目：\n")
    helpText.config(state=tk.DISABLED)
DefaultSecRules = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(DefaultSecRules, width=200, height=35)
rightPane = tk.PanedWindow(DefaultSecRules, width=260, height=35)
DefaultSecRulesLabel = tk.Label(text="是否配置SecRule默认推荐规则")
btnDefaultRules = tk.Button(frame, image=help_img, command=defaultRules)
default_rule_check = tk.IntVar(value=1)
DefaultSecRulesEntry = tk.Checkbutton(frame, text='是', variable=default_rule_check)
DefaultSecRules.grid()
DefaultSecRules.add(leftPane)
DefaultSecRules.add(rightPane)
leftPane.add(DefaultSecRulesLabel)
leftPane.add(btnDefaultRules, width=23, height=23, sticky='w')
rightPane.add(DefaultSecRulesEntry)

# 自定义规则
def helpSecRule():
    newWindow = tk.Toplevel(window)
    newWindow.geometry("600x400")
    newWindow.title("日志记录内容说明")
    helpText = tk.Text(newWindow, width=600, height=300, undo=True, padx=20, pady=20, relief=tk.FLAT)
    helpText.pack()
    helpText.insert(tk.INSERT, "基础语法：SecRule VARIABLES OPERATOR [ACTIONS] \n\n"
                               "VARIABLES:\n"
                               "ARGS,ARGS_GET,ARGS_POST,FILES,FULL_REQUEST_QUERY_STRING,REQUEST_BODY,REQUEST_HEADERS,REQUEST_MATHOD,REQUEST_URI\n\n"
                               "OPERATOR:\n"
                               "@rx,@eq,@ge,@gt,@le,@lt\n\n"
                               "ACTIONS:\n"
                               "allow,ms,gid,rev,severity,log,deny,block,status,phase,t,skip,chain\n\n"
                               "TRANSFORMATION FUNCTIONS:\n"
                               "lowercase,urlDecode,none,compressWhitespace,removeWhitespace,replaceNulls,removeNulls\n\n"
                               "PHASES:\n"
                               "phase:1 - Request headers stage\nphase:2 - Request body stage\nphase:3 - Response headers stage\nphase:4 - Response body stage\n\n"
                               "更多语法细节参考：https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-%28v2.x%29-%28Split%29#processing-phases")
    helpText.config(state=tk.DISABLED)
SecRule = tk.PanedWindow(frame, width=460, height=60)
leftPane = tk.PanedWindow(SecRule, width=200, height=60)
rightPane = tk.PanedWindow(SecRule, width=260, height=60)
SecRuleLabel = tk.Label(text="自定义规则\n(每条规则占一行)")
SecRuleEntry = tk.Text(frame)
btnHelpSecRules = tk.Button(frame, image=help_img, command=helpSecRule)
SecRule.grid()
SecRule.add(leftPane, padx=36, width=130)
SecRule.add(rightPane)
leftPane.add(SecRuleLabel)
leftPane.add(btnHelpSecRules, width=23, height=23, sticky='w')
rightPane.add(SecRuleEntry, padx=20, pady=5)

sre_close()


'''-- Miscellaneous  --'''
MISC_Boundary = tk.PanedWindow(frame, width=460, height=40)
MISCLabel = tk.Label(text="*** Miscellaneous ***")
MISC_Boundary.grid()
MISC_Boundary.add(MISCLabel)

# 参数分隔符
SecArgumentSeparator = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecArgumentSeparator, width=200, height=35)
rightPane = tk.PanedWindow(SecArgumentSeparator, width=260, height=35)
SecArgumentSeparatorLabel = tk.Label(text="参数分隔符")
variable_SecArgumentSeparator = tk.StringVar()
variable_SecArgumentSeparator.set("&")
SecArgumentSeparatorEntry = tk.Entry(frame, textvariable=variable_SecArgumentSeparator)
SecArgumentSeparator.grid()
SecArgumentSeparator.add(leftPane)
SecArgumentSeparator.add(rightPane)
leftPane.add(SecArgumentSeparatorLabel)
rightPane.add(SecArgumentSeparatorEntry, padx=20, pady=5)

# 指定Unicode的Code Point
SecUnicodeMapFile = tk.PanedWindow(frame, width=460, height=35)
leftPane = tk.PanedWindow(SecUnicodeMapFile, width=200, height=35)
rightPane = tk.PanedWindow(SecUnicodeMapFile, width=260, height=35)
SecUnicodeMapFileLabel = tk.Label(text="Unicode Mapping位置\n及指定Code Point")
variable_SecUnicodeMapFile = tk.StringVar()
variable_SecUnicodeMapFile.set("unicode.mapping 20127")
SecUnicodeMapFileEntry = tk.Entry(frame, textvariable=variable_SecUnicodeMapFile)
SecUnicodeMapFile.grid()
SecUnicodeMapFile.add(leftPane)
SecUnicodeMapFile.add(rightPane)
leftPane.add(SecUnicodeMapFileLabel)
rightPane.add(SecUnicodeMapFileEntry, padx=20, pady=5)


def getInput():
    with open("ModSecurity.conf", "w+") as f:
        flist = []
        errortip = 0
        error_mx = ""

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
        flist.append(input)

        '''SecRequestBodyAccess'''
        SecRequestBodyAccess = sra_open.get()
        content = "SecRequestBodyAccess "
        if SecRequestBodyAccess == 1:
            option = "On"
        elif SecRequestBodyAccess == 2:
            option = "Off"
        input = content + option + "\n\n"
        flist.append(input)

        if SecRequestBodyAccess == 1:
            '''SecRequestBodyLimit'''
            SecRequestBodyLimit = SecRequestBodyLimitEntry.get()
            if SecRequestBodyLimit != "":
                content = "SecRequestBodyLimit "
                option = SecRequestBodyLimit
                input = content + option + "\n\n"
                flist.append(input)

            '''SecRequestBodyNoFilesLimit'''
            SecRequestBodyNoFilesLimit = SecRequestBodyNoFilesLimitEntry.get()
            if SecRequestBodyNoFilesLimit != "":
                content = "SecRequestBodyNoFilesLimit "
                option = SecRequestBodyNoFilesLimit
                input = content + option + "\n\n"
                flist.append(input)

            '''SecRequestBodyLimitAction '''
            SecRequestBodyLimitAction = srbl_action.get()
            content = "SecRequestBodyLimitAction "
            if SecRequestBodyLimitAction == 1:
                option = "Reject"
            elif SecRequestBodyLimitAction == 2:
                option = "ProcessPartial"
            input = content + option + "\n\n"
            flist.append(input)

            '''SecRequestBodyJsonDepthLimit'''
            SecRequestBodyJsonDepthLimit = SecRequestBodyJsonDepthLimitEntry.get()
            if SecRequestBodyJsonDepthLimit != "":
                content = "SecRequestBodyJsonDepthLimit "
                option = SecRequestBodyJsonDepthLimit
                input = content + option + "\n\n"
                flist.append(input)

            '''SecArgumentsLimit'''
            SecArgumentsLimit = SecArgumentsLimitEntry.get()
            if SecArgumentsLimit != "":
                content = "SecArgumentsLimit "
                option = SecArgumentsLimit
                input = content + option + "\n\n"
                flist.append(input)

        '''SecResponseBodyAccess'''
        SecResponseBodyAccess = srp_open.get()
        content = "SecResponseBodyAccess "
        if SecResponseBodyAccess == 1:
            option = "On"
        elif SecResponseBodyAccess == 2:
            option = "Off"
        input = content + option + "\n\n"
        flist.append(input)

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
            if plain != 0 or html != 0 or xml != 0:
                input = content + option + "\n\n"
                flist.append(input)

            '''SecResponseBodyLimit'''
            SecResponseBodyLimit = SecResponseBodyLimitEntry.get()
            if SecResponseBodyLimit != "":
                content = "SecResponseBodyLimit "
                option = SecResponseBodyLimit
                input = content + option + "\n\n"
                flist.append(input)

            '''SecRequestBodyLimitAction '''
            SecResponseBodyLimitAction = srpl_action.get()
            content = "SecResponseBodyLimitAction "
            if SecResponseBodyLimitAction == 1:
                option = "Reject"
            elif SecResponseBodyLimitAction == 2:
                option = "ProcessPartial"
            input = content + option + "\n\n"
            flist.append(input)

            '''SecUploadKeepFiles'''
            SecUploadKeepFiles = sukf_model.get()
            content = "SecUploadKeepFiles "
            if SecUploadKeepFiles == 1:
                option = "On"
            elif SecUploadKeepFiles == 2:
                option = "Off"
            input = content + option + "\n\n"
            flist.append(input)

            if SecUploadKeepFiles == 1:
                '''SecUploadDir'''
                SecUploadDir = SecUploadDirEntry.get()
                content = "SecUploadDir "
                option = SecUploadDir
                input = content + option + "\n\n"
                flist.append(input)
                if SecUploadDir == "":
                    errortip = 1
                    error_mx += "请指定上传文件的保存位置\n"

                '''SecUploadFileMode'''
                SecUploadFileMode = SecUploadFileModeEntry.get()
                content = "SecUploadFileMode "
                option = SecUploadFileMode
                input = content + option + "\n\n"
                flist.append(input)
                if SecUploadFileMode == "":
                    errortip = 1
                    error_mx += "请指定上传文件的权限模式\n"

        '''SecDebugLogAccess'''
        if sdl_open.get() == 1:
            '''SecDebugLog'''
            SecDebugLog = SecDebugLogEntry.get()
            content = "SecDebugLog "
            option = SecDebugLog
            if SecDebugLog == "":
                option = "/var/log/modsec_debug.log"
            input = content + option + "\n\n"
            flist.append(input)

            '''SecDebugLogLevel'''
            SecDebugLogLevel = sdll_model.get()
            content = "SecDebugLogLevel "
            option = str(SecDebugLogLevel)
            input = content + option + "\n\n"
            flist.append(input)

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
        flist.append(input)

        if SecAuditEngine == 1 or SecAuditEngine == 2:
            if SecAuditEngine == 1:
                '''SecAuditLogRelevantStatus'''
                SecAuditLogRelevantStatus = SecAuditLogRelevantStatusEntry.get()
                if SecAuditLogRelevantStatus != "":
                    content = "SecAuditLogRelevantStatus "
                    option = SecAuditLogRelevantStatus
                    input = content + option + "\n\n"
                    flist.append(input)

            '''SecAuditLogParts'''
            SecAuditLogParts = SecAuditLogPartsEntry.get()
            content = "SecAuditLogParts "
            option = SecAuditLogParts
            input = content + option + "\n\n"
            flist.append(input)
            if SecAuditLogParts == "":
                errortip = 1
                error_mx += "请指定审计日志的记录内容\n"

            '''SecAuditLogType'''
            SecAuditLogType = salt_model.get()
            content = "SecAuditLogType "
            if SecAuditLogType == 1:
                option = "Serial"
            elif SecAuditLogType == 2:
                option = "Concurrent"
            input = content + option + "\n\n"
            flist.append(input)

            '''SecAuditLog or SecAuditLogStorageDir'''
            SecAuditLog = SecAuditLogEntry.get()
            option = SecAuditLog
            if SecAuditLogType == 1:
                content = "SecAuditLog "
            elif SecAuditLogType == 2:
                content = "SecAuditLogStorageDir "
            input = content + option + "\n\n"
            flist.append(input)
            if SecAuditLog == "":
                errortip = 1
                error_mx += "请指定审计日志的保存位置\n"

            '''SecAuditLogFormat'''
            SecAuditLogFormat = salf_model.get()
            content = "SecAuditLogFormat "
            if SecAuditLogFormat == 1:
                option = "Native"
            elif SecAuditLogFormat == 2:
                option = "JSON"
            input = content + option + "\n\n"
            flist.append(input)

        '''SecRuleEngine'''
        SecRuleEngine = sre_model.get()
        if SecRuleEngine == 1 or SecRuleEngine == 2:
            '''DefaultSecRules'''
            DefaultSecRules = default_rule_check.get()
            print(DefaultSecRules)
            if DefaultSecRules == 1:
                input = \
"""
SecRule REQUEST_HEADERS:Content-Type "^(?:application(?:/soap\+|/)|text/)xml" \\ \n
     "id:'200000',phase:1,t:none,t:lowercase,pass,nolog,ctl:requestBodyProcessor=XML"\n
SecRule REQUEST_HEADERS:Content-Type "^application/json" \\\n
     "id:'200001',phase:1,t:none,t:lowercase,pass,nolog,ctl:requestBodyProcessor=JSON"\n
SecRule &ARGS "@ge 1000" \\\n
"id:'200007', phase:2,t:none,log,deny,status:400,msg:'Failed to fully parse request body due to large argument count',severity:2"\n
SecRule REQBODY_ERROR "!@eq 0" \\\n
"id:'200002', phase:2,t:none,log,deny,status:400,msg:'Failed to parse request body.',logdata:'%{reqbody_error_msg}',severity:2"\n
SecRule MULTIPART_STRICT_ERROR "!@eq 0" \\\n
"id:'200003',phase:2,t:none,log,deny,status:400, \\\n
msg:'Multipart request body failed strict validation: \\\n
PE %{REQBODY_PROCESSOR_ERROR}, \\\n
BQ %{MULTIPART_BOUNDARY_QUOTED}, \\\n
BW %{MULTIPART_BOUNDARY_WHITESPACE}, \\\n
DB %{MULTIPART_DATA_BEFORE}, \\\n
DA %{MULTIPART_DATA_AFTER}, \\\n
HF %{MULTIPART_HEADER_FOLDING}, \\\n
LF %{MULTIPART_LF_LINE}, \\\n
SM %{MULTIPART_MISSING_SEMICOLON}, \\\n
IQ %{MULTIPART_INVALID_QUOTING}, \\\n
IP %{MULTIPART_INVALID_PART}, \\\n
IH %{MULTIPART_INVALID_HEADER_FOLDING}, \\\n
FL %{MULTIPART_FILE_LIMIT_EXCEEDED}'"\n
SecRule MULTIPART_UNMATCHED_BOUNDARY "@eq 1" \\\n
    "id:'200004',phase:2,t:none,log,deny,msg:'Multipart parser detected a possible unmatched boundary.'"\n
SecRule TX:/^MSC_/ "!@streq 0" \\\n
        "id:'200005',phase:2,t:none,deny,msg:'ModSecurity internal error flagged: %{MATCHED_VAR_NAME}'"\n
"""
                flist.append(input)
            '''SecRule'''
            SecRules = SecRuleEntry.get("1.0","end")
            if SecRules != "":
                for line in SecRules:
                    flist.append(line)

        '''SecArgumentSeparator'''
        SecArgumentSeparator = SecArgumentSeparatorEntry.get()
        content = "SecArgumentSeparator "
        option = SecArgumentSeparator
        if SecArgumentSeparator == "":
            option = "&"
        input = content + option + "\n\n"
        flist.append(input)

        '''SecUnicodeMapFile'''
        SecUnicodeMapFile = SecUnicodeMapFileEntry.get()
        content = "SecUnicodeMapFile "
        option = SecUnicodeMapFile
        if SecUnicodeMapFile == "":
            option = "unicode.mapping 20127"
        input = content + option + "\n\n"
        flist.append(input)

        if errortip == 1:
            showerror(title="出错", message=error_mx)
        else:
            for i in flist:
                f.writelines(i)


btnOutput = tk.Button(frame, height=1, width=10, text="OUTPUT", command=getInput, font=("Times", 10, "bold"))
btnOutput.grid(pady=50)

moreInfoLabel = tk.Label(frame, height=1, width=10, text="更多参考手册", font=('Arial', 9, 'underline'), cursor="hand2")
moreInfoLabel.grid()
def open_url(event):
    webbrowser.open("https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-%28v3.x%29", new=0)
moreInfoLabel.bind("<Button-1>", open_url)

frame.update()
canvas.configure(yscrollcommand=scroll.set, scrollregion=canvas.bbox("all"))
scroll.config(command=canvas.yview)
canvas.yview_moveto(0)

window.mainloop()
