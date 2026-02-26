import re

html_design = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>発達特性セルフチェック</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Kiwi+Maru:wght@300;400;500&family=Murecho:wght@300;400;700&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          colors: {
            "primary": "#88c0d0",
            "accent-pink": "#f3a6b1",
            "accent-yellow": "#f9e1a1",
            "background-light": "#fdfbf7",
            "text-main": "#4a4e69",
          },
          fontFamily: {
            "handwriting": ["'Kiwi Maru'", "serif"],
            "sans": ["'Murecho'", "sans-serif"]
          },
        },
      },
    }
  </script>
<style type="text/tailwindcss">
    @layer utilities {
      .watercolor-blob { filter: blur(60px); opacity: 0.5; z-index: -1; }
      .storybook-border { border-radius: 60px 30px 70px 40px / 40px 60px 30px 70px; }
      .paper-texture { background-image: url('https://www.transparenttextures.com/patterns/handmade-paper.png'); }
      .speech-bubble-left { position: relative; background: white; border-radius: 2rem; }
      .speech-bubble-left::after { content: ''; position: absolute; left: -15px; top: 30px; width: 0; height: 0; border: 15px solid transparent; border-right-color: white; border-left: 0; }
      .handwritten-font { font-family: 'Kiwi Maru', serif; }
      .card { display: none; animation: fadeIn 0.5s ease; }
      .card.active { display: block; }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
      .flow-arrow { position: relative; }
      .flow-arrow::after { content: '↓'; display: block; text-align: center; color: #88c0d0; font-weight: bold; margin: 4px 0; }
      .flow-arrow:last-child::after { display: none; }
      .high { color: #e11d48 !important; }
    }
</style>
</head>
<body class="bg-background-light font-sans text-text-main selection:bg-accent-pink/30 paper-texture min-h-screen relative overflow-x-hidden">
<div class="fixed inset-0 overflow-hidden pointer-events-none">
  <div class="absolute -top-24 -left-24 w-[500px] h-[500px] bg-accent-pink/20 rounded-full watercolor-blob"></div>
  <div class="absolute top-1/4 -right-24 w-96 h-96 bg-primary/20 rounded-full watercolor-blob"></div>
  <div class="absolute bottom-10 left-1/4 w-[600px] h-[600px] bg-accent-yellow/30 rounded-full watercolor-blob"></div>
</div>

<div class="relative w-full max-w-[800px] mx-auto z-10 px-4 py-8 md:py-12">

  <!-- ================= スタート画面 ================= -->
  <div id="start-screen" class="card active">
    <div class="bg-white/70 backdrop-blur-sm storybook-border shadow-xl border-8 border-white p-6 md:p-12 text-center mb-12 relative overflow-hidden">
      
      <div class="absolute top-4 right-8 opacity-20 rotate-12 pointer-events-none">
        <span class="material-symbols-outlined text-6xl text-accent-pink">auto_stories</span>
      </div>

      <div class="text-slate-500 font-bold handwritten-font tracking-widest text-sm mb-4">────────────</div>
      <h1 class="text-3xl md:text-5xl font-bold handwritten-font text-slate-800 mb-6 leading-tight">
        発達特性<br><span class="text-accent-pink decoration-wavy underline underline-offset-8 mt-2 inline-block">セルフチェック</span>
      </h1>
      <div class="text-slate-500 font-bold handwritten-font tracking-widest text-sm mb-6">────────────</div>
      
      <p class="text-slate-600 text-lg md:text-xl leading-loose handwritten-font mb-8 font-bold">
        診断がなくても利用できます<br>
        特性の傾向と<br>
        支援の進め方がわかります
      </p>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-sm mx-auto mb-10 text-left bg-white/50 p-6 rounded-3xl border-2 border-primary/20">
        <div class="flex items-center gap-3"><span class="text-2xl">🧠</span><span class="handwritten-font font-bold text-slate-700">傾向がわかる</span></div>
        <div class="flex items-center gap-3"><span class="text-2xl">🏫</span><span class="handwritten-font font-bold text-slate-700">支援がわかる</span></div>
        <div class="flex items-center gap-3"><span class="text-2xl">📄</span><span class="handwritten-font font-bold text-slate-700">手続きがわかる</span></div>
        <div class="flex items-center gap-3"><span class="text-2xl">📍</span><span class="handwritten-font font-bold text-slate-700">相談先がわかる</span></div>
      </div>

      <div class="mb-4">
        <span class="bg-primary/10 text-primary font-bold handwritten-font text-lg px-6 py-2 rounded-full border border-primary/20">（小）約3分 / 無料</span>
      </div>

      <button onclick="startCheck()" class="w-full max-w-[300px] h-16 bg-accent-pink text-white rounded-full handwritten-font font-bold text-2xl shadow-xl shadow-accent-pink/30 hover:-translate-y-1 transition-all mx-auto focus:outline-none mb-6 mt-4 flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-3xl">play_circle</span>スタート
      </button>
      
      <div class="bg-accent-yellow/30 border-2 border-dashed border-accent-yellow/60 rounded-2xl p-4 max-w-md mx-auto">
          <strong class="block text-amber-700 text-sm handwritten-font font-bold mb-1">【免責事項】</strong>
          <p class="text-slate-600 handwritten-font text-xs leading-relaxed">
              本サイトは医学的診断ではありません。利用は自己責任でお願いします。運営者は一切の責任を負いません。
          </p>
      </div>
    </div>

    <!-- 困り感フローチャート -->
    <div class="bg-white/80 backdrop-blur-sm rounded-[2rem] border-4 border-white shadow-lg p-6 md:p-10 relative overflow-hidden">
      <!-- 装飾 -->
      <div class="absolute top-4 left-4 opacity-10 rotate-[-15deg] pointer-events-none">
        <span class="material-symbols-outlined text-6xl text-primary">route</span>
      </div>
      
      <h2 class="text-2xl font-bold handwritten-font text-center text-slate-800 mb-8 flex items-center justify-center gap-2">
        <span class="text-primary text-3xl">🚏</span>
        支援の進め方マップ
      </h2>

      <!-- 困り感ルート -->
      <div class="mb-10 p-6 bg-primary/5 rounded-3xl border-2 border-primary/20 relative">
        <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-white px-6 py-2 rounded-full shadow-sm border border-slate-100 font-bold handwritten-font text-slate-700 text-lg">困り感を感じた</div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
          <!-- 軽い困り感 -->
          <div class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center text-center flow-arrow border-t-4 border-t-accent-yellow/50">
            <span class="text-sm font-bold text-slate-600 mb-3">軽い困り感</span>
            <span class="text-amber-700/80 font-bold text-sm mb-3">学校へ相談</span>
            <div class="bg-accent-yellow/30 text-amber-800 font-bold px-4 py-2 rounded-xl text-sm w-full">通級指導教室</div>
          </div>
          <!-- 日常生活 -->
          <div class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center text-center flow-arrow border-t-4 border-t-accent-pink/50">
            <span class="text-sm font-bold text-slate-600 mb-3">日常生活で困難が多い</span>
            <span class="text-pink-700/80 font-bold text-sm mb-3">市役所へ相談</span>
            <div class="bg-accent-pink/20 text-pink-800 font-bold px-4 py-2 rounded-xl text-sm w-full">療育<br><span class="text-[10px] opacity-80">(放課後等デイ)</span></div>
          </div>
          <!-- 通常授業 -->
          <div class="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 flex flex-col items-center text-center flow-arrow border-t-4 border-t-primary/50">
            <span class="text-sm font-bold text-slate-600 mb-3">通常授業の継続が難しい</span>
            <span class="text-teal-700/80 font-bold text-sm mb-3">学校へ相談</span>
            <div class="bg-primary/20 text-teal-800 font-bold px-4 py-2 rounded-xl text-sm w-full">支援学級<br><span class="text-[10px] opacity-80">(ひまわり学級)</span></div>
          </div>
        </div>
      </div>

      <!-- 具体的な手続きフロー -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- 療育のながれ -->
        <div class="bg-accent-pink/5 rounded-2xl p-5 border border-accent-pink/20 hover:shadow-md transition-shadow">
          <h4 class="font-bold handwritten-font text-center text-pink-700 mb-4 border-b-2 border-accent-pink/30 pb-2">🍀 療育の流れ</h4>
          <ol class="text-sm space-y-3 font-bold text-slate-600 handwritten-font relative pl-1 text-center">
            <li class="flow-arrow">① 市役所へ相談</li>
            <li class="flow-arrow">② 発達相談</li>
            <li class="flow-arrow">③ 受給者証申請</li>
            <li class="flow-arrow">④ 支給決定</li>
            <li class="flow-arrow">⑤ 事業所見学</li>
            <li class="flow-arrow">⑥ 利用開始</li>
          </ol>
        </div>
        <!-- 通級のながれ -->
        <div class="bg-accent-yellow/10 rounded-2xl p-5 border border-accent-yellow/30 hover:shadow-md transition-shadow">
          <h4 class="font-bold handwritten-font text-center text-amber-700 mb-4 border-b-2 border-accent-yellow/40 pb-2">✏️ 通級の流れ</h4>
          <ol class="text-sm space-y-3 font-bold text-slate-600 handwritten-font relative pl-1 text-center">
            <li class="flow-arrow">① 担任に相談</li>
            <li class="flow-arrow">② 校内検討</li>
            <li class="flow-arrow">③ 教育委員会申請</li>
            <li class="flow-arrow">④ 面談</li>
            <li class="flow-arrow">⑤ 通級開始</li>
          </ol>
        </div>
        <!-- 支援学級のながれ -->
        <div class="bg-primary/10 rounded-2xl p-5 border border-primary/20 hover:shadow-md transition-shadow">
          <h4 class="font-bold handwritten-font text-center text-teal-700 mb-4 border-b-2 border-primary/30 pb-2">🌻 支援級の流れ</h4>
          <ol class="text-sm space-y-3 font-bold text-slate-600 handwritten-font relative pl-1 text-center">
            <li class="flow-arrow">① 担任に相談</li>
            <li class="flow-arrow">② 校内会議</li>
            <li class="flow-arrow">③ 教育委員会申請</li>
            <li class="flow-arrow">④ 見学・体験</li>
            <li class="flow-arrow">⑤ 判定</li>
            <li class="flow-arrow">⑥ 支援学級開始</li>
          </ol>
        </div>
      </div>

    </div>
  </div>

  <!-- ================= 質問画面 ================= -->
  <div id="question-screen" class="card">
    <div class="bg-white/80 backdrop-blur-md storybook-border shadow-2xl border-8 border-white p-6 md:p-12 relative overflow-hidden">
        <div class="flex justify-between items-center mb-8">
            <div class="inline-block bg-accent-yellow/40 text-amber-800 px-6 py-2 rounded-full font-bold handwritten-font tracking-widest border-2 border-white shadow-sm" id="category-badge">
                情緒型発達
            </div>
            <div class="text-primary font-bold handwritten-font text-lg">
                <span id="current-count" class="text-2xl">1</span> / <span id="total-count" class="text-lg text-primary/70">100</span>
            </div>
        </div>

        <div class="w-full h-4 bg-primary/10 rounded-full overflow-hidden mb-12 shadow-inner">
            <div class="h-full bg-accent-pink transition-all duration-300 ease-out w-0 rounded-full" id="progress-fill"></div>
        </div>

        <div class="bg-white border-2 border-primary/20 rounded-3xl p-8 mb-10 shadow-sm relative min-h-[12rem] flex items-center justify-center speech-bubble-left">
            <p class="text-xl md:text-3xl font-bold handwritten-font text-slate-800 leading-relaxed md:leading-loose text-center" id="question-text">
                <!-- 質問文 -->
            </p>
        </div>

        <div class="flex flex-col md:flex-row gap-4 justify-center items-center mb-6">
            <button onclick="answer(true)" class="w-full md:w-1/2 h-20 bg-accent-pink text-white rounded-[2rem] handwritten-font font-bold text-2xl shadow-xl shadow-accent-pink/20 border-4 border-white hover:-translate-y-1 hover:bg-pink-400 transition-all flex items-center justify-center gap-3">
                <span class="material-symbols-outlined text-3xl">mood</span> はい
            </button>
            <button onclick="answer(false)" class="w-full md:w-1/2 h-20 bg-primary/80 text-white rounded-[2rem] handwritten-font font-bold text-2xl shadow-xl shadow-primary/20 border-4 border-white hover:-translate-y-1 hover:bg-primary transition-all flex items-center justify-center gap-3">
                <span class="material-symbols-outlined text-3xl">sentiment_neutral</span> いいえ
            </button>
        </div>

        <div class="text-center mt-6">
            <button onclick="goBack()" id="back-btn" style="display: none;" class="text-slate-400 hover:text-primary underline handwritten-font text-sm transition-colors bg-transparent border-0">
                前の問題に戻る
            </button>
        </div>
    </div>
  </div>

  <!-- ================= 結果画面 ================= -->
  <div id="result-screen" class="card">
    <div class="bg-white/80 backdrop-blur-md storybook-border shadow-2xl border-8 border-white p-6 md:p-12 text-center relative overflow-hidden">
        <div class="mb-10 text-center">
            <h2 class="text-3xl md:text-4xl font-bold handwritten-font text-slate-800 mb-2">チェックが終わりました</h2>
            <div class="w-24 h-1 bg-accent-yellow mx-auto rounded-full mb-4"></div>
            <p class="text-slate-600 handwritten-font">該当する項目の割合（％）</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-10">
            <div class="bg-white border-4 border-primary/20 rounded-[3rem] p-8 shadow-md relative group hover:border-primary/50 transition-colors">
                <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-primary rounded-full flex items-center justify-center border-4 border-white shadow-sm">
                    <span class="material-symbols-outlined text-white">favorite</span>
                </div>
                <div class="text-primary font-bold handwritten-font tracking-widest mb-4 mt-2">情緒型発達</div>
                <div class="text-5xl md:text-6xl font-bold text-slate-700 handwritten-font" id="res-emotion">0<span class="text-2xl text-slate-400 ml-1">%</span></div>
            </div>
            
            <div class="bg-white border-4 border-accent-yellow/40 rounded-[3rem] p-8 shadow-md relative group hover:border-accent-yellow transition-colors">
                <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-accent-yellow rounded-full flex items-center justify-center border-4 border-white shadow-sm text-amber-700">
                    <span class="material-symbols-outlined">psychology</span>
                </div>
                <div class="text-amber-700 font-bold handwritten-font tracking-widest mb-4 mt-2">知育型発達</div>
                <div class="text-5xl md:text-6xl font-bold text-slate-700 handwritten-font" id="res-intellect">0<span class="text-2xl text-slate-400 ml-1">%</span></div>
            </div>
        </div>

        <div id="guidance-section" style="display: none;" class="bg-accent-pink/10 border-4 border-dashed border-accent-pink/50 rounded-[2rem] p-8 mb-10 text-left relative">
            <div class="absolute -top-5 -left-5 w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md rotate-[-10deg]">
                <span class="material-symbols-outlined text-accent-pink">notifications_active</span>
            </div>
            <h3 class="text-xl font-bold handwritten-font text-slate-800 mb-4 flex items-center gap-2">
                <span class="material-symbols-outlined text-accent-pink">info</span>
                専門機関へのご案内
            </h3>
            <p class="text-slate-600 leading-relaxed handwritten-font mb-6">
                該当率が80%を超えました。より詳しい状況の確認やサポートのために、以下の専門機関・窓口へご相談されることをお勧めいたします。
            </p>
            <div class="flex flex-col gap-4">
                <a href="https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/shougaishahukushi/hattatsu/index.html" target="_blank" rel="noopener noreferrer" class="flex justify-between items-center bg-white p-4 rounded-xl border-2 border-primary/20 text-slate-700 font-bold handwritten-font hover:border-accent-pink hover:text-accent-pink transition-all hover:shadow-md group">
                    発達障害者支援センター一覧
                    <span class="material-symbols-outlined text-slate-400 group-hover:text-accent-pink group-hover:translate-x-1 transition-all">arrow_forward_ios</span>
                </a>
                <a href="https://h-navi.jp/" target="_blank" rel="noopener noreferrer" class="flex justify-between items-center bg-white p-4 rounded-xl border-2 border-primary/20 text-slate-700 font-bold handwritten-font hover:border-accent-pink hover:text-accent-pink transition-all hover:shadow-md group">
                    LITALICO発達ナビ（病院検索）
                    <span class="material-symbols-outlined text-slate-400 group-hover:text-accent-pink group-hover:translate-x-1 transition-all">arrow_forward_ios</span>
                </a>
            </div>
        </div>

        <div class="flex flex-col gap-4 items-center justify-center">
            <button onclick="location.reload()" class="bg-white border-2 border-primary/30 text-primary h-14 px-10 rounded-full handwritten-font font-bold text-lg hover:bg-primary/5 transition-all inline-flex items-center justify-center gap-2 shadow-sm focus:outline-none w-full max-w-sm">
                <span class="material-symbols-outlined">refresh</span>
                もう一度チェックする
            </button>
            <button onclick="showScreen('start-screen')" class="bg-primary text-white h-14 px-10 rounded-full handwritten-font font-bold text-lg hover:bg-primary/90 transition-all inline-flex items-center justify-center gap-2 shadow-sm focus:outline-none w-full max-w-sm">
                <span class="material-symbols-outlined">route</span>
                支援の進め方を確認する
            </button>
        </div>
    </div>
  </div>

</div>
"""

with open('c:/Users/minib/OneDrive/ドキュメント/code/adhd/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the script
match = re.search(r'<script(?! id="tailwind-config").*?</script>', text, flags=re.DOTALL)
if match:
    script_content = match.group(0)
    final_html = html_design + "\n    " + script_content + "\n</body>\n</html>"
    with open('c:/Users/minib/OneDrive/ドキュメント/code/adhd/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Done rewriting index.html")
else:
    print("Script tags not found in index.html!")
