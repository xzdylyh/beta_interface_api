#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest

@ddt.ddt
class TestCredit(unittest.TestCase):
    """积分模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #-----------------------------------------Credit START--------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Credit.yaml',caseflag='CREDIT_CASE1')))
    def testCreditchange(self,data):
        '''积分接口:手工调整积分/credit/change'''

        #biz_id唯一标识
        biz_id = scripts.rndTimeStr() + '001'
        data['CreditChange']['biz_id'] = biz_id

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CreditChange'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res']['result']=='SUCCESS')



    @ddt.data(*(scripts.loadDdtData(filename='Credit.yaml',caseflag='CREDIT_CASE3')))
    def testCreditrule(self,data):
        '''积分接口:查看积分设置/credit/rule '''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CreditRule'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('consume'))



    @ddt.data(*(scripts.loadDdtData(filename='Credit.yaml',caseflag='CREDIT_CASE2')))
    def testCreditexchange(self,data):
        '''积分接口:积分换礼/credit/exchange'''

        biz_id = scripts.rndTimeStr() +'004'
        data['CreditExChange']['biz_id'] = biz_id

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CreditExChange'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res']['result']=='SUCCESS')



    @ddt.data(*(scripts.loadDdtData(filename='Credit.yaml',caseflag='CREDIT_CASE4')))
    def testCreaditshoprule(self,data):
        '''积分规则新接口/credit/shoprule'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CreditShopRule'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('consume'))




if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestCredit)]
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