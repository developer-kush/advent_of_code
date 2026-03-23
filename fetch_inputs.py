import os
import urllib.request
import urllib.error
import sys
import time

# usage: python fetch_inputs.py <session_cookie>
# or ensure AOC_SESSION env var is set
# or put cookie in .session file

YEAR = 2025
OUTPUT_DIR = os.path.join("input", str(YEAR))

def get_session_cookie():
    # 1. Check command line args
    if len(sys.argv) > 1:
        return sys.argv[1]
    
    # 2. Check environment variable
    session = os.environ.get("AOC_SESSION")
    if session:
        return session
    
    # 3. Check .session file
    if os.path.exists(".session"):
        with open(".session", "r") as f:
            return f.read().strip()
            
    return None

def download_inputs():
    session_cookie = get_session_cookie()
    if not session_cookie:
        print("Error: Session cookie not found.")
        print("Usage: python fetch_inputs.py <session_cookie>")
        print("Or set AOC_SESSION environment variable.")
        print("Or create a .session file with the cookie.")
        print("\nTo get your session cookie:")
        print("1. Go to adventofcode.com and log in.")
        print("2. Open Developer Tools (F12) -> Application/Storage -> Cookies.")
        print("3. Copy the value of the 'session' cookie.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "github.com/developer-kush/advent_of_code by bot"
    }

    print(f"Fetching inputs for Year {YEAR}...")
    
    for day in range(12, 13):
        filename = f"{day:02d}.input"
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath):
            # Check if empty, maybe retry if empty? 
            # For now, just skip if exists.
            if os.path.getsize(filepath) > 0:
                print(f"Day {day}: Already exists. Skipping.")
                continue

        url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                data = response.read()
                if not data:
                    print(f"Day {day}: Warning - Empty response.")
                else:
                    with open(filepath, "wb") as f:
                        f.write(data)
                    print(f"Day {day}: Saved to {filepath}")
                    
            # Respect rate limits/server load
            time.sleep(1) 
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"Day {day}: Not available yet (404). Stopping.")
                break # Future days not unlocked
            elif e.code == 400:
                print(f"Day {day}: Bad request (400). Check credentials.")
                break
            else:
                print(f"Day {day}: Failed with error {e.code}")
        except Exception as e:
            print(f"Day {day}: Error {e}")

if __name__ == "__main__":
    download_inputs()