import os
import sys

def split_file(filename, chunk_size, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_number = 1
    with open(filename, 'rb') as f:
        chunk = f.read(chunk_size)
        while chunk:
            output_filename = os.path.join(output_dir, f"{os.path.basename(filename)}.part{file_number}")
            with open(output_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            file_number += 1
            chunk = f.read(chunk_size)
            
            # 顯示進度
            print(f"\r已處理 {file_number - 1} 個分割檔案", end='', flush=True)

    print(f"\n分割完成，共產生 {file_number - 1} 個檔案")

if __name__ == "__main__":
    filename = input("請輸入要分割的檔案名稱 (包括路徑): ")
    chunk_size = int(input("請輸入每個分割檔案的大小 (單位: 位元組, 60GB = 64424509440): "))
    output_dir = input("請輸入輸出目錄 (例如: C:\\output): ")

    split_file(filename, chunk_size, output_dir)
