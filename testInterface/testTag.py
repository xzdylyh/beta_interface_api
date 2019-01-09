#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest
from interface_project.library.scripts import retry


@ddt.ddt
class TestTag(unittest.TestCase):
    """标签模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    #-------------------------------------------------Tag START---------------------------------#

    @ddt.data(*(scripts.loadDdtData(filename='Tags.yaml',caseflag='TAGS_CASE2')))
    def testTaglistusertags(self,data):
        '''用户接口:用户标签列表/tag/listusertags'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['TagListUserTags'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])



    @ddt.data(*(scripts.loadDdtData(filename='Tags.yaml',caseflag='TAGS_CASE1')))
    def testTagtouser(self,data):
        '''用户接口:用户增加标签/tag/touser'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['TagToUser'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])

if __name__=="__main__":

    suite = unittest.TestSuite()
    tests = [unittest.TestLoader().loadTestsFromTestCase(TestTag)]
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