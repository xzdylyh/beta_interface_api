#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest

@ddt.ddt
class TestCharge(unittest.TestCase):
    """点评微生活－API单接口"""
    @classmethod
    def setUpClass(cls):
        cls.__name__='储值模块'

    @classmethod
    def tearDownClass(cls):
        pass


    # ---------------------------------------charge START------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE1')))
    def testChargetoday(self, data):
        '''储值模块:当日储值统计/charge/today'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeToDay'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res'].has_key('shop_offline'))



    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE2')))
    def testChargeReceipt(self,data):
        '''储值模块:储值是否开发票/charge/receipt'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeReceipt'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res']['result']=='SUCCESS')


    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE3')))
    def testChargeChange(self,data):
        '''储值模块:储值调整/charge/change'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeChange'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res'].has_key('deal_id'))



    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE4')))
    def testChargeRule(self,data):
        '''储值模块:查看门店储值规则设置/charge/rule'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeRule'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res'].has_key('content'))


    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE5')))
    def testChargeView(self,data):
        '''储值模块:储值记录详情/charge/view'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeView'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res'].has_key('status'))



    @ddt.data(*(scripts.loadDdtData(filename='Charge.yaml',caseflag='CHARGE_CASE6')))
    def testPosChargedetail(self,data):
        '''储值模块/pos/chargedetail'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['PosChargeDetail'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('payStatus'))




if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestCharge)]
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