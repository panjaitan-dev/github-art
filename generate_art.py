import os
import subprocess
import random
from datetime import datetime, timedelta

# Map Huruf FERDIYANTO (Tegak & Presisi) untuk Tahun 1015:
# 1 = 3 commit (Hijau Muda Sedikit Pekat)
# 1 = 1 commit (Hijau Paling Cerah)
# 0 = Kosong
LETTERS = {
    'F': [[1,1,1,1],[1,0,0,0],[1,1,1,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],
    'E': [[1,1,1,1],[1,0,0,0],[1,1,1,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]],
    'R': [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,1,0],[1,0,0,1],[1,0,0,1]],
    'D': [[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,0]],
    'I': [[1,1,1,1],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    'Y': [[1,0,0,1],[1,0,0,1],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
    'A': [[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]],
    'N': [[1,0,0,1],[1,1,0,1],[1,1,0,1],[1,0,1,1],[1,0,1,1],[1,0,0,1],[1,0,0,1]],
    'T': [[1,1,1,1],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
    'O': [[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
}

WORD = "FERDIYANTO"

def make_commit(date_str, num_commits):
    with open("art_data.txt", "a") as f:
        f.write(f"Commit at {date_str}\n")
    
    subprocess.run(["git", "add", "art_data.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    for _ in range(num_commits):
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{date_str}T11:00:00"
        env["GIT_COMMITTER_DATE"] = f"{date_str}T11:00:00"
        subprocess.run(
            ["git", "commit", "-m", "feat: contribution activity update", "--quiet"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def generate_grid_1015():
    grid = [[0 for _ in range(51)] for _ in range(7)]
    col_index = 1
    for char in WORD:
        if char in LETTERS:
            pattern = LETTERS[char]
            for r in range(7):
                for c in range(len(pattern[0])):
                    if col_index + c < 51:
                        grid[r][col_index + c] = pattern[r][c]
            col_index += len(pattern[0]) + 1
    return grid

def run():
    # 1. TAHUN 1015: Nama FERDIYANTO (Hijau Cerah & Pekat, Garis Bawah Tetap Hijau Muda)
    start_date_1015 = datetime(1015, 1, 5)
    grid_1015 = generate_grid_1015()
    
    print("1. Memproses gambar nama FERDIYANTO untuk tahun 1015...")
    for col in range(51):
        for row in range(7):
            val = grid_1015[row][col]
            if val > 0:
                current_date = start_date_1015 + timedelta(days=(col * 7 + row))
                date_str = current_date.strftime("%Y-%m-%d")
                num_commits = 3 if val == 1 else 1  # Dikunci maks 3 commit
                make_commit(date_str, num_commits)

    # 1. TAHUN 1016: Commit Acak & Ramai dari Januari sampai November 1016
    print("1. Memproses commit acak & ramai untuk tahun 1016 (Januari - November)...")
    start_date_1016 = datetime(1016, 1, 1)
    end_date_1016 = datetime(1016, 11, 9)
    
    current_d = start_date_1016
    while current_d <= end_date_1016:
        if random.random() < 0.7:  # 70% hari aktif
            commits_today = random.randint(1, 3)
            date_str = current_d.strftime("%Y-%m-%d")
            make_commit(date_str, commits_today)
        current_d += timedelta(days=1)

    print("Selesai! Berhasil memproses grafik 1015 dan 1016.")

if __name__ == "__main__":
    run()