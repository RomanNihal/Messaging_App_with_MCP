import os
from pathlib import Path

# --- Configuration ---
PACKAGE_NAME = "messaging_app"
BASE_DIR = Path.cwd() / PACKAGE_NAME

# --- Execution ---
def create_project_structure():
    print(f"🚀 Initializing {PACKAGE_NAME}...")

    # 1. Create the package directory
    if not BASE_DIR.exists():
        BASE_DIR.mkdir()
        print(f"📂 Created package directory: {BASE_DIR}")
    else:
        print(f"📂 Directory exists: {BASE_DIR}")

    # 2. Create static directory for Frontend (New)
    static_dir = BASE_DIR / "static"
    if not static_dir.exists():
        static_dir.mkdir()
        print(f"📂 Created directory: {static_dir}")
    else:
        print(f"📂 Directory exists: {static_dir}")

    # 3. Define all necessary files
    files_to_create = [
        BASE_DIR / "__init__.py",        # Python Package marker
        BASE_DIR / "database.py",        # DB Connection
        BASE_DIR / "models.py",          # DB Tables
        BASE_DIR / "schemas.py",         # Validation
        BASE_DIR / "main.py",            # API Routes
        BASE_DIR / "messaging_mcp.py",   # MCP Server
        static_dir / "index.html",       # Frontend Dashboard (New)
    ]

    # 4. Create empty files
    for file_path in files_to_create:
        if not file_path.exists():
            with open(file_path, "w") as f:
                pass 
            print(f"📄 Created file: {file_path.name}")
        else:
            print(f"⚠️  Skipped (already exists): {file_path.name}")

    print(f"\n✅ Success! Structure ready. Run:")
    print(f"   python -m uvicorn {PACKAGE_NAME}.main:app --reload")

if __name__ == "__main__":
    create_project_structure()