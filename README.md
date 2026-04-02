# 🛠️ Image Optimization Dependencies

To run this script locally from scratch, you need to install the following Python libraries:

### 🐍 Required Packages
- **Pillow**: The core library for image processing (supports `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.tif`, and `.bmp`).
- **pillow-heif**: Essential for support of the **HEIC** (Apple High Efficiency) format.

---

### 🚀 Setup Instructions (Recommended)
Since many modern Linux/Ubuntu/WSL environments are "externally managed," using a virtual environment is the best practice to avoid system conflicts:

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate and/or install dependencies**:
   ```bash
   ./venv/bin/pip install pillow pillow-heif
   ```

3. **Run the script**:
   ```bash
   ./venv/bin/python3 img_optimize.py
   ```
