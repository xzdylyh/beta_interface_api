#_*_coding:utf-8_*_
import unittest
from interface_project.testScenario import testScenarioCase
from interface_project.testInterface import testActivity,testCharge,\
    testCoupon,testCredit,testDeal,testGrade,testManage,testProduct,\
    testSearch,testTag,testUser
import os,time,json
from interface_project.globalVar import gl
from interface_project.library import HTMLTESTRunnerCN
from interface_project.library import scripts
from interface_project.library.emailstmp import EmailClass
import gevent
from gevent.pool import Pool

def loadTestsList():
    list = [testCoupon, testCharge, testActivity]

    tests = []
    for module in list:
        tests.append(unittest.TestLoader().loadTestsFromModule(module))
    return tests


if __name__=="__main__":
    suite = []
    for m,v in enumerate(loadTestsList()):
        suite.append(unittest.TestSuite())
        suite[m].addTests(list(v))


    task = []
    pool = Pool(10)
    k=0
    for i in suite:
        k+=1
        filePath = os.path.join(gl.reportPath, 'Report{}.html'.format(k))  # 确定生成报告的路径
        print filePath
        print i
        with file(filePath, 'wb') as fp:
            runner = HTMLTESTRunnerCN.HTMLTestRunner(
                stream=fp,
                title=u'接口自动化测试报告',
                description=u'详细测试用例结果',  # 不传默认为空
                tester=u"yhleng"  # 测试人员名字，不传默认为小强
            )
            # 运行测试用例
        task.append(pool.spawn(runner.run,(i,)))
        #.run(suite)
        fp.close()
    gevent.joinall(task)
    pool.kill()

    # #发送测试报告To Email
    # EmailClass().send
