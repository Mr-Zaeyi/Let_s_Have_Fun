<header>

# Image Processing and Lidar Analysis

_A project combining image filtering, edge detection, and real-time Lidar data visualization._

</header>

## 🚀 Introduction  

This project implements **image processing techniques** and **Lidar data analysis** to extract key features, detect objects, and visualize sensor data.  

📌 **Key Features:**  
- **Image Processing:** Load images, apply color filters, edge detection (Sobel, Laplacian), and cropping.  
- **Video Processing:** Process video frames in real-time.  
- **Lidar Data Processing:** Retrieve, visualize, and analyze real-time Lidar sensor data.  

---

## 📌 Features  

### 🖼️ Image Processing  
- **Load & Display Images** – Read and visualize an image.  
- **Color Filters** – Apply **red, green, and blue** channel filtering.  
- **Cropping (ROI Extraction)** – Extract the conveyor belt region.  
- **Edge Detection:**  
  - **Sobel Filter:** Detect contours along the **x-axis, y-axis**, and **combined gradient**.  
  - **Laplacian Filter:** Find object edges.  

#### 📸 Example Output (Sobel Filter)
| Original Image | Sobel X | Sobel Y | Sobel Combined |
|---------------|---------|---------|----------------|
| ![original](example_images/original.jpg) | ![sobel_x](example_images/sobel_x.jpg) | ![sobel_y](example_images/sobel_y.jpg) | ![sobel_combined](example_images/sobel_combined.jpg) |

---

### 🎥 Video Processing  
- Process video frames and apply **image filters** dynamically.  

📌 **Run the script:**  
```sh
python video_processing.py --video path/to/video.mp4
```

---

### 🔍 Lidar Data Processing  
- **Connect to Lidar** – Establish a serial connection.  
- **Retrieve Data** – Fetch **angle-distance** pairs from the sensor.  
- **Convert to Cartesian Coordinates** – Transform polar data into `(x, y)`.  
- **Visualize Data** – Plot scanned points.  
- **Obstacle Detection** – Compute **average distances** for **North, East, South, and West**.  
- **Convex Hull Algorithm** – Find the **outer boundary** of detected obstacles.  

#### 📡 Example Output (Lidar Obstacle Detection & Convex Hull)
| Raw Lidar Points | Convex Hull Applied |
|------------------|---------------------|
| ![lidar_raw](example_images/lidar_raw.jpg) | ![lidar_hull](example_images/lidar_hull.jpg) |

---

## 🛠 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2️⃣ Install Dependencies  
```sh
pip install -m PyLidar3
```

---

## 🚀 Usage  

### 🖼️ Image Processing  
```sh
python image_processing.py --image path/to/image.jpg --filter sobel
```
💡 **Filters available:**  
- `sobel` → Apply Sobel filter  
- `laplacian` → Apply Laplacian filter  

### 🎥 Video Processing  
```sh
python video_processing.py --video path/to/video.mp4
```

### 📡 Lidar Data Processing  
```sh
python lidar_processing.py
```

📌 **What this does:**  
✅ Reads real-time Lidar data  
✅ Converts polar to Cartesian coordinates  
✅ Plots the scanned environment  
✅ Highlights detected obstacles  

---

## 📂 File Structure  
```
📂 yourproject  
 ├── 📂 example_images         # Example outputs  
 ├── 📜 image_processing.py    # Image processing module  
 ├── 📜 video_processing.py    # Video processing module  
 ├── 📜 lidar_processing.py    # Lidar data handling  
 ├── 📜 requirements.txt       # Dependencies  
 ├── 📜 README.md              # Documentation  
```

---

## 🛠 Dependencies  
This project requires:  
- **OpenCV** – Image processing (`cv2`)  
- **NumPy** – Matrix operations (`numpy`)  
- **Matplotlib** – Data visualization (`matplotlib`)  
- **PyLidar3** – Lidar communication (`PyLidar3`)  
- **SciPy** – Convex hull calculations (`scipy.spatial.ConvexHull`)  

📌 To install with pip command such as :  
```sh
pip install -m PyLidar3
```

---

<footer>

## 🔗 Additional Resources  
- [OpenCV Documentation](https://docs.opencv.org/)  
- [PyLidar3 GitHub](https://github.com/yourrepo/pylidar3)  
- [SciPy Spatial Library](https://docs.scipy.org/doc/scipy/reference/spatial.html)
- This software contains code licensed as described in LICENSE.

💡 Need help? [Open an issue](https://github.com/yourusername/yourproject/issues) on GitHub.

&copy; 2024 Your Name • [MIT License](LICENSE)  

</footer>
