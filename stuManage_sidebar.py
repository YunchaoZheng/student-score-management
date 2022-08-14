import streamlit as st
import stuManage_data
import stuManage_page_delete
import stuManage_page_insert
import stuManage_page_query
import stuManage_page_update
import stuManage_page_weighted_score


def sidebar():
    st.sidebar.markdown(stuManage_data.sidebar_website_title, unsafe_allow_html=True)
    # 页面选择视图
    st.sidebar.markdown('---')
    option = st.sidebar.selectbox(stuManage_data.sidebar_selectbox_choice['caption'], (
        stuManage_data.sidebar_selectbox_choice['page_query_caption'],
        stuManage_data.sidebar_selectbox_choice['page_insert_caption'],
        stuManage_data.sidebar_selectbox_choice['page_delete_caption'],
        stuManage_data.sidebar_selectbox_choice['page_update_caption'],
        stuManage_data.sidebar_selectbox_choice['page_weighted_score_caption']))
    if option == stuManage_data.sidebar_selectbox_choice['page_query_caption']:
        stuManage_page_query.page()
    elif option == stuManage_data.sidebar_selectbox_choice['page_insert_caption']:
        stuManage_page_insert.page()
    elif option == stuManage_data.sidebar_selectbox_choice['page_delete_caption']:
        stuManage_page_delete.page()
    elif option == stuManage_data.sidebar_selectbox_choice['page_update_caption']:
        stuManage_page_update.page()
    elif option == stuManage_data.sidebar_selectbox_choice['page_weighted_score_caption']:
        stuManage_page_weighted_score.page()
    st.sidebar.markdown(stuManage_data.sidebar_introduction, unsafe_allow_html=True)
    st.sidebar.markdown(stuManage_data.sidebar_team, unsafe_allow_html=True)
    st.sidebar.markdown(stuManage_data.sidebar_repos, unsafe_allow_html=True)
