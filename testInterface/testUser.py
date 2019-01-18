#_*_coding:utf-8_*_
import unittest,os,ddt,json
from globalVar import gl
from library import HTMLTESTRunnerCN

from library import scripts
from library.http import HttpWebRequest

@ddt.ddt
class TestUser(unittest.TestCase):
    """用户模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    #-----------------------------------------User START----------------------------------------#
    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE1')))
    def testUseraccount(self,data):
        '''用户接口:获取用户账户信息/user/account'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserAccount'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])



    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE2')))
    def testUsergetinfo(self,data):
        '''用户接口:获取微信用户账户信息/user/getinfo'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserGetinfo'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE3')))
    def testUsercheckcard(self,data):
        '''用户接口:验证实体卡信息/user/checkcard'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserCheckCard'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE4')))
    def testUsercardinfo(self,data):
        '''用户接口:查询电子卡接口/user/cardinfo'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserCardinfo'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE5')))
    def testUseredit(self,data):
        '''用户接口:修改会员信息/user/edit'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserEdit'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE6')))
    def testUserugetinfo(self,data):
        '''用户接口:unionid查询用户/user/ugetinfo'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserUgetinfo'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE7')))
    def testUseruopencard(self,data):
        '''用户接口:unionid开卡/user/uopencard'''

        #unionid电子卡号
        data['UserUopencard']['unionid'] = scripts.rndTimeStr()  +'005'

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserUopencard'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE8')))
    def testUserSendCode(self,data):
        '''用户接口:给指定用户发送验证码/user/sendcode'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserSendcode'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言 给指定用户发送验证码
        self.assertEqual(res['res']['result'],'SUCCESS',res['res']['result'])



    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE9')))
    def testUserCreditListI(self,data):
        '''用户接口:用户积分记录/user/creditlist'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserCreditList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言，用户积分记录
        self.assertTrue(res['res'],"查询结果为空") #查询res为空


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE10')))
    def testUserDynamic(self,data):
        '''用户接口：获取用户动态卡号/user/dynamic'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserDynamic'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言获取用户动态卡号接口
        self.assertTrue(res['res']['dynamic_uno'],msg='查询卡号为空')


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE11')))
    def testUserGetoverdueCoupon(self,data):
        '''用户接口：获取已使用优惠券/user/getusedcoupons'''

        # 获取已使用优惠券
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UsedCoupon'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言获取已使用优惠券
        self.assertTrue(res['res'])


    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE12')))
    def testUserGetUseCoupon(self,data):
        '''用户接口：获取已过期优惠券user/getoverduecoupons'''

        # 获取已过期优惠券
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['OverDueCoupon'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言获取已过期优惠券
        self.assertTrue(res['res'])




    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE13')))
    def testUserGetc2uInfo(self,data):
        '''用户接口：根据券获取用户账户信息/user/getc2uinfo'''

        # 根据券获取用户账户信息
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['Getc2uinfo'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #断言获取已过期优惠券
        self.assertTrue(res['res'])



    @ddt.data(*(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE14')))
    def testUserMergeActualCard(self,data):
        '''用户接口：根据券获取用户账户信息/user/mergeActualCard'''

        # 合并微信和实体卡
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['MergeActualCard'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        #断言
        self.assertEqual(res['errcode'],22019,res['errmsg']) #断言该实体卡已被其他微信卡绑定



    @ddt.data(
        *(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE15'))
    )
    def testUserCouponlist(self,data):
        """会员全部券接口/user/couponlist"""

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserCouponList'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])


    @ddt.data(
        *(scripts.loadDdtData(filename='User.yaml',caseflag='USER_CASE16'))
    )
    def testUserPhoneCard(self,data):
        """手机开卡/user/phonecard"""

        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserPhoneCard'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res']['result']=='SUCCESS')




if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestUser)]
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