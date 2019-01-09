#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest



@ddt.ddt
class TestActivity(unittest.TestCase):
    """活动模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass



    #---------------------------------------Activity START-------------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Activity.yaml',caseflag='ACTIVITY_CASE1')))
    def testActivityGetuserthumbuplog(self,data):
        '''活动接口:查询用户参与的集赞活动/activity/getuserthumbuplog'''
        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Getuserthumbuplog'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # me,he = scripts.MultipartPartData(
        #     req=data['Getuserthumbuplog'],
        #     appid = data['Appid'],
        #     v = 2.0,
        #     ts = 1,
        #     sig = 1,
        #     boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        # )
        # interface = HttpWebRequest()
        # interface.url = data['Url']
        # interface.payload = me
        # interface.headers = he
        # res = interface.post

        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])#断言
        self.assertTrue(res['res'])


    # @ddt.data(*(scripts.loadDdtData(filename='Activity.yaml',caseflag='ACTIVITY_CASE2')))
    # def testActivitylist(self,data):
    #     '''活动接口:获取活动列表/activity/list'''
    #
    #     # 整合数据，调用接口，获取返回结果
    #     res = scripts.loadtestInterface(
    #         instance=HttpWebRequest(),
    #         instance_pro='post',
    #         data=data['ActivityList'],
    #         appid=data['Appid'],
    #         desc=data['Desc'],
    #         url=data['Url']
    #     )
    #     #断言
    #     self.assertEqual(res['errcode'],0,res['errmsg'])
    #     self.assertTrue(res['res'])
    #
    #
    # @ddt.data(*(scripts.loadDdtData(filename='Activity.yaml',caseflag='ACTIVITY_CASE3')))
    # def testActivityOtherlist(self,data):
    #     '''异业营销:获取异业营销活动列表/activity/otherlist'''
    #
    #     # 整合数据，调用接口，获取返回结果
    #     res = scripts.loadtestInterface(
    #         instance=HttpWebRequest(),
    #         instance_pro='post',
    #         data=data['ActivityOtherList'],
    #         appid=data['Appid'],
    #         desc=data['Desc'],
    #         url=data['Url']
    #     )
    #
    #     #断言
    #     self.assertEqual(res['errcode'],0,res['errmsg'])
    #     self.assertTrue(res['res'])


if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestActivity)]
    suite.addTests(tests)

    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yhleng"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()