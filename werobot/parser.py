#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
from utils import to_unicode

def ParserXml(xml):
    """
    XML文件解析
    """
    if not xml: return
    _msg = dict((child.tag, to_unicode(child.text))
                for child in ET.fromstring(xml))
    D={}

    D['ToUserName'] = _msg.get('ToUserName')
    D['FromUserName'] = _msg.get('FromUserName')
    D['CreateTime'] = int(_msg.get('CreateTime'))
    D['MsgType'] = _msg.get('MsgType')

    if D['MsgType']=='text':
        D['Content'] = _msg.get('Content')
        return D

    elif D['MsgType']=='location':
        D['Location_X'] = _msg.get('Location_X')
        D['Location_Y'] = _msg.get('Location_Y')
        D['Scale'] = int(_msg.get('Scale'))
        D['Label'] = _msg.get('Label')
        return D

    elif D['MsgType']=='image':
        D['PicUrl'] = _msg.get('PicUrl')
        return D

    elif D['MsgType']=='event':
        D['Event'] = _msg.get('Event')
        if D['Event'] == "click":
            D['EventKey'] = _msg.get('EventKey')
        return D

    return {'MsgType':'unkown','xml':xml}



if __name__ == '__main__':
    #关注
    a = """<xml><ToUserName><![CDATA[gh_b85e68a5fbc9]]></ToUserName>
    <FromUserName><![CDATA[oB3OBjp1S4KXK0gGjlRLErdIyHxU]]></FromUserName>
    <CreateTime>1385571577</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    <EventKey><![CDATA[]]></EventKey>
    </xml>"""

    print ParserXml(a)

    #文字
    a = """<xml><ToUserName><![CDATA[gh_19317ec8c4c1]]></ToUserName>
    <FromUserName><![CDATA[oU8KHt2JTqmAeDjAj-tFmzM17MNg]]></FromUserName>
    <CreateTime>1385804872</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[帮助]]></Content>
    <MsgId>5951986603887477314</MsgId>
    </xml>"""

    print ParserXml(a)

    #位置
    a = """<xml><ToUserName><![CDATA[gh_19317ec8c4c1]]></ToUserName>
    <FromUserName><![CDATA[oU8KHt2JTqmAeDjAj-tFmzM17MNg]]></FromUserName>
    <CreateTime>1385805246</CreateTime>
    <MsgType><![CDATA[location]]></MsgType>
    <Location_X>30.606155</Location_X>
    <Location_Y>114.288499</Location_Y>
    <Scale>15</Scale>
    <Label><![CDATA[中国湖北省武汉市江岸区开明路46号 邮政编码: 430000]]></Label>
    <MsgId>5951988210205246020</MsgId>
    </xml>"""
    print ParserXml(a)

    #图片
    a = """<xml><ToUserName><![CDATA[gh_19317ec8c4c1]]></ToUserName>
    <FromUserName><![CDATA[oU8KHt2JTqmAeDjAj-tFmzM17MNg]]></FromUserName>
    <CreateTime>1385805445</CreateTime>
    <MsgType><![CDATA[image]]></MsgType>
    <PicUrl><![CDATA[http://mmbiz.qpic.cn/mmbiz/Ge5ibOZsoialBf43aKPbdWpxIhxibsJvB1DmiaXbiafzEV59rxNeL7GdX3sCmIuCQCJ8SbqGAJrhOKa8j7h6oSXNR0Q/0]]></PicUrl>
    <MsgId>5951989064903737925</MsgId>
    <MediaId><![CDATA[Gz8XvDrX4GGWGabMmuGg-o7C-cFBxTrDEftsqlNLIgkVWLibnkoh8VDa-jytVpah]]></MediaId>
    </xml>"""
    print ParserXml(a)

    a = """<xml><ToUserName><![CDATA[gh_19317ec8c4c1]]></ToUserName>
    <FromUserName><![CDATA[oU8KHt2JTqmAeDjAj-tFmzM17MNg]]></FromUserName>
    <CreateTime>1385808469</CreateTime>
    <MsgType><![CDATA[video]]></MsgType>
    <MediaId><![CDATA[Hq5dW07AsEh1WQLwbFWQzCasIEepCjyH-SY8LmL1o_kUCnBgyycJ-OB9a5QC4yJi]]></MediaId>
    <ThumbMediaId><![CDATA[RtZoS9u6nngUJVap_aeJbvvIWIhMh3ImrhK8yShEsZtsVojDmR_L-YwgCPOUAA5b]]></ThumbMediaId>
    <MsgId>5952002052884841033</MsgId>
    </xml>"""
    print ParserXml(a)


    #~ <a href="http://www.baidu.com/">点击蓝色字体,打开百度搜索</a>



