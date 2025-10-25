import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="Mini Data Analyzer", page_icon="📊", layout="wide")

st.title("🧠 Mini Data Analyzer")
st.write("Easily explore and visualize your dataset in seconds!")

uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="latin1")

    st.subheader("🟢 First 5 Rows of the Dataset:")
    st.dataframe(df.head())

    with st.expander("📊 Dataset Info (click to expand)"):
        info_df = pd.DataFrame({
            "Column Name": df.columns,
            "Non-Null Count": df.notnull().sum()
        })

        st.markdown("""
            <style>
            .center-table {
                display: flex;
                justify-content: center;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="center-table">', unsafe_allow_html=True)
        st.dataframe(info_df, use_container_width=False, width=400)
        st.markdown("</div>", unsafe_allow_html=True)

        st.caption(
            f"📦 Rows: {df.shape[0]} | Columns: {df.shape[1]} | "
            f"Memory Usage: ~{round(df.memory_usage(deep=True).sum()/1024, 2)} KB"
        )

    st.subheader("📈 Summary Statistics:")
    summary_df = df.describe()

    st.markdown('<div class="center-table">', unsafe_allow_html=True)
    st.dataframe(summary_df, use_container_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("🧩 Columns in the Dataset:")
    st.write(list(df.columns))

    st.subheader("🚫 Missing Values per Column:")
    st.write(df.isnull().sum())

    if "Category" in df.columns:
        st.subheader("📊 Category Distribution:")
        category_counts = df["Category"].value_counts()

        fig, ax = plt.subplots(figsize=(8, 6))
        category_counts.plot(kind="barh", ax=ax, color="#69b3a2", edgecolor="black")
        ax.set_title("Category Distribution", fontsize=14, pad=10)
        ax.set_xlabel("Count", fontsize=12)
        ax.set_ylabel("Category", fontsize=12)
        ax.invert_yaxis()  
        plt.grid(axis="x", linestyle="--", alpha=0.7)
        st.pyplot(fig)

    if "Difficulty" in df.columns:
        st.subheader("💪 Difficulty Level Distribution:")
        diff_counts = df["Difficulty"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 4))
        diff_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax, startangle=90, colors=["#90CAF9", "#A5D6A7", "#FFCC80"])
        ax.set_ylabel("")  
        ax.set_title("Difficulty Distribution", fontsize=14)
        st.pyplot(fig)

else:
    st.info("⬆️ Upload a CSV file to get started.")