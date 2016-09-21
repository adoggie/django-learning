# --  coding:utf-8 --

__author__ = 'scott'


# 1
# 公文类别
# SYS_T_ARCHIVES_TYPE
class ArchiveType:
	FILE 			= 0x01                         # 文件
	MEETING_NOTICE 	= 0x02              # 会议通知
	PERIODICAL 		= 0x03                   # 刊物杂志
	MATERIAL 		= 0x04                     # 材料
	BRIEF 			= 0x05                        # 简报
	OTHER 			= 0x06                        # 其他


# 2
# 密级
# SYS_T_SECRETLEVEL
class SecurityClassification:
	UNCLASSIFIED 	= 0x01                 # 无密级=1
	SECRET 			= 0x02                 # 秘密=2
	CONFIDENTIAL 	= 0x03                 # 机密=3


# 紧急程度
class EmergencyType:
	URGENT 		= 0x01                   	# 平急=1
	MORE_URGENT = 0x02                  	# 加急=2
	TOP_URGENT 	= 0x03                   	# 特急=3
	UNDEFINED 	= 0x04                    	# 无紧急程度=4

# 角色
class UserRoleType():
	RECEIVER 	= 0x01                     # 收文员
	SENDER 		= 0x02                       # 发文员
	READER 		= 0x04                         # 阅文

	@staticmethod
	def nameValue(type):
		name = ''
		if not type:
			return name
		if type& UserRoleType.RECEIVER:
			name+=u'收文员'
		if type&UserRoleType.SENDER:
			if name:name+=','
			name+=u'发文员'
		if type&UserRoleType.READER:
			if name: name+=','
			name+=u'阅文员'
		return name

# 管理员
class AdminUserType:
	SYS 	= 0x01                 # 系统管理员
	SEC 	= 0x02                   # 安全审计管理员
	LGO 	= 0x04               # 安全保密管理员

	@staticmethod
	def nameValue(type):
		name = ''
		if not type:
			return name
		if type& AdminUserType.SYS:
			name+=u'系统管理员'
		if type&AdminUserType.SEC:
			if name:name+=','
			name+=u'安全保密管理员'
		if type&AdminUserType.LGO:
			if name: name+=','
			name+=u'安全审计管理员'
		return name


# 公文在不同环节下的状态
class ArchiveStatus:
	TO_BE_SEND = 20                     # 待发=20
	FILING_OF_SENDER = 23               # 发文者留档=23
	REVOCATION = 25                     # 撤销发文=25
	UNREAD = 30                         # 已发未收=30
	# 拒收=35
	# 已收未阅=40
	READ_AND_UNPRINTED = 40             # 已阅未打印=50
	ALLOW_PRINT = 60                    # 已打印未打印完=60
	NOT_ALLOW_PRINT = 70                # 已打印完=70
	# 已办=80
	ALREADY_PIGEONHOLE = 90             # 已归档=90
	COMPLETION = 100                    # 全部完成=100


# 审批结果
class ApprovalResults:
	UNAPPROVED = 0                      # 未审批=0
	ALLOW = 1                           # 通过=1
	NOT_ALLOW = 2                       # 不通过=2


# 接收状态
class ReceiveStatus:
	ALL_UNREAD = 0                      # 全未收取=0
	PARTIAL_READ = 1                    # 部分收取=1
	ALL_READ = 2                        # 全部收取=2
	ALL_REVOCATION = 3                  # 全部撤销=3


# 回执
class FeedbackType:
	NOT_REQUIRE_FEEDBACK = 1            # 不需要回执=1
	REQUIRE_FEEDBACK = 2                # 普通回执=2
	REQUIRE_MEETING_FEEDBACK = 3        # 会议回执=3
	REQUIRE_ATTENDANCE_FEEDBACK = 4     # 会议回执且需要人员名单=4




# 事件类型 - 日志
class EventType:
	# 登录
	# 登出
	# 修改密码
	# 设置管理员
	# 取消管理员
	# 添加节点
	# 删除节点
	# 设置收文单位
	# 取消收文单位
	# 赋收文权限
	# 赋发文权限
	# 赋收发文权限
	# 赋阅文权限
	pass


# 操作行为 - 日志 ？
class OperatingBehavior:
	pass


# 日志状态 - 日志
class LogEvent:
	pass


# 公文来源 - 公文表
class ArchiveSource:
	pass


# 操作状态 - 收发文操作日志
class ArchiveLogEvent:
	# 阅读公文
	# 发送回执
	# 发送会议回执
	# 下载附件
	# 转发公文
	# 打印公文
	# 撤回公文
	# 公文归档
	pass


#消息类型定义
class MessageType:
	"""
		用户通知消息定义
		手动发送：
		1. 新建消息
		2. 回复消息
		自动发送
		1. 发送公文（重发公文）
		2. 转发公文
		3. 催办消息
		4. 撤销发文
		5. 重打印申请【发送给发文员】
		6. 重打印审批【发送给收文员】
		7. 转发申请【发送给发文员】
		8. 转发审批【发送给收文员】
	"""
	Undefined = 0

	MessageCreate = 201
	MessageReply = 202

	ArchiveReach = 203
	ArchiveRelay = 204
	ArchiveHosten = 205
	ArchiveCallback = 206
	RePrintRequest  = 207
	RePrintApprove = 208
	RelayRequest = 209
	RelayApprove = 210

class OrgNodeType:
	User = 0x02
	Unit = 0x01

class ArchiveRASStatusType:
	# 1 - 创建（未开始传递） 2 - 开始投递 , 3 - 投递中  4 - 投递失败 , 5 -到达 , 6 - 已撤回
	NORMAL 		= 0
	RECALLED 	= 6 #已被撤回

class SystemParameterType:
	class Entry:
		def __init__(self,name,value=None):
			self.name = name
			self.value = value

		def __str__(self):
			return self.name

	SYSTEM_ID = Entry('sys_id','ras_sh_001')
	ROUTER_ADDRESS = Entry('router_address')
	ROUTER_PASSWORD = Entry('router_password')
	PARENT_SYS_ADDRESS = Entry('parent_sys_address')
	PARENT_SYS_PASSWORD = Entry('parent_sys_password')
	ROOT_UNIT = Entry('root_unit')


class LogActionType:
	"""
	日志行为类型
	"""
	class Entry:
		def __init__(self,id,name):
			self.id = id
			self.name = name

		def __str__(self):
			return self.name


	L101= Entry(101,u'登录')
	L102= Entry(102,u'注销')
	L103= Entry(103,u'修改密码')
	L201 = Entry(201,u'公文新建')
	L202 = Entry(202,u'公文修改')
	L203 = Entry(203,u'公文删除')
	L204 = Entry(204,u'公文发送')
	L205 = Entry(205,u'公文阅读')
	L206 = Entry(206,u'公文打印')
	L207 = Entry(207,u'公文回执')
	L208 = Entry(208,u'公文撤回')
	L209 = Entry(209,u'公文催办')
	L210 = Entry(210,u'公文转发')
	L211 = Entry(211,u'公文授权')
	L212 = Entry(212,u'附件上传')
	L213 = Entry(213,u'附件删除')
	L214 = Entry(214,u'重打印申请')
	L215 = Entry(215,u'重打印申请审批')
	L216 = Entry(216,u'转发申请')
	L217 = Entry(217,u'转发审批')
	L218 = Entry(218,u'创建公文编号')
	L219 = Entry(219,u'修改公文编号')
	L220 = Entry(220,u'删除公文编号')
	L221 = Entry(221,u'发送消息')
	L222 = Entry(222,u'回复消息')
	L223 = Entry(223,u'附件阅读')
	L301 = Entry(301,u'创建单位')
	L302 = Entry(302,u'更新单位')
	L303 = Entry(303,u'删除单位')
	L304 = Entry(304,u'创建用户')
	L305 = Entry(305,u'更新用户')
	L306 = Entry(306,u'删除用户')
	L307 = Entry(307,u'更新单位和用户位置')
	L308 = Entry(308,u'收文单位授权')
	L309 = Entry(309,u'发文单位授权')
	L310 = Entry(310,u'阅文顶层单位授权')

	L311 = Entry(311,u'设置用户角色')
	L312 = Entry(312,u'创建通知')
	L313 = Entry(313,u'修改通知')
	L314 = Entry(314,u'删除通知')



class CacheEntryFormat:
	'''
		缓冲记录类型以 . 分隔 a.b.c.d.e
	'''
	UserWithTGS  = 'user.%s.tgs' 		# user.101#aaccff5544.tgs:tgs_001
	UserWithDevice = 'user.%s.device' 	# 用户的终端设备列表 user.101.device:[aaccff5544,90785566ee]
	UserWithLocation = 'user.%s.location'	#用户当前的位置信息 {lon,lat,time,direction,speed}
	UserWithToken = 'user.%s.token'				#用户当前登录的token
	UserWithAppToken = 'user.%s.app.%s.token'	#用户当前登录的appp的token
	# UnitWithUsersSending = 'units.%s.users'			#单位相关的发文用户
	# UnitWithUsersReceiving = 'units.%s.users'		#单位相关的收文用户
	UnitRelatedUsers = 'units.%s.users'		#单位相关的用户
	UnitFullname = 'unit.%s.fullname'		#单位全路径名称


class LoginUserType:
	"""
	登录用户类型
	  普通用户、管理员用户
	"""
	UNKNOWN = 0
	USER = 1 	#
	ADMIN = 2

if __name__=='__main__':
	print SystemParameterType.SYSTEM_ID