#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest

@ddt.ddt
class TestSearch(unittest.TestCase):
    """查询模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #---------------------------------------Search START-------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE1')))
    def testConsumeall(self,data):
        '''查询接口:/consume/all'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ConsumeAll'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE2')))
    def testConsumelist(self,data):
        '''查询接口:消费记录列表/consume/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ConsumeList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE3')))
    def testChargelist(self,data):
        '''查询接口:储值记录列表/charge/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])

    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE4')))
    def testConsumeview(self,data):
        '''查询接口:消费记录详情/consume/view '''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ConsumeView'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE5')))
    def testConsumeuser(self,data):
        '''查询接口:用户消费记录/consume/user'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ConsumeUser'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE6')))
    def testCouponoverdue(self,data):
        '''查询接口:/coupon/overdue'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponOverdue'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Search.yaml',caseflag='SEARCH_CASE7')))
    def testChargeuser(self,data):
        '''查询接口:指定会员储值记录列表/charge/user'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeUser'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res']['data'],msg='查询内容为空')



if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestSearch)]
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