#_*_coding:utf-8_*_
import os,time,unittest
import requests,yaml,json,ddt
from library.excel import Excel
from base import base_config
from globalVar import gl
from library import scripts

from library import HTMLTESTRunnerCN
from library.http import HttpWebRequest

'''
点评微生活－API接口场景
'''
@ddt.ddt
class TestScenario(unittest.TestCase):#点评微生活API接口
    '''点评微生活－API接口场景'''
    #初始化,setUp每个测试方法,执行一次;如果需要只执行一次使用setUpClass(cls)  需要classmethod修饰

    def setUp(self):
        self.configPath =  gl.configPath
        configyaml = os.path.join(self.configPath,'config.yaml')
        self.reportPath = gl.reportPath



    '''
    #储值撤销场景:储值预览->储值提交->储值撤销
    '''
    @unittest.skipIf(scripts.getRunFlag('testChargeAndCancel') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s',filename='ChargeAndCancel.yaml',caseflag='ChargeAndCancel'))
    def testChargeAndCancel(self,data):
        '''储值撤销场景:储值预览->储值提交->储值撤销'''
        '''--------------------------交易预览接口----------------------'''
        biz_id_01 = scripts.rndTimeStr() + '007'
        data['ChargePreview']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargePreview'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargePreviewUrl']
        )
        self.assertEquals(res['errcode'], 0, res['errmsg']) #交易预览断言

        '''--------------------------交易提交接口----------------------'''
        data['ChargeCommit']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        commitResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargeCommit'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargeCommitUrl']
        )
        self.assertEquals(commitResult['errcode'], 0, commitResult['errmsg']) #交易提交断言

        time.sleep(5)

        '''--------------------------交易撤销接口----------------------'''
        data['ChargeCancel']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        cancelResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargeCancel'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargeCancelUrl']
        )
        self.assertEquals(cancelResult['errcode'], 0, cancelResult['errmsg']) #交易撤销断言


    '''
    #自定义充值并消费储值业务场景:储值预览->储值提交->交易预览->交易提交->交易撤销
    '''
    @unittest.skipIf(scripts.getRunFlag('testChargeAndDeal') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='ChargeAndDeal.yaml', caseflag='ChargeAndDeal'))
    def testChargeAndDeal(self,data):
        '''自定义充值并消费储值业务场景:储值预览->储值提交->交易预览->交易提交->交易撤销'''

        biz_id_01 = str(scripts.rndTimeStr()) +'008'
        data['ChargePreview']['biz_id'] = biz_id_01

        '''--------------------------储值预览----------------------'''
        # 整合数据，调用接口，获取返回结果
        previewResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargePreview'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargePreviewUrl']
        )
        self.assertEquals(previewResult['errcode'], 0,previewResult['errmsg'])#储值预览

        '''--------------------------储值提交----------------------'''
        data['ChargeCommit']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        commitResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargeCommit'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargeCommitUrl']
        )
        self.assertEquals(commitResult['errcode'], 0, commitResult['errmsg']) #储值提交

        '''--------------------------交易预览----------------------'''
        biz_id_03 = scripts.rndTimeStr() + '009'
        data['DealPreview']['biz_id'] = biz_id_03

        # 整合数据，调用接口，获取返回结果
        dealPreviewResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['DealPreview'],appid=data['Appid'],
            desc=data['Desc'],url=data['DealPreviewUrl']
        )
        self.assertEquals(dealPreviewResult['errcode'], 0,dealPreviewResult['errmsg'])#交易预览

        '''--------------------------交易提交---------------------'''
        data['DealCommit']['biz_id'] = biz_id_03

        # 整合数据，调用接口，获取返回结果
        dealcommitResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['DealCommit'],appid=data['Appid'],
            desc=data['Desc'],url=data['DealCommitUrl']
        )
        self.assertEquals(dealcommitResult['errcode'], 0, dealcommitResult['errmsg']) #交易提交


        '''-------------------------交易撤销---------------------'''
        data['DealCancel']['biz_id'] = biz_id_03

        # 整合数据，调用接口，获取返回结果
        dealcancelResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['DealCancel'],appid=data['Appid'],
            desc=data['Desc'],url=data['DealCancelUrl']
        )
        self.assertEquals(dealcancelResult['errcode'], 0,dealcancelResult['errmsg']) #交易取消



    '''
    #发券并撤销
    '''
    @unittest.skipIf(scripts.getRunFlag('testCouponSendAndCancel')=='N','验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='CouponSendAndCancel.yaml', caseflag='couponSendAndCancel'))
    def testCouponSendAndCancel(self,data):
        '''发券并撤销业务场景:发券->撤销'''

        # 场景顺序执行
        biz_id_01 = scripts.rndTimeStr() + '010'
        # ----修改数据----
        data['CouponSend']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        sendResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['CouponSend'],appid=data['Appid'],
            desc=data['Desc'],url=data['CouponSendUrl']
        )
        self.assertEqual(sendResult['errcode'],0,sendResult['errmsg']) #发券断言


        #撤销发券
        data['CouponCancel']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        cancelResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['CouponCancel'],appid=data['Appid'],
            desc=data['Desc'],url=data['CouponCancelUrl']
        )
        #断言
        self.assertEqual(cancelResult['errcode'],0,cancelResult['errmsg']) #撤销发券断言




    @unittest.skipIf(scripts.getRunFlag('testGradeEditAndDesc') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='GradeEditAndDesc.yaml', caseflag='Grade'))
    def testGradeEditAndDesc(self,data):
        '''会员升级降级:储值调整增加200->会员升级->储值调整减少200'''

        # 整合数据，调用接口，获取返回结果
        Result = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargeChangeAdd'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargeChangeUrl']
        )
        self.assertEqual(Result['errcode'], 0, Result['errmsg']) #储值调整接口断言

        #会员升级
        # 整合数据，调用接口，获取返回结果
        editResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['GradeEdit'],appid=data['Appid'],
            desc=data['Desc'],url=data['GradeEditUrl']
        )
        self.assertEqual(editResult['errcode'], 0, editResult['errmsg']) #会员升级接口断言

        #储值调整 减少200
        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['ChargeChange'],appid=data['Appid'],
            desc=data['Desc'],url=data['ChargeChangeUrl']
        )
        #断言
        self.assertEqual(res['errcode'],0,res['errmsg']) #储值调整接口减少200断言



    @unittest.skipIf(scripts.getRunFlag('testCouponCmbSendAndCancel') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='CouponCmbSendAndCancel.yaml', caseflag='OtherCoupon'))
    def testCouponCmbSendAndCancel(self,data):
        '''异业营销cmb发券并撤销场景: 获取异业营销活动列表->异业营销cmb发券->异业营销券码核销'''

        # 获取异业营销活动列表
        # 整合数据，调用接口，获取返回结果
        result = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['OtherList'],appid=data['Appid'],
            desc=data['Desc'],url=data['OtherListUrl']
        )
        self.assertTrue(result['res']) #异业营销活动列表res[]不为空断言
        aid = result['res'][0]['id']

        # 异业营销CMB发券
        biz_id = scripts.rndTimeStr() + '01'
        # ----------参数给值------------#
        data['CmbSend']['biz_id'] = biz_id  # 唯一值
        data['CmbSend']['aid'] = aid  # 活动id
        # -------------------------------#
        # 整合数据，调用接口，获取返回结果
        sendresult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['CmbSend'],appid=data['Appid'],
            desc=data['Desc'],url=data['CmbSendUrl']
        )
        self.assertEqual(sendresult['errcode'], 0, sendresult['errmsg']) #异业营销CMB发券接口
        coupon_code = sendresult['res']['coupon_codes'][0]['code']


        # 异业营销券码核销
        data['OtherVerification']['coupon_code'] = str(coupon_code)

        # 整合数据，调用接口，获取返回结果
        cancelResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['OtherVerification'],appid=data['Appid2'],
            desc=data['Desc'],url=data['OtherVerificationUrl']
        )
        self.assertEqual(cancelResult['errcode'],0, cancelResult['errmsg']) #异业营销券码核销接口



    @unittest.skipIf(scripts.getRunFlag('testCouponOtherSendAndCancel') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='CouponOtherSendAndCancel.yaml',
                                   caseflag='OtherCoupon'))
    def testCouponOtherSendAndCancel(self,data):
        '''异业营销发券并撤销场景: 获取异业营销活动列表->异业营销发券->异业营销券码核销'''

        # 获取异业营销活动列表
        # 整合数据，调用接口，获取返回结果
        result = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['OtherList'],appid=data['Appid'],
            desc=data['Desc'],url=data['OtherListUrl']
        )
        self.assertTrue(result['res'])
        aid = str(result['res'][0]['id'])

        # 异业营销发券
        biz_id_01 = scripts.rndTimeStr() + '011'
        #----------参数给值------------#
        data['OtherSend']['biz_id'] = biz_id_01 #唯一值
        data['OtherSend']['aid'] = aid #活动id

        # 整合数据，调用接口，获取返回结果
        sendresult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['OtherSend'],appid=data['Appid'],
            desc=data['Desc'],url=data['OtherSendUrl']
        )
        self.assertEqual(sendresult['errcode'],0,sendresult['errmsg']) #异业营销发券接口断言
        coupon_code = sendresult['res']['coupon_codes'][0]['code']



        #异业营销券码核销
        data['OtherVerification']['coupon_code'] = coupon_code

        # 整合数据，调用接口，获取返回结果
        cancelresult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['OtherVerification'],appid=data['Appid2'],
            desc=data['Desc'],url=data['OtherVerificationUrl']
        )
        self.assertEqual(cancelresult['errcode'],0,cancelresult['errmsg']) #断言




    @unittest.skipIf(scripts.getRunFlag('testDealAndRollback') == 'N', '验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='DealAndRollback.yaml',
                                   caseflag='DealAndRollback'))
    def testDealAndRollback(self,data):
        '''消费并冲正场景: 交易预览->交易冲正'''

        #交易预览
        biz_id_01 = scripts.rndTimeStr() +'012'
        data['DealPreview']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        reviewResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['DealPreview'],appid=data['Appid'],
            desc=data['Desc'],url=data['DealPreviewUrl']
        )
        #断言
        self.assertEqual(reviewResult['errcode'],0,reviewResult['errmsg']) #消费预览断言



        #交易冲正
        data['DealRollback']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        rollResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['DealRollback'],appid=data['Appid'],
            desc=data['Desc'],url=data['DealRollbackUrl']
        )
        #断言
        self.assertEqual(rollResult['errcode'],0,rollResult['errmsg']) #交易冲正断言




    @unittest.skipIf(scripts.getRunFlag('testCouponSendAndAdjust')=='N','验证执行配置')
    @ddt.data(*scripts.loadDdtData(Itype='s', filename='CouponSendAndAdjust.yaml',caseflag='couponSendAndAdjust'))
    def testCouponSendAndAdjust(self,data):
        '''发券并手工调账核销券:发券->获取用户账户信息->手工调账核销券'''

        #发券
        biz_id_01 = scripts.rndTimeStr() + '013'
        # ----修改数据----
        data['CouponSend']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        sendResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['CouponSend'],appid=data['Appid'],
            desc=data['Desc'],url=data['CouponSendUrl']
        )
        self.assertEqual(sendResult['errcode'],0,sendResult['errmsg']) #发送券接口断言

        #获取用户账户信息
        # 整合数据，调用接口，获取返回结果
        accountResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['UserAccount'],appid=data['Appid'],
            desc=data['Desc'],url=data['UserAccountUrl']
        )
        #接口断言
        self.assertEqual(accountResult['errcode'],0,accountResult['errmsg']) #获取用户账户信息接口断言
        self.assertTrue(accountResult['res'],accountResult['errmsg'])
        coupon_id_02 = accountResult['res'][0]['coupons'][0]['coupon_ids'][0] #券id结构取值

        #手工调账核销券
        data['CouponAdjust']['coupon_ids'].append(coupon_id_02) #将上一步查到的id传给核销接口

        # 整合数据，调用接口，获取返回结果
        adjustResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),instance_pro='post',data=data['CouponAdjust'],appid=data['Appid'],
            desc=data['Desc'],url=data['CouponAdjustUrl']
        )
        #断言
        self.assertEqual(adjustResult['errcode'],0,adjustResult['errmsg'])#手工调帐核销断言
        self.assertEqual(adjustResult['res']['result'],'SUCCESS',adjustResult['res']['result']) #手工调帐返回结果断言


    '''
    储值并开发票场景:储值预览->储值提交->可开发票查询->开发票
    '''
    @unittest.skipIf(
        scripts.getRunFlag(
            'testChargeAndReceipt') == 'N', '验证执行配置'
    )
    @ddt.data(
        *scripts.loadDdtData(
            Itype='s',
            filename='ChargeAndReceipt.yaml',
            caseflag='ChargeAndReceipt')
    )
    def testChargeAndReceipt(self,data):
        '''储值并开发票场景:储值预览->储值提交->可开发票查询->开发票'''
        '''step-1--------------------------交易预览接口----------------------'''
        biz_id_01 = scripts.rndTimeStr() + '007'
        data['ChargePreview']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargePreview'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['ChargePreviewUrl']
        )
        self.assertEquals(res['errcode'], 0, res['errmsg']) #交易预览断言

        '''step-2--------------------------交易提交接口----------------------'''
        data['ChargeCommit']['biz_id'] = biz_id_01

        # 整合数据，调用接口，获取返回结果
        commitResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeCommit'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['ChargeCommitUrl']
        )
        self.assertEquals(commitResult['errcode'], 0, commitResult['errmsg']) #交易提交断言

        '''step-3--------------------------用户可开发票查询接口----------------------'''
        # 整合数据，调用接口，获取返回结果
        selectResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeReceiptstat'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['ChargeReceiptstatUrl']
        )
        self.assertEquals(selectResult['errcode'], 0, selectResult['errmsg'])
        self.assertTrue(selectResult['res'])

        '''step-4--------------------------开发票接口----------------------'''
        data['ChargeReceiptbatch']['biz_id'] = str(biz_id_01)
        # 整合数据，调用接口，获取返回结果
        batchResult = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['ChargeReceiptbatch'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['ChargeReceiptbatchUrl']
        )
        self.assertEquals(batchResult['errcode'], 0, batchResult['errmsg'])
        self.assertTrue(batchResult['res']['result']=="开发票成功")


if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestScenario)]
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

