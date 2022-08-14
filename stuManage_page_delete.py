import streamlit as st
import stuManage_data


def page():
    # title 部分
    col_l, col_r = st.columns([stuManage_data.page_col_left_width, stuManage_data.page_col_right_width])
    with col_l:
        st.markdown(stuManage_data.page_3_main_title)
        st.markdown(stuManage_data.page_3_second_title)
        st.markdown(stuManage_data.page_3_introduction)
    with col_r:
        stuManage_data.not_welcomed_login()
    temp_df = stuManage_data.stuManage_score_data[stuManage_data.page_1_score_data_columns]
    temp_df.columns = [stuManage_data.stuManage_score_column_names_dict[name]
                       for name in stuManage_data.page_1_score_data_columns]
    st.markdown('---')
    col_l, col_m, col_r = st.columns([1, 1, 1])
    with col_l:
        to_be_deleted_id = st.selectbox(stuManage_data.page_3_to_be_deleted_id_label, temp_df['学号'].tolist())
    with col_m:
        st.markdown(stuManage_data.page_3_to_be_deleted_into_memory_introduction)
        to_be_deleted_into_memory = st.button(label=stuManage_data.page_3_to_be_deleted_into_memory_label, )
        if to_be_deleted_into_memory:
            stuManage_data.stuManage_score_data.drop(axis=0, index=to_be_deleted_id-10000, inplace=True)
    with col_r:
        st.markdown(stuManage_data.page_3_to_be_deleted_into_hard_drive_introduction)
        to_be_deleted_into_hard_drive = st.button(label=stuManage_data.page_3_to_be_deleted_into_hard_drive_label, )
        if to_be_deleted_into_hard_drive:
            stuManage_data.stuManage_score_data.to_csv(stuManage_data.stuManage_score_data_path, index=False)
    st.markdown('---')
    st.markdown(stuManage_data.page_3_delete_introduction)
    st.table(temp_df)
    pass
