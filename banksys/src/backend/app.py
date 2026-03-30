"""Streamlit 银行数据分析系统主应用"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from src.core.data_loader import DataLoader
from src.utils.analyzer import DataAnalyzer


def health_check():
    """健康检查端点"""
    return {"status": "healthy", "message": "BankSys is running"}


def main():
    """主应用函数"""
    st.set_page_config(
        page_title="银行数据分析系统",
        page_icon="🏦",
        layout="wide"
    )

    st.title("🏦 银行数据分析系统")
    st.markdown("---")

    # 侧边栏配置
    st.sidebar.header("配置")
    
    # 数据目录选择
    data_dir = st.sidebar.text_input(
        "数据目录路径",
        value=str(Path(__file__).parent.parent.parent.parent / "data")
    )

    # 初始化数据加载器
    loader = DataLoader(data_dir)

    # 获取可用文件
    available_files = loader.get_available_files()
    
    if available_files:
        selected_file = st.sidebar.selectbox(
            "选择数据文件",
            available_files
        )
    else:
        st.warning("数据目录为空或不存在，请使用示例数据演示")
        selected_file = None

    # 加载数据
    if selected_file:
        try:
            if selected_file.endswith('.csv'):
                df = loader.load_csv(selected_file)
            elif selected_file.endswith(('.xlsx', '.xls')):
                df = loader.load_excel(selected_file)
            else:
                st.error("不支持的文件格式")
                return
        except Exception as e:
            st.error(f"加载数据失败：{str(e)}")
            return
    else:
        # 创建示例数据
        st.info("使用示例数据进行演示")
        df = pd.DataFrame({
            '客户 ID': range(1, 101),
            '年龄': [25 + i % 40 for i in range(100)],
            '存款余额': [10000 + i * 100 for i in range(100)],
            '贷款金额': [5000 + i * 50 for i in range(100)],
            '信用等级': ['A', 'B', 'C', 'D'] * 25
        })

    # 显示数据概览
    st.header("📊 数据概览")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("记录数", len(df))
    with col2:
        st.metric("特征数", len(df.columns))
    with col3:
        st.metric("缺失值总数", df.isnull().sum().sum())

    # 数据预览
    with st.expander("查看原始数据"):
        st.dataframe(df)

    # 统计分析
    st.header("📈 统计分析")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("数值型特征统计")
        st.dataframe(DataAnalyzer.get_summary(df))
    
    with col2:
        st.subheader("缺失值分析")
        missing_info = DataAnalyzer.get_missing_info(df)
        if len(missing_info) > 0:
            st.dataframe(missing_info)
        else:
            st.success("无缺失值")

    # 可视化分析
    st.header("📉 可视化分析")
    
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_cols:
        # 相关性热力图
        if len(numeric_cols) > 1:
            st.subheader("特征相关性热力图")
            corr_matrix = DataAnalyzer.correlation_matrix(df)
            fig = px.imshow(
                corr_matrix,
                labels=dict(color="相关系数"),
                color_continuous_scale="RdBu_r"
            )
            st.plotly_chart(fig, use_container_width=True)

        # 分布直方图
        st.subheader("特征分布直方图")
        selected_col = st.selectbox("选择特征", numeric_cols)
        fig = px.histogram(df, x=selected_col, nbins=30)
        st.plotly_chart(fig, use_container_width=True)

        # 散点图
        if len(numeric_cols) > 1:
            st.subheader("散点图分析")
            col_x = st.selectbox("X 轴", numeric_cols, key="x_axis")
            col_y = st.selectbox("Y 轴", numeric_cols, key="y_axis")
            fig = px.scatter(df, x=col_x, y=col_y)
            st.plotly_chart(fig, use_container_width=True)

    # 数据导出
    st.header("💾 数据导出")
    csv = df.to_csv(index=False)
    st.download_button(
        label="下载 CSV 文件",
        data=csv,
        file_name="banksys_export.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.caption("银行数据分析系统 v0.1.0 | 基于 Streamlit 构建")


if __name__ == "__main__":
    main()
