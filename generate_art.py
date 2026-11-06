import os
import subprocess
from datetime import datetime, timedelta

# Map Huruf FERDIYANTO dengan Gradasi:
# 2 = Hijau Tua Pekat (15 commit)
# 1 = Hijau Cerah/Muda (3 commit)
# 0 = Kosong/Abu-abu (0 commit)

LETTERS = {
    'F': [[1,2,2,1],[2,0,0,0],[2,2,1,0],[2,0,0,0],[2,0,0,0],[2,0,0,0],[2,0,0,0]],
    'E': [[1,2,2,1],[2,0,0,0],[2,2,1,0],[2,0,0,0],[2,0,0,0],[2,0,0,0],[1,2,2,1]],
    'R': [[2,2,2,1],[2,0,0,2],[2,0,0,2],[2,2,2,1],[2,0,1,0],[2,0,0,2],[2,0,0,2]],
    'D': [[2,2,2,1],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,2,2,1]],
    'I': [[1,2,2,1],[0,2,2,0],[0,2,2,0],[0,1,2,0],[0,2,2,0],[0,2,2,0],[1,2,2,1]],
    'Y': [[2,0,0,2],[2,0,0,2],[1,2,2,1],[0,1,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0]],
    'A': [[1,2,2,1],[2,0,0,2],[2,0,0,2],[2,2,2,2],[2,0,0,2],[2,0,0,2],[2,0,0,2]],
    'N': [[2,0,0,2],[2,1,0,2],[2,2,0,2],[2,0,2,2],[2,0,1,2],[2,0,0,2],[2,0,0,2]],
    'T': [[1,2,2,1],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0],[0,2,2,0]],
    'O': [[1,2,2,1],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[2,0,0,2],[1,2,2,1]]
}

WORD = "FERDIYANTO"
START_YEAR = 2025 # Target Tahun 2025

def get_start_date(year):
    d = datetime(year, 1, 1)
    while d.weekday() != 6:
        d += timedelta(days=1)
    return d

def make_commit(date_str, num_commits):
    with open("art_data.txt", "a") as f:
        f.write(f"Commit at {date_str}\n")
    
    subprocess.run(["git", "add", "art_data.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    for _ in range(num_commits):
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = f"{date_str}T12:00:00"
        env["GIT_COMMITTER_DATE"] = f"{date_str}T12:00:00"
        subprocess.run(
            ["git", "commit", "-m", "feat: pixel art commit", "--quiet"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def generate_grid():
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
    start_date = get_start_date(START_YEAR)
    grid = generate_grid()
    
    print(f"Memproses pembuatan commit gradasi untuk nama {WORD} ({START_YEAR})... Harap tunggu.")
    
    total_dots = 0
    for col in range(52):
        for row in range(7):
            val = grid[row][col]
            if val > 0:
                current_date = start_date + timedelta(days=(col * 7 + row))
                date_str = current_date.strftime("%Y-%m-%d")
                
                num_commits = 15 if val == 2 else 3
                make_commit(date_str, num_commits)
                total_dots += 1
                
    print(f"Selesai! Berhasil membuat commit gradasi pada {total_dots} titik piksel.")

if __name__ == "__main__":
    run()