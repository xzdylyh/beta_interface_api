#_*_coding:utf-8_*_
import unittest,os,ddt,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN

from interface_project.library import scripts
from interface_project.library.http import HttpWebRequest

@ddt.ddt
class TestGrade(unittest.TestCase):
    """等级模块"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #----------------------------------------Grade START---------------------------------------#
    #等级接口
    @ddt.data(*(scripts.loadDdtData(filename='Grade.yaml',caseflag='GRADE_CASE1')))
    def testGraderule(self,data):
        '''等级接口:查看等级设置/grade/rule'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['GradeRule'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('grades'))



    @ddt.data(*(scripts.loadDdtData(filename='Grade.yaml',caseflag='GRADE_CASE2')))
    def testUsergrade(self,data):
        '''等级接口:查询会员等级信息/user/grade'''

        # 整合数据，调用接口，获取返回结果
        res = scripts.loadtestInterface(
            instance=HttpWebRequest(),
            instance_pro='post',
            data=data['UserGrade'],
            appid=data['Appid'],
            desc=data['Desc'],
            url=data['Url']
        )
        # 断言
        self.assertEqual(res['errcode'], 0, res['errmsg'])
        self.assertTrue(res['res'].has_key('name'))


if __name__=="__main__":

    suite = unittest.TestSuite()

    tests = [unittest.TestLoader().loadTestsFromTestCase(TestGrade)]
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