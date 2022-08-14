import time

import pandas as pd
import streamlit as st
import stuManage_data


def page():
    # title 部分
    col_l, col_r = st.columns([stuManage_data.page_col_left_width, stuManage_data.page_col_right_width])
    with col_l:
        st.markdown(stuManage_data.page_5_main_title)
        st.markdown(stuManage_data.page_5_second_title)
        st.markdown(stuManage_data.page_5_introduction)
    with col_r:
        stuManage_data.not_welcomed_login()
    st.markdown('---')
    st.markdown(stuManage_data.page_5_weighted_score_formula_introduction)
    weighted_score_formula_data = pd.DataFrame({'CET4 权重': stuManage_data.stuManage_score_data_cet4_weight,
                                                'CET6 权重': stuManage_data.stuManage_score_data_cet6_weight,
                                                'CET 总权重': stuManage_data.stuManage_score_data_cet_weight,
                                                'GPA 权重': stuManage_data.stuManage_score_data_gpa_weight,
                                                '奖学金 权重': stuManage_data.stuManage_score_data_scholarship_weight,
                                                '推荐信 权重': stuManage_data.stuManage_score_data_recommendation_weight,
                                                '实习 权重': stuManage_data.stuManage_score_data_fieldwork_weight,
                                                '面试 权重': stuManage_data.stuManage_score_data_interview_weight, },
                                               index=['权重系数'])
    st.table(weighted_score_formula_data)
    formula_str = rf'''成绩 = \left ( CET4\times {stuManage_data.stuManage_score_data_cet4_weight} +
                 CET6 \times {stuManage_data.stuManage_score_data_cet6_weight}\right )
                 \times {stuManage_data.stuManage_score_data_cet_weight} +
                 GPA\times {stuManage_data.stuManage_score_data_gpa_weight} +
                 奖学金\times {stuManage_data.stuManage_score_data_scholarship_weight} +
                 推荐信 \times{stuManage_data.stuManage_score_data_recommendation_weight} +
                 实习 \times {stuManage_data.stuManage_score_data_fieldwork_weight} +
                 面试 \times {stuManage_data.stuManage_score_data_interview_weight}'''
    st.latex(formula_str)
    st.markdown('---')
    st.markdown(stuManage_data.page_5_weight_setting_panel_introduction)
    col_1, col_2, col_3, col_4 = st.columns([1, 1, 1, 1])
    with col_1:
        cet4_weight = st.number_input(stuManage_data.page_5_cet4_weight_label,
                                      value=stuManage_data.stuManage_score_data_cet4_weight,
                                      min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                      max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                      step=stuManage_data.stuManage_score_data_score_weight_step)
        scholarship_weight = st.number_input(stuManage_data.page_5_scholarship_weight_label,
                                             value=stuManage_data.stuManage_score_data_scholarship_weight,
                                             min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                             max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                             step=stuManage_data.stuManage_score_data_score_weight_step)
    with col_2:
        cet6_weight = st.number_input(stuManage_data.page_5_cet6_weight_label,
                                      value=stuManage_data.stuManage_score_data_cet6_weight,
                                      min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                      max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                      step=stuManage_data.stuManage_score_data_score_weight_step)
        recommendation_weight = st.number_input(stuManage_data.page_5_recommendation_weight_label,
                                                value=stuManage_data.stuManage_score_data_recommendation_weight,
                                                min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                                max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                                step=stuManage_data.stuManage_score_data_score_weight_step)
    with col_3:
        cet_weight = st.number_input(stuManage_data.page_5_cet_weight_label,
                                     value=stuManage_data.stuManage_score_data_cet_weight,
                                     min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                     max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                     step=stuManage_data.stuManage_score_data_score_weight_step)
        fieldwork_weight = st.number_input(stuManage_data.page_5_fieldwork_weight_label,
                                           value=stuManage_data.stuManage_score_data_fieldwork_weight,
                                           min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                           max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                           step=stuManage_data.stuManage_score_data_score_weight_step)
    with col_4:
        gpa_weight = st.number_input(stuManage_data.page_5_gpa_weight_label,
                                     value=stuManage_data.stuManage_score_data_gpa_weight,
                                     min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                     max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                     step=stuManage_data.stuManage_score_data_score_weight_step)
        interview_weight = st.number_input(stuManage_data.page_5_interview_weight_label,
                                           value=stuManage_data.stuManage_score_data_interview_weight,
                                           min_value=stuManage_data.stuManage_score_data_score_weight_min,
                                           max_value=stuManage_data.stuManage_score_data_score_weight_max,
                                           step=stuManage_data.stuManage_score_data_score_weight_step)
    st.markdown('---')
    col_l, col_m, col_r = st.columns([1, 1, 1])
    with col_l:
        st.markdown(stuManage_data.page_5_to_be_applied_weight_into_memory_introduction)
        to_be_applied_weight_into_memory = st.button(label=stuManage_data.page_5_to_be_applied_weight_into_memory_label)
        if to_be_applied_weight_into_memory:
            stuManage_data.stuManage_score_data_cet4_weight = cet4_weight
            stuManage_data.stuManage_score_data_cet6_weight = cet6_weight
            stuManage_data.stuManage_score_data_cet_weight = cet_weight
            stuManage_data.stuManage_score_data_gpa_weight = gpa_weight
            stuManage_data.stuManage_score_data_scholarship_weight = scholarship_weight
            stuManage_data.stuManage_score_data_recommendation_weight = recommendation_weight
            stuManage_data.stuManage_score_data_fieldwork_weight = fieldwork_weight
            stuManage_data.stuManage_score_data_interview_weight = interview_weight
    with col_m:
        st.markdown(stuManage_data.page_5_to_be_applied_weighted_score_into_memory_introduction)
        to_be_applied_weighted_score_into_memory = st.button(
            label=stuManage_data.page_5_to_be_applied_weighted_score_into_memory_label)
        if to_be_applied_weighted_score_into_memory:
            stuManage_data.recalculate_score()
    with col_r:
        st.markdown(stuManage_data.page_2_to_be_inserted_into_hard_drive_introduction)
        to_be_updated_into_hard_drive = st.button(label=stuManage_data.page_2_to_be_inserted_into_hard_drive_label, )
        if to_be_updated_into_hard_drive:
            stuManage_data.stuManage_score_data.to_csv(stuManage_data.stuManage_score_data_path, index=False)
    st.markdown('---')
    temp_df = stuManage_data.stuManage_score_data[stuManage_data.page_1_score_data_columns]
    temp_df.columns = [stuManage_data.stuManage_score_column_names_dict[name]
                       for name in stuManage_data.page_1_score_data_columns]
    st.table(temp_df)
    pass
