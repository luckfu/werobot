# -*- coding: utf-8 -*-
import hashlib
from parser import ParserXml
from reply import ReplyText,ReplyNews
from utils import to_unicode

class robot():
    def __init__(self,auth):
        self.auth=auth
        self.Recv = {}
        self.RecvType = None
        self.FromUserName = None
        self.ToUserName = None

    def chkauth(self,args):
        """
        接口验证函数
        从微信Server请求的URL中拿到‘signature’,‘timestamp’,‘nonce’和‘echostr’，
        然后再将token, timestamp, nonce三个排序并进行Sha1计算，并将计算结果和拿到的signature进行比较，
        如果相等，就说明验证通过。 其实只要把echostr返回去，就能通过验证。
        GET /smmt?signature=ce7dc595af984f707f5097d27a0d2e48d61b9b39&echostr=5918948252231272763&timestamp=1378486587&nonce=1378112535
        """
        _signature = _timestamp = _nonce = ''
        #print args

        if 'signature' in args: _signature = args['signature']
        if 'timestamp' in args: _timestamp = args['timestamp']
        if 'nonce' in args: _nonce = args['nonce']

        _s =[_timestamp, _nonce, self.auth]
        _s.sort()
        _s = ''.join(_s)
        if (hashlib.sha1(_s).hexdigest() == _signature):
            return True
        else:
            return False

    def parser(self,args,xml):
        try:
            if self.chkauth(args):
                self.recv = ParserXml(xml)
                self.RecvType = self.recv['MsgType']
                self.FromUserName = self.recv['FromUserName']
                self.ToUserName = self.recv['ToUserName']
                return True
            else:
                return False
        except :
            return False

    def replytext(self,text):
        return ReplyText(FromUserName=self.ToUserName,
                         ToUserName=self.FromUserName,
                         Content=text)


if __name__ == '__main__':

    robot = robot('smmt')

    D = {'signature':'ce7dc595af984f707f5097d27a0d2e48d61b9b39'
        ,'timestamp':'1378486587'
        ,'nonce':'1378112535'}

    a = """<xml><ToUserName><![CDATA[gh_b85e68a5fbc9]]></ToUserName>
    <FromUserName><![CDATA[oB3OBjp1S4KXK0gGjlRLErdIyHxU]]></FromUserName>
    <CreateTime>1385571577</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[subscribe]]></Event>
    <EventKey><![CDATA[]]></EventKey>
    </xml>"""

    print robot.chkauth(D)
    print robot.parser(D,a)
    print robot.replytext('拿百度测试')

    Attention = [
    {'Title':"欢迎使用<<店员微助手>>",
    'Description':'发送"帮助"获取使用指导',
    'PicUrl':"http://www.luckfu.com/cmcc/cmcclog.jpg",
    'Url':"http://www.luckfu.com/cmcc/index.php"}]