# app.py（合否データ + 公開期間 + 入力制限）
import streamlit as st
from datetime import datetime
import re

# 公開期間の設定
start_time = datetime(2025, 7, 1, 10, 0)
end_time = datetime(2025, 7, 3, 14, 0)
now = datetime.now()

st.set_page_config(page_title="入塾テスト合否結果", page_icon="🔢")
st.title("📈 入塾テスト合否結果")

# 公開期間チェック
if now < start_time:
    st.warning(f"このページは {start_time.strftime('%Y/%m/%d %H:%M')} から公開されます。")
    st.stop()
elif now > end_time:
    st.warning(f"このページの公開期間は終了しました（{end_time.strftime('%Y/%m/%d %H:%M')} まで）。")
    st.stop()
else:
    st.markdown("""
    受験番号とパスワードを入力してください。
    （※ 半角英数字のみ、有効な入力は自動的に大文字に変換されます）
    """)

    # 合否データ（受験番号, パスワード） → 結果
    data = {
        ('9C01', '1234'): '合格です。',
        ('9C02', '1235'): '残念ながら、ご希望に添うことが出来ませんでした。',
        ('9C03', '1236'): '合格です。',
        ('9C04', '1237'): '残念ながら、ご希望に添うことが出来ませんでした。',
        ('9C05', '1238'): '合格です。',
        ('9C06', '1239'): '残念ながら、ご希望に添うことが出来ませんでした。',
        ('9C07', '1240'): '合格です。',
        ('9C08', '1241'): '残念ながら、ご希望に添うことが出来ませんでした。',
    }

    # 入力欄
    exam_id_input = st.text_input("受験番号")
    password_input = st.text_input("パスワード", type="password")

    # 入力を大文字化・半角英数字のみに制限
    def sanitize_input(text):
        return re.sub(r'[^A-Za-z0-9]', '', text.upper())

    exam_id = sanitize_input(exam_id_input)
    password = sanitize_input(password_input)

    # ボタン押下で確認
    if st.button("確認する"):
        if not exam_id or not password:
            st.error("⚠️ 半角英数字で受験番号とパスワードを入力してください。")
        else:
            result = data.get((exam_id, password))
            if result:
                st.success(f"\u2705 【結果】{result}")
            else:
                st.error("⚠️ 受験番号あるいはパスワードが一致しません。")
