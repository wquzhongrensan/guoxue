from django.http import HttpResponse
import codecs
import json
import os
from django.views.decorators.csrf import csrf_exempt
import random
from datetime import *
from django.conf import settings
from urllib.parse import urlsplit

ROOT = os.path.dirname(__file__)
UEDITOR_UPLOAD_PATH = settings.UEDITOR_UPLOAD_PATH
# 本地上传图片时构造json返回值


class JsonResult(object):
	def __init__(self,state="未知错误",url="",title="",original="",error="null"):
		super(JsonResult,self).__init__()
		self.state = state	
		self.url = url
		self.title = title
		self.original = original
		self.error = error

#构造返回json
def buildJsonResult(result):
	jsondata = {"state":result.state,"url":result.url,"title":result.title,"original":result.original,"error":result.error}
	return json.dumps(jsondata)

def buildFileName(filename):
	dt = datetime.now()
	name,ext = os.path.splitext(filename)
	return dt.strftime("%Y%m%d%M%H%S{0}{1}".format(random.randint(1,999999),ext))

#读取json文件
def getConfigContent():
	jsonfile = ROOT+"/ueconfig.json"

	with open(jsonfile, 'r', encoding='utf-8') as fp:
		content = json.loads(fp.read())

	# content = json.load(jsonfile)
	return content

#上传配置类
class UploadConfig(object):
	def __init__(self,PathFormat,UploadFieldName,SizeLimit,AllowExtensions,SavePath,Base64,Base64Filename):
		super(UploadConfig,self).__init__()
		self.PathFormat = PathFormat
		self.UploadFieldName = UploadFieldName
		self.SizeLimit = SizeLimit
		self.AllowExtensions = AllowExtensions
		self.SavePath = SavePath
		self.Base64 = Base64
		self.Base64Filename = Base64Filename

#获取json配置中的某属性值
def GetConfigValue(key):
	config = getConfigContent()
	return config[key]

#检查文件扩展名是否在允许的扩展名内
def CheckFileType(filename,AllowExtensions):
	exts = list(AllowExtensions)
	name,ext = os.path.splitext(filename)
	return ext in exts

def CheckFileSize(filesize,SizeLimit):
	return filesize<SizeLimit

#处理上传图片、文件、视频文件
@csrf_exempt
def uploadFile(request,config):
	result = JsonResult()
	if config.Base64:
		pass
	else:
		buf = request.FILES.get(config.UploadFieldName)
		filename = buf.name
		if not CheckFileType(filename,config.AllowExtensions):
			result.error ="不允许的文件格式"
			return HttpResponse(buildJsonResult(result))
		if not CheckFileSize(buf.size,config.SizeLimit):
			result.error = "文件大小超出服务器限制"
			return HttpResponse(buildJsonResult(result))

		
		try:
			truelyName = buildFileName(filename)
			webUrl = config.SavePath+ truelyName
			savePath =UEDITOR_UPLOAD_PATH+webUrl
			f = codecs.open(savePath,"wb")
			for chunk in buf.chunks():
				f.write(chunk)
			f.flush()
			f.close()
			result.state = "SUCCESS"
			# result.url = truelyName

			# 获得当前的HTTP或HTTPS
			http = urlsplit(request.build_absolute_uri(None)).scheme
			# 获取当前域名
			host = request.META['HTTP_HOST']
			total_host = http + '://' + host

			result.url = total_host + "media"+webUrl
			result.title = truelyName
			result.original = truelyName
			response = HttpResponse(buildJsonResult(result))
			response["Content-Type"] = "text/plain"
			response["X-Frame-Options"] = "ALLOWALL"
			response["Access-Control-Allow-Headers"] = "*"
			return response
		except Exception as e:
			result.error = "网络错误"
			return HttpResponse(buildJsonResult(result))

#处理在线图片与在线文件
#返回的数据格式：{"state":"SUCCESS","list":[{"url":"upload/image/20140627/6353948647502438222009315.png"},{"url":"upload/image/20140627/6353948659383617789875352.png"},{"url":"upload/image/20140701/6353980733328090063690725.png"},{"url":"upload/image/20140701/6353980745691597223366891.png"},{"url":"upload/image/20140701/6353980747586705613811538.png"},{"url":"upload/image/20140701/6353980823509548151892908.png"}],"start":0,"size":20,"total":6}
def listFileManage(request,imageManagerListPath,imageManagerAllowFiles,listsize):
	pstart = request.GET.get("start")
	start = pstart==None and int(pstart) or 0
	psize = request.GET.get("size")
	size = psize==None and int(GetConfigValue(listsize)) or int(psize)
	localPath = UEDITOR_UPLOAD_PATH+imageManagerListPath
	filelist = []
	exts = list(imageManagerAllowFiles)
	index = start
	for imagename in os.listdir(localPath):
		name,ext = os.path.splitext(imagename)
		if ext in exts:
			filelist.append(dict(url=imagename))
			index+=1
			if index-start>=size:
				break
	jsondata = {"state":"SUCCESS","list":filelist,"start":start,"size":size,"total":index}
	response = HttpResponse(json.dumps(jsondata))
	response["X-Frame-Options"] = "ALLOWALL"
	response["Access-Control-Allow-Headers"] = "x-requested-with"

	return response





#返回配置信息
def configHandler(request):
	content = getConfigContent()
	callback = request.GET.get("callback")
	if callback:
		return HttpResponse("{0}({1})".format(callback,json.dumps(content)))
	return HttpResponse(json.dumps(content))

#图片上传控制
@csrf_exempt
def uploadimageHandler(request):
	AllowExtensions = GetConfigValue("imageAllowFiles")
	PathFormat = GetConfigValue("imagePathFormat")
	SizeLimit = GetConfigValue("imageMaxSize")
	UploadFieldName = GetConfigValue("imageFieldName")
	SavePath = GetConfigValue("imageUrlPrefix")
	upconfig = UploadConfig(PathFormat,UploadFieldName,SizeLimit,AllowExtensions,SavePath,False,'')
	return uploadFile(request,upconfig)

def uploadvideoHandler(request):
	AllowExtensions = GetConfigValue("videoAllowFiles")
	PathFormat = GetConfigValue("videoPathFormat")
	SizeLimit = GetConfigValue("videoMaxSize")
	UploadFieldName = GetConfigValue("videoFieldName")
	SavePath = GetConfigValue("videoUrlPrefix")
	upconfig = UploadConfig(PathFormat,UploadFieldName,SizeLimit,AllowExtensions,SavePath,False,'')
	return uploadFile(request,upconfig)


def uploadfileHandler(request):
	AllowExtensions = GetConfigValue("fileAllowFiles")
	PathFormat = GetConfigValue("filePathFormat")
	SizeLimit = GetConfigValue("fileMaxSize")
	UploadFieldName = GetConfigValue("fileFieldName")
	SavePath = GetConfigValue("fileUrlPrefix")
	upconfig = UploadConfig(PathFormat,UploadFieldName,SizeLimit,AllowExtensions,SavePath,False,'')
	return uploadFile(request,upconfig)

#在线图片
def listimageHandler(request):
	imageManagerListPath = GetConfigValue("imageManagerListPath")
	imageManagerAllowFiles = GetConfigValue("imageManagerAllowFiles")
	imagelistsize = GetConfigValue("imageManagerListSize")
	return listFileManage(request,imageManagerListPath,imageManagerAllowFiles,imagelistsize)

#在线文件
def ListFileManagerHander(request):
	fileManagerListPath = GetConfigValue("fileManagerListPath")
	fileManagerAllowFiles = GetConfigValue("fileManagerAllowFiles")
	filelistsize = GetConfigValue("fileManagerListSize")
	return listFileManage(request,fileManagerListPath,fileManagerAllowFiles,filelistsize)

actions = {
	"config":configHandler,
	"uploadimage":uploadimageHandler,
	"uploadvideo":uploadvideoHandler,
	"uploadfile":uploadfileHandler,
	"listimage":listimageHandler,
	"listfile":ListFileManagerHander
}

@csrf_exempt
def handler(request):
	action = request.GET.get("action")
	return actions.get(action)(request) 