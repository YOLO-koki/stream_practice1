import streamlit as st
import numpy as np
from PIL import Image
import time


# タイトルの追加
st.title('Streamlit 入門')

# テキストの追加
st.write('DataFrame')

df = pd.DataFrame({
    '1項目':[1, 2, 3, 4],
    '2項目':[10, 20, 30, 40],
})

# データフレームの表を追加
# write()・・・表の細かい設定ができない
# dataframe()・・・表の細かい設定ができる
# table()・・・static(静的な)なテーブルを作る
st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

# マジックコマンドを使用
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd 
```
"""

# <<チャート(グラフ)をかく>>
df = pd.DataFrame(
    # np.random.rand(行数, 列数),
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# 折れ線グラフでプロット
st.line_chart(df)

# 折れ線グラフの中身を塗りつぶし
st.area_chart(df)

# 棒グラフをプロット
st.bar_chart(df)

# マップ(地図)をプロット
df = pd.DataFrame(
    # np.random.rand(行数, 列数),
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

# <<画像を表示>>

# 画像の読み込み
img = Image.open('urb.jpg')

# 表示
# use_column_width・・・実際のレイアウトに合わせて表示させる
st.image(image=img, caption='Urban', use_column_width=True)

# チェックボックスによるメディアの表示の可否
# checkbox()・・・True か False を返す
if st.checkbox('Show Image'):
    img = Image.open('urb.jpg')
    st.image(image=img, caption='Urban', use_column_width=True)
    
# セレクトボックスによる値の動的変更
option_selectbox = st.selectbox(
   'あなたが好きな数字を教えてください。',
   list(range(1, 11)), 
)

'あなたの好きな数字は、', option_selectbox, 'です。'

# # テキスト入力による値の動的変更
# option_text = st.text_input('あなたの趣味はを教えてください。')

# 'あなたの趣味は、', option_text, 'です。'

# # スライダーによる値の動的変更
# # slider(ラベル, 最小値, デフォルト値, 最大値)
# condition = st.slider('あなたの今の調子は？', 0, 150, 50)
# 'コンディション：', condition, 'です。'



# <<レイアウトを整える>>
# サイドバーの追加
# option_text = st.sidebar.text_input('あなたの趣味はを教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 150, 50)

# 'あなたの趣味は、', option_text, 'です。'

# 'コンディション：', condition, 'です。'

# 2カラムレイアウトにする
left_column, right_columns = st.columns(2)
# 左にボタン、右にテキスト
button = left_column.button('右カラムに文字を表示')
if button:
    right_columns = st.write('ここに右カラム')
    
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

# プログレスバーの表示
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteratoin {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!!!!!!!!!'