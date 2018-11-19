# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : case.py
from Interface.testFengzhuang import TestApi
from Public.get_excel import datacel
from Public.log import LOG, logger
import os
from config.config_T import Config_Try_Num, TestPlanUrl

path = os.getcwd() + '/test_case_data/case.xlsx'
listid, listtoken, listconeent, listurl, listfangshi, listqiwang, listname, listbingxing = datacel(path)
from Public.panduan import assert_in

global list_pass
global list_fail
global list_json
global listrelust
global list_elapsed
global list_weizhi
global list_exption
global error_num

@logger('测试')
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_elapsed = []  # 相应时间
    list_weizhi = 0
    list_exption = 0
    error_num = 0
    for i in range(len(listurl)):

        if isinstance(listbingxing[i], float):

            print('1')

        else:

            while error_num <= Config_Try_Num + 1:
                api = TestApi(url=TestPlanUrl + listurl[i], token=listtoken[i], connent=listconeent[i],
                              fangshi=listfangshi[i])
                apijson = api.getJson()
                if apijson['code'] == 0:
                    LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listconeent[i], listurl[i], apijson, listqiwang[i]))
                    assert_re = assert_in(asserqiwang=listqiwang[i], fanhuijson=apijson)
                    if assert_re['code'] == 0:
                        list_json.append(apijson['result'])
                        listrelust.append('pass')
                        list_elapsed.append(apijson['elapsed'])
                        list_pass += 1
                        error_num = 0
                        break
                    elif assert_re['code'] == 1:
                        if error_num <= Config_Try_Num:
                            error_num += 1
                            LOG.info('失败重试中')
                        else:
                            LOG.info('失败重试中次数用完，最后结果')
                            error_num = 0
                            list_fail += 1
                            listrelust.append('fail')
                            list_json.append(apijson['result'])
                            list_elapsed.append(apijson['elapsed'])
                            break
                    elif assert_re['code'] == 2:
                        if error_num < Config_Try_Num:
                            error_num += 1
                            LOG.info('失败重试中')
                        else:
                            LOG.info('失败重试中次数用完，最后结果')
                            error_num = 0
                            list_exption += 1
                            listrelust.append('exception')
                            list_json.append(assert_re['result'])
                            break
                    else:
                        if error_num < Config_Try_Num:
                            error_num += 1
                            LOG.info('失败重试中')
                        else:
                            LOG.info('失败重试中次数用完，最后结果')
                            error_num = 0
                            list_weizhi += 1
                            listrelust.append('未知错误')
                            list_json.append('未知错误')
                            break
                else:
                    if error_num < Config_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(apijson['result'])
                        break
    return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi, list_elapsed


def executionapi(i):
    while error_num <= Config_Try_Num + 1:
        api = TestApi(url=TestPlanUrl + listurl[i], token=listtoken[i], connent=listconeent[i],
                      fangshi=listfangshi[i])
        apijson = api.getJson()
        if apijson['code'] == 0:
            LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listconeent[i], listurl[i], apijson, listqiwang[i]))
            assert_re = assert_in(asserqiwang=listqiwang[i], fanhuijson=apijson)
            if assert_re['code'] == 0:
                list_json.append(apijson['result'])
                listrelust.append('pass')
                list_elapsed.append(apijson['elapsed'])
                list_pass += 1
                error_num = 0
                break
            elif assert_re['code'] == 1:
                if error_num <= Config_Try_Num:
                    error_num += 1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num = 0
                    list_fail += 1
                    listrelust.append('fail')
                    list_json.append(apijson['result'])
                    list_elapsed.append(apijson['elapsed'])
                    break
            elif assert_re['code'] == 2:
                if error_num < Config_Try_Num:
                    error_num += 1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num = 0
                    list_exption += 1
                    listrelust.append('exception')
                    list_json.append(assert_re['result'])
                    break
            else:
                if error_num < Config_Try_Num:
                    error_num += 1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num = 0
                    list_weizhi += 1
                    listrelust.append('未知错误')
                    list_json.append('未知错误')
                    break
        else:
            if error_num < Config_Try_Num:
                error_num += 1
                LOG.info('失败重试中')
            else:
                LOG.info('失败重试中次数用完，最后结果')
                error_num = 0
                list_exption += 1
                listrelust.append('exception')
                list_json.append(apijson['result'])
                break

    return list
