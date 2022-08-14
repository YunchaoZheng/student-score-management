import streamlit as st
import stuManage_data


def page():
    # title 部分
    col_l, col_r = st.columns([stuManage_data.page_col_left_width, stuManage_data.page_col_right_width])
    with col_l:
        st.markdown(stuManage_data.page_1_main_title)
        st.markdown(stuManage_data.page_1_second_title)
        st.markdown(stuManage_data.page_1_introduction)
    with col_r:
        stuManage_data.not_welcomed_login()
    st.markdown('---')
    st.markdown(stuManage_data.page_1_query_introduction)
    temp_df = stuManage_data.stuManage_score_data[stuManage_data.page_1_score_data_columns]
    temp_df.columns = [stuManage_data.stuManage_score_column_names_dict[name]
                       for name in stuManage_data.page_1_score_data_columns]
    st.table(temp_df)
    pass
