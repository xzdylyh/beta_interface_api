#_*_coding:utf-8_*_
import unittest,os,ddt,json
from globalVar import gl
from library import HTMLTESTRunnerCN

from library import scripts
from library.http import HttpWebRequest

@ddt.ddt
class TestCoupon(unittest.TestCase):
    """券模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    #----------------------------------------Coupon START---------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE1')))
    def testCouponsend(self,data):
        '''券接口:发券/coupon/send'''

        biz_id = scripts.rndTimeStr() + '006'
        data['CouponSend']['biz_id'] = biz_id

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponSend'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg'])
        self.assertTrue(res['res'].has_key('biz_id'))



    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE2')))
    def testCoupondetail(self,data):
        '''券接口:券模板详情/coupon/detail'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponDetail'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('give_friend'))



    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE3')))
    def testCouponList(self,data):
        '''券接口:券列表/coupon/list'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'])



    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE4')))
    def testUsergetusercoupons(self,data):
        '''根据卡号查询券列表/user/getusercoupons'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserGetusercoupons'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'])



    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE5')))
    def testCoupongift(self,data):
        '''券转赠接口/coupon/gift断言30013,该券已转赠过不能重复提交'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponGift'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 30013, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE6')))
    def testCouponSendSearch(self,data):
        '''券接口:根据biz_id查询发券详情/coupon/sendsearch'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['SendSearch'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言根据biz_id查询发券详情
        self.assertTrue(res['res'].has_key('cno'))


    @ddt.data(*(scripts.loadDdtData(filename='Coupon.yaml',caseflag='COUPON_CASE7')))
    def testCouponC2uinfo(self,data):
        '''券接口:查询用户下一张券的信息/coupon/c2uinfo'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['CouponC2uinfo'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言查询用户下一张券的信息接口
        self.assertTrue(res['res'].has_key('status'))



if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestCoupon)]
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
