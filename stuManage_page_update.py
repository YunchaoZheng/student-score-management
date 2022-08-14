import streamlit as st
import stuManage_data


def page():
    # title 部分
    col_l, col_r = st.columns([stuManage_data.page_col_left_width, stuManage_data.page_col_right_width])
    with col_l:
        st.markdown(stuManage_data.page_4_main_title)
        st.markdown(stuManage_data.page_4_second_title)
        st.markdown(stuManage_data.page_4_introduction)
    with col_r:
        stuManage_data.not_welcomed_login()
    st.markdown('---')
    st.markdown(stuManage_data.page_4_update_introduction)
    to_be_updated_id = st.selectbox(label=stuManage_data.page_4_to_be_updated_id_label,
                                    options=stuManage_data.stuManage_score_data['id'].tolist())
    df = stuManage_data.stuManage_score_data[stuManage_data.stuManage_score_data['id'] == to_be_updated_id]
    st.markdown('---')
    col_1, col_2, col_3, col_4 = st.columns([1, 1, 1, 1])

    with col_1:
        to_be_updated_cet4 = st.number_input(label=stuManage_data.page_2_to_be_inserted_cet4_label,
                                             value=df['CET4'].values[0],
                                             min_value=stuManage_data.page_2_to_be_inserted_cet4_min_value,
                                             max_value=stuManage_data.page_2_to_be_inserted_cet4_max_value, )
        to_be_updated_will = st.slider(label=stuManage_data.page_2_to_be_inserted_will_label,
                                       value=float(df['will'].values[0]),
                                       min_value=stuManage_data.page_2_to_be_inserted_will_min_value,
                                       max_value=stuManage_data.page_2_to_be_inserted_will_max_value,
                                       step=0.5)
    with col_2:
        to_be_updated_cet6 = st.number_input(label=stuManage_data.page_2_to_be_inserted_cet6_label,
                                             value=df['CET6'].values[0],
                                             min_value=stuManage_data.page_2_to_be_inserted_cet6_min_value,
                                             max_value=stuManage_data.page_2_to_be_inserted_cet6_max_value, )
        to_be_updated_recommendation = st.slider(label=stuManage_data.page_2_to_be_inserted_recommendation_label,
                                                 value=float(df['recommendation'].values[0]),
                                                 min_value=stuManage_data.page_2_to_be_inserted_recommendation_min_value,
                                                 max_value=stuManage_data.page_2_to_be_inserted_recommendation_max_value,
                                                 step=0.5)
    with col_3:
        to_be_updated_gpa = float(st.number_input(label=stuManage_data.page_2_to_be_inserted_gpa_label,
                                                  value=df['GPA'].values[0],
                                                  min_value=stuManage_data.page_2_to_be_inserted_gpa_min_value,
                                                  max_value=stuManage_data.page_2_to_be_inserted_gpa_max_value,
                                                  step=0.0001, ))
        st.markdown(stuManage_data.page_2_to_be_inserted_fieldwork_introduction)
        to_be_updated_fieldwork = int(st.checkbox(label=stuManage_data.page_2_to_be_inserted_fieldwork_label,
                                                  value=df['fieldwork'].values[0], ))

    with col_4:
        to_be_updated_scholarship = st.slider(label=stuManage_data.page_2_to_be_inserted_scholarship_label,
                                              value=int(df['scholarship'].values[0]),
                                              min_value=stuManage_data.page_2_to_be_inserted_scholarship_min_value,
                                              max_value=stuManage_data.page_2_to_be_inserted_scholarship_max_value, )
        to_be_updated_interview = st.slider(label=stuManage_data.page_2_to_be_inserted_interview_label,
                                            value=int(df['interview'].values[0]),
                                            min_value=stuManage_data.page_2_to_be_inserted_interview_min_value,
                                            max_value=stuManage_data.page_2_to_be_inserted_interview_max_value, )
    st.markdown('---')
    st.markdown(stuManage_data.page_4_to_be_updated_score_introduction)
    to_be_updated_score = round((to_be_updated_cet4 * stuManage_data.stuManage_score_data_cet4_weight +
                                 to_be_updated_cet6 * stuManage_data.stuManage_score_data_cet6_weight) * \
                                stuManage_data.stuManage_score_data_cet_weight + \
                                to_be_updated_gpa * stuManage_data.stuManage_score_data_gpa_weight + \
                                to_be_updated_scholarship * stuManage_data.stuManage_score_data_scholarship_weight + \
                                to_be_updated_recommendation * stuManage_data.stuManage_score_data_recommendation_weight + \
                                to_be_updated_fieldwork * stuManage_data.stuManage_score_data_fieldwork_weight + \
                                to_be_updated_interview * stuManage_data.stuManage_score_data_interview_weight, 2)
    st.text_input(label=stuManage_data.page_4_to_be_updated_score_label, value=to_be_updated_score, disabled=True)
    st.markdown('---')
    col_l, col_r = st.columns([1, 1])
    with col_l:
        st.markdown(stuManage_data.page_4_to_be_updated_into_memory_introduction)
        to_be_updated_into_memory = st.button(label=stuManage_data.page_4_to_be_updated_into_memory_label, )
        if to_be_updated_into_memory:
            stuManage_data.stuManage_score_data.loc[to_be_updated_id-10000] = [to_be_updated_id,
                                                                               to_be_updated_cet4, to_be_updated_cet6,
                                                                               to_be_updated_gpa,
                                                                               to_be_updated_scholarship,
                                                                               to_be_updated_will,
                                                                               to_be_updated_recommendation,
                                                                               to_be_updated_fieldwork,
                                                                               to_be_updated_interview,
                                                                               to_be_updated_score]
    with col_r:
        st.markdown(stuManage_data.page_2_to_be_inserted_into_hard_drive_introduction)
        to_be_updated_into_hard_drive = st.button(label=stuManage_data.page_2_to_be_inserted_into_hard_drive_label, )
        if to_be_updated_into_hard_drive:
            stuManage_data.stuManage_score_data.to_csv(stuManage_data.stuManage_score_data_path, index=False)
    pass
