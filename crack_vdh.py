import os
import re

def final_crack():
    file_path = 'main.js'
    if not os.path.exists(file_path): return print("❌ 找不到 main.js")
    with open(file_path, 'r', encoding='utf-8') as f: code = f.read()
    # 逻辑 1：删除任务时重置
    code = re.sub(r'(\w+)\.downloading\.delete\(i\.download_id\)', 
                  r'ie(state => state.lsd = yc),\1.downloading.delete(i.download_id)', code)
    # 逻辑 2：判断时间前预重置（核心：绕过第4个报错）
    code = code.replace('a = state.lsd || yc', 'ie(state => state.lsd = yc), a = yc')
    with open(file_path, 'w', encoding='utf-8') as f: f.write(code)
    print("🚀 深度破解完成！")

if __name__ == '__main__': final_crack()