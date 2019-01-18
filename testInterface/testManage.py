#_*_coding:utf-8_*_
import unittest,os,ddt,json
from globalVar import gl
from library import HTMLTESTRunnerCN

from library import scripts
from library.http import HttpWebRequest

@ddt.ddt
class TestManage(unittest.TestCase):
    """商户管理模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    #------------------------------------------Manage START----------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Manage.yaml',caseflag='MANAGE_CASE1')))
    def testCashierlist(self,data):
        '''商家接口:获取收银员列表/cashier/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CashierList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'])


    @ddt.data(*(scripts.loadDdtData(filename='Manage.yaml',caseflag='MANAGE_CASE2')))
    def testShoplist(self,data):
        '''商家接口:获取门店列表/shop/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ShopList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'])

    @ddt.data(*(scripts.loadDdtData(filename='Manage.yaml',caseflag='MANAGE_CASE3')))
    def testEmployee(self,data):
        '''商家接口:查询员工/employee/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['EmployeeList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'])



    @ddt.data(*(scripts.loadDdtData(filename='Manage.yaml',caseflag='MANAGE_CASE4')))
    def testPossignin(self,data):
        '''商家接口:收银员账号登陆签到/pos/signin'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['PosSignin'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )

        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('cashier_id'))



    @ddt.data(*(scripts.loadDdtData(filename='Manage.yaml',caseflag='MANAGE_CASE5')))
    def testPosshopcredit(self,data):
        '''硬pos获取用户的积分规则/pos/shopcredit'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['PosShopcredit'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('giftRange'))


if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestManage)]
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