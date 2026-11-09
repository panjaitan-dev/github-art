import os
import subprocess
import random
from datetime import datetime, timedelta

# Map Huruf FERDIYANTO (Tegak & Presisi) untuk Tahun 2025:
# 2 = 3 commit (Hijau Muda Sedikit Pekat)
# 1 = 1 commit (Hijau Paling Cerah)
# 0 = Kosong
LETTERS = {
    'F': [[1,2,2,1],[2,0,0,0],[2,2,1,0],[2,0,0,0],[2,0,0,0],[2,0,0,0],[2,0,0,0]],
    'E': [[1,2,2,1],[2,0,0,0],[2,2,1,0],[2,0,0,0],[2,0,0,0],[2,0,0,0],[1,2,2,1]],
    'R': [[2,2,2,1],[2,0,0,2],[2,0,0,2],[2,2,2,1],[2,0,1,0],[2,0,0,2],[2,0,0,2]],
    'D': [[2,2,2,0],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,2,2,0]],
    'I': [[1,2,2,1],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[1,2,2,1]],
    'Y': [[2,0,0,2],[2,0,0,2],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0]],
    'A': [[0,2,2,0],[2,0,0,2],[2,0,0,2],[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,0,0,2]],
    'N': [[2,0,0,2],[2,2,0,2],[2,1,0,2],[2,0,1,2],[2,0,2,2],[2,0,0,2],[2,0,0,2]],
    'T': [[1,2,2,1],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0]],
    'O': [[0,2,2,0],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[0,2,2,0]]
}

WORD = "FERDIYANTO"

def make_commit(date_str, num_commits):
    with open("art_data.txt", "a") as f:
        f.write(f"Commit at {date_str}\n")
    
    subprocess.run(["git", "add", "art_data.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    for _ in range(num_commits):
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{date_str}T12:00:00"
        env["GIT_COMMITTER_DATE"] = f"{date_str}T12:00:00"
        subprocess.run(
            ["git", "commit", "-m", "feat: contribution activity update", "--quiet"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def generate_grid_2025():
    grid = [[0 for _ in range(52)] for _ in range(7)]
    col_index = 1
    for char in WORD:
        if char in LETTERS:
            pattern = LETTERS[char]
            for r in range(7):
                for c in range(len(pattern[0])):
                    if col_index + c < 52:
                        grid[r][col_index + c] = pattern[r][c]
            col_index += len(pattern[0]) + 1
    return grid

def run():
    # 1. TAHUN 2025: Nama FERDIYANTO (Hijau Cerah & Pekat, Garis Bawah Tetap Hijau Muda)
    start_date_2025 = datetime(2025, 1, 5)
    grid_2025 = generate_grid_2025()
    
    print("1. Memproses gambar nama FERDIYANTO untuk tahun 2025...")
    for col in range(52):
        for row in range(7):
            val = grid_2025[row][col]
            if val > 0:
                current_date = start_date_2025 + timedelta(days=(col * 7 + row))
                date_str = current_date.strftime("%Y-%m-%d")
                num_commits = 3 if val == 2 else 1  # Dikunci maks 3 commit
                make_commit(date_str, num_commits)

    # 2. TAHUN 2026: Commit Acak & Ramai dari Januari sampai November 2026
    print("2. Memproses commit acak & ramai untuk tahun 2026 (Januari - November)...")
    start_date_2026 = datetime(2026, 1, 1)
    end_date_2026 = datetime(2026, 11, 9)
    
    current_d = start_date_2026
    while current_d <= end_date_2026:
        if random.random() < 0.7:  # 70% hari aktif
            commits_today = random.randint(1, 3)
            date_str = current_d.strftime("%Y-%m-%d")
            make_commit(date_str, commits_today)
        current_d += timedelta(days=1)

    print("Selesai! Berhasil memproses grafik 2025 dan 2026.")

if __name__ == "__main__":
    run()