import csv

def get_fname(csv_path):
    fname = csv_path.split('/')[-1]
    fname = fname.split('.')[0]
    return f'view/{fname}.md'

def csv_to_markdown(csv_path):
    markdown_lines = []
    
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        headers = next(reader)
        headers.pop(1) # no の除去
        headers = ["#"] + headers
        
        # ヘッダーの作成
        markdown_lines.append(f"| {' | '.join(headers)} |")
        # 区切り線の作成
        markdown_lines.append(f"| {' | '.join(['---'] * len(headers))} |")
        
        # データ行の作成
        for i, row in enumerate(reader):
            row.pop(1) # no の除去
            row = [str(i+1)] + row
            # 各セルの半角スペースを &nbsp; に置換
            # ( ) の中にあるスペースだけでなく、全ての半角スペースを対象にする
            processed_row = [cell.replace(' ', '&nbsp;&nbsp;') for cell in row]
            markdown_lines.append(f"| {' | '.join(processed_row)} |")
            
    # ファイルへの書き出し（または標準出力）
    output_file = get_fname(csv_path)
    with open(output_file, mode='w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))

if __name__=='__main__':
    csv_path = 'prob.csv'
    csv_to_markdown(csv_path)