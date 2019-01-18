#_*_coding:utf-8_*_
import unittest,os,ddt,json
from globalVar import gl
from library import HTMLTESTRunnerCN

from library import scripts
from library.http import HttpWebRequest


@ddt.ddt
class TestDeal(unittest.TestCase):
    """消费模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #--------------------------------------Deal START---------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Deal.yaml',caseflag='DEAL_CASE1')))
    def testDealconsumetoday(self,data):
        '''交易模块:当日交易计录统计/consume/today'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ConsumeToday'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('shop'))



    @ddt.data(*(scripts.loadDdtData(filename='Deal.yaml',caseflag='DEAL_CASE2')))
    def testDealgetpaytype(self,data):
        '''交易模块:获取交易/储值支付方式/deal/getpaytype'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['DealGetPayType'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('1'))



    @ddt.data(*(scripts.loadDdtData(filename='Deal.yaml',caseflag='DEAL_CASE3')))
    def testDealsendnotification(self,data):
        '''交易模块/deal/sendnotification'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['DealSendnotification'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res']['result'] == 'SUCCESS')



    @ddt.data(*(scripts.loadDdtData(filename='Deal.yaml',caseflag='DEAL_CASE4')))
    def testDealsendnotification(self,data):
        '''交易模块/deal/verifypassword检查支付密码'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['dealVerifypassword'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res']['result'] == 'OK')



if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestDeal)]
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