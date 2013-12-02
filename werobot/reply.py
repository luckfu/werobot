#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from utils import to_unicode
def ReplyText(ToUserName,FromUserName,Content):      
    Temp="""<xml>
 <ToUserName><![CDATA[%s]]></ToUserName>
 <FromUserName><![CDATA[%s]]></FromUserName>
 <CreateTime>%s</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[%s]]></Content>
 </xml>"""
    return Temp % (ToUserName,FromUserName,str(int(time.time())),to_unicode(Content))

def ReplyMusic(ToUserName,FromUserName,Title,Description,MusicUrl,HQMusicUrl):      
    Temp="""<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
        <Title><![CDATA[%s]]></Title>
        <Description><![CDATA[%s]]></Description>
        <MusicUrl><![CDATA[%s]]></MusicUrl>
        <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>
        </Music>
        </xml>"""
    return Temp % (ToUserName,FromUserName,str(int(time.time())),Title,Description,MusicUrl,HQMusicUrl)

def ReplyNews(ToUserName,FromUserName,News=[]):      
    Temp1="""<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[news]]></MsgType>
        <ArticleCount>%s</ArticleCount>
        <Articles> """
    Temp2="""<item>
        <Title><![CDATA[%s]]></Title> 
        <Description><![CDATA[%s]]></Description>
        <PicUrl><![CDATA[%s]]></PicUrl>
        <Url><![CDATA[%s]]></Url>
        </item>"""
    Temp3="""</Articles></xml>"""
    
    Res = Temp1 % (ToUserName,FromUserName,str(int(time.time())),len(News))
    
    for i in News: Res += Temp2 % (text(i['Title']),text(i['Description']),text(i['PicUrl']),text(i['Url']))
        
    Res += Temp3
    print Res
    return Res

if __name__ == '__main__':

    ReplyText('123','321','拿百度测试')

    News=[{'Title':'测试','Description':'拿百度测试','PicUrl':'http://www.baidu.com/img/bdlogo.gif','Url':'http://michael.lustfield.net/nginx/bottle-uwsgi-nginx-quickstart'}]
    ReplyNews('123','321',News)