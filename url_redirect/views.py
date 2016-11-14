#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render_to_response, redirect
import json
import urllib2
# Create your views here.


def detail(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))	

def idlist(request,listid):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))	

def bymonth(request,month):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))	

def carousel(request):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))	

def reading_index(request):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))			

def essay(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))			

def serialcontent(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))

def question(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))

def bymonthandtype(request,typeid,month):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	print request_url
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))		

def music_idlist(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))

def music_bymonth(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))

def music_detail(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))

def movie_list(request,query_id):
	host = "http://v3.wufazhuce.com:8000"
	request_url = host + request.get_full_path()
	data = json.load(urllib2.urlopen(request_url))
	print data
	return HttpResponse(json.dumps(data,ensure_ascii=False,indent=2))