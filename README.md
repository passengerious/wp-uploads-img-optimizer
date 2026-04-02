# 🖼️ WordPress Uploads Image Optimizer

A lightweight and powerful Python tool designed to optimize WordPress image galleries by converting them to the **.webp** format. 

### 🌟 Core Functionality
WordPress stores all images uploaded via the admin panel in the `./uploads/` directory (categorized by year and month). This script recursively scans that directory and converts all legacy formats into modern `.webp` files to significantly improve page load speeds and SEO.

### ✨ Key Features
- **Broad Format Support**: Converts `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.tif`, and `.gif`.
- **HEIC Support**: Seamlessly handles Apple High Efficiency images (`.heic`).
- **In-Place Optimization**: Converted files are saved directly in their original month/year subdirectories.
- **Automatic Cleanup**: Deletes the original high-resolution files after successful conversion to save server space.
- **Structure Preservation**: Keeps your WordPress media folder structure exactly as it was.

---

### 🛠️ Quick Start

#### 1. Setup Environment (WSL/Ubuntu)
```bash
python3 -m venv venv
./venv/bin/pip install pillow pillow-heif
```

#### 2. Run Optimization
Make sure your WordPress `uploads/` folder is in the project root:
```bash
./venv/bin/python3 img_optimize.py
```

### 📦 Dependencies
- **Pillow**: Core image processing.
- **pillow-heif**: Added support for HEIC format.

---

*Developed by [@passengerious](https://github.com/passengerious)*
