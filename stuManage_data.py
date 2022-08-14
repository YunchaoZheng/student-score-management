import streamlit as st
import pandas as pd
import time


def not_welcomed_login():
    # This is the most useless function in this project
    with st.form(key='登录框'):
        st.markdown('**不欢迎使用！也不要登录**')
        password = st.text_input('密码', placeholder='********', disabled=True)
        clicked = st.form_submit_button('登录(已由管理员禁用)')
        if clicked:
            with st.spinner('野郎！都说这个按钮已经禁用了'):
                time.sleep(1.5)
                st.experimental_rerun()
    pass


# 数据信息
stuManage_score_data_path = r'data/stuManage_scores.csv'
stuManage_score_data = pd.read_csv(stuManage_score_data_path)
stuManage_score_data_columns = stuManage_score_data.columns
stuManage_score_column_names_dict = {'id': '学号', 'CET4': 'CET4', 'CET6': 'CET6',
                                     'GPA': 'GPA', 'scholarship': '奖学金', 'will': '意愿',
                                     'recommendation': '推荐', 'fieldwork': '实习', 'interview': '面试',
                                     'score': '分数'}
stuManage_score_column_names = stuManage_score_data_columns.map(stuManage_score_column_names_dict)
stuManage_score_data_cet4_weight = 0.3
stuManage_score_data_cet6_weight = 0.7
stuManage_score_data_cet_weight = 0.1
stuManage_score_data_gpa_weight = 10.0
stuManage_score_data_scholarship_weight = 1.0
stuManage_score_data_will_weight = 1.0  # 木大木大
stuManage_score_data_recommendation_weight = 1.0
stuManage_score_data_fieldwork_weight = 5.0
stuManage_score_data_interview_weight = 0.4
stuManage_score_data_score_weight_min = 0.0
stuManage_score_data_score_weight_max = 10.0
stuManage_score_data_score_weight_step = 0.1


def recalculate_score():
    # 根据其他数据重新计算分数
    stuManage_score_data['score'] = (stuManage_score_data['CET4'] * stuManage_score_data_cet4_weight +
                                    stuManage_score_data['CET6'] * stuManage_score_data_cet6_weight) * \
                                   stuManage_score_data_cet_weight + \
                                   stuManage_score_data['GPA'] * stuManage_score_data_gpa_weight + \
                                   stuManage_score_data['scholarship'] * stuManage_score_data_scholarship_weight + \
                                   stuManage_score_data['recommendation'] * stuManage_score_data_recommendation_weight + \
                                   stuManage_score_data['fieldwork'] * stuManage_score_data_fieldwork_weight + \
                                   stuManage_score_data['interview'] * stuManage_score_data_interview_weight
    stuManage_score_data['score'] = stuManage_score_data['score'].apply(lambda x: round(x, 2))


recalculate_score()

# 网站信息
website_icon = '👩‍🎓'
website_title = '学生成绩管理系统'
# Sidebar
sidebar_website_title = '# 👩‍🎓 学生成绩管理系统'

sidebar_selectbox_choice = {'caption': '选择页面',
                            'page_query_caption': '查询成绩',
                            'page_insert_caption': '插入成绩',
                            'page_delete_caption': '删除成绩',
                            'page_update_caption': '更新成绩',
                            'page_weighted_score_caption': '加权成绩'}
sidebar_introduction = '''
---
<h2>项目名称</h2>
基于咖啡の学生成绩管理系统
<h2>项目描述</h2>
采用咖妃因作为系统内核，可以查询、插入、删除、更新、加权成绩。
'''
sidebar_team = '''
---
<h2>项目团队</h2>
<a href="https://user.qzone.qq.com/1530312643" target="blank">
<img src="https://img.shields.io/badge/%E4%BD%9C%E8%80%85-%E6%97%A9%E5%9D%82%E7%A7%80%E6%A8%B9-green?style=flat-square&logo=appveyor">
</img>
</a>
'''
sidebar_repos = ''''''
#
page_col_left_width = 3
page_col_right_width = 1
# 页 1 query
page_1_main_title = '## 生徒の查询成绩'
page_1_second_title = '#### Student Score Query'
page_1_introduction = '学生成绩查询模块，没有足够的咖啡的话我很办  ————  Hayasaka Hideki'
page_1_query_introduction = '这里查询到的分数是缺省权重计算的分数'
page_1_score_data_columns = ['id', 'CET4', 'CET6', 'GPA', 'scholarship', 'will', 'recommendation', 'fieldwork',
                             'interview', 'score']
# 页 2 insert
page_2_main_title = '## 生徒の插入成绩'
page_2_second_title = '#### Student Score Insert'
page_2_introduction = '这位是从夏威夷转学过来的夏川ゆか同学，人称天才少女  ————  排球女将'
page_2_to_be_inserted_id_label = '即将插入的学号(新增记录学号禁止更改)'
page_2_to_be_inserted_cet4_label = 'CET4'
page_2_to_be_inserted_cet4_default = 0
page_2_to_be_inserted_cet4_min_value = 0
page_2_to_be_inserted_cet4_max_value = 750
page_2_to_be_inserted_cet6_label = 'CET6'
page_2_to_be_inserted_cet6_default = 0
page_2_to_be_inserted_cet6_min_value = 0
page_2_to_be_inserted_cet6_max_value = 750
page_2_to_be_inserted_gpa_label = 'GPA'
page_2_to_be_inserted_gpa_default = 0.0
page_2_to_be_inserted_gpa_min_value = 0.0
page_2_to_be_inserted_gpa_max_value = 5.0
page_2_to_be_inserted_scholarship_label = '奖学金(等级1~5)'
page_2_to_be_inserted_scholarship_default = 0
page_2_to_be_inserted_scholarship_min_value = 0
page_2_to_be_inserted_scholarship_max_value = 5
page_2_to_be_inserted_will_label = '意愿(0.5一级)'
page_2_to_be_inserted_will_default = 0.0
page_2_to_be_inserted_will_min_value = 0.0
page_2_to_be_inserted_will_max_value = 5.0
page_2_to_be_inserted_recommendation_label = '推荐(0.5一级)'
page_2_to_be_inserted_recommendation_default = 0.0
page_2_to_be_inserted_recommendation_min_value = 0.0
page_2_to_be_inserted_recommendation_max_value = 5.0
page_2_to_be_inserted_fieldwork_label = '实习经历'
page_2_to_be_inserted_fieldwork_introduction = '是否具有实习经验'
page_2_to_be_inserted_fieldwork_default = False
page_2_to_be_inserted_interview_label = '面试'
page_2_to_be_inserted_interview_default = 0
page_2_to_be_inserted_interview_min_value = 0
page_2_to_be_inserted_interview_max_value = 100
page_2_to_be_inserted_score_introduction = '缺省权重计算的分数'
page_2_to_be_inserted_score_label = '即将插入的分数(新增记录缺省分数禁止更改)'
page_2_to_be_inserted_into_memory_introduction = '##### 点击按钮插入数据'
page_2_to_be_inserted_into_memory_label = '点我插入数据'
page_2_to_be_inserted_into_hard_drive_introduction = '##### 点击按钮持久化更改到硬盘 ⚠'
page_2_to_be_inserted_into_hard_drive_label = '点我持久化更改到硬盘 ⚠'
page_3_main_title = '## 生徒の删除成绩'
page_3_second_title = '#### Student Score Delete'
page_3_introduction = '啊，是我，将第三适格者少年的资料全部删除  ————  新世纪福音战士'
page_3_delete_introduction = '从下方选择一个倒霉蛋删除数据'
page_3_to_be_deleted_id_label = '即将删除的学号'
page_3_to_be_deleted_into_memory_introduction = '##### 点击按钮删除数据'
page_3_to_be_deleted_into_memory_label = '点我删除数据'
page_3_to_be_deleted_into_hard_drive_introduction = '##### 点击按钮持久化删除到硬盘 ⚠'
page_3_to_be_deleted_into_hard_drive_label = '点我持久化删除到硬盘 ⚠'
# 页 4 update
page_4_main_title = '## 生徒の更新成绩'
page_4_second_title = '#### Student Score Update'
page_4_introduction = 'JOJO 我不做人啦  ————  JOJO的奇妙冒险'
page_4_update_introduction = '从下方选择一个DIO更新数据'
page_4_to_be_updated_id_label = '即将更新数据的学号'
page_4_to_be_updated_score_introduction = '权重计算的分数'
page_4_to_be_updated_score_label = '即将更新的分数(更新记录分数禁止更改)'
page_4_to_be_updated_into_memory_introduction = '##### 点击按钮更新数据'
page_4_to_be_updated_into_memory_label = '点我更新数据'
# 页 5 weighted_score
page_5_main_title = '## 生徒の加权成绩'
page_5_second_title = '#### Student Weighted Score'
page_5_introduction = 'お願いします！  ————  海潮之声'
page_5_weighted_score_formula_introduction = '##### 成绩计算公式'
page_5_weight_setting_panel_introduction = '##### 权重设置面板'
page_5_cet4_weight_label = 'CET4 权重'
page_5_cet6_weight_label = 'CET6 权重'
page_5_cet_weight_label = 'CET 总权重'
page_5_gpa_weight_label = 'GPA 权重'
page_5_scholarship_weight_label = '奖学金 权重'
page_5_recommendation_weight_label = '推荐信 权重'
page_5_fieldwork_weight_label = '实习 权重'
page_5_interview_weight_label = '面试 权重'
page_5_to_be_applied_weight_into_memory_introduction = '##### 点击按钮应用权重'
page_5_to_be_applied_weight_into_memory_label = 'The World！'
page_5_to_be_applied_weighted_score_into_memory_introduction = '##### 点击按钮更新分数'
page_5_to_be_applied_weighted_score_into_memory_label = '点我更新数据'
